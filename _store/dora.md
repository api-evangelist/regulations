---
headers:
- name: access-control-allow-origin
  basis: evidentiary
  observable: edge
papers:
- title: The State of Blockchain & Crypto APIs
  url: https://papers.apievangelist.com/papers/state-of-blockchain-crypto-apis/
  note: "A MiCA-authorised crypto-asset service provider is a financial entity under DORA, in a market scoring 11.1 on governance and 17.9 on operational transparency."
- title: The State of Data & Analytics APIs
  url: https://papers.apievangelist.com/papers/state-of-data-analytics-apis/
  note: "Where a data platform is critical infrastructure for a regulated financial customer."
- title: The State of Cybersecurity APIs
  url: https://papers.apievangelist.com/papers/state-of-cybersecurity-apis/
  note: "The regime that reaches security vendors who are not themselves regulated — a designated critical ICT third-party provider is supervised directly, in a market where operational transparency averages 21.8."
- title: The State of Developer Tools APIs
  url: https://papers.apievangelist.com/papers/state-of-developer-tools-apis/
  note: "The clearest instance of inherited exposure: a CI/CD or observability vendor is not regulated as one, but is inside its EU financial customers' DORA perimeter — and can be designated and supervised in its own right."
name: DORA
kind: regulation
jurisdiction: European Union
slug: dora
title: Digital Operational Resilience Act (DORA)
description: "DORA is the EU regulation governing information and communication technology risk across the financial sector — banks, insurers, investment firms, payment institutions, crypto-asset providers and market infrastructure. It sets requirements for ICT risk management, incident classification and reporting, digital operational resilience testing, and the management of ICT third-party risk. Uniquely among the regimes in this catalog, it can designate a technology vendor a critical ICT third-party provider and supervise it directly, which is how it reaches companies that are not financial entities at all."
tags:
- Operational Resilience
- ICT Risk
- Financial Services
- Third-Party Risk
- Incident Reporting
- Europe
- Regulation
common:
- type: Legislation
  url: https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- type: Regulator
  url: https://www.esma.europa.eu/
url: https://eur-lex.europa.eu/eli/reg/2022/2554/oj
yearCreated: 2022
alternativeNames:
- Digital Operational Resilience Act
- Regulation (EU) 2022/2554
jurisdiction: European Union
---

**DORA** answers a question the financial regulators had been circling for a decade: what happens when the systems a bank depends on are not the bank's. It applies ICT risk requirements across the EU financial sector and then, unusually, reaches past that sector into the technology supply chain.

  * **ICT risk management as a governed function** - Identification, protection, detection, response and recovery, owned and evidenced by the management body rather than delegated to a vendor.
  * **Incident classification and reporting** - Major ICT-related incidents are classified against common criteria and reported to the competent authority on a defined clock.
  * **Digital operational resilience testing** - Regular testing, with threat-led penetration testing for the most significant entities.
  * **ICT third-party risk, with contractual minimums** - Register of information on all ICT arrangements, mandatory contractual provisions, exit strategies, and audit and access rights.
  * **Critical ICT third-party provider designation** - The lever that matters here. A technology vendor whose failure would threaten financial stability can be **designated and supervised directly by the European Supervisory Authorities** — not through its customers, but as an entity in its own right.

That last clause is why DORA belongs in a catalog about APIs rather than only in one about banking. Across this research the recurring finding for developer tools and cybersecurity is **inherited exposure**: those markets carry no regime of their own, and their regulatory surface is the union of their customers'. DORA is the sharpest instance, because it does not stop at inheritance. A cloud platform, an observability vendor, an identity provider or a CI/CD service that becomes load-bearing for EU financial entities can be pulled directly into supervision.

Like the [EU Cyber Resilience Act](/store/eu-cyber-resilience-act/) and the [EU AI Act](/store/eu-ai-act/), DORA **compels no interface**. It compels provable process — a register you can produce, an incident you can classify and report on a clock, an exit you can demonstrate, a test you can evidence. Every one of those is cheaper to satisfy from published, machine-readable artifacts than to reconstruct from screenshots, which is why *The State of Developer Tools APIs* found operational transparency zero for 14.0% of that market and *The State of Cybersecurity APIs* found it averaging 21.8 with a quarter of companies at zero. The clock does not care how good your security is. It cares whether you can see and say what happened.
