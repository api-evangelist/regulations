---
papers:
- title: The State of Supply Chain APIs
  url: https://reports.apievangelist.com/reports/state-of-supply-chain-apis/
  note: A due diligence obligation that lands on the report rather than the interface — the mechanism
    behind an industry that buys reporting software instead of building contracts.
name: Corporate Sustainability Due Diligence Directive
kind: directive
jurisdiction: European Union
slug: csddd
title: Corporate Sustainability Due Diligence Directive (CSDDD)
description: Directive (EU) 2024/1760 requires large companies operating in the EU to identify, prevent,
  mitigate and account for adverse human rights and environmental impacts across their own operations,
  their subsidiaries, and their chains of activities — with a transition plan for climate change mitigation.
tags:
- Supply Chain
- Human Rights
- Sustainability
- Due Diligence
- European Union
- Regulation
common:
- type: Website
  url: https://commission.europa.eu/business-economy-euro/doing-business-eu/sustainability-due-diligence-responsible-business_en
url: https://commission.europa.eu/business-economy-euro/doing-business-eu/sustainability-due-diligence-responsible-business_en
yearCreated: 2024
alternativeNames:
- CSDDD
- CS3D
- Directive (EU) 2024/1760
companyCount: 4
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 90
precisionGrade: high
precisionBasis:
- 'acronym-shape -10: shortest bare needle is 4 characters, halved — it neither collides nor appears in
  the corpus frequency table'
---

The **Corporate Sustainability Due Diligence Directive** obliges large companies to run a risk-based
due diligence process across their chain of activities — identify adverse human rights and
environmental impacts, act to prevent or end them, and report on it. It is the EU-level sibling of
Germany's [LkSG](/store/lksg/), and it applies to non-EU companies above a turnover threshold in the
EU market as well.

  * **Chain of activities, not just tier one** - The obligation reaches upstream to established business relationships, which is where the data problem begins.
  * **Risk-based, not exhaustive** - Companies prioritize by severity and likelihood, which leaves the depth of the evidence to the company.
  * **Climate transition plan** - A separate obligation to adopt a plan compatible with limiting warming to 1.5°C.
  * **Civil liability** - Member states must provide for liability for damage caused by failure to comply.

For API operations the salient fact is what the directive does *not* say. It requires a company to
know things about its suppliers and to report what it knows. It specifies no exchange format, no
interface, and no interoperability requirement between the companies that have to share the
underlying data. A company can satisfy it completely with a questionnaire, a warehouse and a PDF,
and *The State of Supply Chain APIs* found that most do — which is why supply chain carries a wave
of new regulation and no corresponding rise in machine-readable contracts.
