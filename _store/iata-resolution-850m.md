---
papers:
- title: The State of Australian Travel APIs
  url: https://papers.apievangelist.com/papers/state-of-australian-travel-apis/
  note: "How distribution policy is actually enforced — Air Transat's CRS policy bars redistribution without written consent and enforces it through ADMs under this resolution."
standards:
- title: IATA BSP and ARC
  url: https://standards.apievangelist.com/store/iata-bsp/
  note: "ADMs are raised and settled through the same billing and settlement machinery."
name: IATA Resolution 850m
slug: iata-resolution-850m
title: IATA Resolution 850m (Agency Debit Memos)
kind: industry-policy
jurisdiction: International
description: >-
  Resolution 850m governs Agency Debit Memos — the instrument by which an airline charges an accredited
  agency for a breach of fare rules, booking policy or distribution terms. ADMs are the enforcement
  mechanism behind airline distribution policy: not litigation, not regulatory penalty, but a debit
  raised through the settlement system the agency depends on.
tags:
- Travel
- Aviation
- Enforcement
- Distribution
- Industry Policy
- IATA
common:
- type: Website
  url: https://www.iata.org/en/programs/accreditation-travel/
url: https://www.iata.org/en/programs/accreditation-travel/
yearCreated: 2010
alternativeNames:
- Resolution 850m
- ADM
- Agency Debit Memo
---

An **Agency Debit Memo** is how an airline enforces its distribution policy against an agency. Not a
lawsuit, not a regulatory complaint — a debit raised through
[BSP or ARC](https://standards.apievangelist.com/store/iata-bsp/), the settlement system the agency must use to get paid. Resolution 850m sets
the rules for raising, disputing and settling them.

*   **Enforcement inside the payment rail** - the agency's exposure runs through the same machinery that
    remits its ticket sales.
*   **Airline-initiated** - the carrier raises the memo; the agency disputes within a defined window.
*   **Scope is distribution policy** - fare rule breaches, prohibited booking practices, churning,
    passive segments, unauthorised redistribution.

## Why a travel API report cares

Because ADMs are where the **published technical surface and the enforceable commercial rule meet**, and
the second is invisible in the first.

*The State of Australian Travel APIs* records **Air Transat's CRS policy** barring the sharing or
redistribution of its content to any third-party agent, GDS or metasearch without prior written consent,
requiring booking and ticketing within the same CRS, prohibiting passive segments and inventory holding —
**and enforcing all of it through ADMs under Resolution 850m.**

None of that appears in a specification. An engineer reading Transat's downloadable contract sees a
Radixx SOAP API. The rule that determines what may lawfully be done with the response sits in a
distribution policy enforced through a settlement debit.

The same pattern runs through the quartet's other terms: **WestJet** requires Canadian OTAs to hold a
direct sales incentive contract or book through an Official Redistributor, on pain of suspension, and
raises ADMs *"without limitation of minimum value"*. **Qantas** revokes ticketing authority at sole
discretion after six months of inactivity.

## The transferable lesson

For anyone assessing an API in an intermediated industry: **read the enforcement mechanism before the
specification.** A well-documented endpoint governed by a discretionary debit regime is a different
commercial proposition from an identical endpoint governed by a contract with defined remedies — and the
Kin Score, which reads published artifacts, cannot tell them apart.

That gap is precisely what the Switchability lens on the Kin Score roadmap exists to record, alongside
[Resolution 824](https://regulations.apievangelist.com/store/iata-resolution-824/) accreditation and the access-model evidence the travel
quartet collected.
