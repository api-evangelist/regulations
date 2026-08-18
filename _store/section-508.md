---
headers:
- name: content-language
  basis: inferred
  observable: edge
papers:
- title: The State of Education & EdTech APIs
  url: https://reports.apievangelist.com/reports/state-of-education-apis/
  note: Accessibility enforced through procurement, met with a self-asserted PDF — an obligation ABOUT
    the interface, discharged with a document.
name: Section 508
kind: regulation
jurisdiction: United States
slug: section-508
title: Section 508 of the Rehabilitation Act
description: Section 508 requires US federal agencies — and, through procurement rules and state adoptions,
  the institutions that take federal funds — to make information and communications technology accessible
  to people with disabilities. The Revised 508 Standards adopt WCAG Level AA as the technical requirement.
tags:
- Accessibility
- Procurement
- Public Sector
- Education
- United States
- Regulation
common:
- type: Regulator
  url: https://www.section508.gov/
- type: Specification
  url: https://www.access-board.gov/ict/
url: https://www.section508.gov/
yearCreated: 1998
alternativeNames:
- Section 508
- 29 U.S.C. § 794d
- Revised 508 Standards
standards:
- title: WCAG
  url: https://standards.apievangelist.com/store/wcag/
  note: The Revised 508 Standards adopt WCAG Level AA as their technical requirement rather than defining
    separate criteria.
companyCount: 10
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 75
precisionGrade: medium
precisionBasis:
- 'collision -25: a surviving needle is also claimed by standards:Accessibility Standards'
precisionRecognition: 100
---

**Section 508** works through purchasing. An agency or institution subject to it cannot buy software that fails the standard, which turns accessibility from an ethical position into a procurement gate — and makes the vendor's accessibility conformance report a document salespeople carry to every education deal in the United States.

  * **WCAG Level AA by reference** - The Revised Standards adopt [WCAG](https://standards.apievangelist.com/store/wcag/) rather than defining their own criteria.
  * **Enforced through procurement** - The mechanism is the purchase decision, which is why it reaches vendors with no direct federal relationship.
  * **VPAT and ACR** - A voluntary product accessibility template, filled in by the vendor — self-asserted, PDF, and universal in education RFPs.
  * **Reaches education broadly** - Public institutions and federally funded programmes carry it into the classroom software market.

The VPAT is worth noticing as an artifact. It is a compliance claim about an interface, produced for every education sale, distributed as a PDF, and self-asserted — a document where a machine-readable conformance statement would serve everyone better. [The State of Education & EdTech APIs](https://reports.apievangelist.com/reports/state-of-education-apis/) records this market's pattern precisely: obligations are met with documents rather than artifacts, even where the obligation is *about* the interface.
