---
name: EU Deforestation Regulation
kind: regulation
jurisdiction: European Union
slug: eudr
title: EU Deforestation Regulation (EUDR)
description: Regulation (EU) 2023/1115 prohibits placing specified commodities — cattle, cocoa, coffee,
  oil palm, rubber, soya and wood, and products derived from them — on the EU market unless they are deforestation-free,
  legally produced, and covered by a due diligence statement carrying the geolocation of the plots of
  land where they were produced.
tags:
- Supply Chain
- Sustainability
- Traceability
- Due Diligence
- European Union
- Regulation
common:
- type: Website
  url: https://environment.ec.europa.eu/topics/forests/deforestation/regulation-deforestation-free-products_en
url: https://environment.ec.europa.eu/topics/forests/deforestation/regulation-deforestation-free-products_en
yearCreated: 2023
alternativeNames:
- EUDR
- Regulation (EU) 2023/1115
- Deforestation-free products regulation
companyCount: 7
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

The **EU Deforestation Regulation** bans a defined list of commodities from the EU market unless the
operator placing them there can show the land they came from was not deforested after 31 December
2020. The mechanism is a **due diligence statement**, submitted per consignment, carrying the
geolocation coordinates of the plots of production.

  * **Geolocation is the payload** - The obligation is not a policy attestation; it is coordinates tied to a consignment, which forces real data collection deep into the supply chain.
  * **Submitted to a state system** - Statements go into the EU's TRACES environment, which exposes a machine interface to operators.
  * **Liability sits with the operator** - The company placing goods on the market carries the obligation, so it propagates upstream contractually rather than legally.
  * **Commodity-scoped** - Cattle, cocoa, coffee, oil palm, rubber, soya and wood, plus derived products.

EUDR is one of the more interesting regimes in this catalog because of *which direction the API
points*. Most data mandates covered here — open banking, the CDR — compel the regulated company to
publish an interface. EUDR compels the regulated company to *call* one. The state builds the
endpoint and the industry builds the client. *The State of Supply Chain APIs* flags this as the
pattern to watch: if the next wave of supply chain regulation keeps this shape, it will produce an
industry fluent in consuming government systems and no better at publishing contracts of its own.
