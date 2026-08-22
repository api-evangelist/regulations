---
name: FSMA Section 204 Food Traceability Rule
kind: regulation
jurisdiction: United States
slug: fsma-204
title: FSMA Section 204 Food Traceability Rule
description: The FDA rule implementing Section 204 of the Food Safety Modernization Act, requiring persons
  who manufacture, process, pack or hold foods on the Food Traceability List to keep key data elements
  for critical tracking events and to provide them to the FDA within 24 hours of a request.
tags:
- Supply Chain
- Food Safety
- Traceability
- United States
- Regulation
common:
- type: Website
  url: https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods
url: https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods
yearCreated: 2022
alternativeNames:
- FSMA 204
- Food Traceability Final Rule
- FSMA Rule 204(d)
companyCount: 0
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---

The **FSMA Section 204** rule is the FDA's answer to outbreak investigations that used to take weeks.
It requires anyone handling a food on the Food Traceability List to record **key data elements** at
**critical tracking events** — growing, receiving, transforming, creating, shipping — and to hand
them to the FDA within 24 hours of a request.

  * **Traceability lot codes** - The identifier that links records across companies.
  * **Critical tracking events** - The defined points at which records must be captured.
  * **24-hour production** - The obligation is speed of retrieval, which is what forces the data to be structured rather than filed.
  * **Sortable electronic spreadsheet** - The rule's stated expectation for how records are produced to the agency.

The design detail worth noting is the last one. The rule requires structured data produced *fast*,
which is genuinely demanding, and then names a spreadsheet as the delivery mechanism. That is enough
to force food companies to build real traceability data models and not quite enough to make them
interoperable with each other. *The State of Supply Chain APIs* found the food-traceability vendors
scoring above their segment on the strength of the data work, with the exchange layer still left to
each pair of trading partners.
