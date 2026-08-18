---
papers:
- title: The State of Digital Health APIs
  url: https://reports.apievangelist.com/reports/state-of-digital-health-apis/
  note: Federal privacy law that restricts use without compelling an interface, in the most regulated
    market in the series.
- title: The State of Canadian Banking APIs
  url: https://reports.apievangelist.com/reports/state-of-canadian-banking-apis/
  note: The existing privacy regime Canada's not-yet-live consumer-driven banking framework is layered
    on.
name: PIPEDA
kind: statute
jurisdiction: Canada
slug: pipeda
title: Personal Information Protection and Electronic Documents Act (PIPEDA)
description: PIPEDA is Canada's federal private-sector privacy law, governing how organizations collect,
  use, and disclose personal information in the course of commercial activity. It is the privacy backdrop
  against which Canada's Consumer-Driven Banking framework is being built — the existing consent-and-data-handling
  regime that any Canadian financial-data sharing has to work within until, and after, open banking goes
  live.
tags:
- Privacy
- Data Protection
- Consent
- Canada
- Regulation
common:
- type: Legislation
  url: https://laws-lois.justice.gc.ca/eng/acts/P-8.6/
- type: Regulator
  url: https://www.priv.gc.ca/
url: https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/
yearCreated: 2000
alternativeNames:
- PIPEDA
- Personal Information Protection and Electronic Documents Act
companyCount: 18
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 85
precisionGrade: high
precisionBasis:
- 'bare-channel -15: 84% of matching companies were reached only on the bare word (16 bare vs 3 phrase)'
---

**PIPEDA** — the Personal Information Protection and Electronic Documents Act — is Canada's federal private-sector privacy law, governing how businesses handle personal information in commercial activity, on a consent-and-reasonable-purposes model.

  * **Consent-based handling** - Organizations must obtain meaningful consent to collect, use, or disclose personal information, and limit it to reasonable purposes.
  * **The pre-open-banking regime** - Like the US GLBA, PIPEDA governed financial data long before Canada legislated consumer-driven banking; the new framework sits on top of it.
  * **Under reform** - PIPEDA has been the subject of modernization efforts, which matter for how a future open-banking regime handles data.

PIPEDA is part of why Canada's open-banking story is one of *absence*: the privacy law existed, the banks handled data under it, but nothing required them to let a consumer *port* that data through an API. Canada did not lack privacy regulation; it lacked an access mandate — and the consumer-driven banking framework is the attempt to add one on top of PIPEDA.
