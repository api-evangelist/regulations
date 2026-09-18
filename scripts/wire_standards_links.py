#!/usr/bin/env python3
"""Wire the regulation <-> standard graph in BOTH directions, idempotently.

A regulation is the law; a standard is the machine-readable contract that satisfies it.
The catalog already models the edge on both sides — `standards:` on a regulation and
`regulations:` on a standard — but the edge has to be written twice or the graph is
one-way, and a one-way edge is how a standard page ends up claiming no legal driver
while the regulation page points straight at it.

This writes both halves from a single declaration below. Re-running replaces the edges
this file owns and leaves hand-authored ones alone.
"""
import os
import re
import sys

REG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_store")
STD = os.path.expanduser("~/GitHub/api-evangelist/standards/_store")

# regulation slug -> [(standard slug, note rendered on BOTH pages)]
EDGES = {
    "eu-cyber-resilience-act": [
        ("cyclonedx", "The CRA requires a software bill of materials covering at least the top-level "
                      "dependencies; CycloneDX is one of the two formats the market actually ships."),
        ("spdx", "The other SBOM format a CRA conformity assessment will accept, and the one with "
                 "the deeper licensing model."),
        ("security-txt", "The CRA obliges a coordinated vulnerability disclosure policy and a contact "
                         "point for reporting; RFC 9116 is how that becomes machine-readable."),
    ],
    "psti-act": [
        ("security-txt", "PSTI requires a published vulnerability disclosure policy with a working "
                         "contact — exactly what security.txt exists to publish."),
    ],
    "australia-cyber-security-act": [
        ("security-txt", "The smart-device standards carry the same vulnerability-disclosure "
                         "requirement the UK's PSTI Act established."),
        ("cyclonedx", "Component transparency for connectable products, converging with the CRA."),
    ],
    "ada-title-iii": [
        ("wcag", "No US regulation names a standard for private entities, but settlements, consent "
                 "decrees and expert testimony converge on WCAG 2.1 AA — a de facto standard that "
                 "was never adopted as one."),
    ],
    "aoda": [
        ("wcag", "The Integrated Accessibility Standards Regulation names WCAG 2.0 Level AA directly, "
                 "which is what distinguishes AODA from the US approach of litigating it case by case."),
    ],
    "eu-ai-act": [
        ("iso-42001", "The AI Act compels no specific management system, but an ISO/IEC 42001 AI "
                      "management system is the closest thing to a certifiable answer to its "
                      "governance, documentation and risk-management duties."),
    ],
    "texas-traiga": [
        ("iso-42001", "TRAIGA's safe harbour runs to the NIST AI RMF specifically; ISO/IEC 42001 is "
                      "the certifiable sibling organisations pair with it."),
    ],
    "california-sb-53": [
        ("iso-42001", "SB 53 requires a published frontier AI framework describing how national and "
                      "international standards are incorporated — which is the question 42001 answers."),
    ],
}

# Edges already authored by hand on the REGULATION side that were never written back on
# the standard side. Declaring them here writes only the reciprocal half, so the existing
# hand-authored entry is left exactly as it is rather than duplicated.
REVERSE_ONLY = {
    "european-accessibility-act": [
        ("wcag", "EN 301 549, the European standard the EAA leans on, incorporates WCAG success "
                 "criteria — which is how a W3C guideline acquired the force of EU product law."),
    ],
    "section-508": [
        ("wcag", "Section 508's refreshed standards incorporate WCAG 2.0 Level AA by reference for "
                 "US federal procurement."),
    ],
}

MARK = "  # wired by scripts/wire_standards_links.py"


def front_matter(path):
    text = open(path).read()
    lines = text.split("\n")
    if lines[0].strip() != "---":
        return None, None, None
    end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    return lines, 1, end


def field(lines, start, end, key):
    for i in range(start, end):
        m = re.match(rf"^{key}:\s*(.*)$", lines[i])
        if m:
            return m.group(1).strip().strip("'\"")
    return None


