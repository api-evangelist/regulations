#!/usr/bin/env python3
"""Add machine-readable region/country/industry joins to regulations.apievangelist.com.

`jurisdiction:` stays exactly as it is — it is display prose and it carries nuance the
slugs cannot ("United States (California, and state adoptions)"). What it has never been
is joinable: 20 spellings for five jurisdictions, and nothing reads it.

This adds four keys next to it, all drawn from the CANONICAL apis.io vocabularies so a
regulation page and a /countries/<slug>/ page are talking about the same thing:

  scope:      horizontal | sectoral  — does this bind every company, or one sector?
  countries:  slugs from api-search/countries/_countries   (48-term vocabulary)
  regions:    slugs from api-search/network/_data/regions.yml (18-term vocabulary)
  industries: slugs from api-search/industries/_industries  (82-term vocabulary)

For a SECTORAL regime `industries:` is the set it binds. For a HORIZONTAL one it is the
set where the regime creates specific, additional duties beyond the baseline — the layout
says so, so "GDPR: marketing-advertising" never reads as "GDPR only covers advertising."

Line-based on purpose. Round-tripping the YAML would reflow every hand-wrapped description
block and bury the real change in a 96-file whitespace diff. Idempotent: re-running replaces
the four keys and touches nothing else.
"""
import glob
import os
import re
import sys

STORE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_store")

# ---------------------------------------------------------------------------
# Jurisdiction prose -> (countries, regions). Keyed on the exact string in the file.
# ---------------------------------------------------------------------------
EU_COUNTRIES = ["austria", "belgium", "denmark", "estonia", "finland", "france", "germany",
                "ireland", "italy", "netherlands", "poland", "portugal", "spain", "sweden"]
# Every European sub-region EXCEPT united-kingdom-ireland: the UK left, and a reader who
# sees GDPR on /regions/united-kingdom-ireland/ should be seeing UK GDPR, not this one.
EU_REGIONS = ["europe", "dach", "france-iberia", "nordics", "benelux",
              "italy-southern-europe", "cee"]

US = (["united-states"], ["north-america"])
CA = (["canada"], ["north-america"])
UK = (["united-kingdom"], ["united-kingdom-ireland"])
AU = (["australia"], ["anz"])
EU = (EU_COUNTRIES, EU_REGIONS)
GLOBAL = ([], ["global"])

JURISDICTION = {
    "United States": US,
    "United States (federal)": US,
    "United States (California)": US,
    "United States (California, and state adoptions)": US,
    "United States (trade association)": US,
    "United States (trade association / local MLS)": US,
    "United States (state, 20 in effect)": US,
    "United States (state)": US,
    "United States (state and municipal)": US,
    "United States (Colorado)": US,
    "United States (Texas)": US,
    "United States (Illinois)": US,
    "United States (Washington)": US,
    "United States (with UK and Canadian equivalents)":
        (["united-states", "united-kingdom", "canada"], ["north-america", "united-kingdom-ireland"]),
    "Canada": CA,
    "Ontario, Canada": CA,
    "Canada (Quebec)": CA,
    "United Kingdom": UK,
    "Great Britain": UK,
    "Australia": AU,
    "Australia (state and territory)": AU,
    "European Union": EU,
    "European Union / United Kingdom":
        (EU_COUNTRIES + ["united-kingdom"], EU_REGIONS + ["united-kingdom-ireland"]),
    "Germany": (["germany"], ["dach", "europe"]),
    "International": GLOBAL,
    "Global (FATF member jurisdictions)": GLOBAL,
    "United Nations / EU / adopting states": (EU_COUNTRIES, EU_REGIONS + ["global"]),
}

