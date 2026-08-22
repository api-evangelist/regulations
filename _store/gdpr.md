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
companyCount: 297
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 37
precisionGrade: low
precisionBasis:
- 'acronym-shape -20: shortest bare needle is 4 characters'
- 'collision -25: a surviving needle is also claimed by standards:GDPR'
- 'bare-channel -18: 89% of matching companies were reached only on the bare word (279 bare vs 33 phrase)'
precisionRecognition: 62
---

The **General Data Protection Regulation (GDPR)** is the privacy law that sits underneath open banking rather than beside it. Open banking moves personal financial data between parties; GDPR (and the retained UK GDPR) governs whether that movement is lawful — the consent, the lawful basis, the minimization, and the individual's right to port their data.

  * **A right to data portability** - GDPR's Article 20 gives individuals a right to receive and transmit their personal data, a general-purpose portability right that predates and reinforces the sector-specific open-banking mandates.
  * **Consent and lawful basis** - Every account-information consent in open banking has to rest on a GDPR-valid basis; the consent surface is not just an open-banking artifact, it is a data-protection requirement.
  * **Data minimization by design** - The least-privilege scope models in open-banking APIs are, in part, GDPR's minimization principle expressed in machine-readable form.

GDPR is why the consent layer matters as much as the contract in my scoring. A regulated data-sharing API is not just an OpenAPI and an auth stack — it is a lawful-basis machine, and the thinness of machine-readable consent surfaces across every banking market I scored is, in part, a GDPR gap as much as an open-banking one.
