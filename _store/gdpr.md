---
papers:
- title: The State of Cybersecurity APIs
  url: https://papers.apievangelist.com/papers/state-of-cybersecurity-apis/
  note: "Cybersecurity vendors sit in the processor role for their customers; the market publishes a machine-readable consent surface 7.1% of the time."
- title: The State of Developer Tools APIs
  url: https://papers.apievangelist.com/papers/state-of-developer-tools-apis/
  note: "Developer tools sit in the processor role for their customers' data; this industry's regulatory surface is the union of its customers' regulatory surfaces."
- title: The State of Artificial Intelligence APIs
  url: https://papers.apievangelist.com/papers/state-of-artificial-intelligence-apis/
  note: "The lawful-basis and automated-decision backbone under every model that touches personal data, in an industry with 3.9% machine-readable consent coverage."
- title: The State of UK Banking APIs
  url: https://papers.apievangelist.com/papers/state-of-uk-banking-apis/
  note: "The privacy and consent backbone beneath the UK's open-banking data sharing — the lawful basis every AIS consent rests on."
name: GDPR
kind: statute
jurisdiction: European Union
slug: gdpr
title: General Data Protection Regulation (GDPR)
description: "The General Data Protection Regulation is the EU's comprehensive data-protection law (retained in the UK as the UK GDPR), governing how personal data is processed, consented to, and ported. It is the privacy backbone beneath open banking; the lawful-basis, consent, and data-minimization requirements that any account-data-sharing regime must satisfy, and a right to data portability that predates and reinforces open banking."
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
jurisdiction: European Union / United Kingdom
---

The **General Data Protection Regulation (GDPR)** is the privacy law that sits underneath open banking rather than beside it. Open banking moves personal financial data between parties; GDPR (and the retained UK GDPR) governs whether that movement is lawful — the consent, the lawful basis, the minimization, and the individual's right to port their data.

  * **A right to data portability** - GDPR's Article 20 gives individuals a right to receive and transmit their personal data, a general-purpose portability right that predates and reinforces the sector-specific open-banking mandates.
  * **Consent and lawful basis** - Every account-information consent in open banking has to rest on a GDPR-valid basis; the consent surface is not just an open-banking artifact, it is a data-protection requirement.
  * **Data minimization by design** - The least-privilege scope models in open-banking APIs are, in part, GDPR's minimization principle expressed in machine-readable form.

GDPR is why the consent layer matters as much as the contract in my scoring. A regulated data-sharing API is not just an OpenAPI and an auth stack — it is a lawful-basis machine, and the thinness of machine-readable consent surfaces across every banking market I scored is, in part, a GDPR gap as much as an open-banking one.
