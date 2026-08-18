---
papers:
- title: The State of UK Energy APIs
  url: https://reports.apievangelist.com/reports/state-of-uk-energy-apis/
  note: The reason Britain's distribution networks out-publish every mandated market in the study — UK
    Power Networks and Northern Powergrid both hit 94.2 agent-readiness under a 'presumed open' licence
    condition, not a consumer data right.
standards:
- title: OpenAPI
  url: https://standards.apievangelist.com/store/openapi/
  note: The DNO open-data portals publish OpenAPI 3.0.3 contracts alongside DCAT catalogues to satisfy
    the guidance.
name: Ofgem Data Best Practice Guidance
slug: ofgem-data-best-practice
title: Ofgem Data Best Practice Guidance
kind: regulator-guidance
jurisdiction: Great Britain
description: Ofgem's Data Best Practice Guidance sets the data obligations of Great Britain's energy network
  licensees. Published in November 2021 and applied through licence conditions under the RIIO price controls,
  its defining principle is that Energy System Data is "presumed open" — a licensee must publish unless
  it can justify withholding. It is an open-data mandate aimed at network operational data rather than
  at consumer data, and it is the reason British distribution networks publish better than the utilities
  of any mandated market studied.
tags:
- Energy
- Open Data
- United Kingdom
- Networks
- Regulation
common:
- type: Regulator
  url: https://www.ofgem.gov.uk/
- type: Guidance
  url: https://www.ofgem.gov.uk/publications/data-best-practice-guidance
url: https://www.ofgem.gov.uk/
yearCreated: 2021
alternativeNames:
- Data Best Practice
- DBP
- RIIO data licence conditions
- Presumed Open
companyCount: 3
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 85
precisionGrade: high
precisionBasis:
- 'acronym-shape -15: shortest bare needle is 3 characters, halved — it neither collides nor appears in
  the corpus frequency table'
---

**Ofgem's Data Best Practice Guidance** is the most under-discussed data mandate in this catalog, and on
the evidence it is one of the most effective.

It applies to Great Britain's network licensees — the distribution and transmission operators — through
licence conditions attached to the **RIIO** price controls. Version 1.0 landed in November 2021. The
principle that matters is **"presumed open"**: Energy System Data must be published unless the licensee
can justify not publishing it. The default is inverted from almost every other regime in this catalog.

*   **A licence condition, not a statute** - enforcement runs through the regulator's control of the
    licence rather than through a court, which makes it fast to apply and specific to the licensed party.
*   **Aimed at network data, not customer data** - it covers substation capacity, outages, connections
    and system data. It is *not* a consumer data right, and Great Britain still has none.
*   **Presumption inverted** - most regimes require disclosure of enumerated things. This one requires
    disclosure of everything, with the burden on the licensee to argue otherwise.
*   **Attached to a price control** - RIIO funds network investment, so digitalisation obligations arrive
    with the money rather than as an unfunded requirement.

## What it produced

*The State of UK Energy APIs* scored twenty-six organizations and found the distribution networks at the
top of the machine-readable rankings. **UK Power Networks and Northern Powergrid both score 94.2 on
agent-readiness — the highest figures in the entire four-market energy study, above anything in
mandate-driven Australia.** Electricity North West follows at 79.8, SSEN at 78.8.

These are regional monopolies with no competitive pressure and no consumer-facing data obligation. The
guidance is what explains them, and it is worth stating precisely because it is easy to misread the
result as voluntary excellence. It was not. Britain aimed a real open-data obligation at network
operational data and got world-class results exactly where it aimed.

The counter-example inside the same regime is instructive: **National Grid Electricity Distribution
scores 35.1 with 28.8 agent-readiness** under the identical price control and identical licence
condition. **The obligation sets a floor, not an outcome.**

Read alongside the [Consumer Data Right](https://regulations.apievangelist.com/store/consumer-data-right/),
which aimed a comparable instrument at *customer* data in Australia and produced thirteen live consumer
APIs. Britain and Australia both mandated. They mandated different things, and each got what it asked for.
