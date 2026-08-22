---
standards:
- title: HL7 FHIR
  url: https://standards.apievangelist.com/store/fhir/
  note: TEFCA increasingly incorporates FHIR alongside document-based exchange.
name: TEFCA
kind: regulator-guidance
jurisdiction: United States
slug: tefca
title: Trusted Exchange Framework and Common Agreement (TEFCA)
description: TEFCA is a US framework, established under the 21st Century Cures Act and operationalized
  by the ONC with a Recognized Coordinating Entity, that creates a nationwide floor for health information
  exchange. It defines a common set of principles (the Trusted Exchange Framework) and a legal contract
  (the Common Agreement) that connect networks through certified Qualified Health Information Networks
  (QHINs), so participants can exchange data across the country under one trust arrangement rather than
  thousands of bilateral deals. It became operational in 2023.
tags:
- Healthcare
- Interoperability
- Health Information Exchange
- United States
- FHIR
- Regulation
common:
- type: Regulator
  url: https://www.healthit.gov/topic/interoperability/policy/trusted-exchange-framework-and-common-agreement-tefca
- type: Website
  url: https://rce.sequoiaproject.org/
url: https://www.healthit.gov/topic/interoperability/policy/trusted-exchange-framework-and-common-agreement-tefca
yearCreated: 2023
companyCount: 2
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 95
precisionGrade: high
precisionBasis:
- 'acronym-shape -5: shortest bare needle is 5 characters, halved — it neither collides nor appears in
  the corpus frequency table'
---

**TEFCA** is the attempt to give US health data exchange a single national trust floor. Instead of thousands of point-to-point agreements, it establishes a common legal contract and a set of certified Qualified Health Information Networks (QHINs) through which any participant can reach any other — the connective tissue above the individual FHIR and document APIs.

  * **A framework plus an agreement** - The Trusted Exchange Framework sets principles; the Common Agreement is the enforceable contract that binds participants.
  * **QHINs as the backbone** - Certified networks interconnect, so joining one reaches the whole.
  * **FHIR, arriving** - Historically document-and-query based, TEFCA is incorporating FHIR-based exchange as it matures.

TEFCA is worth cataloguing because it operates one layer above what my scoring reads: I measure the FHIR CapabilityStatement a provider publishes; TEFCA governs whether a query can legally and technically cross the country to reach it. It is the difference between an API existing and a nationwide network being able to use it — and, like the rest of US health interoperability, its promise depends on the messy work of making the underlying contracts consistent, discoverable, and usable, which is exactly where the sector's scores say the effort is still needed.
