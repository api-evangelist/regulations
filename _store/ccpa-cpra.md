---
headers:
- name: sec-gpc
  basis: mandated
  observable: edge
  standard: global-privacy-control
  note: 'The strongest case in the entire catalog: a request header that California recognises as a legally
    binding opt-out signal, with Colorado and Connecticut following through their universal-opt-out lists.
    Zero providers in the catalog declare it.'
papers:
- title: The State of Marketing & Advertising APIs
  url: https://reports.apievangelist.com/reports/state-of-marketing-advertising-apis/
  note: Sale and sharing of personal information, global opt-out signals, and the data-broker registry
    several companies in that cohort appear on — in a market describing consent in its APIs at 3.1%.
- title: The State of Data & Analytics APIs
  url: https://reports.apievangelist.com/reports/state-of-data-analytics-apis/
  note: 'Reaches the data-provider segment directly: people data, firmographics and web extraction, where
    consent is legible at 2.7% of the market.'
name: CCPA / CPRA
kind: regulation
jurisdiction: United States (California)
slug: ccpa-cpra
title: California Consumer Privacy Act (CCPA/CPRA)
description: The California Consumer Privacy Act, as amended and expanded by the California Privacy Rights
  Act, gives Californians rights over the personal information businesses hold about them — to know, to
  delete, to correct, and to opt out of its sale or sharing. It created a dedicated regulator in the California
  Privacy Protection Agency, a registry for data brokers, and an opt-out signal browsers can send on a
  person's behalf.
tags:
- Privacy
- Consumer Rights
- Data Brokers
- United States
- California
- Regulation
common:
- type: Regulator
  url: https://cppa.ca.gov/
- type: Legislation
  url: https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?division=3.&part=4.&lawCode=CIV&title=1.81.5
url: https://cppa.ca.gov/regulations/
yearCreated: 2018
alternativeNames:
- CCPA
- CPRA
- California Consumer Privacy Act
- California Privacy Rights Act
companyCount: 171
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 47
precisionGrade: low
precisionBasis:
- 'acronym-shape -20: shortest bare needle is 4 characters'
- 'collision -25: a surviving needle is also claimed by standards:CCPA'
- 'bare-channel -8: 73% of matching companies were reached only on the bare word (132 bare vs 49 phrase)'
precisionRecognition: 72
---

**CCPA and CPRA** are the closest the United States has to a general privacy law, and they arrived state-first rather than federally. What makes them interesting for API operations is less the rights themselves than their machine-readable edges: a required response to the Global Privacy Control signal, a public data-broker registry, and deletion and opt-out obligations that have to propagate to every downstream recipient of the data.

  * **Right to know, delete and correct** - Obligations that land on whatever system actually holds the record, which in practice means several.
  * **Opt-out of sale and sharing** - 'Sharing' explicitly covers cross-context behavioural advertising, which is what makes this an adtech rule as much as a privacy one.
  * **The data-broker registry** - Businesses meeting the definition register publicly — a rare case of a regulator publishing a machine-readable list of who holds data about people.
  * **Global Privacy Control** - A browser-level opt-out signal that must be honoured, and one of the few consent artifacts that travels automatically rather than by conversation.
  * **A dedicated regulator** - The CPPA has rulemaking and enforcement authority, which distinguishes this from the sectoral US regimes around it.

The reason this regime keeps appearing in API Evangelist research is the propagation problem. An opt-out or a deletion is trivial to honour in one system and hard to honour across the fifteen a business integrated — and in the two markets where it bites hardest, the interfaces do not describe permission at all. [The State of Marketing & Advertising APIs](https://reports.apievangelist.com/reports/state-of-marketing-advertising-apis/) finds consent legible in 3.1% of that market's APIs, and [The State of Data & Analytics APIs](https://reports.apievangelist.com/reports/state-of-data-analytics-apis/) finds `preferences` and `suppression` published as resources by nobody at all. The obligation is unambiguous and the artifact that would satisfy it at machine speed is missing, which is an opportunity rather than only a risk.
