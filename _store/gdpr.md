---
headers:
- name: access-control-allow-origin
  basis: evidentiary
  observable: edge
  note: A negative signal. A wildcard origin on an authenticated surface is a data-protection failure
    anyone can observe without credentials.
- name: clear-site-data
  basis: evidentiary
  observable: edge
  note: Erasure carried out at the client boundary rather than only in the datastore.
- name: set-cookie
  basis: evidentiary
  observable: edge
papers:
- title: The State of Blockchain & Crypto APIs
  url: https://reports.apievangelist.com/reports/state-of-blockchain-crypto-apis/
  note: Personal data on an immutable ledger, and an erasure right that cannot be honoured on-chain.
- title: The State of Marketing & Advertising APIs
  url: https://reports.apievangelist.com/reports/state-of-marketing-advertising-apis/
  note: 'The report that scores the industry GDPR was written about: consent is a legible API surface
    at 3.1% of the marketing and advertising market, below the whole-catalog rate.'
- title: The State of Data & Analytics APIs
  url: https://reports.apievangelist.com/reports/state-of-data-analytics-apis/
  note: In data and analytics, GDPR reaches the data plane the market does not describe — access, portability
    and erasure land on interfaces built for administration.
- title: The State of Digital Health APIs
  url: https://reports.apievangelist.com/reports/state-of-digital-health-apis/
  note: In digital health, GDPR restricts what may be done with the data rather than requiring that it
    be reachable — one of nine regimes in this market that compel no interface.
- title: The State of Cybersecurity APIs
  url: https://reports.apievangelist.com/reports/state-of-cybersecurity-apis/
  note: Cybersecurity vendors sit in the processor role for their customers; the market publishes a machine-readable
    consent surface 7.1% of the time.
- title: The State of Developer Tools APIs
  url: https://reports.apievangelist.com/reports/state-of-developer-tools-apis/
  note: Developer tools sit in the processor role for their customers' data; this industry's regulatory
    surface is the union of its customers' regulatory surfaces.
- title: The State of Artificial Intelligence APIs
  url: https://reports.apievangelist.com/reports/state-of-artificial-intelligence-apis/
  note: The lawful-basis and automated-decision backbone under every model that touches personal data,
    in an industry with 3.9% machine-readable consent coverage.
- title: The State of UK Banking APIs
  url: https://reports.apievangelist.com/reports/state-of-uk-banking-apis/
  note: The privacy and consent backbone beneath the UK's open-banking data sharing — the lawful basis
    every AIS consent rests on.
name: GDPR
kind: statute
jurisdiction: European Union / United Kingdom
slug: gdpr
title: General Data Protection Regulation (GDPR)
description: The General Data Protection Regulation is the EU's comprehensive data-protection law (retained
  in the UK as the UK GDPR), governing how personal data is processed, consented to, and ported. It is
  the privacy backbone beneath open banking; the lawful-basis, consent, and data-minimization requirements
  that any account-data-sharing regime must satisfy, and a right to data portability that predates and
  reinforces open banking.
tags:
- Privacy
- Data Protection
- Consent
- Data Portability
- Europe
- United Kingdom
- Regulation
common:
- type: Legislation
  url: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- type: Regulator
  url: https://edpb.europa.eu/
url: https://eur-lex.europa.eu/eli/reg/2016/679/oj
yearCreated: 2016
alternativeNames:
- General Data Protection Regulation
- Regulation (EU) 2016/679
- UK GDPR
companyCount: 295
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 36
precisionGrade: low
precisionBasis:
- 'acronym-shape -20: shortest bare needle is 4 characters'
- 'collision -25: a surviving needle is also claimed by standards:GDPR'
- 'bare-channel -19: 90% of matching companies were reached only on the bare word (278 bare vs 32 phrase)'
precisionRecognition: 61
---

The **General Data Protection Regulation (GDPR)** is the privacy law that sits underneath open banking rather than beside it. Open banking moves personal financial data between parties; GDPR (and the retained UK GDPR) governs whether that movement is lawful — the consent, the lawful basis, the minimization, and the individual's right to port their data.

  * **A right to data portability** - GDPR's Article 20 gives individuals a right to receive and transmit their personal data, a general-purpose portability right that predates and reinforces the sector-specific open-banking mandates.
  * **Consent and lawful basis** - Every account-information consent in open banking has to rest on a GDPR-valid basis; the consent surface is not just an open-banking artifact, it is a data-protection requirement.
  * **Data minimization by design** - The least-privilege scope models in open-banking APIs are, in part, GDPR's minimization principle expressed in machine-readable form.

GDPR is why the consent layer matters as much as the contract in my scoring. A regulated data-sharing API is not just an OpenAPI and an auth stack — it is a lawful-basis machine, and the thinness of machine-readable consent surfaces across every banking market I scored is, in part, a GDPR gap as much as an open-banking one.
