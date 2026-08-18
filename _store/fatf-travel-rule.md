---
papers:
- title: The State of Blockchain & Crypto APIs
  url: https://reports.apievangelist.com/reports/state-of-blockchain-crypto-apis/
  note: An inter-institution data exchange — the exact shape of an API standard — met with private networks
    rather than an open contract, the same pattern as EDI in supply chain.
name: FATF Travel Rule
kind: regulation
jurisdiction: Global (FATF member jurisdictions)
slug: fatf-travel-rule
title: FATF Travel Rule (Recommendation 16)
description: The FATF Travel Rule requires originator and beneficiary information to travel alongside
  a transfer between regulated institutions. Extended to virtual asset service providers in 2019, it obliges
  crypto exchanges and custodians to exchange identifying data about the parties to a transfer — which
  is, unavoidably, an inter-organisational data exchange problem.
tags:
- Anti-Money Laundering
- Crypto Assets
- Data Exchange
- Global
- Regulation
common:
- type: Regulator
  url: https://www.fatf-gafi.org/
- type: Guidance
  url: https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Targeted-update-virtual-assets-vasps.html
url: https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Targeted-update-virtual-assets-vasps.html
yearCreated: 2019
alternativeNames:
- Travel Rule
- FATF Recommendation 16
- Crypto Travel Rule
- VASP Travel Rule
companyCount: 5
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---

**The Travel Rule** is a compliance obligation shaped exactly like an API standard. Two institutions that may never have spoken need to exchange structured, verified data about the parties to a transfer, at the moment of that transfer, across borders and across jurisdictions that implement the rule differently.

  * **Originator and beneficiary data** - Names, account identifiers and, above a threshold, address or identity details, travelling with the transfer.
  * **Applies between institutions** - It governs the message between VASPs rather than anything on-chain, which is why the chain itself does not solve it.
  * **Sunrise problem** - Jurisdictions adopted it at different times, so counterparties are frequently subject to different rules.
  * **Counterparty due diligence** - A sending institution must know something about the receiving one, which requires a directory of some kind.
  * **Met by private networks** - Several proprietary networks exist to carry these messages; an open, published contract does not.

[The State of Blockchain & Crypto APIs](https://reports.apievangelist.com/reports/state-of-blockchain-crypto-apis/) makes the comparison plainly: this is an inter-organisational data exchange met with a handful of proprietary networks rather than an open specification, and the parallel with EDI in supply chain is close. A compliance obligation, a private network, and an industry entirely capable of writing the open version. It is worth watching whether the market that standardised [ERC-20](https://standards.apievangelist.com/store/erc-20/) voluntarily does the same here, or whether the Travel Rule stays a set of walled directories.