# ---------------------------------------------------------------------------
# Per-regulation scope + industries. Hand-authored: deriving industry from the `tags:`
# block is exactly the defect in roadmap#431, where 48 providers landed in the Insurance
# regime because a tag contained the word "policy".
# ---------------------------------------------------------------------------
H, S = "horizontal", "sectoral"
MAP = {
    "21-cfr-part-11":            (S, ["pharmaceutical", "life-sciences", "biotechnology", "healthcare"]),
    "21st-century-cures-act":    (S, ["healthcare", "digital-health", "life-sciences"]),
    "air-passenger-protection-regulations": (S, ["travel-technology", "transportation"]),
    "apra-prudential-standards": (S, ["banking", "insurance", "financial-services"]),
    "atol":                      (S, ["travel-technology"]),
    "australia-privacy-act":     (H, ["technology", "artificial-intelligence", "marketing-advertising", "healthcare"]),
    "australian-consumer-law":   (H, ["e-commerce-platform", "retail", "travel-technology"]),
    "australian-telecommunications-act": (S, ["telecommunications"]),
    "bsa-aml":                   (S, ["banking", "financial-services", "financial-technology", "payments", "blockchain-crypto"]),
    "can-spam":                  (H, ["marketing-advertising", "e-commerce-platform", "communications-platform-as-a-service-cpaas"]),
    "cap-accreditation":         (S, ["healthcare", "life-sciences", "biotechnology"]),
    "cbam":                      (S, ["industrial", "chemicals", "mining", "climate-sustainability", "supply-chain"]),
    "ccpa-cpra":                 (H, ["marketing-advertising", "technology", "data-analytics", "artificial-intelligence"]),
    "cfpb-personal-financial-data-rights": (S, ["banking", "financial-services", "financial-technology", "payments"]),
    "clia":                      (S, ["healthcare", "life-sciences", "biotechnology"]),
    "cma-open-banking-order":    (S, ["banking", "financial-technology", "payments"]),
    "cms-interoperability-prior-authorization": (S, ["healthcare", "digital-health", "insurance"]),
    "consumer-data-right":       (S, ["banking", "energy", "telecommunications", "financial-services"]),
    "consumer-driven-banking":   (S, ["banking", "financial-technology", "payments"]),
    "coppa":                     (H, ["gaming", "education", "video-streaming", "creator-economy", "marketing-advertising"]),
    "csddd":                     (H, ["supply-chain", "retail", "consumer-goods", "industrial", "chemicals"]),
    "csrd":                      (H, ["climate-sustainability", "financial-services", "industrial", "energy"]),
    "digital-markets-act":       (S, ["technology", "e-commerce-platform", "cloud-data-platform", "marketing-advertising", "media"]),
    "dmcca-2024":                (H, ["technology", "e-commerce-platform", "marketing-advertising", "retail"]),
    "dodd-frank-1033":           (S, ["banking", "financial-services", "financial-technology"]),
    "dora":                      (S, ["banking", "insurance", "financial-services", "financial-technology", "payments", "cybersecurity"]),
    "dscsa":                     (S, ["pharmaceutical", "supply-chain", "life-sciences", "healthcare"]),
    "dtac":                      (S, ["healthcare", "digital-health"]),
    "easa-u-space":              (S, ["aerospace", "air-traffic-airspace", "robotics"]),
    "eidas":                     (H, ["cybersecurity", "government", "banking", "legal-compliance"]),
    "electronic-conveyancing-national-law": (S, ["real-estate", "legal-compliance"]),
    "eprivacy-directive":        (H, ["marketing-advertising", "media", "e-commerce-platform", "data-analytics"]),
    "esign-ueta":                (H, ["legal-compliance", "real-estate", "financial-services"]),
    "eu-ai-act":                 (H, ["artificial-intelligence", "healthcare", "human-capital-management", "education", "government", "cybersecurity"]),
    "eu-chips-act":              (S, ["semiconductors-hardware", "industrial"]),
    "eu-cyber-resilience-act":   (H, ["cybersecurity", "iot", "developer-tools", "enterprise-software", "semiconductors-hardware", "technology"]),
    "eu-data-act":               (H, ["cloud-data-platform", "iot", "automotive", "industrial", "enterprise-software"]),
    "eu-ivdr":                   (S, ["biotechnology", "life-sciences", "healthcare", "pharmaceutical"]),
    "eu-machinery-regulation":   (S, ["industrial", "robotics", "automotive"]),
    "eu-mdr":                    (S, ["healthcare", "life-sciences", "digital-health", "biotechnology"]),
    "eu-taxonomy":               (S, ["climate-sustainability", "financial-services", "banking", "energy"]),
    "eudr":                      (S, ["supply-chain", "agriculture", "consumer-goods", "retail", "climate-sustainability"]),
    "european-accessibility-act": (H, ["e-commerce-platform", "banking", "media", "video-streaming", "travel-technology", "technology"]),
    "faa-part-107":              (S, ["aerospace", "air-traffic-airspace", "robotics"]),
    "fatf-travel-rule":          (S, ["blockchain-crypto", "payments", "financial-services", "banking"]),
    "fca-pra-insurance-regulation": (S, ["insurance", "financial-services"]),
    "fcra":                      (S, ["financial-services", "banking", "human-capital-management", "real-estate"]),
    "ferc-order-889":            (S, ["energy", "utilities"]),
    "ferpa":                     (S, ["education"]),
    "fmcsa-eld-mandate":         (S, ["logistics", "transportation", "mobility"]),
    "fsma-204":                  (S, ["food-service", "food-delivery", "agriculture", "supply-chain", "consumer-goods"]),
    "gdpr":                      (H, ["marketing-advertising", "artificial-intelligence", "healthcare", "data-analytics", "technology"]),
    "glba":                      (S, ["banking", "financial-services", "insurance", "financial-technology"]),
    "gxp":                       (S, ["pharmaceutical", "life-sciences", "biotechnology", "healthcare"]),
    "hipaa":                     (S, ["healthcare", "digital-health", "insurance", "life-sciences"]),
    "hitech":                    (S, ["healthcare", "digital-health"]),
    "iata-resolution-787":       (S, ["travel-technology", "transportation", "aerospace"]),
    "iata-resolution-824":       (S, ["travel-technology", "transportation", "aerospace"]),
    "iata-resolution-850m":      (S, ["travel-technology", "transportation", "aerospace"]),
    "idx-policy":                (S, ["real-estate"]),
    "itu-constitution":          (S, ["telecommunications", "space"]),
    "lksg":                      (S, ["supply-chain", "consumer-goods", "industrial", "retail"]),
    "mccarran-ferguson-act":     (S, ["insurance"]),
    "mica":                      (S, ["blockchain-crypto", "financial-services", "payments"]),
    "mifid-ii":                  (S, ["financial-services", "banking"]),
    "naic-model-laws":           (S, ["insurance"]),
    "nar-policy-statement-790":  (S, ["real-estate"]),
    "nhs-dspt":                  (S, ["healthcare", "digital-health", "cybersecurity"]),
    "nis2":                      (H, ["cybersecurity", "cloud-data-platform", "energy", "utilities", "healthcare", "telecommunications", "transportation", "government"]),
    "ofgem-data-best-practice":  (S, ["energy", "utilities"]),
    "onc-health-it-certification": (S, ["healthcare", "digital-health"]),
    "ontario-reg-633-21":        (S, ["energy", "utilities"]),
    "open-government-licence":   (S, ["government", "data-analytics"]),
    "osfi-guideline-b13":        (S, ["banking", "insurance", "financial-services", "cybersecurity"]),
    "package-travel-regulations-2018": (S, ["travel-technology"]),
    "phipa":                     (S, ["healthcare", "digital-health"]),
    "pipeda":                    (H, ["technology", "marketing-advertising", "data-analytics", "artificial-intelligence"]),
    "psd2":                      (S, ["banking", "payments", "financial-technology", "financial-services"]),
    "psd3-psr":                  (S, ["banking", "payments", "financial-technology", "financial-services"]),
    "quebec-law-25":             (H, ["technology", "marketing-advertising", "artificial-intelligence", "data-analytics"]),
    "retail-payment-activities-act": (S, ["payments", "financial-technology"]),
    "rohs":                      (S, ["semiconductors-hardware", "industrial", "consumer-goods", "iot"]),
    "sarbanes-oxley":            (H, ["accounting-finance-ops", "financial-services", "enterprise-software"]),
    "section-508":               (S, ["government", "technology"]),
    "sfdr":                      (S, ["financial-services", "banking", "climate-sustainability"]),
    "sopipa":                    (S, ["education"]),
    "strong-customer-authentication": (S, ["payments", "banking", "financial-technology", "e-commerce-platform"]),
    "tefca":                     (S, ["healthcare", "digital-health"]),
    "uflpa":                     (S, ["supply-chain", "consumer-goods", "retail", "semiconductors-hardware"]),
    "uk-communications-act-2003": (S, ["telecommunications", "media"]),
    "uk-smart-energy-code":      (S, ["energy", "utilities"]),
    "unece-wp29":                (S, ["automotive", "cybersecurity", "mobility"]),
    "us-advanced-computing-export-controls": (S, ["semiconductors-hardware", "artificial-intelligence", "cloud-data-platform"]),
    "us-chips-act":              (S, ["semiconductors-hardware", "industrial"]),
    "us-communications-act":     (S, ["telecommunications", "media"]),
    "vow-policy":                (S, ["real-estate"]),
    # --- 2026 internet + software technology round -------------------------------
    "digital-services-act":      (H, ["technology", "media", "e-commerce-platform", "video-streaming", "creator-economy", "marketing-advertising", "artificial-intelligence"]),
    "eu-digital-omnibus":        (H, ["artificial-intelligence", "technology", "cybersecurity", "cloud-data-platform", "financial-services"]),
    "eidas2-digital-identity-wallet": (H, ["cybersecurity", "government", "banking", "financial-services", "technology", "legal-compliance"]),
    "uk-online-safety-act":      (H, ["technology", "media", "video-streaming", "gaming", "creator-economy", "artificial-intelligence", "communications-platform-as-a-service-cpaas"]),
    "data-use-and-access-act":   (H, ["technology", "data-analytics", "artificial-intelligence", "marketing-advertising", "banking", "financial-services", "healthcare"]),
    "psti-act":                  (S, ["iot", "consumer-goods", "cybersecurity", "semiconductors-hardware", "hvac-building-automation", "telecommunications"]),
    "uk-cyber-security-and-resilience-bill": (S, ["cybersecurity", "cloud-data-platform", "energy", "utilities", "healthcare", "telecommunications", "transportation", "government"]),
    "us-state-comprehensive-privacy-laws": (H, ["technology", "marketing-advertising", "data-analytics", "e-commerce-platform", "retail", "artificial-intelligence"]),
    "colorado-ai-act":           (H, ["artificial-intelligence", "human-capital-management", "banking", "insurance", "healthcare", "education", "real-estate"]),
    "texas-traiga":              (H, ["artificial-intelligence", "government", "healthcare", "financial-services", "human-capital-management"]),
    "california-sb-53":          (S, ["artificial-intelligence", "cloud-data-platform", "technology"]),
    "california-ab-2013":        (H, ["artificial-intelligence", "technology", "developer-tools", "media", "creator-economy"]),
    "us-state-employment-ai-laws": (S, ["human-capital-management", "artificial-intelligence", "professional-services", "enterprise-software"]),
    "illinois-bipa":             (H, ["artificial-intelligence", "cybersecurity", "human-capital-management", "retail", "technology", "healthcare"]),
    "washington-my-health-my-data": (H, ["digital-health", "healthcare", "fitness-wellness", "artificial-intelligence", "marketing-advertising", "technology"]),
    "doj-bulk-sensitive-data-rule": (H, ["technology", "cloud-data-platform", "data-analytics", "artificial-intelligence", "healthcare", "financial-services", "cybersecurity"]),
    "sec-cybersecurity-disclosure": (H, ["cybersecurity", "financial-services", "technology", "enterprise-software", "accounting-finance-ops"]),
    "us-state-age-verification-laws": (H, ["technology", "video-streaming", "gaming", "creator-economy", "media", "e-commerce-platform"]),
    "app-store-accountability-laws": (H, ["technology", "gaming", "creator-economy", "e-commerce-platform", "media"]),
    "ada-title-iii":             (H, ["e-commerce-platform", "retail", "banking", "travel-technology", "healthcare", "education", "technology"]),
    "casl":                      (H, ["marketing-advertising", "e-commerce-platform", "technology", "communications-platform-as-a-service-cpaas", "enterprise-software", "developer-tools"]),
    "ppcda-bill-c-36":           (H, ["technology", "marketing-advertising", "data-analytics", "artificial-intelligence", "financial-services", "e-commerce-platform"]),
    "safe-social-media-act-bill-c-34": (H, ["technology", "media", "artificial-intelligence", "video-streaming", "creator-economy", "gaming"]),
    "aoda":                      (H, ["e-commerce-platform", "retail", "education", "government", "banking", "technology"]),
    "australia-online-safety-act": (H, ["technology", "media", "video-streaming", "gaming", "creator-economy", "artificial-intelligence"]),
    "australia-cyber-security-act": (H, ["cybersecurity", "iot", "consumer-goods", "technology", "enterprise-software", "semiconductors-hardware"]),
    "soci-act":                  (S, ["cybersecurity", "cloud-data-platform", "energy", "utilities", "healthcare", "telecommunications", "transportation", "banking"]),
    "spam-act-2003":             (H, ["marketing-advertising", "e-commerce-platform", "communications-platform-as-a-service-cpaas", "retail", "technology"]),
}

