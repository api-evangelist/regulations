---
papers:
- title: The State of Legal & Compliance APIs
  url: https://reports.apievangelist.com/reports/state-of-legal-compliance-apis/
  note: Why an agreement executed through an API is enforceable in the US — technology-neutral where eIDAS
    is verifiable, and both underpin the market's strongest segment.
standards:
- title: AdES
  url: https://standards.apievangelist.com/store/ades/
  note: The European approach specifies the cryptographic construction; ESIGN and UETA deliberately do
    not.
name: ESIGN and UETA
kind: regulation
jurisdiction: United States
slug: esign-ueta
title: ESIGN Act and UETA
description: ESIGN is the US federal statute giving electronic signatures and records the same legal effect
  as their paper equivalents, and UETA is the uniform state law adopted in almost every state that does
  the same at state level. Together they are why an agreement executed through an API is enforceable in
  the United States.
tags:
- E-Signature
- Contracts
- Legal
- United States
- Regulation
common:
- type: Legislation
  url: https://www.congress.gov/bill/106th-congress/senate-bill/761
- type: Regulator
  url: https://www.uniformlaws.org/committees/community-home?CommunityKey=2c04b76c-2b7d-4399-977e-d5876ba7e034
url: https://www.fdic.gov/regulations/compliance/manual/10/x-3.1.pdf
yearCreated: 1999
alternativeNames:
- ESIGN Act
- Electronic Signatures in Global and National Commerce Act
- UETA
- Uniform Electronic Transactions Act
companyCount: 1
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

**ESIGN and UETA** removed the question of whether an electronic signature counts. What they did not do is specify a format: unlike [eIDAS](https://regulations.apievangelist.com/store/eidas/) in Europe, the American approach is technology-neutral, requiring intent, consent, attribution and a retainable record rather than a particular cryptographic construction.

  * **Legal effect, not format** - A signature may not be denied effect for being electronic; how it is made is left open.
  * **Consumer consent** - ESIGN requires disclosure and affirmative consent before electronic records replace paper for consumers.
  * **Attribution and intent** - The evidentiary questions move to who signed and whether they meant to — which is what audit trails exist to answer.
  * **Record retention** - The record must be capable of accurate reproduction, which shapes retention design.
  * **Carve-outs** - Wills, certain family law and some notices remain outside, which is why some workflows stay on paper.

The contrast with Europe is instructive and it shows up in the scores. eIDAS attaches legal consequence to a **machine-verifiable** artifact; ESIGN and UETA attach it to intent and process. Both produced a functioning e-signature market, and [The State of Legal & Compliance APIs](https://reports.apievangelist.com/reports/state-of-legal-compliance-apis/) finds that market leading its sector on published contracts at 55.0% — well ahead of the contract-management segment next door at 18.2%. Where a legal requirement lands on the artifact, the artifact gets published.
