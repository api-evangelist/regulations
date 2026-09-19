---
name: DOJ Bulk Sensitive Data Rule
kind: regulation
jurisdiction: United States (federal)
scope: horizontal
countries:
- united-states
regions:
- north-america
industries:
- technology
- cloud-data-platform
- data-analytics
- artificial-intelligence
- healthcare
- financial-services
- cybersecurity
slug: doj-bulk-sensitive-data-rule
title: Preventing Access to US Sensitive Personal Data by Countries of Concern (28 CFR Part 202)
description: The DOJ Data Security Program prohibits or restricts transfers of bulk US sensitive personal
  data and government-related data to countries of concern and to covered persons — including through
  ordinary vendor, employment and investment agreements. It is a national-security regime that operates
  on the shape of a company's data flows and supply chain, it has been fully in force since October 2025,
  and it reaches a very large number of companies that have never thought of themselves as export-controlled.
tags:
- Data Security
- Export Control
- National Security
- Third-Party Risk
- United States
- Regulation
common:
- type: Legislation
  url: https://www.ecfr.gov/current/title-28/chapter-I/part-202
- type: Regulator
  url: https://www.justice.gov/nsd/data-security
url: https://www.justice.gov/nsd/data-security
yearCreated: 2025
alternativeNames:
- Data Security Program
- DSP
- 28 CFR Part 202
- Bulk Data Rule
companyCount: 97
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 64
precisionGrade: medium
precisionBasis:
- 'acronym-shape -15: shortest bare needle is 3 characters, halved — it neither collides nor appears in
  the corpus frequency table'
- 'bare-channel -21: 94% of matching companies were reached only on the bare word (95 bare vs 6 phrase)'
---

The **DOJ Data Security Program** is the American regulation I most often find missing from a compliance inventory, and the one whose absence surprises me most, because it is the only US rule that can make a routine vendor contract unlawful.

It implements Executive Order 14117 and it does not work like privacy law. It does not care about consent, notice or purpose. It cares about **who ends up with the data**.

  * **Six categories of covered data** - Precise geolocation, biometric identifiers, human genomic and other 'omic data, personal health data, personal financial data, and certain personal identifiers. Plus government-related data, which has no volume threshold at all.
  * **Bulk thresholds, and they are low** - As few as 100 US persons for genomic data, 1,000 for biometric or precise geolocation, 10,000 for health or financial, 100,000 for identifiers — measured over any twelve months.
  * **Countries of concern and covered persons** - China (including Hong Kong and Macau), Russia, Iran, North Korea, Cuba and Venezuela, plus entities and individuals subject to their control or direction — which includes employees and contractors.
  * **Prohibited versus restricted** - Data brokerage and human 'omic transfers are prohibited outright. Vendor, employment and investment agreements are restricted: permitted only with CISA-specified security requirements in place.
  * **Full compliance since 6 October 2025** - Audits, due diligence and reporting obligations are live, not pending.

The reason this catches software companies is that "vendor agreement" and "employment agreement" are the ordinary furniture of a technology business. A contractor in a covered country with production access to a database over the threshold is a restricted transaction. An offshore support desk that can pull customer records is a restricted transaction. A cloud region choice can be one. None of this looks like exporting anything.

There is a second-order effect worth planning for. The rule pushes companies toward being able to answer, concretely and on demand, *who can reach which data from where* — not as a policy claim but as an enumerable fact about their systems. That is an access-control and data-residency question expressed as a national-security obligation, and it is the same question DORA asks of financial firms about their ICT providers, and the same question the EU Data Act asks about third-country government access to cloud data. Three regimes, three rationales, one underlying capability.

Most providers cannot produce that answer today. The ones that can tend to have built it for a different reason — FedRAMP, or a sovereign-cloud sales requirement — which is the usual pattern: the capability arrives because a customer demanded it before a regulator did.
