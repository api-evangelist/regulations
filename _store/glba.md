---
headers:
- name: cache-control
  basis: evidentiary
  observable: edge
- name: strict-transport-security
  basis: evidentiary
  observable: edge
  note: The FTC's 2021 Safeguards amendments require encryption in transit explicitly.
papers:
- title: The State of Blockchain & Crypto APIs
  url: https://reports.apievangelist.com/reports/state-of-blockchain-crypto-apis/
  note: Where a crypto firm is a money services business.
- title: The State of Data & Analytics APIs
  url: https://reports.apievangelist.com/reports/state-of-data-analytics-apis/
  note: Financial data enrichment and transaction intelligence, inside the data-provider segment of the
    data and analytics market.
- title: The State of Artificial Intelligence APIs
  url: https://reports.apievangelist.com/reports/state-of-artificial-intelligence-apis/
  note: Reaches an AI system the moment it touches financial records — inherited exposure rather than
    a regime aimed at the sector.
- title: The State of US Banking APIs
  url: https://reports.apievangelist.com/reports/state-of-us-banking-apis/
  note: The pre-existing US financial-privacy regime the 1033 rule has to operate within — the security-and-privacy
    floor beneath open banking.
name: Gramm-Leach-Bliley Act
kind: statute
jurisdiction: United States
slug: glba
title: Gramm-Leach-Bliley Act (GLBA)
description: The Gramm-Leach-Bliley Act is the 1999 US law governing how financial institutions handle
  and protect consumers' nonpublic personal information, including the Privacy Rule and the Safeguards
  Rule. It is the long-standing privacy and data-security backdrop against which US open banking and the
  CFPB's 1033 rule operate — the pre-existing obligation that any US financial-data-sharing regime has
  to work within.
tags:
- Privacy
- Data Protection
- Security
- Finance
- United States
- Regulation
common:
- type: Legislation
  url: https://www.ftc.gov/business-guidance/privacy-security/gramm-leach-bliley-act
- type: Regulator
  url: https://www.ftc.gov/
url: https://www.ftc.gov/business-guidance/privacy-security/gramm-leach-bliley-act
yearCreated: 1999
alternativeNames:
- GLBA
- Financial Services Modernization Act of 1999
- GLB Act
companyCount: 36
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 75
precisionGrade: medium
precisionBasis:
- 'acronym-shape -10: shortest bare needle is 4 characters, halved — it neither collides nor appears in
  the corpus frequency table'
- 'bare-channel -15: 83% of matching companies were reached only on the bare word (30 bare vs 6 phrase)'
---

The **Gramm-Leach-Bliley Act (GLBA)** is the US financial-privacy law that was governing consumer financial data long before anyone said "open banking." Its Privacy Rule constrains how institutions share nonpublic personal information, and its Safeguards Rule requires them to secure it — the backdrop the CFPB's 1033 rule and the whole US data-sharing effort have to operate within.

  * **The Privacy Rule** - Governs when and how a financial institution may disclose a consumer's nonpublic personal information, and requires privacy notices.
  * **The Safeguards Rule** - Requires a written information-security program to protect that data — the security floor beneath any API that exposes it.
  * **The pre-existing regime** - Unlike the UK or Australia, where open banking arrived into a purpose-built regime, US open banking is layered on top of a twenty-five-year-old privacy law, which shapes how §1033 and the CFPB rule can operate.

GLBA is a useful reminder that the US did not lack financial-privacy law — it lacked an *access* mandate. The security and privacy obligations were always there; what was missing until the CFPB rule was the requirement to let a consumer *port* their data through an API. That gap, not a privacy vacuum, is what produced the fragmented US market I scored.
