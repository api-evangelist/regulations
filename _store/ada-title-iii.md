---
name: ADA Title III (web accessibility)
kind: statute
jurisdiction: United States (federal)
scope: horizontal
countries:
- united-states
regions:
- north-america
industries:
- e-commerce-platform
- retail
- banking
- travel-technology
- healthcare
- education
- technology
slug: ada-title-iii
title: Americans with Disabilities Act Title III, as applied to websites and apps
description: 'Title III of the ADA prohibits discrimination in places of public accommodation, and US
  courts have overwhelmingly read that to reach websites and mobile apps — without any regulation
  specifying a technical standard. The result is the most litigated accessibility regime in the world
  and the least specified: thousands of suits a year, settlements that reference WCAG, and no rule
  that says so. The 2024 DOJ rule for state and local government fixed this only for the public sector.'
tags:
- Accessibility
- WCAG
- Litigation
- Public Accommodation
- United States
- Regulation
common:
- type: Legislation
  url: https://www.ada.gov/law-and-regs/ada/
- type: Regulator
  url: https://www.ada.gov/
url: https://www.ada.gov/law-and-regs/ada/
yearCreated: 1990
alternativeNames:
- ADA
- Title III
- Web accessibility litigation
- Americans with Disabilities Act
companyCountStatus: pending-corpus-pass
standards:
- title: WCAG  # wired by scripts/wire_standards_links.py
  url: https://standards.apievangelist.com/store/wcag/
  note: No US regulation names a standard for private entities, but settlements, consent decrees and
    expert testimony converge on WCAG 2.1 AA — a de facto standard that was never adopted as one.
---

**ADA Title III** is the mirror image of the European Accessibility Act, and the contrast is the most useful thing about it. The EAA specifies EN 301 549, names the products and services in scope, sets a date, and appoints market-surveillance authorities. Title III specifies nothing, names nothing digital, sets no date, and is enforced by several thousand private lawsuits a year.

  * **No technical standard for private entities** - The statute predates the web. DOJ has repeatedly declined to issue a Title III web rule.
  * **WCAG 2.1 AA by convention** - Settlements, consent decrees and expert testimony converge on it, so it is the de facto standard without ever having been adopted as one.
  * **Circuit split on whether a website alone is a public accommodation** - Some circuits require a nexus to a physical location; others do not. Your exposure genuinely depends on where you are sued.
  * **High-volume serial litigation** - A small number of firms file the large majority of claims. Most settle for well under the cost of defending.
  * **State analogues raise the stakes** - California's Unruh Act attaches statutory damages per violation, which is why so much of this litigation is filed there.
  * **The 2024 DOJ rule fixed the public sector only** - Title II entities — state and local government, including public universities — now have a real rule with WCAG 2.1 AA and dated compliance deadlines. Private companies got nothing.

I include this alongside the EAA, Section 508 and AODA deliberately, because an API provider selling into all of these markets faces one engineering task and four completely different compliance postures. The engineering task is the same in every case: conform to WCAG, and increasingly to EN 301 549's software provisions. What differs is who asks, how, and what happens if you have not.

There is an API-specific point that gets lost in a conversation dominated by screen readers and colour contrast. EN 301 549 has a software clause that reaches non-web software, and accessibility conformance increasingly attaches to the *components and SDKs* a provider ships, not only to the provider's own site. An embedded checkout widget, a hosted sign-in page, a charting library, a documentation theme — each of these lands inside a customer's product and carries the customer's compliance obligation with it.

That makes an **Accessibility Conformance Report** — the VPAT, in its EU form — a genuine artefact of an API product, in exactly the way an SBOM is. It is a structured, publishable, versioned statement about a shipped component, requested by procurement, and almost never present in developer documentation. Of everything in this catalog, it is among the easiest for a provider to produce and among the least often produced.
