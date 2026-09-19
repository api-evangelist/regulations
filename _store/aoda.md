---
name: Accessibility for Ontarians with Disabilities Act
kind: statute
jurisdiction: Ontario, Canada
scope: horizontal
countries:
- canada
regions:
- north-america
industries:
- e-commerce-platform
- retail
- education
- government
- banking
- technology
slug: aoda
title: Accessibility for Ontarians with Disabilities Act (S.O. 2005, c. 11)
description: 'AODA and its Integrated Accessibility Standards Regulation require organisations with 50
  or more employees in Ontario to make their public websites and web content conform to WCAG 2.0 Level
  AA, and to file periodic compliance reports with the province. It is the North American regime that
  most resembles the European Accessibility Act: a named technical standard, a stated deadline, and a
  filing obligation — rather than the American approach of litigating it one defendant at a time.'
tags:
- Accessibility
- WCAG
- Compliance Reporting
- Ontario
- Canada
- Regulation
common:
- type: Legislation
  url: https://www.ontario.ca/laws/statute/05a11
- type: Regulator
  url: https://www.ontario.ca/page/accessibility-in-ontario
url: https://www.ontario.ca/laws/statute/05a11
yearCreated: 2005
alternativeNames:
- AODA
- Accessibility for Ontarians with Disabilities Act
- IASR
standards:
- title: WCAG
  url: https://standards.apievangelist.com/store/wcag/
  note: The Integrated Accessibility Standards Regulation names WCAG 2.0 Level AA directly, which is what
    distinguishes AODA from the US approach of litigating it case by case.
companyCount: 20
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 90
precisionGrade: high
precisionBasis:
- 'acronym-shape -10: shortest bare needle is 4 characters, halved — it neither collides nor appears in
  the corpus frequency table'
---

**AODA** is the quiet counterexample to the American way of doing web accessibility, and it sits in this catalog next to ADA Title III deliberately so the comparison is visible.

  * **A named standard** - WCAG 2.0 Level AA, for public websites and web content, under the Integrated Accessibility Standards Regulation.
  * **A stated threshold** - Organisations with 50 or more employees in Ontario, plus the public sector.
  * **A filing obligation** - Periodic accessibility compliance reports filed with the province. Non-filing is itself the violation, and it is trivially detectable.
  * **Administrative penalties** - Up to CAD 100,000 per day for a corporation, in principle.
  * **Enforcement by inspection and audit, not by lawsuit** - Which is the whole difference.

Ontario set itself a goal of full accessibility by 2025 and did not reach it; successive independent reviews have been blunt about under-enforcement. So I am not holding AODA up as a success. I am holding it up as the *right architecture with insufficient enforcement*, against a US regime that has vigorous enforcement and no architecture at all.

The distinction matters to anyone trying to build compliance into a product rather than into a legal budget. Under AODA you can ask "are we compliant?" and get an answer: conform to WCAG 2.0 AA, file the report. Under ADA Title III there is no standard to conform to, so the only available answers are "no lawsuit yet" and "we settled". One of those is an engineering target and the other is a risk posture.

The federal **Accessible Canada Act** (2019) layers on top for federally regulated sectors — banking, telecommunications, transportation, broadcasting — with accessibility plans, feedback processes and progress reports, and the CRTC and Canadian Transportation Agency enforcing in their own domains. A bank operating in Ontario is subject to both.

For an API provider the practical consequence is the same one the European Accessibility Act creates, and the two now stack. If you ship UI — an embedded widget, a hosted page, an SDK component, a documentation theme — that artefact lands inside a customer's compliance boundary. A customer in Ontario with 50 employees needs to file a report that covers it. A customer in the EU needs it to meet EN 301 549. Neither customer can produce that from your marketing site.

What they need is an accessibility conformance report attached to the component, versioned with it, and retrievable. It is the same artefact in both jurisdictions, it is standardised in form, and it belongs in developer documentation next to the changelog. Across this catalog it is one of the cheapest unmet asks I can point at.
