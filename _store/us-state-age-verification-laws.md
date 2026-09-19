---
name: US State Age Verification Laws
kind: statute
jurisdiction: United States (state)
scope: horizontal
countries:
- united-states
regions:
- north-america
industries:
- technology
- video-streaming
- gaming
- creator-economy
- media
- e-commerce-platform
slug: us-state-age-verification-laws
title: US State Age Verification and Minor Protection Laws
description: Roughly half of US states now require age verification for access to adult content, and a
  growing group requires parental consent for minors' social media accounts. The Supreme Court upheld
  Texas's statute in Free Speech Coalition v. Paxton in June 2025, removing the constitutional argument
  that had blocked these laws for two decades and converting a First Amendment question into an identity-infrastructure
  procurement question.
tags:
- Age Verification
- Minors
- Online Safety
- Identity
- United States
- Regulation
common:
- type: Legislation
  url: https://www.supremecourt.gov/opinions/24pdf/23-1122_3e04.pdf
url: https://www.supremecourt.gov/opinions/24pdf/23-1122_3e04.pdf
yearCreated: 2023
alternativeNames:
- Age verification laws
- HB 1181
- Free Speech Coalition v. Paxton
- Minor social media consent laws
companyCount: 0
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---

**US state age verification** went from a recurring legislative failure to settled law in a single decision. For twenty years, statutes requiring age verification for online content were struck down under *Ashcroft v. ACLU* and its successors. In June 2025 the Supreme Court upheld Texas HB 1181 in *Free Speech Coalition v. Paxton*, applying intermediate rather than strict scrutiny to age verification for material harmful to minors. The constitutional question closed, and the legislative dam broke.

  * **Adult-content verification in roughly half the states** - Commercial sites above a threshold of such material must verify users are 18 or over by a transactional or government-ID method. Enforcement is usually by private right of action or Attorney General, and several statutes carry per-violation damages.
  * **Minor social media consent laws** - Utah, Arkansas, Texas, Florida, Tennessee, Mississippi and others require parental consent, or ban accounts below an age, with varying litigation outcomes. This line of statutes is on far less settled ground than the adult-content line.
  * **Design-code laws** - California's Age Appropriate Design Code, Maryland's and others, imposing default-privacy and impact-assessment duties for services likely to be accessed by children. These remain heavily litigated.
  * **App store accountability laws** - A separate and increasingly favoured approach, covered in its own entry.

The reason this belongs in an API catalog rather than only in a content-policy briefing is what happens next. A verification requirement creates a verification market, and a verification market runs on APIs: an identity provider, an age-estimation model, a document-scanning service, a wallet attestation. Every one of those is a call across a trust boundary carrying the most sensitive possible payload — a government identity document — for the sole purpose of producing a single boolean.

That mismatch is the design problem of the decade in this space, and it is the same problem in the UK, Australia and the EU. The regulator wants one bit. The naive implementation transfers a full identity. Every privacy objection to these laws is a restatement of that gap, and the answer that already exists in specification form is selective disclosure — prove the predicate, release nothing else — which is what eIDAS 2's wallet does and what nothing in the United States has an equivalent of.

The practical guidance I would give an API provider is narrow. Do not build age verification. Integrate one, and make the integration's contract explicit: what is stored, for how long, what is passed upstream, and whether a re-verification is required per session or per account. Those four facts are the whole of the privacy posture, none of them appear in any provider's public documentation today, and all four are things a schema could carry.
