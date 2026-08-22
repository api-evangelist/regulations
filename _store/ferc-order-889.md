---
name: FERC Order 889
slug: ferc-order-889
title: FERC Order 889 (OASIS)
kind: regulator-guidance
jurisdiction: United States (federal)
description: FERC Order 889, issued in 1996 alongside the Order 888 open-access rules, requires public
  utilities that own or control interstate transmission to operate an Open Access Same-Time Information
  System — OASIS — posting available transmission capacity and related data on equal terms to all users,
  and to separate transmission operations from wholesale marketing. It is arguably the oldest machine-readable
  data-posting mandate still operating in any sector this research has scored.
tags:
- Energy
- United States
- Transmission
- Open Access
- Regulation
common:
- type: Regulator
  url: https://www.ferc.gov/
- type: Order
  url: https://www.ferc.gov/industries-data/electric/industry-activities/open-access-transmission-tariff-oatt-reform
url: https://www.ferc.gov/
yearCreated: 1996
alternativeNames:
- Order 889
- OASIS
- Open Access Same-Time Information System
- NAESB WEQ-002
- NAESB WEQ-003
companyCount: 0
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 100
precisionGrade: high
precisionBasis:
- 'note: 1 needle(s) dropped by the stoplist — precision gained, recall lost'
---

**FERC Order 889** is the finding that complicates the simple story about American energy data.

Issued in 1996 with the Order 888 open-access reforms, it requires transmission providers to run an
**Open Access Same-Time Information System** — a public posting of available transmission capacity,
prices and related data, offered on identical terms to every market participant, with a strict
separation between transmission operations and the utility's own wholesale marketing arm. The message
formats are standardised through **NAESB WEQ-002 and WEQ-003** OASIS templates.

*   **A genuine data-posting mandate, three decades old** - long before open banking, before Green
    Button, before anyone framed this as an API question.
*   **Structural in purpose** - the point was to stop a vertically-integrated utility from advantaging
    its own trading desk with information its competitors could not see. Equal access to *data* as an
    antitrust remedy.
*   **Standardised message formats** - NAESB WEQ templates, versioned (2.0, 2.1, 2.2, 3.3), which is why
    OASIS data is comparable across operators at all.
*   **Wholesale only** - it binds transmission providers. It says nothing about the retail customer's
    own usage data.

## Why it matters to the reading of US energy

*The State of US Energy APIs* found the wholesale market operators to be the functioning half of the
American sector: the `system-operator` tier averages **48.3** against `utility-retailer` at **29.8**.
ERCOT 55.0, ISO New England 54.4, MISO 54.2, PJM 48.3. PJM and ISO-NE both operate OASIS surfaces under
this order.

Meanwhile thirteen investor-owned utilities sit in the Minimal band with agent-readiness of 0.0.

The tempting summary — "the United States has no energy data mandate" — is wrong, and the precise version
is more interesting. **The United States mandated wholesale transmission data in 1996 and never mandated
retail customer data at all.** The tier under an obligation publishes; the tier without one does not. The
eighteen-and-a-half point gap between those tiers is the clearest single measurement in that report of
what an obligation is worth.

It is also a caution for anyone citing OASIS as evidence of good practice: ISO New England's OASIS posting
surface claims NAESB WEQ conformance that could not be verified from outside, and the modern developer
surfaces these operators publish are proprietary shapes sitting alongside the mandated one rather than
built on it. A thirty-year-old mandate produces a thirty-year-old artifact.
