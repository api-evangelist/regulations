---
papers:
- title: The State of Data & Analytics APIs
  url: https://papers.apievangelist.com/papers/state-of-data-analytics-apis/
  note: "Where a data platform is critical infrastructure for a regulated customer."
- title: The State of Developer Tools APIs
  url: https://papers.apievangelist.com/papers/state-of-developer-tools-apis/
  note: "Reaches developer-tools vendors through the supply-chain duty: a regulated customer must account for its suppliers' posture and will ask for evidence."
- title: The AsyncAPI Standard
  url: https://papers.apievangelist.com/papers/the-asyncapi-standard/
  note: "The 24-hour incident clock mandates the event and not its description; no regime anywhere requires an event surface to be machine-readable."
- title: The State of Cybersecurity APIs
  url: https://papers.apievangelist.com/papers/state-of-cybersecurity-apis/
  note: "Puts security operations on a 24-hour reporting clock, in an industry where operational transparency averages 21.8 and a quarter of companies publish nothing operational at all."
name: NIS2
kind: directive
jurisdiction: European Union
slug: nis2
title: NIS2 Directive (Network and Information Security)
description: "NIS2 is the EU's second-generation network and information security directive, widening the scope of regulated 'essential' and 'important' entities across eighteen sectors, imposing baseline risk-management measures, holding management personally accountable, and putting incident reporting on a strict clock — an early warning within 24 hours, an incident notification within 72, and a final report within a month. It regulates how organizations run security, not how they expose it, but its reporting clock is only survivable with the operational instrumentation an API contract can carry."
tags:
- Cybersecurity
- Incident Reporting
- Risk Management
- Supply Chain
- Europe
- Directive
common:
- type: Legislation
  url: https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- type: Regulator
  url: https://www.enisa.europa.eu/
url: https://eur-lex.europa.eu/eli/dir/2022/2555/oj
yearCreated: 2022
alternativeNames:
- NIS2 Directive
- Directive (EU) 2022/2555
- Network and Information Security Directive 2
jurisdiction: European Union
---

**NIS2** replaced the original NIS Directive and substantially widened who is covered — energy, transport, banking, health, digital infrastructure, ICT service management, public administration, space, postal services, waste, chemicals, food, manufacturing, digital providers and research, split into *essential* and *important* entities with different supervisory regimes.

  * **A reporting clock, not a reporting policy** - An early warning within 24 hours of becoming aware of a significant incident, a fuller notification within 72 hours, and a final report within one month.
  * **Baseline risk-management measures** - Incident handling, business continuity, supply-chain security, vulnerability handling and disclosure, cryptography, access control and asset management.
  * **Management accountability** - Governing bodies must approve and oversee the measures and can be held personally liable, which is what moved NIS2 from a security-team concern to a board one.
  * **Supply-chain security as a named duty** - Entities must account for the security posture of their direct suppliers, which is how the directive reaches vendors who are not themselves in scope.

The supply-chain clause is why NIS2 matters to a cybersecurity vendor that is not itself a regulated entity: it reaches you through your customers. An essential entity that must account for its suppliers' posture will ask for evidence, and the vendors who can answer from published artifacts — a disclosure policy, a status and incident surface, an audit trail, a scope model showing least privilege — will answer in an afternoon.

That is the gap this research measures. Across the cybersecurity cohort, operational transparency averages **21.8** and is zero for **26.8%** of companies, while a published vulnerability disclosure policy reaches **28%**. The 24-hour clock does not care whether a company is good at security. It cares whether it can see and say what happened, quickly, and that capability shows up in a catalog as artifacts or not at all.

Sits alongside the [EU Cyber Resilience Act](/store/eu-cyber-resilience-act/), which covers the product rather than the operator.
