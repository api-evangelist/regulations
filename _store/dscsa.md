---
papers:
- title: The State of Supply Chain APIs
  url: https://papers.apievangelist.com/papers/state-of-supply-chain-apis/
  note: "The closest any supply chain regime comes to compelling machine-to-machine exchange — and the segment built for it outscores the segments around it."
standards:
- title: EPCIS
  url: https://standards.apievangelist.com/store/epcis/
  note: "The format the pharmaceutical industry converged on to satisfy the interoperable electronic tracing requirement."
name: Drug Supply Chain Security Act
kind: statute
jurisdiction: United States
slug: dscsa
title: Drug Supply Chain Security Act (DSCSA)
description: Title II of the US Drug Quality and Security Act, requiring an interoperable, electronic, package-level traceability system for prescription drugs across manufacturers, repackagers, wholesale distributors and dispensers, including serialization, verification and the electronic exchange of transaction information.
tags:
- Supply Chain
- Healthcare
- Pharmaceuticals
- Traceability
- Serialization
- United States
- Regulation
common:
- type: Website
  url: https://www.fda.gov/drugs/drug-supply-chain-integrity/drug-supply-chain-security-act-dscsa
url: https://www.fda.gov/drugs/drug-supply-chain-integrity/drug-supply-chain-security-act-dscsa
yearCreated: 2013
alternativeNames:
- DSCSA
- Drug Quality and Security Act Title II
---

The **Drug Supply Chain Security Act** phased in over a decade toward a single end state: unit-level
electronic traceability of prescription drugs through the US supply chain, with trading partners
passing transaction information to one another electronically and interoperably.

  * **Serialization** - Every saleable unit carries a unique product identifier.
  * **Electronic, interoperable exchange** - Transaction information moves between trading partners as data, not as paper or PDF.
  * **Verification** - Trading partners can verify a product identifier with the manufacturer.
  * **Converged on [EPCIS](https://standards.apievangelist.com/store/epcis/)** - The industry settled on a GS1 event standard as the interchange format rather than each pair of partners inventing one.

DSCSA is the exception that proves the rule for this sector. Almost every supply chain regulation in
this catalog compels a *record* or a *report* and leaves the exchange to the market, which reliably
produces reporting software and no contracts. DSCSA compelled the **exchange itself** — partner to
partner, electronically, interoperably — and the industry responded by converging on a shared event
format and building the platforms to move it. *The State of Supply Chain APIs* found the traceability
vendors built for this obligation among the strongest in their segment, which is the measurable
difference between naming a report and naming an interface.
