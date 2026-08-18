---
papers:
- title: The State of Canadian Travel APIs
  url: https://reports.apievangelist.com/reports/state-of-canadian-travel-apis/
  note: Canada's equivalent licence is why the only unconditionally open organization in Canadian travel
    is a regulator — Transport Canada serves WMS and CKAN under it with nothing to sign, while VIA Rail's
    GTFS feed is undercut by site terms that contradict the licence.
- title: The State of UK Real Estate APIs
  url: https://reports.apievangelist.com/reports/state-of-uk-real-estate-apis/
  note: The legal instrument that makes Britain the best-published real estate market in the world — HM
    Land Registry and Ordnance Survey answer anonymously because of it, and the UK beats the mandated
    US market 42.8 to 31.2.
standards:
- title: UPRN
  url: https://standards.apievangelist.com/store/uprn/
  note: OS Open UPRN is published under OGL, which is why the UK's property identifier works as a shared
    key.
- title: SPARQL
  url: https://standards.apievangelist.com/store/sparql/
  note: HM Land Registry serves Price Paid Data and the UK House Price Index as SPARQL under OGL v3.0.
name: Open Government Licence
slug: open-government-licence
title: Open Government Licence (OGL)
kind: licence
jurisdiction: United Kingdom
description: The Open Government Licence is the United Kingdom's standard legal instrument for releasing
  public sector information for reuse. Administered by The National Archives, it grants a worldwide, royalty-free,
  perpetual right to copy, adapt and commercially exploit licensed data, subject only to attribution.
  It is the mechanism through which UK government property, mapping and addressing data becomes reachable
  without a contract.
tags:
- Open Data
- Licensing
- United Kingdom
- Government
- Real Estate
common:
- type: Website
  url: https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- type: Administrator
  url: https://www.nationalarchives.gov.uk/
url: https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
yearCreated: 2010
alternativeNames:
- OGL
- OGL v3.0
- Open Government Licence for public sector information
companyCount: 2
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

The **Open Government Licence** is not an obligation on a regulated party — it is a grant. That makes it
unusual in this catalog, and it is precisely why it belongs here: in the sector where every other market
gates property data behind a commercial contract, the United Kingdom's answer is a licence that removes
the contract entirely.

*   **Royalty-free and perpetual** - Copy, publish, adapt, exploit commercially, and combine with other
    data. Attribution is effectively the only condition.
*   **Standardised across government** - One instrument, used consistently, so a developer does not
    negotiate terms per dataset or per department.
*   **Machine-consumable by design** - Because no agreement is executed, an anonymous client — including
    an autonomous agent — can retrieve and use the data. No other access model in the real estate study
    has that property.

*The State of UK Real Estate APIs* found this licence doing structural work. HM Land Registry publishes
Price Paid Data and the UK House Price Index as SPARQL and Linked Data endpoints that answer with **no key
and no account**; Ordnance Survey publishes the addressing and mapping layer, including
[UPRN](https://standards.apievangelist.com/store/uprn/), the identifier the entire British property market
keys on. Ordnance Survey scores 68.5 — the highest of any organization in the four-market study — and HM
Land Registry carries the highest agent-readiness at 93.3.

The comparison that makes the point: Britain has no MLS, no data dictionary, no certification programme and
no mandate of any kind, and it out-publishes the United States — which has all four — by 42.8 to 31.2. The
American market standardised its schema and left distribution licensed. Britain left the schema alone and
made distribution free. **On the evidence of this study, the licence mattered more than the standard.**

A caveat worth stating plainly: OGL is not a universal solvent even within HM Land Registry. The same
organization operates three tiers — an open OGL tier, a self-serve key tier where individual datasets still
require a signed licence and carry fees (the National Polygon Service at £20,000/yr, Registered Leases at
£5,000/yr), and a Business Gateway tier requiring mutual TLS with an issued client certificate. That is a
deliberate, well-built separation of *credential* from *entitlement*, and it is the only such design in the
study.