MANAGED = ("scope", "countries", "regions", "industries")


def block(key, values):
    if not values:
        return []
    return [f"{key}:"] + [f"- {v}" for v in values]


def main():
    vocab_root = os.path.expanduser("~/GitHub/api-search")
    countries_ok = {f[:-3] for f in os.listdir(f"{vocab_root}/countries/_countries")}
    industries_ok = {f[:-3] for f in os.listdir(f"{vocab_root}/industries/_industries")}
    regions_ok = {f[:-3] for f in os.listdir(f"{vocab_root}/regions/_regions")}

    changed = unknown_j = 0
    problems = []

    for path in sorted(glob.glob(os.path.join(STORE, "*.md"))):
        slug = os.path.basename(path)[:-3]
        lines = open(path).read().split("\n")

        # locate front matter
        if lines[0].strip() != "---":
            problems.append(f"{slug}: no front matter")
            continue
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")

        jm = next((i for i in range(1, end) if lines[i].startswith("jurisdiction:")), None)
        if jm is None:
            problems.append(f"{slug}: no jurisdiction:")
            continue
        jur = lines[jm][len("jurisdiction:"):].strip()

        if jur not in JURISDICTION:
            problems.append(f"{slug}: UNMAPPED jurisdiction {jur!r}")
            unknown_j += 1
            continue
        countries, regions = JURISDICTION[jur]

        if slug not in MAP:
            problems.append(f"{slug}: no scope/industries mapping")
            continue
        scope, industries = MAP[slug]

        for name, vals, ok in (("country", countries, countries_ok),
                               ("region", regions, regions_ok),
                               ("industry", industries, industries_ok)):
            for v in vals:
                if v not in ok:
                    problems.append(f"{slug}: {name} slug {v!r} not in vocabulary")

        # strip any previously-managed keys (idempotence)
        out, i = [], 1
        while i < end:
            k = re.match(r"^([a-zA-Z_][a-zA-Z_0-9]*):", lines[i])
            if k and k.group(1) in MANAGED:
                i += 1
                while i < end and (lines[i].startswith("- ") or lines[i].startswith("  ")):
                    i += 1
                continue
            out.append(lines[i])
            i += 1

        # re-insert directly after jurisdiction:
        at = next(i for i, l in enumerate(out) if l.startswith("jurisdiction:")) + 1
        new = ([f"scope: {scope}"] + block("countries", countries)
               + block("regions", regions) + block("industries", industries))
        body = out[:at] + new + out[at:]

        rebuilt = "\n".join(["---"] + body + lines[end:])
        if rebuilt != "\n".join(lines):
            open(path, "w").write(rebuilt)
            changed += 1

    emit_joins_data()
    print(f"{changed} file(s) updated, {unknown_j} unmapped jurisdiction(s)")
    if problems:
        print("\nPROBLEMS:")
        for p in problems:
            print("  " + p)
        return 1
    return 0



