---
standards:
- title: IATA NDC
  url: https://standards.apievangelist.com/store/iata-ndc/
  note: The XML messaging standard this resolution authorised and the certification programme built on
    it.
name: IATA Resolution 787
slug: iata-resolution-787
title: IATA Resolution 787 (New Distribution Capability)
kind: industry-policy
jurisdiction: International
description: Resolution 787 is the IATA industry resolution, adopted in 2012, that authorised New Distribution
  Capability — the XML messaging standard for airline retailing. It is not law and no regulator enforces
  it. It permits airlines to distribute their own offers directly rather than through the shared fare
  and availability model, and IATA layered a voluntary certification programme on top of it.
tags:
- Travel
- Aviation
- Distribution
- Industry Policy
- Standards
- IATA
common:
- type: Website
  url: https://www.iata.org/en/programs/airline-distribution/ndc/
- type: Certification
  url: https://www.iata.org/en/programs/airline-distribution/ndc/certification/
url: https://www.iata.org/en/programs/airline-distribution/ndc/
yearCreated: 2012
alternativeNames:
- Resolution 787
- NDC resolution
- New Distribution Capability
companyCount: 3
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 75
precisionGrade: medium
precisionBasis:
- 'collision -25: a surviving needle is also claimed by standards:IATA NDC'
precisionRecognition: 100
---

**This is not a law**, and unlike [NAR Policy Statement 7.90](https://regulations.apievangelist.com/store/nar-policy-statement-790/) it is not
even a requirement. Resolution 787 **permits**. It authorised a standard, and left adoption, timing,
schema version and access terms to each airline.

The comparison between the two is the most instructive thing this catalog holds about industry mandates.
7.90 *compels* association-owned MLSs to certify against a machine-readable contract. 787 *enables*
airlines to publish one. Both are private rules written by an industry for itself. They produce very
different evidence.

*   **Permissive by construction** - an airline may adopt NDC, at a schema version of its choosing, on
    terms of its choosing.
*   **Certification is voluntary and tiered** - from entry-level conformance to Level 4 full offer and
    order management, plus the separate volume-based NDC@Scale programme.
*   **Silent on access** - the resolution concerns message format. Who may call the endpoint is left to
    [Resolution 824](https://regulations.apievangelist.com/store/iata-resolution-824/) accreditation and bilateral commercial agreement.

## What a decade of permission produced

The four *State of Travel APIs* Sector Reports scored sixty-four organizations against this standard and
found **three separable things that the industry treats as one**: holding a certification, publishing a
schema, and operating a reachable endpoint.

- **Air Canada** publishes NDC 17.2 (EDIST) properly and fully, then gates production access behind
  certification, application audit, unilateral thirty-day changes to display obligations, and revocation
  at sole discretion. Standard published, access discretionary.
- **WestJet** has held **NDC Certification Level 2 since March 2017** and has Direct Connect built in
  17.2 and 21.3/24.1 — **not live**, with rollout stated for Q4 2026 — while a **US$20–22 surcharge on
  non-NDC bookings is already in force.** The penalty for using the old channel arrived nine years before
  the new one.
- **Flight Centre** holds **Level 4**, the highest tier, claiming to have been the first global TMC to
  reach full offer and order management. It scores **15.6**, with no public NDC endpoint, no published
  NDC API, and `/terms`, `/terms-of-use` and `/legal` all returning 404.
- **Transat** publishes an NDC programme page in two languages and ships a proprietary Radixx SOAP API
  underneath, claiming no certification level.
- **Qantas** is NDC@Scale certified and prices the standard as a ladder: **A$11.50 per segment on
  EDIFACT, A$4.50 on Standard NDC**, and no surcharge at all on its own portal, its Certified Technology
  Partners, and an **invitation-only Premium NDC tier.**

Across all forty newly researched organizations, **three publish an open standard, and not one of them is
an airline, hotel group or GDS.**

## The finding worth carrying forward

NDC was designed to reduce switching cost by letting any seller reach airline content directly. On the
evidence it did something else at the identifier layer: **NDC introduces a platform-minted `OrderID`,
moving the primary booking record key out of the portable column** — IATA designators, PNR locators,
agency numbers, [PADIS](https://standards.apievangelist.com/store/iata-padis/) code lists, ATPCO fare bases — **and into the vendor column.**

That is the first instance this research programme has recorded of an interoperability standard
*increasing* lock-in through its own design, and it is why the Kin Score roadmap now carries a standalone
Switchability lens.

**For anyone designing a standards programme:** 7.90 shows that compelling a schema without deciding who
may call the endpoint produces an excellent description of something nobody can reach. 787 shows the
weaker case — permit a schema, leave both adoption and access to the incumbents, and you get a decade of
certifications with no reachable interfaces behind them.
