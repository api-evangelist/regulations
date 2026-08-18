---
papers:
- title: The State of Education & EdTech APIs
  url: https://reports.apievangelist.com/reports/state-of-education-apis/
  note: Binds the EdTech operator directly rather than through the district's contract — in a K-12 segment
    publishing a contract 15.9% of the time with a governance facet of 3.3.
name: SOPIPA
kind: regulation
jurisdiction: United States (California, and state adoptions)
slug: sopipa
title: Student Online Personal Information Protection Act (SOPIPA)
description: 'SOPIPA is California''s student privacy law, and the template most other US states adopted.
  Where FERPA regulates what a school may disclose, SOPIPA regulates the operator directly: it prohibits
  targeted advertising to students, profiling for non-educational purposes, and the sale of student data,
  and requires deletion at a school''s request.'
tags:
- Privacy
- Education
- Student Data
- Children
- California
- Regulation
common:
- type: Legislation
  url: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=201320140SB1177
- type: Regulator
  url: https://oag.ca.gov/privacy/education
url: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=201320140SB1177
yearCreated: 2014
alternativeNames:
- Student Online Personal Information Protection Act
- SB 1177
- state student privacy laws
companyCount: 0
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---

**SOPIPA** shifted the obligation. FERPA governs the institution and reaches vendors through contract; SOPIPA binds the **operator** of the service directly, regardless of what the contract says. That change — plus adoption in some form by a majority of US states — is why student data is one of the more tightly constrained categories in American privacy law.

  * **No targeted advertising** - Advertising to students based on information gathered through the service is prohibited outright.
  * **No profiling for other purposes** - Profiles may not be built for anything other than K-12 educational purposes.
  * **No sale of student data** - A flat prohibition rather than an opt-out.
  * **Deletion on request** - A school can require deletion, which has to propagate to every system holding the data.
  * **Binds the operator directly** - The vendor is liable on its own account, not only through the district's contract.

SOPIPA and its state analogues are the reason the K-12 segment carries obligations closer to a regulated financial market than to ordinary SaaS — and [The State of Education & EdTech APIs](https://reports.apievangelist.com/reports/state-of-education-apis/) finds that segment publishing a machine-readable contract 15.9% of the time, with a governance facet of 3.3. A deletion obligation that has to propagate across every downstream system is an integration problem, and the interfaces that would make it tractable are largely unpublished.
