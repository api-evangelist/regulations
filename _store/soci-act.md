---
name: Security of Critical Infrastructure Act
kind: statute
jurisdiction: Australia
scope: sectoral
countries:
- australia
regions:
- anz
industries:
- cybersecurity
- cloud-data-platform
- energy
- utilities
- healthcare
- telecommunications
- transportation
- banking
slug: soci-act
title: Security of Critical Infrastructure Act 2018 (Cth)
description: 'The SOCI Act imposes registration, mandatory incident reporting and a Critical
  Infrastructure Risk Management Program on responsible entities across eleven sectors — and, unusually,
  treats DATA STORAGE AND PROCESSING as a critical infrastructure asset class in its own right. It also
  gives government last-resort step-in powers to intervene directly in a serious incident, which is the
  most intrusive provision in this catalog.'
tags:
- Critical Infrastructure
- Risk Management
- Incident Reporting
- Data Storage
- Australia
- Regulation
common:
- type: Legislation
  url: https://www.legislation.gov.au/C2018A00029/latest/text
- type: Regulator
  url: https://www.cisc.gov.au/
url: https://www.cisc.gov.au/
yearCreated: 2018
alternativeNames:
- SOCI
- SOCI Act
- Critical Infrastructure Act
- CIRMP
companyCountStatus: pending-corpus-pass
---

The **SOCI Act** is the Australian regime most likely to apply to a technology company that does not think of itself as infrastructure, and the reason is a definitional choice made in the 2021–22 amendments: **critical data storage or processing** is its own asset class. A provider holding or processing business-critical data on behalf of a responsible entity in a covered sector can be regulated directly, rather than being managed as somebody else's supply-chain risk.

  * **Eleven sectors** - Communications, data storage and processing, financial services and markets, water, energy, health care and medical, higher education and research, food and grocery, transport, space technology, and defence industry.
  * **Register of Critical Infrastructure Assets** - Ownership and operational control, reported to government.
  * **Mandatory cyber incident reporting** - 12 hours for a critical incident having a significant impact; 72 hours for a relevant incident. The 12-hour clock is the shortest in this catalog.
  * **Critical Infrastructure Risk Management Program** - Covering cyber, personnel, physical and **supply chain** hazards, with an annual board-approved report.
  * **Government assistance measures** - Information gathering, action direction, and an intervention power allowing the Australian Signals Directorate to act directly on a system in a serious incident.

That last power deserves to be named plainly, because there is nothing else like it in the regimes I track. Every other cyber regime tells an operator what to do. SOCI contemplates the state doing it instead, on the operator's systems, as a last resort. It was contested during passage and its practical use has been minimal — but it exists, and any risk assessment for an Australian critical-infrastructure asset has to account for it.

The 12-hour reporting clock is the operational constraint that shapes everything else. Twelve hours is not enough time to complete an investigation, which means it cannot be an investigation-complete report — it is a detection-and-notify obligation, and meeting it requires the detection, the triage path, the decision authority and the reporting channel all to be pre-built. A company that plans to work out who signs off during the incident will miss it.

The convergence point is worth noting for anyone already doing this work elsewhere. SOCI's risk-management program, DORA's ICT risk framework, NIS2's supply-chain requirements and the DOJ bulk data rule's vendor due diligence are four regimes asking variations of one question: **who touches your critical systems and data, what is their security posture, and can you demonstrate you assessed it?** Four jurisdictions, four legal theories, one control. An organisation that builds a genuine third-party risk capability once can answer all four; one that builds four compliance artefacts will maintain four and satisfy none of them well.
