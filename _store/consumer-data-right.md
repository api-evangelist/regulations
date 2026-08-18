---
headers:
- name: x-cds-client-headers
  basis: mandated
  observable: credentialed
  standard: consumer-data-standards
- name: x-fapi-auth-date
  basis: mandated
  observable: credentialed
  standard: fapi
- name: x-fapi-customer-ip-address
  basis: mandated
  observable: credentialed
  standard: fapi
- name: x-fapi-interaction-id
  basis: mandated
  observable: credentialed
  standard: fapi
  note: Required by the Consumer Data Standards, which the Data Standards Chair makes binding.
- name: x-min-v
  basis: mandated
  observable: credentialed
  standard: consumer-data-standards
- name: x-v
  basis: mandated
  observable: credentialed
  standard: consumer-data-standards
  note: Version negotiation made binding by the Consumer Data Standards.
- name: deprecation
  basis: evidentiary
  observable: contract
  standard: http
  note: The Consumer Data Standards run published retirement schedules.
- name: sunset
  basis: evidentiary
  observable: edge
  standard: http
papers:
- title: The OpenID Connect Standard
  url: https://reports.apievangelist.com/reports/the-openid-connect-standard/
  note: Requires FAPI-profiled OIDC, producing broad uniform coverage and near-zero differentiation above
    it.
- title: The OAuth 2.0 Standard
  url: https://reports.apievangelist.com/reports/the-oauth-2-standard/
  note: One of the few regimes that genuinely compels OAuth-based, FAPI-profiled authorization — and,
    characteristically, stops exactly at the line the regulation draws.
- title: The State of Australian Travel APIs
  url: https://reports.apievangelist.com/reports/state-of-australian-travel-apis/
  note: 'The control group: designated for banking in 2019 and energy in 2022, NEVER for travel — and
    undesignated Australian travel returns contract quality of 5.8 with nine of eleven organizations at
    zero, the lowest reading in the entire series.'
- title: The State of Australian Energy APIs
  url: https://reports.apievangelist.com/reports/state-of-australian-energy-apis/
  note: Extended from banking into ENERGY and live — the proof a statutory data mandate is replicable
    across industries, worth about twelve points when verified and less than nothing when merely claimed.
- title: The State of Australian Insurance APIs
  url: https://reports.apievangelist.com/reports/state-of-australian-insurance-apis/
  note: Designated to extend to general insurance and then deferred — so Australia holds the complete
    legal machinery for open insurance and no live obligation, making it the cleanest measurement of what
    a mandate is actually worth.
- title: The State of Australian Banking APIs
  url: https://reports.apievangelist.com/reports/state-of-australian-banking-apis/
  note: The law behind the fifty-bank commodity contract the report anatomizes — read-only data sharing,
    no payment initiation.
standards:
- title: Consumer Data Standards
  url: https://standards.apievangelist.com/store/consumer-data-standards/
  note: The machine-readable Banking API contract every accredited data holder implements to satisfy the
    CDR.
name: Consumer Data Right
kind: statute
jurisdiction: Australia
slug: consumer-data-right
title: Consumer Data Right (CDR)
description: Australia's Consumer Data Right (CDR) is an economy-wide data-portability law that gives
  consumers the right to share their data with accredited third parties, beginning with banking (open
  banking). It is the legal mandate behind the Consumer Data Standards, requiring every accredited data
  holder to expose a byte-for-byte machine-readable API contract under a consent-and-accreditation regime.
tags:
- Finance
- Open Banking
- Data Portability
- Consent
- Australia
- Regulation
common:
- type: Website
  url: https://www.cdr.gov.au/
- type: Regulator
  url: https://www.accc.gov.au/consumers/consumer-data-right
url: https://www.cdr.gov.au/
yearCreated: 2019
alternativeNames:
- CDR
- Consumer Data Right (Australia)
- Competition and Consumer (CDR) Rules
companyCount: null
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 0
precisionGrade: unmeasurable
precisionBasis:
- 'human verdict: `cdr` is Critical Design Review in aerospace, always paired with PDR ("pdr CDR etc for
  customer and program seit"). Stoplisted.'
---

Australia's **Consumer Data Right (CDR)** is a general, economy-wide data-portability law — not a banking rule that happens to touch data. It gives consumers a legal right to direct that their data be shared, securely, with accredited recipients, and it was switched on in banking first as the country's version of open banking.

  * **A right, sector by sector** - The CDR is designed to roll across the economy (banking, then energy, then beyond), with banking as the proving ground; the law defines the accreditation, consent, and privacy-safeguard machinery, and the Data Standards Body writes the technical contract.
  * **Data sharing, not payment initiation** - Unlike the UK and EU regimes, the CDR as implemented is read-only — an accredited recipient can *read* a consumer's banking data but cannot initiate a payment. An agent can see your account; it cannot act on it.
  * **Accreditation and consent as the gate** - Access to the consumer-data surface is gated behind ACCC accreditation and explicit, revocable consumer consent, mapped to a least-privilege scope model.

The CDR is the cleanest specimen in my research of a mandate producing *existence, not quality*: it dragged an entire banking sector across the machine-readability line, and left governance, operational transparency, and product maturity to each bank. It is the law; the [Consumer Data Standards](https://standards.apievangelist.com/store/consumer-data-standards/) are the contract that makes it real.

## The energy extension — a mandate proved replicable

The CDR was designed for banking and then **designated into energy**, where it is live. That makes it
the only regime in this catalog tested twice, in two different industries, under the same statute,
regulator and standards body — and *The State of Australian Energy APIs* measured what happened.

**It transplanted.** Across ninety-five energy organizations researched across four markets, those with a
**live, verified** mandate implementation average **42.2** against **30.2** for organizations under no
obligation at all. Australia leads the four-market energy quartet at 41.6 with agent-readiness of 57.3,
against the United States' 30.2 — and the United States has had a perfectly serviceable voluntary
standard, [Green Button](https://standards.apievangelist.com/store/green-button/), for over a decade.

Three things that regime designers should take from it:

*   **Verification is the whole mechanism.** Organizations that *claim* the mandate but whose
    implementation could not be verified average **30.4** — *lower* than having no obligation. The CDR's
    public register, standards-conformant discovery endpoints and ACCC-issued certificates are what make
    the difference checkable from outside. A compliance page proves nothing.
*   **It produced the only shared vocabulary in the series.** Four Australian retailers publish
    byte-identical `cds-energy` and `cds-common` documents. No unmandated market anywhere in this
    research shares a domain resource across more than two organizations.
*   **The obligation transplanted; the architecture did not.** CDR banking has every bank self-hosting
    its own Product Reference Data. CDR energy **centralises** it at the regulator: AGL's own base URI
    returns 404 on `/energy/plans` while the AER's gateway serves 1,343 AGL plans anonymously. Same law,
    redesigned topology — plan for that when designating the next sector.

What it did not deliver is governance. Australian energy scores **1.6** on that facet with twenty-one of
twenty-four organizations at zero. The CDR specifies schemas, a security profile and a consent model, and
says nothing about versioning or deprecation. **A mandate delivers exactly what it asks for.**

Worth reading against the two other energy instruments in this catalog:
[Ontario Regulation 633/21](https://regulations.apievangelist.com/store/ontario-reg-633-21/), which
compelled adoption of an existing standard and produced far less, and
[Ofgem's Data Best Practice Guidance](https://regulations.apievangelist.com/store/ofgem-data-best-practice/),
which aimed a comparable obligation at network data instead of customer data and got world-class results
in that lane.

