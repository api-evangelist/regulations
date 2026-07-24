---
papers:
- title: The State of Canadian Healthcare APIs
  url: https://papers.apievangelist.com/papers/state-of-canadian-healthcare-apis/
  note: The health-specific privacy regime governing the province-fragmented Canadian market the report
    scores.
name: PHIPA
slug: phipa
title: Personal Health Information Protection Act (PHIPA)
description: The Personal Health Information Protection Act (PHIPA) is Ontario's health-sector privacy
  law, in force since 2004 and overseen by the Information and Privacy Commissioner of Ontario. It governs
  how health information custodians collect, use, and disclose personal health information, and establishes
  patients' rights of access and correction. As Canadian healthcare is province-regulated, PHIPA is the
  most prominent of several provincial health-privacy regimes (alongside the federal PIPEDA), and it is
  the consent-and-access framework Canadian health-data APIs operate under.
tags:
- Healthcare
- Privacy
- Consent
- Canada
- Ontario
- Regulation
common:
- type: Legislation
  url: https://www.ontario.ca/laws/statute/04p03
- type: Regulator
  url: https://www.ipc.on.ca/
url: https://www.ontario.ca/laws/statute/04p03
yearCreated: 2004
regulations:
- title: PIPEDA
  url: https://regulations.apievangelist.com/store/pipeda/
  note: PHIPA is Ontario's health-sector-specific counterpart to the federal PIPEDA.
---

**PHIPA** is Ontario's health-privacy law, and the most prominent example of a structural fact about Canadian healthcare: it is regulated province by province, not nationally. PHIPA governs how health information custodians handle personal health information and gives patients rights of access and correction, sitting alongside the federal PIPEDA and a patchwork of other provincial regimes.

  * **Custodian-centric** - It places obligations on the health information custodians who hold the data, with consent as the organizing principle.
  * **Access and correction rights** - The patient's rights that a data-access API would, in principle, operationalize.
  * **One of many** - Ontario's law is the best-known, but each province has its own, which is part of why there is no national access layer.

PHIPA is the consent framework behind the emptiest healthcare market I scored. Canada has the privacy law and, federally through Canada Health Infoway, the FHIR standards — and almost no live clinical FHIR to apply them to. The province fragmentation PHIPA exemplifies is precisely why there is no national patient-facing API: the legal and standards groundwork exists, and the connective, usable, consent-legible layer that would let an app or an agent act on it does not. It is the same compliance-without-usability gap, in a federated form.
