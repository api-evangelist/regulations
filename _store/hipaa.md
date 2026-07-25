---
papers:
- title: The State of US Healthcare APIs
  url: https://papers.apievangelist.com/papers/state-of-us-healthcare-apis/
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
---

**HIPAA** is the law that makes consent the moral center of US healthcare, and it is the reason the patient-directed API is more than a nice idea. Its Privacy Rule sets when protected health information may move and gives patients a right of access to their own records; its Security Rule requires real safeguards on electronic PHI. Together they are the baseline every healthcare API in the country operates under.

  * **The right of access (§164.524)** - The paper-era right that a patient can get, and direct, their own record — the legal seed of the patient-directed API.
  * **The Security Rule** - Administrative, physical, and technical safeguards, the floor that frameworks like HITRUST are built to demonstrate against.
  * **Enforced with teeth** - The HHS Office for Civil Rights investigates and penalizes, which is why compliance posture is a first-order concern for every vendor.

HIPAA is the regulation I keep pointing to when I say healthcare should have been the API economy's gift on consent. The law makes consent foundational; the technical layer has never caught up. Across every healthcare cohort I score, not one provider exposes consent as a first-class, machine-legible surface — HIPAA makes it central, FHIR even defines a Consent resource, and still the agent gets scopes and no consent state. Closing that gap is the single most important thing the sector could do, and HIPAA is the reason it is not optional.
