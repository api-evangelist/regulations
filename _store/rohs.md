---
name: RoHS
kind: directive
jurisdiction: European Union
slug: rohs
title: RoHS, WEEE and REACH
description: The EU's material-compliance regime for electrical and electronic equipment — RoHS restricting
  hazardous substances in products, WEEE governing collection and recycling, and REACH requiring declaration
  of substances of very high concern — producing an ongoing per-part data obligation across the electronics
  supply chain.
tags:
- Hardware
- Electronics
- Environment
- Compliance
- European Union
- Regulation
common:
- type: Website
  url: https://environment.ec.europa.eu/topics/waste-and-recycling/rohs-directive_en
url: https://environment.ec.europa.eu/topics/waste-and-recycling/rohs-directive_en
yearCreated: 2003
alternativeNames:
- RoHS Directive
- Directive 2011/65/EU
- WEEE
- REACH
companyCount: 46
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 75
precisionGrade: medium
precisionBasis:
- 'human verdict: RoHS and WEEE both sampled REAL in materials-compliance postings ("reach scip rohs tsca
  WEEE", "rohs reach WEEE pfas bom"). The `REACH` alias was revoked — REACH is a separate EU regulation,
  not a spelling of RoHS, and the bare word is the English verb in 51% of corpora. REACH needs its own
  catalog entry to be measurable.'
---

**RoHS**, **WEEE** and **REACH** together form the EU's material-compliance regime for electronics.
RoHS restricts specified hazardous substances in electrical and electronic equipment, WEEE governs
end-of-life collection and recycling, and REACH obliges declaration of substances of very high
concern present above a threshold.

  * **Per-part obligation** - Compliance is asserted at the level of an individual component or assembly, so the data has to exist for every part number.
  * **Flows up the supply chain** - A manufacturer's declaration depends on declarations from every supplier beneath it.
  * **Ongoing, not one-off** - Substance lists are revised, so declarations have to be maintained.
  * **Widely mirrored** - Comparable regimes exist in other jurisdictions, and conflict-minerals reporting adds a parallel obligation.

This regime is the most useful precedent in the catalog for predicting how hardware markets respond to
a data mandate, because it has been running for two decades. It created a genuine, granular,
continuously-maintained per-part data obligation across the entire electronics industry — exactly the
data an agent selecting a component would want. **The industry answered it with spreadsheets,
supplier questionnaires and distributor portals.** Twenty years on, material declarations are still
not callable.

*The State of Compute & Hardware APIs* reads the [EU Cyber Resilience
Act](/store/eu-cyber-resilience-act/) against this precedent. The CRA is the first regulation to
require an ongoing structured security data flow from hardware manufacturers to their customers.
Whether it is met with a portal or an endpoint is the open question, and RoHS is the reason not to
assume the answer.
