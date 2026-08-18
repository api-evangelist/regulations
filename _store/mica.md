---
papers:
- title: The State of Blockchain & Crypto APIs
  url: https://reports.apievangelist.com/reports/state-of-blockchain-crypto-apis/
  note: The most consequential regime this market has faced, and it asks for exactly the artifacts the
    market scores worst on — governance at 11.1 and operational transparency at 17.9.
name: MiCA
kind: regulation
jurisdiction: European Union
slug: mica
title: Markets in Crypto-Assets Regulation (MiCA)
description: 'MiCA is the EU regulation that brings crypto-asset issuance and services inside a single
  authorisation regime. It covers asset-referenced tokens and e-money tokens — the stablecoins — with
  reserve, redemption and disclosure obligations, and it licenses crypto-asset service providers: exchanges,
  custodians, brokers, portfolio managers and advice. It is the first comprehensive crypto framework in
  a major jurisdiction, and its practical effect on API operations is indirect but substantial: authorisation
  brings supervision, supervision brings change control, incident reporting and evidence, and those are
  the published-artifact facets this market scores lowest on.'
tags:
- Crypto Assets
- Stablecoins
- Digital Assets
- Authorisation
- Europe
- Regulation
common:
- type: Legislation
  url: https://eur-lex.europa.eu/eli/reg/2023/1114/oj
- type: Regulator
  url: https://www.esma.europa.eu/
url: https://eur-lex.europa.eu/eli/reg/2023/1114/oj
yearCreated: 2023
alternativeNames:
- Markets in Crypto-Assets Regulation
- Regulation (EU) 2023/1114
standards:
- title: OpenAPI
  url: https://standards.apievangelist.com/store/openapi/
  note: Authorised providers carry change-control and disclosure obligations that a published contract
    satisfies more cheaply than a document.
regulations:
- title: DORA
  url: https://regulations.apievangelist.com/store/dora/
  note: A MiCA-authorised crypto-asset service provider is a financial entity under DORA, so operational-resilience
    obligations arrive with the licence.
companyCount: null
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 0
precisionGrade: unmeasurable
precisionBasis:
- 'human verdict: `mica` is an accent-folding artifact — "acad MICA" from *academica* and "qu MICA" from
  *quimica* in Spanish and Portuguese postings. Stoplisted.'
---

**MiCA** is the first comprehensive crypto framework adopted by a major jurisdiction, and it changes the question a European crypto company answers from "is this regulated?" to "under which authorisation?". It sets rules for issuers of asset-referenced and e-money tokens — reserves, redemption rights, disclosure — and licenses crypto-asset service providers across trading, custody, exchange, transfer, brokerage, placement and advice.

Nothing in MiCA requires anybody to publish an API. What it requires is the operational discipline that published APIs make cheaper to demonstrate: control over changes, classified and reported incidents, records that hold up to supervision, and clear disclosure to the people using the service. An authorised provider is also a financial entity under [DORA](https://regulations.apievangelist.com/store/dora/), which adds ICT risk management, resilience testing and third-party oversight on top.

For API operations the consequence is a fork in the road. A firm can meet these obligations with documents written for the regulator and nothing else, or it can meet them with artifacts — a versioned contract, a dated changelog, a deprecation policy, a status and incident history, a published scope model — that satisfy the supervisor and the integrator at the same time. The second route costs about the same and also moves the score, which is why MiCA is the most likely near-term cause of movement in a market currently scoring 11.1 on governance and 17.9 on operational transparency.
