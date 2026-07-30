---
papers:
- title: The CAMARA Standard
  url: https://papers.apievangelist.com/papers/the-camara-standard/
  note: "Restricts exactly the subscriber data CAMARA's flagship verbs traffic in — telecom is regulated on the input, not the output."
- title: The State of Telecom APIs
  url: https://papers.apievangelist.com/papers/state-of-telecom-apis/
  note: "The regime governing traffic and location data in EU networks — which is precisely what CAMARA's Device Location and Population Density APIs expose, and why the standard's consent model was designed to be recorded and interrogable."
standards:
- title: CAMARA
  url: https://standards.apievangelist.com/store/camara/
  note: "CAMARA's location and network-data APIs operate on exactly the traffic and location data this Directive restricts."
- title: GSMA Open Gateway
  url: https://standards.apievangelist.com/store/gsma-open-gateway/
  note: "The programme's consent design is a direct answer to regulators operating regimes like this one."
name: ePrivacy Directive
kind: directive
jurisdiction: European Union
slug: eprivacy-directive
title: ePrivacy Directive (2002/58/EC)
description: >-
  The ePrivacy Directive governs privacy in electronic communications across the European Union, regulating the confidentiality of communications, traffic data, and — most relevantly for network APIs — location data. It sits alongside the GDPR as the sector-specific regime for communications providers, and generally requires consent before location or traffic data may be processed for value-added services.
tags:
- Privacy
- Telecommunications
- European Union
- Regulation
- Consent
- Location Data
common:
- type: Website
  url: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32002L0058
url: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32002L0058
yearCreated: 2002
alternativeNames:
- Directive 2002/58/EC
- ePrivacy
- Cookie Law
- ePrivacy Regulation
jurisdiction: European Union
---

ePrivacy is the regulation most directly implicated by the network-API programme, and it is rarely named in
the industry's own marketing.

  * **Traffic and location data** - Processing beyond what is necessary for transmission or billing generally
    requires informed consent, and this is precisely the category CAMARA's Device Location, Geofencing and
    Population Density APIs operate on.
  * **Confidentiality of communications** - A baseline restriction independent of the GDPR's lawful-basis
    machinery.
  * **Applies to the operator** - The obligations fall on the provider of the electronic communications service —
    the carrier — rather than on the developer consuming an API.
  * **A long-delayed successor** - The proposed ePrivacy Regulation, intended to align the regime with the GDPR,
    has been stalled for years, leaving a directive implemented differently in each member state.

This is why the GSMA's consent model is the most thoughtful piece of policy engineering in *The State of Telecom
APIs*: consent recorded when it happens and interrogable afterward is an answer to a regulator asking, later, on
what basis a subscriber's location was disclosed — and under a directive implemented separately in each member
state, "later" and "in which country" are both hard questions.

**A note on provenance.** This entry is analytical rather than cited: the report documents the CAMARA location
APIs and the consent design in detail, and the connection to this Directive is drawn here rather than in the paper
itself.
