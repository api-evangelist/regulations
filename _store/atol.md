---
papers:
- title: The State of UK Travel APIs
  url: https://reports.apievangelist.com/reports/state-of-uk-travel-apis/
  note: "Half a century of statutory financial protection for package holidays, and zero of fourteen UK travel organizations publish an idempotency mechanism — protection reconciles the duplicate payment, it does not prevent it."
name: ATOL
slug: atol
title: Air Travel Organiser's Licence (ATOL)
kind: licence
jurisdiction: United Kingdom
description: >-
  ATOL is the United Kingdom's statutory financial protection scheme for air package holidays,
  administered by the Civil Aviation Authority since 1973. Any business selling flight-inclusive
  packages must hold a licence, contribute to the Air Travel Trust Fund, and issue an ATOL Certificate
  to every customer. If the operator fails, the scheme repatriates travellers and refunds bookings.
tags:
- Travel
- Aviation
- United Kingdom
- Consumer Protection
- Licensing
- Financial Protection
common:
- type: Website
  url: https://www.caa.co.uk/atol-protection/
- type: Regulator
  url: https://www.caa.co.uk/
url: https://www.caa.co.uk/atol-protection/
yearCreated: 1973
alternativeNames:
- Air Travel Organiser's Licence
- ATOL Protection
- Air Travel Trust Fund
---

**ATOL is the oldest consumer-protection instrument in this catalog, and it protects money rather than
data.** A licence is required to sell flight-inclusive packages, licence holders pay into the Air Travel
Trust Fund, and every customer receives an ATOL Certificate naming who is protected and for what. When
an operator collapses, the scheme repatriates travellers and refunds forward bookings.

*   **Licensing, not disclosure** - the obligation is solvency, bonding and certificate issuance. No
    clause requires a machine-readable interface, a published specification, or a data-portability
    right.
*   **Administered by an aviation regulator** - the CAA holds the register, which is why the regulator
    itself is one of the few UK travel organizations publishing anything machine-readable.
*   **Certificate references are portable** - the ATOL Certificate reference travels with the booking,
    joining IATA codes and PNR locators in the small set of travel identifiers that survive a change of
    system.

## What it did and did not produce

*The State of UK Travel APIs* scored fourteen organizations in the market this scheme has governed for
half a century. **The market averages 27.7, and zero organizations publish an idempotency mechanism —
not at full credit, and not even a derived one.**

That juxtaposition is the finding, and it is not a criticism of ATOL as drafted. The regulated product
is a sequence of state changes to a paid booking: deposit, balance, seat change, name change,
cancellation, refund. **ATOL guarantees the traveller is made whole after a failure. It asks nothing of
the interface that would prevent the failure.** A retried request without an idempotency key is a
duplicated payment, and the scheme's answer is reconciliation rather than prevention.

Compare the same country's [CMA Open Banking Order](https://regulations.apievangelist.com/store/cma-open-banking-order/), which produced a
published standard, a directory and conformance testing inside three years. **Britain has demonstrated
in its own economy that a data mandate rewrites an industry's published surface. Travel received
financial protection instead**, and its surface looks like the pre-Open-Banking market did.

The transferable lesson for anyone drafting in this space: protecting the consumer's money and making
the industry legible to machines are independent objectives, and an instrument aimed at the first will
not deliver the second by accident.
