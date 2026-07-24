---
papers:
- title: The State of UK Healthcare APIs
  url: https://papers.apievangelist.com/papers/state-of-uk-healthcare-apis/
  note: The NHS baseline for digital health technology, covering clinical safety, security, interoperability,
    and usability.
name: Digital Technology Assessment Criteria
slug: dtac
title: Digital Technology Assessment Criteria (DTAC)
description: The Digital Technology Assessment Criteria (DTAC) is the NHS's national baseline that digital
  health technologies are assessed against before being adopted across the health and care system. Introduced
  by NHS England, it brings together clinical safety (DCB0129/DCB0160), data protection (including the
  DSPT), technical security, interoperability, and usability and accessibility into a single assessment.
  It is how NHS organizations judge whether a digital product is safe and suitable to deploy, giving health-tech
  vendors one consistent bar to clear.
tags:
- Healthcare
- Clinical Safety
- Security
- Interoperability
- United Kingdom
- NHS
- Regulation
common:
- type: Regulator
  url: https://www.nhsx.nhs.uk/key-tools-and-info/digital-technology-assessment-criteria-dtac/
url: https://transform.england.nhs.uk/key-tools-and-info/digital-technology-assessment-criteria-dtac/
yearCreated: 2021
regulations:
- title: NHS Data Security and Protection Toolkit
  url: https://regulations.apievangelist.com/store/nhs-dspt/
  note: DTAC incorporates the DSPT as its data-protection component.
---

**The Digital Technology Assessment Criteria** is the NHS's single front door for judging whether a digital health product is safe and suitable to deploy. Rather than a vendor facing a different bar at every trust, DTAC brings the key requirements into one baseline assessment.

  * **Five areas** - Clinical safety (DCB0129/DCB0160), data protection (including the DSPT), technical security, interoperability, and usability and accessibility.
  * **One consistent bar** - It gives health-tech vendors a single, national criteria set to clear rather than bespoke local reviews.
  * **Adoption-gating** - NHS organizations use it to decide whether to bring a product in.

DTAC belongs in the catalogue as the interoperability-and-safety companion to the DSPT, and it points at the same finding from my UK healthcare scoring: the NHS has built genuinely rigorous assurance, and its suppliers publish almost none of it in machine-readable form. DTAC even *includes* interoperability as an assessed dimension — yet the cohort's contracts rarely surface the FHIR conformance, consent, or examples that would make that interoperability legible to an agent. The assessment exists; the published, checkable evidence of passing it does not, and that is the gap worth closing.
