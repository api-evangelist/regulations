---
papers:
- title: The State of US Healthcare APIs
  url: https://papers.apievangelist.com/papers/state-of-us-healthcare-apis/
  note: The certification program whose (g)(10) criterion defines what a compliant EHR FHIR API must actually
    contain.
standards:
- title: SMART on FHIR
  url: https://standards.apievangelist.com/store/smart-on-fhir/
  note: The (g)(10) criterion requires SMART App Launch and SMART Backend Services.
- title: US Core
  url: https://standards.apievangelist.com/store/us-core/
  note: Certified APIs must expose US Core profiles.
- title: USCDI
  url: https://standards.apievangelist.com/store/uscdi/
  note: The data classes certified health IT must support.
name: ONC Health IT Certification Program
slug: onc-health-it-certification
title: ONC Health IT Certification Program (Cures Act Final Rule)
description: The ONC Health IT Certification Program is the US voluntary-but-effectively-mandatory program
  under which health IT is certified against federal criteria. Its Cures Act Final Rule 'Standardized
  API for patient and population services' criterion — commonly cited as (g)(10) — requires certified
  systems to expose HL7 FHIR (US Core), SMART App Launch, SMART Backend Services, and Bulk Data, with
  published service base URLs and transparent, non-discriminatory business terms. It defines what a compliant
  healthcare API must technically contain.
tags:
- Healthcare
- Certification
- Interoperability
- United States
- FHIR
- Regulation
common:
- type: Regulator
  url: https://www.healthit.gov/topic/certification-ehrs/certification-health-it
- type: Legislation
  url: https://www.healthit.gov/curesrule/
url: https://www.healthit.gov/topic/certification-ehrs/certification-health-it
yearCreated: 2020
---

**The ONC Health IT Certification Program** is where the Cures Act's 'standardized API' promise becomes a concrete checklist. Certification is nominally voluntary, but because it gates participation in federal programs it is effectively mandatory — and its (g)(10) criterion is the precise definition of what a compliant EHR FHIR API has to be.

  * **The (g)(10) 'Standardized API' criterion** - Certified systems must expose HL7 FHIR with US Core profiles, SMART App Launch, SMART Backend Services, and Bulk Data.
  * **Transparency conditions** - Published service base URLs and transparent, non-discriminatory business and technical terms — an attempt to stop malicious compliance.
  * **The USCDI data floor** - The API must carry the current USCDI data classes.

I catalogue the certification program because it is the rare mandate that reached past 'have an API' toward 'have a *specified* one' — it names the standards, which is more than most regulators do. And yet my scoring shows the limit of even a well-specified rule: a certified (g)(10) endpoint at an incumbent is real and gated, a compliance interface rather than a developer product. Specifying the standard is necessary and not sufficient; the examples, discovery documents, consent surface, and self-serve access that make it usable are still left to the vendor's discretion, and mostly left unbuilt.
