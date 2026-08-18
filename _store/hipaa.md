---
headers:
- name: cache-control
  basis: evidentiary
  observable: edge
  note: '`no-store` on a response carrying PHI, so it does not land in a shared cache.'
- name: strict-transport-security
  basis: evidentiary
  observable: edge
  note: Security Rule technical safeguards for transmission security.
papers:
- title: The State of Digital Health APIs
  url: https://reports.apievangelist.com/reports/state-of-digital-health-apis/
  note: 'The law consent is built on, measured: consent is a legible, machine-readable surface at 3.4%
    of the digital health market against 3.3% of the whole catalog.'
- title: The State of Cybersecurity APIs
  url: https://reports.apievangelist.com/reports/state-of-cybersecurity-apis/
  note: A security vendor holding health data is inside HIPAA; this market's regulatory surface is the
    union of its customers'.
- title: The State of Artificial Intelligence APIs
  url: https://reports.apievangelist.com/reports/state-of-artificial-intelligence-apis/
  note: An AI company's real regulatory exposure is usually inherited from its customers' industries rather
    than its own — HIPAA reaches a model the moment it touches clinical data.
- title: The State of US Healthcare APIs
  url: https://reports.apievangelist.com/reports/state-of-us-healthcare-apis/
  note: The privacy law that makes consent the moral center of healthcare — and whose right of access
    the patient-directed API operationalizes.
standards:
- title: HL7 FHIR
  url: https://standards.apievangelist.com/store/fhir/
  note: FHIR APIs carry the protected health information HIPAA governs.
- title: HITRUST CSF
  url: https://standards.apievangelist.com/store/hitrust/
  note: The framework organizations most use to demonstrate HIPAA Security Rule coverage.
name: HIPAA
kind: statute
jurisdiction: United States
slug: hipaa
title: Health Insurance Portability and Accountability Act (HIPAA)
description: HIPAA is the 1996 US law that governs the privacy and security of protected health information
  (PHI). Its Privacy Rule sets the terms under which PHI may be used and disclosed and grants patients
  a right of access to their own records (§164.524); its Security Rule mandates administrative, physical,
  and technical safeguards for electronic PHI. Enforced by the HHS Office for Civil Rights, HIPAA is the
  legal and ethical baseline every US healthcare API operates under — and the reason consent is not a
  nicety but a foundation.
tags:
- Healthcare
- Privacy
- Security
- Consent
- United States
- Regulation
common:
- type: Legislation
  url: https://www.hhs.gov/hipaa/for-professionals/index.html
- type: Regulator
  url: https://www.hhs.gov/ocr/index.html
url: https://www.hhs.gov/hipaa/
yearCreated: 1996
companyCount: 210
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 44
precisionGrade: low
precisionBasis:
- 'acronym-shape -10: shortest bare needle is 5 characters'
- 'collision -25: a surviving needle is also claimed by standards:HIPAA'
- 'bare-channel -21: 93% of matching companies were reached only on the bare word (210 bare vs 15 phrase)'
---

**HIPAA** is the law that makes consent the moral center of US healthcare, and it is the reason the patient-directed API is more than a nice idea. Its Privacy Rule sets when protected health information may move and gives patients a right of access to their own records; its Security Rule requires real safeguards on electronic PHI. Together they are the baseline every healthcare API in the country operates under.

  * **The right of access (§164.524)** - The paper-era right that a patient can get, and direct, their own record — the legal seed of the patient-directed API.
  * **The Security Rule** - Administrative, physical, and technical safeguards, the floor that frameworks like HITRUST are built to demonstrate against.
  * **Enforced with teeth** - The HHS Office for Civil Rights investigates and penalizes, which is why compliance posture is a first-order concern for every vendor.

HIPAA is the regulation I keep pointing to when I say healthcare should have been the API economy's gift on consent. The law makes consent foundational; the technical layer has never caught up. Across every healthcare cohort I score, not one provider exposes consent as a first-class, machine-legible surface — HIPAA makes it central, FHIR even defines a Consent resource, and still the agent gets scopes and no consent state. Closing that gap is the single most important thing the sector could do, and HIPAA is the reason it is not optional.
