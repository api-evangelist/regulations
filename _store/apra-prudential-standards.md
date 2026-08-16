---
headers:
- name: strict-transport-security
  basis: evidentiary
  observable: edge
papers:
- title: The State of Australian Insurance APIs
  url: https://reports.apievangelist.com/reports/state-of-australian-insurance-apis/
  note: "APRA supervises prudentially and mandates no data exposure — and its own APRA Connect reporting taxonomy is the closest thing Australian insurance has to a published machine-readable standard."
name: APRA Prudential Standards
kind: regulator-guidance
jurisdiction: Australia
slug: apra-prudential-standards
title: APRA Prudential Standards (CPS 234 / CPS 230)
description: >-
  APRA is Australia's prudential regulator for banks, insurers and superannuation funds, operating through binding Prudential Standards — notably CPS 234 on information security and CPS 230 on operational risk management. It regulates the soundness and resilience of institutions; it does not require any of them to expose data or interfaces to third parties.
tags:
- Insurance
- Banking
- Australia
- Regulation
- Prudential
- Information Security
common:
- type: Website
  url: https://www.apra.gov.au/
- type: Regulator
  url: https://www.apra.gov.au/prudential-standards-and-guidance
url: https://www.apra.gov.au/
yearCreated: 1998
alternativeNames:
- Australian Prudential Regulation Authority
- APRA
- CPS 234
- CPS 230
- APRA Connect
jurisdiction: Australia
---

APRA is the counterweight to the Consumer Data Right in any honest reading of Australian financial and
insurance regulation: one regime is about safety, the other about access, and only one of them opens an API.

  * **CPS 234 (Information Security)** - Requires regulated entities to maintain information-security capability
    commensurate with threats, including clear accountability and testing of controls.
  * **CPS 230 (Operational Risk Management)** - Extends to service-provider management and business continuity,
    which reaches the third parties an insurer integrates with.
  * **APRA Connect** - The regulator's own reporting platform, with a published XSD and XBRL taxonomy — genuinely
    machine-readable, and pointed entirely at regulatory reporting rather than at insurance transactions.
  * **Prudential, not access-granting** - Nothing in the prudential framework obliges an insurer to publish a
    contract, a scope catalogue, or a developer surface.

*The State of Australian Insurance APIs* found a market with the complete legal machinery for open insurance —
the CDR, already proven in banking and energy — and no live obligation to use it, because the CDR's extension to
general insurance was designated and then deferred. APRA holds the sector's real regulatory relationship, and
APRA's mandate has never been to make insurers legible to developers.
