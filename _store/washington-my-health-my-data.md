---
name: Washington My Health My Data Act
kind: statute
jurisdiction: United States (Washington)
scope: horizontal
countries:
- united-states
regions:
- north-america
industries:
- digital-health
- healthcare
- fitness-wellness
- artificial-intelligence
- marketing-advertising
- technology
slug: washington-my-health-my-data
title: My Health My Data Act (Washington RCW 19.373)
description: The My Health My Data Act regulates consumer health data held by anyone HIPAA does not cover,
  on an extremely broad definition that reaches inferences, biometrics, precise location near a health
  facility, and anything that identifies a past, present or future physical or mental health status. It
  requires separate consent for collection and for sharing, bans the sale of such data without a signed
  authorisation, and carries a private right of action.
tags:
- Health Data
- Consent
- Private Right of Action
- Geofencing
- United States
- Regulation
common:
- type: Legislation
  url: https://app.leg.wa.gov/RCW/default.aspx?cite=19.373
url: https://app.leg.wa.gov/RCW/default.aspx?cite=19.373
yearCreated: 2023
alternativeNames:
- MHMD
- My Health My Data
- Washington HB 1155
companyCount: 2
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

**My Health My Data** exists because HIPAA covers entities, not data. A hospital is covered; a period-tracking app is not; a fitness wearable is not; an ad network that infers a pregnancy from browsing behaviour is not. Washington closed that gap with a statute so broadly drawn that its central compliance question is not how to comply but whether you are in scope — and the answer is usually yes.

  * **"Consumer health data" is defined expansively** - Personal information that identifies past, present or future physical or mental health status, including inferences, bodily functions, measurements, precise location indicating an attempt to receive health services, and data identifying someone as seeking health care.
  * **Separate consent to collect, and separate consent to share** - Not one consent covering both, and consent must be preceded by disclosure of the specific purpose.
  * **Sale requires a signed authorisation** - A distinct, prescribed instrument, not a consent checkbox.
  * **A geofencing ban** - No geofence around a health-care facility to deliver advertising or collect data. Straightforward, and the most obviously enforceable provision.
  * **A private right of action** - Through the Consumer Protection Act. This is what gives the statute its reach.

The "inference" clause is the one API providers should read twice. Data that is not health data becomes health data when it supports a health inference. A purchase history that reveals a condition, a location trail that reveals a clinic visit, a search query, an app-usage pattern — the underlying data is ordinary and the derived signal is regulated. Any provider running a recommendation, segmentation or enrichment model over consumer behaviour is potentially generating regulated health data as a byproduct of a product that has nothing to do with health.

Nevada passed a close analogue in SB 370, and Connecticut amended its privacy law along similar lines, so this is a pattern rather than an outlier.

Where it bites in practice is data-sharing architecture. The Act's structure — consent to collect, separate consent to share, authorisation to sell — assumes those are three distinguishable events with three distinguishable records. In most systems they are not. Data arrives, lands in a warehouse, and flows onward through pipelines nobody has modelled as a "share". Complying means being able to say, per record, what was consented to and by whom, and to enforce that at the point of egress rather than at the point of collection.

That is a data-contract problem before it is a legal one, and it is the same capability the DOJ bulk data rule and the EU Data Act ask for from different directions: knowing, provably, where a given record is allowed to go.
