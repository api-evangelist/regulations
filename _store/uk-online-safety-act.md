---
name: UK Online Safety Act
kind: statute
jurisdiction: United Kingdom
scope: horizontal
countries:
- united-kingdom
regions:
- united-kingdom-ireland
industries:
- technology
- media
- video-streaming
- gaming
- creator-economy
- artificial-intelligence
- communications-platform-as-a-service-cpaas
slug: uk-online-safety-act
title: Online Safety Act 2023 (c. 50)
description: 'The Online Safety Act imposes duties of care on user-to-user and search services with
  links to the UK, enforced by Ofcom with fines to 10% of global turnover and, ultimately, business
  disruption measures. Its most consequential requirement in practice is highly effective age assurance,
  which has turned an editorial obligation into an identity-infrastructure problem — and Ofcom''s
  enforcement has already reached generative-AI features rather than staying with content platforms.'
tags:
- Online Safety
- Age Assurance
- Content Moderation
- Risk Assessment
- United Kingdom
- Regulation
common:
- type: Legislation
  url: https://www.legislation.gov.uk/ukpga/2023/50
- type: Regulator
  url: https://www.ofcom.org.uk/online-safety/
url: https://www.legislation.gov.uk/ukpga/2023/50
yearCreated: 2023
alternativeNames:
- OSA
- Online Safety Act 2023
- Online Safety Bill
companyCountStatus: pending-corpus-pass
---

The **Online Safety Act** is the most aggressively enforced of the online-safety regimes I track, and the one whose scope companies most consistently underestimate. It does not apply to "social media". It applies to any *user-to-user service* or *search service* with links to the United Kingdom — and links to the UK means a significant number of UK users, or the UK as a target market, or a risk of harm to UK users. A forum inside a product qualifies. User-generated comments qualify. A multiplayer lobby qualifies.

  * **Duties of care, driven by risk assessment** - Services must assess the risk of illegal content and, where children are likely to access them, of content harmful to children — then implement proportionate measures. The assessment is the artefact; Ofcom asks for it.
  * **Highly effective age assurance** - Services carrying pornography, or content on suicide, self-harm or eating disorders, must prevent under-18 access by robust means. Self-declaration is explicitly insufficient. This is the provision that has produced the enforcement.
  * **Illegal content duties** - Proactive systems for priority illegal content, and swift takedown once aware.
  * **Transparency reporting** - Categorised services report on what they found and what they did.
  * **Penalties with teeth** - Up to £18 million or 10% of qualifying worldwide revenue, and business disruption measures that reach payment and ad providers — a route around the jurisdiction problem that has defeated content regulation before.

Enforcement is the story. By February 2026 Ofcom had opened investigations into more than ninety services and issued six fines, the most recent an £800,000 penalty against Kick Online Entertainment for failing to age-check access to pornographic content. The regulator has moved from sending letters to producing outcomes faster than almost anyone predicted.

The development worth flagging to anyone building AI products is that in January 2026 Ofcom opened formal investigations into X — over the Grok chatbot — and into an AI companion service. That is the regime reaching a class of product whose builders had no reason to think of themselves as a user-to-user service, and it is a preview of the same argument playing out in every jurisdiction on this list: when a model generates content in response to a user, and other users can see it, the content rules attach.

For the catalog this creates one of the clearest gaps between a stated posture and a provable one. Age assurance is not a policy page; it is a verification call, a stored assertion, a re-check interval and an appeal path, and a platform either has endpoints for those or it has a vendor doing it opaquely. Nothing in a provider's public contract today says which. It is a good candidate for a scored check because it is genuinely binary — either an age signal crosses an interface or it does not — and because the answer is about to matter in the UK, Australia, roughly half of US states, and Canada if the Safe Social Media Act passes.
