---
name: Australian Consumer Law
slug: australian-consumer-law
title: Australian Consumer Law (ACL)
kind: statute
jurisdiction: Australia
description: The Australian Consumer Law, Schedule 2 to the Competition and Consumer Act 2010, is the
  national regime governing misleading conduct, unfair contract terms and consumer guarantees. Enforced
  by the ACCC, it is the instrument that regulates Australian travel — as distinct from the Consumer Data
  Right, which governs data portability and was never extended to the sector.
tags:
- Australia
- Consumer Protection
- Competition
- Misleading Conduct
- Enforcement
common:
- type: Legislation
  url: https://www.legislation.gov.au/C2004A00109/latest/text
- type: Regulator
  url: https://www.accc.gov.au/
url: https://www.accc.gov.au/consumers/consumer-rights-guarantees
yearCreated: 2010
alternativeNames:
- ACL
- Competition and Consumer Act 2010 Schedule 2
- ACCC enforcement
companyCount: null
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 0
precisionGrade: unmeasurable
precisionBasis:
- 'human verdict: `acl` sampled across 120 corpora and every hit was ACL the audit/analytics product,
  beside Qlik and Tableau ("tools such as ACL qlik sense tableau", "python ACL sas statistical software").
  Never Australian Consumer Law. Bare needle stoplisted; nothing else survives.'
---

The ACL is Australia's general-purpose consumer statute, and in travel it has been used hard. The ACCC
pursued **Trivago** over hotel-ranking practices that presented paid placement as best value, resulting
in a **A$44.7 million** penalty. It pursued **Qantas** over the sale of tickets on flights already
cancelled, resulting in a **A$100 million** penalty settlement.

*   **Conduct, not data** - misleading representations, unfair contract terms, consumer guarantees.
    Nothing in the ACL requires a machine-readable interface or a portability right.
*   **Economy-wide** - it applies to travel because it applies to everything, not because anyone
    designed a travel regime.
*   **Enforced by penalty** - the ACCC's instrument is litigation after the fact.

## Why this entry matters: the control group

Australia is the cleanest natural experiment in the API Evangelist sector series, and this statute is
the reason.

The same country designated **banking** under the [Consumer Data Right](https://regulations.apievangelist.com/store/consumer-data-right/) in
2019 and **energy** in 2022. Both sectors were measured in this series and both produced machine-readable
markets: mandated schemas, shared resource names, documents that compete and still match. **Travel was
never designated.** Same country, same Treasury, same regulator, same firms, same engineering labour
market — one variable different, and the ACL is what travel got instead.

*The State of Australian Travel APIs* measured the result. **Contract quality of 5.8 out of 100, with
nine of eleven organizations at zero — the lowest contract-quality reading in the entire research
programme, across every sector and every market measured, and a figure that survived a full rubric
revision untouched.** Seventeen specifications from a single publisher, and nothing shared with anyone.

**The instrument works on its own terms and produces nothing on this one.** The ACCC extracted A$144.7
million in travel penalties from two companies, and the market it disciplined publishes less
machine-readable evidence than any other measured. Enforcement against misconduct and legibility to
machines are unrelated outcomes, and a regulator equipped only for the first will not deliver the
second.

The corollary is the useful part for anyone forecasting this sector: **if the CDR is ever extended to
travel — booking history, loyalty balances, itinerary data — the numbers in that report become obsolete
within three years.** That is not speculation about travel. It is what the two designated Australian
sectors already did.
