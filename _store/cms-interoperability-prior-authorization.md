---
papers:
- title: The State of US Healthcare APIs
  url: https://papers.apievangelist.com/papers/state-of-us-healthcare-apis/
  note: The rule that points electronic prior authorization at the Da Vinci FHIR IGs — the emptiest frontier
    in the cohort.
standards:
- title: Da Vinci
  url: https://standards.apievangelist.com/store/da-vinci/
  note: CMS-0057-F names the Da Vinci CRD/DTR/PAS IGs for electronic prior authorization.
- title: FHIR Bulk Data Access
  url: https://standards.apievangelist.com/store/fhir-bulk-data/
  note: Payer data exchange under the rule leans on bulk FHIR.
- title: CARIN Blue Button
  url: https://standards.apievangelist.com/store/carin-blue-button/
  note: The Patient Access API exposes claims via CARIN Blue Button.
name: CMS Interoperability & Prior Authorization Rule
kind: regulator-guidance
jurisdiction: United States
slug: cms-interoperability-prior-authorization
title: CMS Interoperability & Prior Authorization Rule (CMS-0057-F)
description: The CMS Interoperability and Prior Authorization Final Rule (CMS-0057-F), finalized in 2024,
  requires impacted US payers — Medicare Advantage, Medicaid, CHIP, and ACA exchange plans — to build
  FHIR APIs for patient access, provider access, payer-to-payer exchange, and, most notably, an electronic
  Prior Authorization API based on the HL7 Da Vinci implementation guides. With compliance dates in 2026–2027,
  it is the regulation pulling the payer and prior-authorization side of US healthcare onto FHIR.
tags:
- Healthcare
- Payer
- Prior Authorization
- Interoperability
- United States
- FHIR
- Regulation
common:
- type: Regulator
  url: https://www.cms.gov/priorities/key-initiatives/burden-reduction/interoperability/policies-and-technology/interoperability-and-prior-authorization-final-rule-cms-0057-f
url: https://www.cms.gov/priorities/key-initiatives/burden-reduction/interoperability/policies-and-technology/interoperability-and-prior-authorization-final-rule-cms-0057-f
yearCreated: 2024
---

**The CMS Interoperability and Prior Authorization Rule** — CMS-0057-F — is the regulation aimed at the part of US healthcare the Cures Act mostly left alone: the payers, the claims, and the prior-authorization paperwork. It requires impacted health plans to stand up a family of FHIR APIs, and it does the thing regulators too rarely do — it names the standard.

  * **Four APIs** - Patient Access, Provider Access, Payer-to-Payer exchange, and an electronic Prior Authorization API.
  * **Da Vinci by name** - The prior-auth API is built on the HL7 Da Vinci CRD/DTR/PAS guides, turning a fax-and-phone process into an API workflow.
  * **Phased compliance** - Dates land in 2026–2027, so much of the build is still ahead of the market.

This rule is the clearest test in my healthcare series of whether naming a good standard is enough. CMS pointed prior authorization squarely at Da Vinci — and Da Vinci is the emptiest frontier I measured, with a single US provider explicitly conforming. The regulation is the right instrument aimed at a genuinely painful problem; whether it produces usable, agent-legible prior-auth APIs or another layer of gated compliance endpoints is exactly the question the next few years will answer, and the one my scoring will keep tracking.
