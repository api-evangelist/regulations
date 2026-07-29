---
papers:
- title: The State of Canadian Travel APIs
  url: https://papers.apievangelist.com/papers/state-of-canadian-travel-apis/
  note: "Statutory compensation and communication duties for delays and cancellations, in a market where zero of nine organizations publish an idempotency mechanism and only two publish an event contract."
name: Air Passenger Protection Regulations
slug: air-passenger-protection-regulations
title: Air Passenger Protection Regulations (APPR)
kind: statute
jurisdiction: Canada
description: >-
  The Air Passenger Protection Regulations set out what Canadian air carriers owe passengers when a
  flight is delayed, cancelled or oversold — compensation tiers, rebooking duties, standards of
  treatment, and obligations to communicate the reason for a disruption and its status. Administered by
  the Canadian Transportation Agency and progressively tightened since taking effect in 2019.
tags:
- Travel
- Aviation
- Canada
- Consumer Protection
- Passenger Rights
common:
- type: Regulator
  url: https://otc-cta.gc.ca/eng/air-passenger-protection-regulations-highlights
- type: Legislation
  url: https://laws-lois.justice.gc.ca/eng/regulations/SOR-2019-150/
url: https://otc-cta.gc.ca/eng/air-passenger-protection-regulations-highlights
yearCreated: 2019
alternativeNames:
- APPR
- SOR/2019-150
- Canadian passenger rights
---

The APPR turned Canadian air passenger rights from airline policy into statutory obligation. Carriers
owe compensation on a tier scale for controllable delays and cancellations, must rebook passengers
within defined windows, must provide standards of treatment during disruption, and — the part that
matters most here — must **communicate the reason for a disruption and update the passenger as the
status changes.**

*   **Communication is a legal duty** - carriers must state why a flight is disrupted and keep the
    passenger informed, on a defined cadence.
*   **Tiered by carrier size and cause** - obligations differ between large and small carriers, and
    between controllable, controllable-for-safety and uncontrollable causes.
*   **Enforced by the CTA** - complaint-driven, with a backlog that has been the subject of successive
    amendments.

## An event obligation with no event contract

*The State of Canadian Travel APIs* scored nine organizations against this backdrop. **Two of nine
publish an event contract. Zero publish an idempotency mechanism — neither at full credit nor as
anything API Evangelist could derive from the documentation.**

The regulation compels carriers to **track and communicate the state of a disruption**. That is,
structurally, an event stream: a flight changes status, and every downstream party — the passenger, the
agency that sold the ticket, the corporate travel manager, the insurer — needs to know. Canadian
carriers do that work today through email, SMS and app notifications aimed at humans.

**Nothing in the APPR asks for a machine-readable version of the same information**, and the market has
not built one voluntarily. The two organizations that do publish event contracts are not the carriers
under the heaviest obligation.

There is a second-order effect worth noting for diligence. A statutory compensation regime creates
reconciliation work — claims, evidence, payment — and that work is exactly where a duplicated or lost
request is expensive. **Canada mandated the obligation and left the transaction-safety layer
unspecified**, which is the same shape as the [UK Package Travel Regulations](https://regulations.apievangelist.com/store/package-travel-regulations-2018/)
and [ATOL](https://regulations.apievangelist.com/store/atol/).

Canada has, meanwhile, built a genuine data-portability framework next door in banking, through
[consumer-driven banking](https://regulations.apievangelist.com/store/consumer-driven-banking/). Travel is not in scope for it, and no
timetable suggests it will be.
