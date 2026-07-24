---
papers:
- title: The State of Australian Healthcare APIs
  url: https://papers.apievangelist.com/papers/state-of-australian-healthcare-apis/
  note: The device regulation that governs software-as-a-medical-device, including the clinical-AI tools
    the cohort ships.
name: EU Medical Device Regulation
slug: eu-mdr
title: EU Medical Device Regulation (MDR)
description: The EU Medical Device Regulation (Regulation (EU) 2017/745, MDR) governs the safety and performance
  of medical devices placed on the European market, and — critically for digital health — brings much
  Software as a Medical Device (SaMD) into scope. It requires CE marking, clinical evaluation, a quality
  management system (typically ISO 13485), risk classification, and post-market surveillance. Fully applicable
  since 2021, it replaced the older Medical Devices Directive and raised the bar for any software that
  diagnoses, monitors, or informs clinical decisions.
tags:
- Healthcare
- Medical Devices
- Software as a Medical Device
- Safety
- Europe
- Regulation
common:
- type: Legislation
  url: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32017R0745
- type: Regulator
  url: https://health.ec.europa.eu/medical-devices-sector_en
url: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32017R0745
yearCreated: 2017
regulations:
- title: GDPR
  url: https://regulations.apievangelist.com/store/gdpr/
  note: MDR sits alongside the GDPR in the EU regulatory stack for health technology.
---

**The EU Medical Device Regulation** is the reason a lot of health *software* is now regulated like a medical device. MDR governs safety and performance for devices on the European market, and it deliberately pulls Software as a Medical Device — anything that diagnoses, monitors, or informs a clinical decision — into scope, with CE marking, clinical evaluation, and post-market surveillance.

  * **Software in scope** - SaMD is classified by risk and must meet the same conformity route as physical devices, up to CE marking.
  * **A quality system behind it** - Compliance typically rests on an ISO 13485 quality management system and documented clinical evaluation.
  * **Post-market obligations** - Surveillance and vigilance duties continue after a product ships.

MDR earns a place in the catalogue because the clinical-AI wave my scoring keeps surfacing runs straight into it: an ambient scribe or a decision-support tool that crosses from documentation into clinical influence can become a regulated device. It is the regulatory counterpart to standards like ISO 42001 — where 42001 asks whether you *govern* your AI, MDR asks whether a clinical software product is *safe and proven* enough to be trusted with a patient. For anyone building agentic clinical tools for Europe, it is the line between a productivity feature and a regulated medical device, and it is worth knowing which side you are on before you ship.
