---
name: Digital Services Act
kind: regulation
jurisdiction: European Union
scope: horizontal
countries:
- austria
- belgium
- denmark
- estonia
- finland
- france
- germany
- ireland
- italy
- netherlands
- poland
- portugal
- spain
- sweden
regions:
- europe
- dach
- france-iberia
- nordics
- benelux
- italy-southern-europe
- cee
industries:
- technology
- media
- e-commerce-platform
- video-streaming
- creator-economy
- marketing-advertising
- artificial-intelligence
slug: digital-services-act
title: Digital Services Act (Regulation (EU) 2022/2065)
description: 'The Digital Services Act governs how online intermediaries handle illegal content,
  advertising, recommendation and risk — layered by size, from every hosting provider up to the very
  large platforms that owe systemic-risk assessments and independent audit. Its API-visible footprint
  is unusual: for the largest platforms it does not merely permit a research and transparency interface,
  it obliges one, which makes it one of the few regimes in this catalog that manufactures an API rather
  than constraining one.'
tags:
- Content Moderation
- Transparency
- Platforms
- Risk Management
- Advertising
- Europe
- Regulation
common:
- type: Legislation
  url: https://eur-lex.europa.eu/eli/reg/2022/2065/oj
- type: Regulator
  url: https://digital-strategy.ec.europa.eu/en/policies/digital-services-act
url: https://eur-lex.europa.eu/eli/reg/2022/2065/oj
yearCreated: 2022
alternativeNames:
- DSA
- Regulation (EU) 2022/2065
companyCountStatus: pending-corpus-pass
---

The **Digital Services Act** is the regime most people in the API world assume does not apply to them, and the assumption is usually wrong. It is written in tiers, and the bottom tier is very wide: any *intermediary service* — mere conduit, caching, or hosting — carries baseline duties, and "hosting" in the DSA's sense reaches a great deal of infrastructure that thinks of itself as plumbing rather than as a platform. Cloud storage, a comment widget, a file-sharing endpoint, a marketplace API: all hosting. The heavy obligations sit at the top, on Very Large Online Platforms and Search Engines above 45 million EU users, but the floor is a floor for everyone.

  * **Tiered by role and size** - Intermediaries owe points of contact, terms transparency and order-response procedures; hosting adds notice-and-action and statements of reasons; platforms add complaint handling, trader traceability and ad repositories; VLOPs add systemic-risk assessment, mitigation, independent audit and a crisis mechanism.
  * **Notice and action, with reasons** - Hosting services must offer an accessible mechanism for flagging illegal content and must issue a *statement of reasons* for each restriction — and those statements are filed to the Commission's public DSA Transparency Database, which is itself an API.
  * **No dark patterns, no ads on profiling of minors** - Interface design becomes a compliance surface, and advertising systems have to be able to prove what they targeted on.
  * **Recommender transparency and an opt-out** - VLOPs must explain the main parameters of their recommender systems and offer at least one option not based on profiling. That is a product requirement expressed as a law.
  * **Article 40 data access for vetted researchers** - The largest platforms must provide researchers access to data for studying systemic risk. This is a mandated interface, and the delegated act that operationalises it settles the shape.

The DSA earns its place in this catalog for the last point especially. Nearly every regime I profile here *restricts* an interface — tells you what you may not expose, or what you must log before exposing it. Open banking is the rare regime that compels one. The DSA is the second, and it compels it for a wholly different reason: not to move a customer's money, but to let an outsider check the platform's own account of itself. The statements-of-reasons database and the Article 40 research interface are both, in the plainest sense, public APIs that exist because a law said so.

Enforcement stopped being theoretical on 5 December 2025, when the Commission issued its first non-compliance decision and fined X €120 million. Penalties reach 6% of global turnover. The pattern worth watching is that investigations have not stayed inside the obvious content cases — the same enforcement apparatus has been turned on generative-AI features bolted onto platforms, which means a company can acquire DSA exposure by shipping a chatbot into a surface that already had users.

What it asks for, a contract can carry. A notice-and-action endpoint is an API. A statement of reasons is a structured object with an enumerated ground. An ad repository is a queryable dataset. A recommender parameter disclosure is documentation with a schema under it. The companies that will struggle are the ones for whom each of these is a bespoke internal tool with a human in front of it, because the DSA's unit of compliance is not a policy page — it is a record somebody outside the company can retrieve and count.
