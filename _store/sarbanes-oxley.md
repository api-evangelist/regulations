---
standards:
- title: OSCAL
  url: https://standards.apievangelist.com/store/oscal/
  note: The format that would make SOX control evidence exchangeable between systems rather than re-keyed.
name: Sarbanes-Oxley
kind: regulation
jurisdiction: United States
slug: sarbanes-oxley
title: Sarbanes-Oxley Act (SOX)
description: Sarbanes-Oxley requires management of US public companies to assess and attest to the effectiveness
  of internal control over financial reporting, with auditor attestation alongside. Sections 302 and 404
  are the operative ones, and between them they created the modern governance, risk and compliance software
  market.
tags:
- Financial Reporting
- Internal Controls
- Audit
- GRC
- United States
- Regulation
common:
- type: Regulator
  url: https://pcaobus.org/
- type: Legislation
  url: https://www.congress.gov/bill/107th-congress/house-bill/3763
url: https://www.sec.gov/spotlight/sarbanes-oxley.htm
yearCreated: 2002
alternativeNames:
- SOX
- Sarbanes-Oxley Act of 2002
- Public Company Accounting Reform Act
companyCount: 500
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 85
precisionGrade: high
precisionBasis:
- 'human verdict: `sox` sampled clean as the statute; no competing sense appeared in the sample.'
---

**Sarbanes-Oxley** is the origin of the GRC industry. Requiring management to attest, personally, that controls over financial reporting are effective turned control testing from an internal-audit activity into a continuous, evidenced, software-supported discipline — and created demand for every platform that automates it.

  * **Section 302** - Officer certification of disclosure controls, with personal liability attached.
  * **Section 404** - Management assessment of internal control over financial reporting, with auditor attestation.
  * **Evidence over assertion** - Controls must be tested and the testing documented, which is what the software exists to do.
  * **The PCAOB** - An audit regulator created by the Act, which sets the standards auditors apply.
  * **Beyond public companies** - Private companies approaching an IPO, and their suppliers, adopt the discipline early.

SOX created the market that *The State of Legal & Compliance APIs* scores at 24.1 with 28.6% publishing a machine-readable contract, inside a market whose governance facet is 9.1 with two-thirds at zero. The obligation SOX creates — evidence a control operated, repeatably, in a form an auditor accepts — is exactly what [OSCAL](https://standards.apievangelist.com/store/oscal/) was built to make exchangeable. Twenty-four years on, most of that evidence still moves as documents.
