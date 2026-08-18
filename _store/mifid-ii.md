---
papers:
- title: The State of Market Data APIs
  url: https://reports.apievangelist.com/reports/state-of-market-data-apis/
  note: The regime that made market data a licensed, entitled, redistribution-controlled product — and
    the reason commercial clarity behaves differently in this sector than anywhere else in the series.
name: MiFID II
kind: directive
jurisdiction: European Union
slug: mifid-ii
title: MiFID II and MiFIR
description: The Markets in Financial Instruments Directive II and its accompanying regulation govern
  investment services across the EU — including pre- and post-trade transparency obligations, the unbundling
  of research from execution, best-execution reporting, and the requirement that trading venues make market
  data available on a reasonable commercial basis.
tags:
- Market Data
- Securities
- Finance
- Transparency
- European Union
- Regulation
common:
- type: Website
  url: https://www.esma.europa.eu/
url: https://www.esma.europa.eu/
yearCreated: 2018
alternativeNames:
- MiFID II
- MiFIR
- Directive 2014/65/EU
- Markets in Financial Instruments Directive
companyCount: 20
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 95
precisionGrade: high
precisionBasis:
- 'acronym-shape -5: shortest bare needle is 5 characters, halved — it neither collides nor appears in
  the corpus frequency table'
---

**MiFID II** is the regime that turned market data from a by-product of trading into a regulated
product in its own right. Alongside MiFIR it governs investment services across the EU, and three of
its provisions shape what this catalog measures.

  * **Pre- and post-trade transparency** - Trading venues and systematic internalisers must publish quotes and executed trades, within defined deferral regimes.
  * **Reasonable commercial basis** - Venues must make that data available on a reasonable commercial basis and, after fifteen minutes, free of charge. What "reasonable" means has been contested since the day it commenced.
  * **Research unbundling** - Investment research must be paid for separately from execution, which repriced a large part of the data and analytics market.
  * **Best execution reporting** - Firms must evidence execution quality, which generates its own demand for reference and transaction data.

MiFID II is the clearest example in this catalog of a regime that compels **publication** without
compelling an **interface**. Venues must make data available; nothing says it must be reachable
through a documented, machine-readable contract, and the commercial terms attached to it — licensing,
entitlement, redistribution control — are precisely what a self-serve API removes.

That tension shows up in the scores. *The State of Market Data APIs* found that in this sector the
feed is the commodity and the operation is the moat, and that commercial clarity behaves unlike any
other market in this research: pricing pages exist, but what they price is an *entitlement* rather
than a call. A regime that made data a licensed product produced an industry whose contracts are
negotiated, and negotiation is the one thing an agent cannot do.
