---
papers:
- title: The State of UK Travel APIs
  url: https://reports.apievangelist.com/reports/state-of-uk-travel-apis/
  note: "Extended package protection to dynamic packaging — the assembly of a holiday from multiple providers — without requiring any of those providers to publish an interface the assembly could run on."
name: Package Travel Regulations 2018
slug: package-travel-regulations-2018
title: Package Travel and Linked Travel Arrangements Regulations 2018
kind: statute
jurisdiction: United Kingdom
description: >-
  The Package Travel and Linked Travel Arrangements Regulations 2018 implement the EU Package Travel
  Directive in UK law, extending long-standing package-holiday protections to modern dynamic packaging —
  holidays assembled from separate flight, accommodation and car-hire components. They impose
  pre-contract information duties, liability for performance of the whole package, and insolvency
  protection on the organiser.
tags:
- Travel
- United Kingdom
- Consumer Protection
- Packages
- Liability
common:
- type: Legislation
  url: https://www.legislation.gov.uk/uksi/2018/634/contents/made
url: https://www.legislation.gov.uk/uksi/2018/634/contents/made
yearCreated: 2018
alternativeNames:
- PTRs 2018
- Package Travel Regulations
- Linked Travel Arrangements
- SI 2018/634
---

The 2018 Regulations exist because the way people buy holidays changed and the old definition of a
"package" stopped fitting. They extend organiser liability and insolvency protection to **dynamic
packaging** — a trip assembled at the point of sale from separate flight, hotel and car-hire components
— and add the category of Linked Travel Arrangements for looser bundles.

*   **Liability follows assembly** - whoever assembles the package answers for its performance, even
    though the components come from third parties.
*   **Pre-contract information duties** - the traveller must be told what they are buying and who is
    responsible before they pay.
*   **Insolvency protection** - alongside [ATOL](https://regulations.apievangelist.com/store/atol/) for flight-inclusive packages.

## The gap this catalog exists to record

Dynamic packaging is, technically, **an integration problem**. Assembling a holiday from separate
providers in real time requires reading availability, holding inventory, taking payment and propagating
changes across several systems that belong to different companies.

The 2018 Regulations impose full liability for that assembly and **require nothing of the interfaces it
runs on**.

*The State of UK Travel APIs* measured the result across fourteen organizations. **Seven publish no
machine-readable contract at all. Contract quality averages 27.6. The entire shared vocabulary of the
UK travel market is one word — `webhooks-api`, shared by two providers.** There is no shared booking
resource, no shared availability resource, no shared offer or order. An organiser carrying statutory
liability for a package is assembling it across interfaces that do not agree on what a booking is
called.

The one organization in the market that solves this cleanly solves it by owning everything: **TUI Group
leads at 52.2** with twenty-one specifications, because a company that owns the aircraft, the hotels,
the ships and the shops has to integrate with itself. Vertical integration substituted for a standard.

**Regulating the assembly without regulating the interfaces is the pattern.** It appears again in
[Canada's Air Passenger Protection Regulations](https://regulations.apievangelist.com/store/air-passenger-protection-regulations/), which
impose obligations on disruption handling in a market where no airline publishes an event contract.
