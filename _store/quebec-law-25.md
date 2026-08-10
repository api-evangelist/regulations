---
headers:
- name: clear-site-data
  basis: evidentiary
  observable: edge
papers:
- title: The State of Canadian Insurance APIs
  url: https://papers.apievangelist.com/papers/state-of-canadian-insurance-apis/
  note: "The strictest privacy regime in North America sits over a sector where consent is a first-class surface at zero of the market leaders."
name: Quebec Law 25
kind: statute
jurisdiction: Quebec, Canada
slug: quebec-law-25
title: Quebec Law 25 (Act 64)
description: >-
  Quebec's Law 25 is the province's modernization of personal-information protection, introducing consent requirements, breach notification, privacy-by-default, automated-decision transparency and a right to data portability. It is widely regarded as the strictest privacy regime in North America and applies to insurers operating in Quebec alongside federal PIPEDA.
tags:
- Privacy
- Canada
- Quebec
- Regulation
- Consent
- Data Portability
common:
- type: Website
  url: https://www.cai.gouv.qc.ca/
- type: Regulator
  url: https://www.cai.gouv.qc.ca/
url: https://www.cai.gouv.qc.ca/
yearCreated: 2021
alternativeNames:
- Law 25
- Bill 64
- Act to modernize legislative provisions as regards the protection of personal information
- Loi 25
jurisdiction: Canada (Quebec)
---

Law 25 matters to API practitioners because it contains the two things that most directly shape an
interface: a consent regime and a portability right.

  * **Explicit, purpose-bound consent** - Consent must be granular and informed, which is precisely the surface
    most regulated sectors fail to expose as a first-class resource.
  * **Data portability** - A right to receive computerized personal information in a structured, commonly used
    technological format — a portability right that implies a machine-readable path.
  * **Automated decision transparency** - Individuals must be informed when a decision is based exclusively on
    automated processing, which reaches insurance underwriting directly.
  * **Real penalties** - Administrative and penal sanctions give the regime teeth that PIPEDA historically lacked.

The pattern this catalog keeps recording holds here too. *The State of Canadian Insurance APIs* found consent
satisfied by 10% of the market and by zero of the three highest-scoring organizations, in a country with PIPEDA
federally and Law 25 provincially. Strict privacy law produced compliance documentation; it did not produce a
consent API.