def emit_joins_data():
    """Write _data/joins.yml — display name AND a resolved URL for every linkable term.

    The URL is resolved here, once, against the checkouts rather than assembled in the
    template, because the two hosts do not carry the same vocabulary. providers.apievangelist.com
    has all 82 industries but only 27 of the 48 countries; apis.io carries the full vocabulary
    for all three. Building the href in Liquid would have shipped a dead link for every EU
    regulation that names Austria, Belgium, Denmark, Estonia or Portugal — 31 regulations
    x 5 countries, and nothing would have reported it.

    Preference is the AE network page when it exists (richer provider listing, same network),
    apis.io otherwise. A term that resolves nowhere gets no url and the layout renders it as
    plain text instead of a link.
    """
    import yaml
    apis = os.path.expanduser("~/GitHub/api-search")
    prov = os.path.expanduser("~/GitHub/api-evangelist/providers")

    def ae_pages(sub):
        d = os.path.join(prov, sub)
        if not os.path.isdir(d):
            return set()
        return {x for x in os.listdir(d) if os.path.isdir(os.path.join(d, x))}

    ae = {"countries": ae_pages("countries"), "industries": ae_pages("industries"), "regions": set()}

    out, unresolved = {}, []
    for key, path, flag in (("countries", f"{apis}/countries/_countries", True),
                            ("regions", f"{apis}/regions/_regions", False),
                            ("industries", f"{apis}/industries/_industries", False)):
        terms = {}
        for f in sorted(os.listdir(path)):
            if not f.endswith(".md"):
                continue
            slug = f[:-3]
            fm = open(os.path.join(path, f)).read().split("---")[1]
            name = re.search(r"^name:\s*(.+)$", fm, re.M)
            entry = {"name": name.group(1).strip().strip('"\'') if name else slug}
            if flag:
                em = re.search(r"^flag:\s*(.+)$", fm, re.M)
                if em:
                    entry["flag"] = em.group(1).strip()
            if slug in ae[key]:
                entry["url"] = f"https://providers.apievangelist.com/{key}/{slug}/"
            elif os.path.isdir(os.path.join(apis, key)):
                entry["url"] = f"https://apis.io/{key}/{slug}/"
            else:
                unresolved.append(f"{key}/{slug}")
            terms[slug] = entry
        out[key] = terms

    dest = os.path.join(os.path.dirname(STORE), "_data", "joins.yml")
    with open(dest, "w") as fh:
        fh.write("# GENERATED by scripts/normalize_joins.py — do not hand-edit.\n"
                 "# Display name + resolved URL for every country/region/industry slug the\n"
                 "# regulation front matter joins on. URLs prefer providers.apievangelist.com\n"
                 "# and fall back to apis.io; a term with no url renders as plain text.\n")
        yaml.safe_dump(out, fh, allow_unicode=True, sort_keys=True, default_flow_style=False)
    total = sum(len(v) for v in out.values())
    linked = sum(1 for v in out.values() for t in v.values() if "url" in t)
    print(f"_data/joins.yml: {total} terms, {linked} linked"
          + (f", UNRESOLVED: {unresolved}" if unresolved else ""))


if __name__ == "__main__":
    sys.exit(main())
