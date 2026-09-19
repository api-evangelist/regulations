---
name: SEC Cybersecurity Disclosure Rules
kind: regulation
jurisdiction: United States (federal)
scope: horizontal
countries:
- united-states
regions:
- north-america
industries:
- cybersecurity
- financial-services
- technology
- enterprise-software
- accounting-finance-ops
slug: sec-cybersecurity-disclosure
title: SEC Cybersecurity Risk Management, Strategy, Governance and Incident Disclosure Rules
description: SEC rules require public companies to disclose a material cybersecurity incident on Form
  8-K Item 1.05 within four business days of determining materiality, and to describe their risk management
  processes and board oversight annually in Form 10-K Item 1C. It is the regime that made a security incident
  a securities-disclosure event, and its reach extends well past registrants to every vendor whose outage
  could be material to one.
tags:
- Cybersecurity
- Incident Disclosure
- Governance
- Materiality
- United States
- Regulation
common:
- type: Legislation
  url: https://www.sec.gov/rules/final/2023/33-11216.pdf
- type: Regulator
  url: https://www.sec.gov/
url: https://www.sec.gov/rules/final/2023/33-11216.pdf
yearCreated: 2023
alternativeNames:
- Item 1.05
- Item 1C
- SEC cyber disclosure rule
- Reg S-K Item 106
companyCount: 1
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---

The **SEC cybersecurity disclosure rules** changed the character of incident response at public companies by attaching a securities-law clock to it. Effective since December 2023.

  * **Form 8-K Item 1.05, four business days** - From the determination that an incident is material, not from discovery. The determination itself must be made "without unreasonable delay", which is where the pressure actually sits.
  * **Describe nature, scope, timing and material impact** - Including reasonably likely impact. Technical detail that would impede response can be withheld.
  * **Form 10-K Item 1C, annually** - Processes for assessing, identifying and managing material cyber risk; board oversight; management's role and expertise.
  * **Third-party risk is explicitly in scope** - Incidents at service providers can be material to the registrant, and the annual disclosure must address how third-party risk is managed.
  * **A national-security delay** - Available only where the Attorney General determines disclosure poses a substantial risk, and rarely granted.

Practice matured faster than most people expected. The early months produced a wave of defensive Item 1.05 filings for incidents that were not material, which the SEC's own staff discouraged — the correct venue for a non-material incident is Item 8.01, voluntarily, or nowhere. By 2026 filings had settled into more calibrated materiality assessments, with board oversight, ransom-payment decisions, service-provider risk and national-security interaction as the recurring themes.

The part of this rule that reaches this catalog hardest is the third-party provision, and it reaches companies that are not registrants at all. If an API provider's outage or breach is material to a public-company customer, that customer has a four-day clock that depends on information only the provider has. The commercial consequence has been a sharp rise in contractual notification terms — 24 hours, 48 hours, immediate — flowing down to vendors, and in practice those contract terms bind far more companies than the rule itself does.

That is the mechanism I keep pointing at. A regulation lands on a registrant, and the registrant converts it into a procurement requirement, and the procurement requirement is what actually changes how software gets built. An API provider that can tell a customer quickly and precisely what happened, what data was reached, and over what window is now selling something. One that cannot is now a disclosure risk. Neither fact appears anywhere in a public API contract today, which is exactly the sort of gap this catalog exists to name: a status page is not an incident notification, and an incident notification is not a materiality input, and the difference is four business days.
