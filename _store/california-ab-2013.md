---
name: California AI Training Data Transparency Act
kind: statute
jurisdiction: United States (California)
scope: horizontal
countries:
- united-states
regions:
- north-america
industries:
- artificial-intelligence
- technology
- developer-tools
- media
- creator-economy
slug: california-ab-2013
title: California AI Training Data Transparency Act (AB 2013)
description: 'AB 2013 requires any developer of a generative AI system made publicly available to
  Californians to publish, on its website, a documented summary of the datasets used to train it —
  sources, whether the data includes personal information or copyrighted material, how it was obtained,
  and the time period it covers. It is the broadest AI disclosure obligation in force in the United
  States and the one most likely to apply to an ordinary API provider.'
tags:
- Artificial Intelligence
- Training Data
- Transparency
- Copyright
- United States
- Regulation
common:
- type: Legislation
  url: https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2013
url: https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2013
yearCreated: 2024
alternativeNames:
- AB 2013
- California Training Data Transparency
- Generative AI Training Data Transparency Act
companyCountStatus: pending-corpus-pass
---

**AB 2013** is the US AI law that most companies in this catalog are actually subject to, and most of them do not know it. Effective 1 January 2026, it applies to a developer of a generative AI system or service made publicly available to Californians — with no frontier threshold, no compute floor, and no revenue test. If you fine-tuned a model and put it behind an endpoint that Californians can call, you are a developer under this statute.

What has to be published, on the developer's own website, for each system released or substantially modified since 1 January 2022:

  * **The sources or owners of the datasets** - Named, at the level of the dataset rather than the record.
  * **A description of how the data furthers the system's purpose** - Which forces a stated purpose.
  * **The number of data points, at least by category** - Approximate is acceptable; silent is not.
  * **Whether the datasets include personal information or aggregate consumer information** - And whether copyrighted, trademarked or patented material is in there.
  * **Whether the data was purchased or licensed, whether synthetic data was used, and the time period of collection** - Plus whether the data was cleaned or modified, and when collection began and ended.

The reason I flag this as the important one is reach. SB 53 governs a dozen labs. The EU AI Act's general-purpose model obligations govern model providers, and its training-content summary requirement is broadly parallel to this — but AB 2013 lands on anyone who ships a generative feature, including the enormous population of companies whose "AI" is somebody else's model with a fine-tune and a system prompt in front of it.

It also lands in an uncomfortable place. A great many companies genuinely cannot answer these questions about their own systems, because they built on a base model whose provenance the base-model provider has never fully disclosed. The statute does not offer an exemption for that. The practical effect is to push the disclosure obligation up the supply chain: a fine-tuner who must publish a training-data summary needs their model provider to have published one first, and will start asking.

That is the dynamic worth watching from an API perspective, because it is the same dynamic that produced SBOMs. Nobody adopted software bills of materials because they wanted an inventory. They adopted them because their customers were compelled to have one and pushed the requirement upstream. AB 2013 creates exactly that pressure for model provenance, and the artefact it implies — a structured, retrievable, versioned statement of what a model was trained on, published at a stable URL — does not yet have a standard shape. It should. It is the clearest unfilled specification gap I can point at in this whole catalog.
