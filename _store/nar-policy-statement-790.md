---
papers:
- title: The State of US Real Estate APIs
  url: https://papers.apievangelist.com/papers/state-of-us-real-estate-apis/
  note: "The only self-imposed machine-readable mandate in the API economy — and it is worth about two points: RESO-certified organizations average 38.0 against 36.0 uncertified."
standards:
- title: RESO Web API
  url: https://standards.apievangelist.com/store/reso-web-api/
  note: "The contract this policy makes compulsory for association-owned MLSs."
- title: RESO Data Dictionary
  url: https://standards.apievangelist.com/store/reso-data-dictionary/
  note: "The vocabulary half of the same requirement."
name: NAR Policy Statement 7.90
slug: nar-policy-statement-790
title: NAR MLS Policy Statement 7.90
kind: industry-policy
jurisdiction: United States (trade association)
description: >-
  Policy Statement 7.90 of the National Association of REALTORS' Multiple Listing Service policy requires
  association-owned MLSs to certify against the RESO Data Dictionary and RESO Web API within one year of
  each version's ratification. It is not legislation and no regulator enforces it; compliance is a
  condition of NAR affiliation. It is the only industry-imposed machine-readable API mandate identified
  across the API Evangelist sector series.
tags:
- Real Estate
- United States
- Industry Policy
- Standards Mandate
- Certification
common:
- type: Website
  url: https://www.nar.realtor/
- type: Standard
  url: https://www.reso.org/certification/
url: https://www.nar.realtor/
yearCreated: 2015
alternativeNames:
- MLS Policy Statement 7.90
- NAR 7.90
- RESO certification mandate
---

**This is not a law.** It is a policy of a trade association, and it is catalogued here because on the
evidence it binds more tightly than several statutes that are — and because the distinction is the single
most useful thing US real estate teaches about mandates.

Policy Statement 7.90 requires association-owned multiple listing services to certify against the
[RESO Data Dictionary](https://standards.apievangelist.com/store/reso-data-dictionary/) and
[RESO Web API](https://standards.apievangelist.com/store/reso-web-api/) within a year of each ratification.
Enforcement runs through NAR affiliation rather than through a court or a regulator.

*   **Self-imposed** - Every other mandate in the API Evangelist sector series came from a state: Open
    Banking in the UK, the Consumer Data Right in Australia, FHIR and the ONC rules in US healthcare. This
    one an industry wrote for itself.
*   **Genuinely enforced** - Certification is real, conformance testing is real, and the public directory
    is verifiable without an account. This is not a voluntary code that everyone ignores.
*   **Schema-only** - It compels a *contract shape*. It says nothing about who may obtain a credential.

## What it bought

*The State of US Real Estate APIs* scored forty-five organizations and measured the return:
**RESO-certified organizations average 38.0 against 36.0 for everyone else.** About two points.

The mechanism of that disappointment is worth stating precisely, because it is not a failure of the policy
as written. **Certification and reachability are independent variables, and 7.90 mandates only the first.**
All three certified parties in the study are data *resellers* rather than portals or MLSs, and every one of
their OData `$metadata` documents returns **401** without an executed MLS licence. Access still runs through
[IDX](https://regulations.apievangelist.com/store/idx-policy/) and
[VOW](https://regulations.apievangelist.com/store/vow-policy/) agreements, broker sponsorship, or a reseller
contract — none of which 7.90 touches.

The corroborating evidence is blunt: across all forty-five organizations, **not one publishes a
specification for `mls`, `idx`, `media`, `openhouse` or `member`** — the mandated Data Dictionary's own core
resources.

## Why it is catalogued as policy, not law

Treating a trade-association rule as equivalent to statute would misinform a reader making a compliance or
diligence decision. But omitting it would leave this catalog silent on the most-mandated sector in the
series. It is recorded here with its `kind` stated so both facts survive: it is binding, and it is private.

For anyone designing a standards programme, the lesson transfers regardless of instrument. **The schema is
the easy half.** Compel a contract shape without deciding who may call the endpoint, and you will have
mandated an excellent description of something nobody can reach.
