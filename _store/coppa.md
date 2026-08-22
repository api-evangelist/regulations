---
name: COPPA
kind: regulation
jurisdiction: United States
slug: coppa
title: Children's Online Privacy Protection Act (COPPA)
description: COPPA governs the online collection of personal information from children under thirteen
  in the United States. It requires verifiable parental consent before collection, limits retention, requires
  disclosure of what is collected and why, and gives parents the right to review and delete. In education
  it operates alongside FERPA, and schools may consent on a parent's behalf in defined circumstances.
tags:
- Privacy
- Children
- Education
- Consent
- United States
- Regulation
common:
- type: Regulator
  url: https://www.ftc.gov/business-guidance/privacy-security/childrens-privacy
- type: Legislation
  url: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-312
url: https://www.ftc.gov/legal-library/browse/rules/childrens-online-privacy-protection-rule-coppa
yearCreated: 1998
alternativeNames:
- Children's Online Privacy Protection Act
- COPPA Rule
- 16 CFR Part 312
companyCount: 14
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 70
precisionGrade: medium
precisionBasis:
- 'acronym-shape -5: shortest bare needle is 5 characters, halved — it neither collides nor appears in
  the corpus frequency table'
- 'bare-channel -25: 100% of matching companies were reached only on the bare word (14 bare vs 0 phrase)'
---

**COPPA** is the strictest consent regime reaching any market in this research, because the subject cannot give consent themselves. Every K-12 EdTech product in the United States operates inside it, and the mechanism it depends on — **verifiable parental consent**, sometimes exercised by the school — is a delegation chain with at least three parties in it.

  * **Verifiable parental consent** - Not a checkbox: the standard requires a method reasonably calculated to confirm a parent gave it.
  * **School-based consent** - In an educational context a school may consent on the parent's behalf for school purposes, which moves the delegation.
  * **Data minimisation and retention limits** - Collect what the activity needs, keep it no longer than necessary.
  * **Parental review and deletion** - Rights that have to be honoured across every downstream system the data reached.
  * **FTC enforcement** - Civil penalties per violation, and an active enforcement record against EdTech.

COPPA makes the education market's consent gap concrete. A parent consents, a school sometimes consents on their behalf, a vendor relies on that consent, and a subprocessor relies on the vendor — and at no point in *The State of Education & EdTech APIs*'s 814-organization cohort is that chain expressed as anything a machine can read. The K-12 segment carrying the heaviest COPPA exposure scores 17.3 and publishes a machine-readable contract 15.9% of the time.
