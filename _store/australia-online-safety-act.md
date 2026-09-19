---
name: Australia Online Safety Act
kind: statute
jurisdiction: Australia
scope: horizontal
countries:
- australia
regions:
- anz
industries:
- technology
- media
- video-streaming
- gaming
- creator-economy
- artificial-intelligence
slug: australia-online-safety-act
title: Online Safety Act 2021 (Cth), including the Social Media Minimum Age obligation
description: 'The Online Safety Act gives Australia''s eSafety Commissioner takedown powers, Basic Online
  Safety Expectations and industry codes — and, since 10 December 2025, the Social Media Minimum Age obligation
  under Part 4A, which made Australia the first country anywhere to require platforms to take reasonable
  steps to prevent under-16s holding accounts. Penalties reach AUD 49.5 million, and the standard is deliberately
  technology-neutral: the platform must justify its method.'
tags:
- Online Safety
- Age Assurance
- Minors
- Takedown
- Australia
- Regulation
common:
- type: Legislation
  url: https://www.legislation.gov.au/C2021A00076/latest/text
- type: Regulator
  url: https://www.esafety.gov.au/
url: https://www.esafety.gov.au/
yearCreated: 2021
alternativeNames:
- Online Safety Act 2021
- SMMA
- Social Media Minimum Age
- Under-16 social media ban
companyCount: 0
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 90
precisionGrade: high
precisionBasis:
- 'acronym-shape -10: shortest bare needle is 4 characters, halved — it neither collides nor appears in
  the corpus frequency table'
---

Australia has been the most willing of the five jurisdictions in this catalog to legislate ahead of consensus, and the **Online Safety Act** is the clearest case. On 10 December 2025 it became the first country in the world to enforce a minimum age for social media accounts.

  * **Social Media Minimum Age, Part 4A** - Age-restricted platforms must take **reasonable steps** to prevent Australians under 16 from creating or holding an account. Penalties to AUD 49.5 million for serious or repeated breaches.
  * **Technology-neutral by design** - The law prescribes no method. Not ID, not biometrics, not inference. The platform chooses and must justify the choice as reasonable — which shifts the burden of proof onto the platform and leaves the standard to be settled by enforcement rather than by statute.
  * **The obligation is on the platform, not the user or the parent** - There is no parental-consent escape hatch, which distinguishes it from most US state approaches.
  * **Basic Online Safety Expectations** - eSafety can require a service to report on how it meets them, with penalties for failing to respond.
  * **Takedown schemes** - Cyberbullying of children, adult cyber abuse, image-based abuse and class 1/2 material, on short statutory clocks.
  * **Industry codes and standards** - Covering app stores, hosting, search and messaging as well as social media.

"Reasonable steps" is doing enormous work, and I think deliberately. A prescriptive standard would have been obsolete on arrival and would have forced the government to bless a verification technology, which is politically and technically unattractive. Instead the regulator gets to develop the standard through compliance engagement, and platforms get a moving target they must document their reasoning against.

For engineering teams that is a genuinely different obligation from the UK's. The UK Online Safety Act asks for *highly effective* age assurance and Ofcom has published guidance on what qualifies. Australia asks for *reasonable steps* and tells you to explain yourself. The first is a conformance question; the second is an evidence question. Meeting the UK standard probably satisfies Australia; the converse is not true.

Australia also matters as the natural experiment everybody else is watching. The UK, Canada, the EU and several US states all have some version of this question open, and Australia is the one with deployed enforcement data. The early evidence is the unglamorous kind: age assurance at scale is a churn, false-positive and appeals problem more than a technology problem, and the hardest population is not the determined fifteen-year-old but the adult wrongly classified with no fast route back.

Which is the catalog point. Age assurance is not a check, it is a lifecycle — verify, store an assertion, re-verify on an interval or a signal, handle a dispute, restore an account. Five states with transitions. Nobody documents any of it, and any provider building it is building a workflow that ought to be describable in a contract and currently is not.
