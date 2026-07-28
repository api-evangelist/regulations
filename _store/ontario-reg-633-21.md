---
papers:
- title: The State of Canadian Energy APIs
  url: https://papers.apievangelist.com/papers/state-of-canadian-energy-apis/
  note: "The only consumer energy data mandate in Canada — and its bound utilities cluster in Thin and Emerging while the country's best energy API belongs to a province with no mandate at all."
standards:
- title: Green Button
  url: https://standards.apievangelist.com/store/green-button/
  note: "The standard this regulation makes compulsory for Ontario's licensed distributors, at NAESB REQ.21 ESPI v3.3."
name: Ontario Regulation 633/21
slug: ontario-reg-633-21
title: Ontario Regulation 633/21 (Energy Data)
kind: statute
jurisdiction: Ontario, Canada
description: >-
  Ontario Regulation 633/21, made under section 25.35.8 of the Electricity Act, 1998, requires Ontario
  electricity and natural gas local distribution companies to make customer energy data available in the
  Green Button format — both Download My Data and Connect My Data. It is the only consumer energy data
  mandate in Canada and one of very few anywhere that compels adoption of an externally-authored
  standard rather than creating a data right of its own.
tags:
- Energy
- Canada
- Ontario
- Data Portability
- Consent
- Regulation
common:
- type: Regulation
  url: https://www.ontario.ca/laws/regulation/210633
- type: Regulator
  url: https://www.oeb.ca/
url: https://www.ontario.ca/laws/regulation/210633
yearCreated: 2021
alternativeNames:
- O. Reg. 633/21
- Ontario Energy Data Regulation
- Green Button mandate
- Electricity Act 1998 s.25.35.8
---

**O. Reg. 633/21** is the cleanest available test of a specific regulatory design: what happens when a
government mandates adoption of a standard someone else wrote, rather than building a data right.

Made under the Electricity Act, 1998, it requires Ontario's licensed electricity and gas distributors to
offer [Green Button](https://standards.apievangelist.com/store/green-button/) — both **Download My Data**
(a customer-exported file) and **Connect My Data** (a consented third-party API). The **Ontario Energy
Board** supervises.

*   **Province-scale** - Ontario only. There is no federal Canadian equivalent and no other province has
    followed, which makes Canada the one country where a mandated and an unmandated utility cohort can be
    compared under otherwise similar conditions.
*   **Standard-adoption, not right-creation** - it points at an existing NAESB specification rather than
    commissioning schemas, an accreditation regime or a register. That is far cheaper to legislate.
*   **Supervised by an energy regulator** - the OEB has a broad remit and no API programme, which is a
    different enforcement posture from a dedicated data-standards body.

## What it produced

*The State of Canadian Energy APIs* scored eighteen organizations. Ontario's bound utilities land in
**Thin and Emerging** — Hydro Ottawa 40.4, Toronto Hydro 39.7, Alectra 27.7, Hydro One 23.1 — against a
national average of 32.8. **The highest score in Canada, 51.6 with the market's best agent-readiness at
87.5, belongs to Hydro-Québec: a Crown corporation in a province with no data mandate at all.**

Two of the bound utilities were recorded as **claiming a compliance that could not be verified from
outside**. In one case the onboarding host returns HTTP 200 for every path requested of it, including
invented control paths, because it is a single-page-app catch-all — precisely how a compliance claim
comes to look like an implementation.

The regulation did do one thing no unmandated market managed: **three Ontario utilities publish the same
Green Button ESPI specification**, a genuine shared vocabulary. But they implement a document the Green
Button Alliance wrote, and conformance is not the same as building an API.

## The comparison that matters

Set this against the [Consumer Data Right](https://regulations.apievangelist.com/store/consumer-data-right/),
which was extended to Australian energy in the same period. Australia legislated a **data right** —
primary legislation, a dedicated regulator, a standards body writing conformant schemas, an accreditation
regime, a public register and a security profile every participant implements identically — and produced
thirteen live consumer APIs and a market average of 41.6.

Ontario required **adoption of a standard** and produced three conformance implementations and two
unverifiable claims.

**Both are called mandates. They are not comparable instruments**, and the difference is the machinery
behind them. Across the ninety-five energy organizations researched for that quartet, a verified mandate
was worth about twelve points and a merely-claimed one was worth less than having no obligation at all.
