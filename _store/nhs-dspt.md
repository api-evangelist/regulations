---
headers:
- name: strict-transport-security
  basis: evidentiary
  observable: edge
papers:
- title: The State of Digital Health APIs
  url: https://papers.apievangelist.com/papers/state-of-digital-health-apis/
  note: "An assurance regime gating access to the national platform, scored alongside ten other health regimes."
- title: The State of UK Healthcare APIs
  url: https://papers.apievangelist.com/papers/state-of-uk-healthcare-apis/
  note: The NHS assurance regime every supplier touching patient data must pass — and which none in the
    cohort publishes as a legible artifact.
name: NHS Data Security and Protection Toolkit
kind: regulator-guidance
jurisdiction: United Kingdom
slug: nhs-dspt
title: NHS Data Security and Protection Toolkit (DSPT)
description: The NHS Data Security and Protection Toolkit (DSPT) is an annual online self-assessment that
  organizations must complete to demonstrate they meet the National Data Guardian's data security standards
  and can be trusted to handle NHS patient data and access NHS systems. Operated by NHS England, it is
  effectively mandatory for any supplier, provider, or partner in the English health and care system,
  and is a prerequisite for connecting to national services such as the Spine and the FHIR-based APIs
  on the NHS API platform.
tags:
- Healthcare
- Security
- Data Protection
- United Kingdom
- NHS
- Regulation
common:
- type: Regulator
  url: https://www.dsptoolkit.nhs.uk/
url: https://www.dsptoolkit.nhs.uk/
yearCreated: 2018
---

**The NHS Data Security and Protection Toolkit** is the assurance gate every organization touching NHS patient data has to pass. It is an annual self-assessment against the National Data Guardian's standards, and it is effectively mandatory: without a satisfactory DSPT, a supplier cannot connect to national services like the Spine or the FHIR APIs on the NHS API platform.

  * **Annual self-assessment** - Organizations attest yearly against a defined set of data-security and information-governance standards.
  * **A connection prerequisite** - It gates access to NHS national systems and APIs, so it is a de-facto requirement, not a nicety.
  * **The NHS-specific layer** - Where SOC 2 and ISO 27001 are the commercial assurances, DSPT (with DTAC) is the NHS's own.

I catalogue DSPT because of a specific gap my UK healthcare scoring surfaced: every member of the cohort handles NHS clinical data, and none publishes its DSPT (or DTAC) status as a legible artifact. The assurance is real and mandatory; it simply lives in a portal rather than in anything an integrator or an agent can read at trust-time. In a single-payer system, publishing NHS-specific assurance as a machine-readable signal is one of the cheapest ways a supplier could differentiate — and, at present, none does.
