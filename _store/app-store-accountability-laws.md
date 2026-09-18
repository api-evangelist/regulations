---
name: App Store Accountability Laws
kind: statute
jurisdiction: United States (state)
scope: horizontal
countries:
- united-states
regions:
- north-america
industries:
- technology
- gaming
- creator-economy
- e-commerce-platform
- media
slug: app-store-accountability-laws
title: US App Store Accountability Acts (Utah, Texas, Louisiana, California)
description: 'App Store Accountability laws move age verification from individual apps to the app
  stores, requiring Apple and Google to determine a user''s age category, obtain verifiable parental
  consent for minors, and pass an age signal to developers — who must then act on it. It is the first
  time US law has mandated a specific piece of data cross an API boundary between a platform and its
  developers, which makes it the most directly API-relevant age regime anywhere.'
tags:
- Age Verification
- App Stores
- Parental Consent
- Platform Obligations
- United States
- Regulation
common:
- type: Legislation
  url: https://le.utah.gov/~2025/bills/static/SB0142.html
url: https://le.utah.gov/~2025/bills/static/SB0142.html
yearCreated: 2025
alternativeNames:
- App Store Accountability Act
- Utah SB 142
- Texas SB 2420
- App store age verification
companyCountStatus: pending-corpus-pass
---

The **App Store Accountability laws** are the most interesting regulatory development in this catalog for anyone who builds software rather than writes policy, because they are the first US statutes that mandate an **API contract between two private parties**.

Utah went first in March 2025, Texas and Louisiana followed, California enacted its own variant, and more states are queued. The mechanism is consistent:

  * **The app store determines an age category** - Not the app. The store, which already has a payment instrument and an account relationship, does the verification.
  * **Verifiable parental consent for minors** - Obtained by the store at account setup and at each download or in-app purchase.
  * **An age signal is passed to the developer** - The store must make the user's age category available to developers through its APIs.
  * **Developers must use it** - Apply age-appropriate treatment, and re-request consent on significant changes to terms.
  * **Enforcement by Attorney General, with private rights of action in some versions** - And meaningful per-violation penalties.

The industry politics are unusually legible here. Meta, Snap and others lobbied hard *for* these laws; Apple and Google lobbied hard *against*. That is not a disagreement about child safety. It is a disagreement about where a costly, privacy-sensitive obligation should sit in the stack, and the app stores lost.

Whatever you think of the outcome, the architecture is the right one. Verifying age once, at the layer that already holds a verified payment relationship, and distributing a minimal derived signal to everyone downstream is strictly better than every app in the world independently collecting identity documents. It is the selective-disclosure pattern, implemented by commercial fiat rather than by a credential standard — the age category crosses the boundary and the birth date does not.

For developers this creates a concrete and near-term integration task, and it is worth being precise about the shape. The signal is a **category**, not a date. It arrives through platform SDKs. It can change. It is a claim by the store, not a verified fact the developer can independently confirm, which means the developer's liability position depends on a representation from a third party they cannot audit — a familiar problem with an unfamiliar counterparty.

And it creates a question this catalog should be able to answer and currently cannot: which providers consume an age signal, what do they do differently when it says minor, and is any of that in their documentation? Age-gating is about to become a routine property of a consumer-facing API, the way rate limiting and authentication are, and right now there is no vocabulary for describing it.
