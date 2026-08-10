---
headers:
- name: prefer
  basis: mandated
  observable: contract
  standard: fhir-bulk-data
papers:
- title: The State of Digital Health APIs
  url: https://papers.apievangelist.com/papers/state-of-digital-health-apis/
  note: "One of exactly two rules in the world that effectively compel a health API — and the report measures what that compulsion produced."
- title: The State of US Healthcare APIs
  url: https://papers.apievangelist.com/papers/state-of-us-healthcare-apis/
  note: The law whose information-blocking rule turned a whole sector's FHIR endpoints into a legal obligation
    — and produced compliance, not product.
standards:
- title: HL7 FHIR
  url: https://standards.apievangelist.com/store/fhir/
  note: The standard the rule requires certified health IT to expose.
- title: US Core
  url: https://standards.apievangelist.com/store/us-core/
  note: The FHIR profiles that define the required data floor.
- title: SMART on FHIR
  url: https://standards.apievangelist.com/store/smart-on-fhir/
  note: The authorization standard the standardized-API criterion mandates.
name: 21st Century Cures Act
kind: statute
jurisdiction: United States
slug: 21st-century-cures-act
title: 21st Century Cures Act (Information Blocking Rule)
description: 'The 21st Century Cures Act is a 2016 US law whose ONC Final Rule (2020) prohibits ''information
  blocking'' — practices that interfere with the access, exchange, or use of electronic health information
  — and requires certified health IT to expose a standardized, FHIR-based API ''without special effort.''
  It is the legal force behind US healthcare API interoperability: it made patient and population access
  to health data over HL7 FHIR, US Core, and SMART on FHIR a compliance obligation rather than a voluntary
  feature.'
tags:
- Healthcare
- Interoperability
- Information Blocking
- United States
- FHIR
- Regulation
common:
- type: Legislation
  url: https://www.congress.gov/bill/114th-congress/house-bill/34
- type: Regulator
  url: https://www.healthit.gov/topic/information-blocking
url: https://www.healthit.gov/topic/information-blocking
yearCreated: 2016
---

**The 21st Century Cures Act** is the law that pried US healthcare data open, and its information-blocking rule is the closest thing American health IT has to the access-to-account mandate that PSD2 gave European banking. It makes it illegal for a certified EHR, provider, or health information network to interfere with the access, exchange, or use of electronic health information, and it requires that data be reachable through a standardized, FHIR-based API 'without special effort.'

  * **Information blocking, defined and prohibited** - Practices that get in the way of legitimate data access — beyond a set of narrow exceptions — are unlawful.
  * **A standardized API mandate** - Certified health IT must expose patient and population data over HL7 FHIR, US Core, and SMART on FHIR (see the ONC certification program).
  * **Patient-directed at its core** - The right it operationalizes is the patient's — the reason the API exists is to benefit the person whose data it is.

This is the regulation I have in mind when I say a rule produces compliance, not quality. Cures made every certified EHR publish a FHIR endpoint; it did not make any of them build a developer product, which is exactly the split my US healthcare scoring finds — real, gated compliance CapabilityStatements at the incumbents, and genuinely usable self-serve FHIR only where a company chose to build it. The law is the right lever; the gap between existence and usability is the part enforcement of the *spirit*, not just the letter, still has to close.
