---
headers:
- name: x-fapi-auth-date
  basis: mandated
  observable: credentialed
  standard: fapi
- name: x-fapi-customer-ip-address
  basis: mandated
  observable: credentialed
  standard: fapi
- name: x-fapi-customer-last-logged-time
  basis: mandated
  observable: credentialed
  standard: fapi
- name: x-fapi-financial-id
  basis: mandated
  observable: credentialed
  standard: uk-open-banking-standard
  note: OBIE-specific; identifies the ASPSP in every request.
- name: x-fapi-interaction-id
  basis: mandated
  observable: credentialed
  standard: fapi
  note: Required by the UK Open Banking read/write standard for every call.
- name: x-idempotency-key
  basis: mandated
  observable: credentialed
  standard: uk-open-banking-standard
  note: Required on payment initiation. The regulatory concern is a duplicated payment, and this header
    is the control.
- name: x-jws-signature
  basis: mandated
  observable: credentialed
  standard: uk-open-banking-standard
  note: Non-repudiation for payment orders. A legal requirement expressed as a detached JWS in a header.
papers:
- title: The OpenID Connect Standard
  url: https://reports.apievangelist.com/reports/the-openid-connect-standard/
  note: Requires FAPI-profiled OIDC — and the UK paradox is that its A2A leaders still describe that spine
    in the contract as a plain bearer token.
- title: The OAuth 2.0 Standard
  url: https://reports.apievangelist.com/reports/the-oauth-2-standard/
  note: Compels OAuth and FAPI, producing the most rigorous auth posture measured anywhere in this research.
- title: The State of UK Banking APIs
  url: https://reports.apievangelist.com/reports/state-of-uk-banking-apis/
  note: The competition remedy that named the CMA9 and funded OBIE — the reason the UK mandate reached
    past existence to usefulness.
standards:
- title: UK Open Banking Standard
  url: https://standards.apievangelist.com/store/uk-open-banking-standard/
  note: OBIE wrote and maintains this standard under the CMA Order.
name: CMA Open Banking Order
kind: regulator-guidance
jurisdiction: United Kingdom
slug: cma-open-banking-order
title: Retail Banking Market Investigation Order (CMA Open Banking Remedy)
description: The UK Competition and Markets Authority's Retail Banking Market Investigation Order 2017
  is the competition remedy that created UK Open Banking. It required the nine largest UK banks (the CMA9)
  to adopt and maintain a common, open API standard and funded the Open Banking Implementation Entity
  (OBIE) to write the specification, run conformance, and operate a directory — the delivery machinery
  that made the UK the reference open-banking regime.
tags:
- Finance
- Open Banking
- Competition
- Antitrust
- United Kingdom
- Regulation
common:
- type: Order
  url: https://www.gov.uk/cma-cases/review-of-banking-for-small-and-medium-sized-businesses-smes-in-the-uk
- type: Delivery Body
  url: https://www.openbanking.org.uk/
url: https://www.gov.uk/cma-cases/review-of-banking-for-small-and-medium-sized-businesses-smes-in-the-uk
yearCreated: 2017
alternativeNames:
- CMA9 Order
- Retail Banking Market Investigation Order 2017
- CMA Open Banking Remedy
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

The UK's **Retail Banking Market Investigation Order 2017** is the piece most people forget when they credit the UK's open-banking success to PSD2. Open banking in Britain was not only a payments directive — it was a **competition remedy**. The Competition and Markets Authority, having found that entrenched incumbents made it too hard for customers to switch and for challengers to compete, ordered the nine largest banks to open up.

  * **It named the CMA9** - The Order applied to the nine largest UK current-account providers and required them to adopt and maintain a single, common, open API standard rather than nine incompatible ones.
  * **It created a delivery body** - The Order established and funded the Open Banking Implementation Entity (OBIE) to write the specification, run a conformance regime, and operate a trust directory — the machinery a bare mandate lacks.
  * **Antitrust through interoperability** - This is mandated interoperability as a competition tool: prying open a concentrated, data-hoarding market by requiring standardized access, redistributing power toward consumers and challengers.

The CMA Order is why the UK is the model everyone copies. A mandate that names its targets, funds a delivery body, and enforces conformance reaches past *existence* to *usefulness* — the distinction at the heart of every open-banking regime I score.
