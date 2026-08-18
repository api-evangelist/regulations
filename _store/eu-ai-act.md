---
papers:
- title: The State of Marketing & Advertising APIs
  url: https://reports.apievangelist.com/reports/state-of-marketing-advertising-apis/
  note: Transparency where marketing content is generated or a person is profiled by an automated system.
- title: The State of Data & Analytics APIs
  url: https://reports.apievangelist.com/reports/state-of-data-analytics-apis/
  note: Training-data governance, provenance and documentation obligations landing on the data layer that
    feeds models.
- title: The OpenAPI Standard
  url: https://reports.apievangelist.com/reports/the-openapi-standard/
  note: For an API-delivered system the Act's documentation, logging and oversight duties live in the
    contract or nowhere — and 32.8% of contracts do not even carry a callable address.
- title: The State of Developer Tools APIs
  url: https://reports.apievangelist.com/reports/state-of-developer-tools-apis/
  note: Reaches the growing share of developer tools shipping agentic CI and AIOps — where a tool that
    acts on production becomes a system whose provider owes documentation, logging and human oversight.
- title: The State of Artificial Intelligence APIs
  url: https://reports.apievangelist.com/reports/state-of-artificial-intelligence-apis/
  note: The first regime to reach the AI industry, and the reason its 3.9% machine-readable consent coverage
    is a liability rather than a stylistic gap.
name: EU AI Act
kind: statute
jurisdiction: European Union
slug: eu-ai-act
title: EU Artificial Intelligence Act
description: 'The EU Artificial Intelligence Act is the world''s first comprehensive, horizontal regulation
  of artificial intelligence — a risk-tiered regime that bans some practices outright, imposes conformity
  assessment, technical documentation, logging, transparency and human-oversight duties on high-risk systems,
  and layers separate obligations on general-purpose AI models. Unlike open banking, it compels no API:
  it regulates what an AI system may do and what its provider must be able to prove, which is why its
  footprint shows up in an API catalog as consent, audit, logging and disclosure surfaces rather than
  as endpoints.'
tags:
- Artificial Intelligence
- Risk Management
- Transparency
- Conformity Assessment
- Governance
- Europe
- Regulation
common:
- type: Legislation
  url: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- type: Regulator
  url: https://digital-strategy.ec.europa.eu/en/policies/ai-office
url: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
yearCreated: 2024
alternativeNames:
- Artificial Intelligence Act
- Regulation (EU) 2024/1689
- AI Act
companyCount: 59
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---

The **EU Artificial Intelligence Act** is the first regime to regulate artificial intelligence horizontally rather than sector by sector, and it arrives at an industry that has almost nothing machine-readable to show it. It sorts AI systems by risk — prohibited practices, high-risk systems carrying the heaviest duties, limited-risk systems owing transparency, and minimal-risk systems left alone — and adds a separate track of obligations for general-purpose AI models, including the systemic-risk tier that the frontier labs sit in.

  * **Risk tiers, not licences** - Obligations attach to what a system does and to whom, so two companies shipping near-identical inference endpoints can land in different tiers based on the downstream use they enable.
  * **Documentation, logging and traceability** - High-risk providers must maintain technical documentation, keep automatic logs, and be able to reconstruct how a system behaved. That is an audit and telemetry requirement expressed in prose, and almost nobody expresses it in a contract.
  * **Transparency and disclosure duties** - Users must be told when they are interacting with an AI system, when content is synthetic, and when emotion recognition or biometric categorization is in play.
  * **Human oversight as a design requirement** - High-risk systems must be built so a person can intervene, which is the regulatory twin of the human-in-the-loop escalation an agentic API contract should declare.
  * **General-purpose model obligations** - Model providers owe technical documentation, copyright policy, and a training-content summary; systemic-risk models owe evaluation, adversarial testing, incident reporting and cybersecurity on top.

The AI Act is the clearest case in my catalog of a regime that **restricts without requiring an interface**. No article of it obliges a provider to publish an OpenAPI, a scope model, or a consent endpoint — which is exactly why the artificial-intelligence cohort scores the way it does. The duties it creates are provable duties: who acted, on whose behalf, under what disclosure, with what human able to stop it, retained in a log somebody can read back. Every one of those is a thing an API contract can carry and almost no AI provider carries it. Consent and identity surfaces appear in 3.9% of the industry; idempotency, the property that decides whether a retried autonomous action happened once or twice, appears in 2.6%. When the conformity assessments start landing, the companies that treated machine-readable governance as optional polish will be assembling their evidence by hand.

This is also why the Kin Score does not yet fold a Regulatory Posture facet into artificial intelligence the way it does for banking, health, energy or telecom: the AI Act compels no interface, so there is no mandated contract to score against. That is a finding about the regime, not an omission in the rubric — and it is the thing most likely to change as the Act's obligations phase in.