def upsert_block(path, key, entries):
    """Replace the `key:` block with `entries`, preserving any entry we did not author."""
    lines, start, end = front_matter(path)
    if lines is None:
        return False, f"{os.path.basename(path)}: no front matter"

    # capture existing entries so hand-authored edges survive
    existing, at = [], None
    i = start
    while i < end:
        if lines[i].startswith(f"{key}:"):
            at = i
            j = i + 1
            cur = []
            while j < end and (lines[j].startswith("- ") or lines[j].startswith("  ")):
                cur.append(lines[j])
                j += 1
            existing = cur
            del lines[i:j]
            end -= (j - i)
            break
        i += 1

    keep = []
    chunk = []
    for ln in existing + [None]:
        if ln is None or ln.startswith("- "):
            if chunk and MARK not in "\n".join(chunk):
                keep.extend(chunk)          # not ours — preserve verbatim
            chunk = []
        if ln is not None:
            chunk.append(ln)

    ours = []
    for title, url, note in entries:
        ours.append(f"- title: {title}{MARK}")
        ours.append(f"  url: {url}")
        ours.append(f"  note: {note}")

    block = [f"{key}:"] + keep + ours
    insert_at = at if at is not None else end
    lines[insert_at:insert_at] = block
    open(path, "w").write("\n".join(lines))
    return True, None


def wrap(note, indent="    "):
    """Keep the YAML readable at the width the rest of the store uses."""
    words, out, line = note.split(), [], ""
    for w in words:
        if len(line) + len(w) + 1 > 96:
            out.append(line)
            line = w
        else:
            line = f"{line} {w}".strip()
    out.append(line)
    return ("\n" + indent).join(out)


def main():
    problems, wired = [], 0
    reverse = {}

    for reg_slug, stds in EDGES.items():
        reg_path = os.path.join(REG, f"{reg_slug}.md")
        if not os.path.exists(reg_path):
            problems.append(f"regulation missing: {reg_slug}")
            continue
        rl, rs, re_ = front_matter(reg_path)
        reg_title = field(rl, rs, re_, "title") or field(rl, rs, re_, "name")

        entries = []
        for std_slug, note in stds:
            std_path = os.path.join(STD, f"{std_slug}.md")
            if not os.path.exists(std_path):
                problems.append(f"standard missing: {std_slug} (for {reg_slug})")
                continue
            sl, ss, se = front_matter(std_path)
            std_title = field(sl, ss, se, "title") or field(sl, ss, se, "name")
            entries.append((std_title,
                            f"https://standards.apievangelist.com/store/{std_slug}/",
                            wrap(note)))
            reverse.setdefault(std_slug, []).append(
                (reg_title, f"https://regulations.apievangelist.com/store/{reg_slug}/", wrap(note)))

        if entries:
            ok, err = upsert_block(reg_path, "standards", entries)
            problems.append(err) if err else None
            wired += len(entries)

    for reg_slug, stds in REVERSE_ONLY.items():
        reg_path = os.path.join(REG, f"{reg_slug}.md")
        if not os.path.exists(reg_path):
            problems.append(f"regulation missing: {reg_slug}")
            continue
        rl, rs, re_ = front_matter(reg_path)
        reg_title = field(rl, rs, re_, "title") or field(rl, rs, re_, "name")
        for std_slug, note in stds:
            if not os.path.exists(os.path.join(STD, f"{std_slug}.md")):
                problems.append(f"standard missing: {std_slug} (for {reg_slug})")
                continue
            reverse.setdefault(std_slug, []).append(
                (reg_title, f"https://regulations.apievangelist.com/store/{reg_slug}/", wrap(note)))

    for std_slug, entries in reverse.items():
        ok, err = upsert_block(os.path.join(STD, f"{std_slug}.md"), "regulations", entries)
        if err:
            problems.append(err)

    print(f"{wired} edge(s) wired across {len(EDGES)} regulation(s) and {len(reverse)} standard(s)")
    if problems:
        print("PROBLEMS:")
        for p in [p for p in problems if p]:
            print("  " + p)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
