---
name: VOW
slug: vow-policy
title: Virtual Office Website (VOW)
kind: industry-policy
jurisdiction: United States (trade association / local MLS)
description: A Virtual Office Website is the National Association of REALTORS policy framework permitting
  a broker to provide MLS listing data to consumers who have registered and established a broker-consumer
  relationship. VOW access typically carries more data than IDX — including some sold and historical information
  — in exchange for authentication, a broker relationship, and stricter terms of use. Like IDX, it is
  a private agreement rather than a statute.
tags:
- Real Estate
- United States
- Industry Policy
- Data Licensing
- Access Control
- Consent
common:
- type: Website
  url: https://www.nar.realtor/
url: https://www.nar.realtor/
yearCreated: 2008
alternativeNames:
- Virtual Office Website
- VOW policy
- VOW feed
companyCount: 0
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 85
precisionGrade: high
precisionBasis:
- 'acronym-shape -15: shortest bare needle is 3 characters, halved — it neither collides nor appears in
  the corpus frequency table'
---

**VOW** is the authenticated tier of American listing access, and it emerged from a genuine antitrust fight
about whether brokers operating primarily online could obtain the same data as brokers with offices.

Where [IDX](https://regulations.apievangelist.com/store/idx-policy/) governs public display, VOW governs what
a broker may show a consumer who has **registered and established a broker-consumer relationship**. The
trade is more data — often including sold and historical records that IDX withholds — for authentication and
tighter terms.

*   **Consent-gated by design** - The consumer must register and agree to terms. In principle this is the
    closest thing US real estate has to a consent primitive.
*   **Richer than IDX** - The data differential is the reason VOW exists and the reason it was contested.
*   **Still per-MLS** - Like IDX, terms are set locally. There is no national VOW contract.

The irony worth recording is measured. VOW is a consent-and-identity framework built into the access layer —
and *The State of US Real Estate APIs* found **zero of forty-five organizations publish a machine-readable
`consent_identity` primitive**, and zero publish idempotency. The sector has an elaborate consent regime
expressed entirely in contracts between institutions, and none of it expressed in a form software can read.
The consent exists; it just lives in a PDF.

Together with IDX and
[NAR Policy Statement 7.90](https://regulations.apievangelist.com/store/nar-policy-statement-790/), VOW
completes the American picture: a mandated schema, a certified conformance programme, and two private
licensing tiers that determine whether any of it is reachable. The standard is public. The data is not. And
an agent, which can satisfy a schema but cannot enter a broker-consumer relationship, is locked out by the
tier that was designed to protect consumers.
