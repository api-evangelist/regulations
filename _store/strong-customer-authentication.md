---
papers:
- title: The State of UK Banking APIs
  url: https://papers.apievangelist.com/papers/state-of-uk-banking-apis/
  note: "The regulatory requirement behind the FAPI/OIDC/mTLS stack every UK bank documents — bank-grade auth as the mandated floor."
standards:
- title: FAPI
  url: https://contracts.apievangelist.com/store/fapi/
  note: "The financial-grade API security profile that operationalizes SCA in open-banking APIs."
- title: UK Open Banking Standard
  url: https://contracts.apievangelist.com/store/uk-open-banking-standard/
  note: "The OBIE standard mandates SCA-compliant auth across its Read/Write APIs."
name: Strong Customer Authentication
slug: strong-customer-authentication
title: Strong Customer Authentication (SCA)
description: Strong Customer Authentication (SCA) is the security requirement mandated by PSD2's Regulatory Technical Standards, requiring multi-factor authentication (two of knowledge, possession, and inherence) for electronic payments and account access in the EU and UK. It is the regulatory backbone of the FAPI-grade security stack that open-banking APIs implement, and the reason bank-grade auth is the floor in European open finance rather than a premium tier.
tags:
- Finance
- Open Banking
- Security
- Authentication
- Consent
- Europe
- United Kingdom
- Regulation
common:
- type: Regulation
  url: https://www.eba.europa.eu/regulation-and-policy/payment-services-and-electronic-money/regulatory-technical-standards-on-strong-customer-authentication-and-secure-communication-under-psd2
- type: Regulator
  url: https://www.eba.europa.eu/
url: https://www.eba.europa.eu/regulation-and-policy/payment-services-and-electronic-money/regulatory-technical-standards-on-strong-customer-authentication-and-secure-communication-under-psd2
yearCreated: 2019
alternativeNames:
- SCA
- PSD2 RTS
- RTS on SCA and CSC
jurisdiction: European Union / United Kingdom
---

**Strong Customer Authentication (SCA)** is the security requirement that sits under European open banking's reputation for rigor. Mandated by PSD2's Regulatory Technical Standards, it requires multi-factor authentication — two independent factors drawn from knowledge, possession, and inherence — for electronic payments and account access, with tightly scoped exemptions.

  * **Two factors, independent** - Something you know, something you have, something you are — at least two, engineered so that compromising one does not compromise the others.
  * **The reason bank-grade auth is the floor** - SCA is why FAPI, OAuth2/OIDC, mutual-TLS, and dynamic client registration show up as the *baseline* across open-banking APIs, not as a premium option.
  * **A regulation implemented by standards** - SCA is the legal requirement; FAPI and the OBIE security profile are how it is met in machine-readable practice.

SCA is the clearest case in banking of a regulation producing genuine technical rigor. When I score a European or UK bank and find the full FAPI stack — PAR, `private_key_jwt`, mTLS-bound tokens — that is SCA having forced bank-grade security as the floor. It is the one place the mandate reliably reached past existence to real quality.
