---
papers:
- title: The State of UK Banking APIs
  url: https://papers.apievangelist.com/papers/state-of-uk-banking-apis/
  note: "The certificate/identity trust framework behind third-party onboarding across the OBIE and Berlin Group ecosystems."
standards:
- title: Dynamic Client Registration
  url: https://contracts.apievangelist.com/store/dynamic-client-registration/
  note: "Open-banking DCR requests carry eIDAS software statements/certificates to bind a registration to an accredited identity."
- title: Mutual TLS
  url: https://contracts.apievangelist.com/store/mtls/
  note: "eIDAS QWAC certificates are what mutual-TLS presents to prove which licensed third party is connecting."
name: eIDAS
slug: eidas
title: eIDAS Regulation (Electronic Identification and Trust Services)
description: "eIDAS is the EU regulation governing electronic identification and trust services — including the qualified website (QWAC) and seal (QSEAL) certificates that identify regulated third parties in open banking. It provides the pan-European identity and certificate framework that PSD2's access-to-account model relies on, so a bank can cryptographically verify which licensed provider is calling its APIs."
tags:
- Identity
- Security
- Trust Services
- Certificates
- Europe
- Regulation
common:
- type: Legislation
  url: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32014R0910
- type: Regulator
  url: https://digital-strategy.ec.europa.eu/en/policies/eidas-regulation
url: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32014R0910
yearCreated: 2014
alternativeNames:
- eIDAS
- Regulation (EU) 910/2014
- QWAC
- QSEAL
- eIDAS 2.0
jurisdiction: European Union
---

**eIDAS** — the EU's Electronic Identification, Authentication and Trust Services regulation — is the identity layer that European open banking quietly runs on. When a third party calls a bank's PSD2 API, the bank has to know *which* licensed provider is on the other end; eIDAS provides the qualified certificates (QWAC for the transport, QSEAL for the seals) that answer that question cryptographically.

  * **Qualified certificates** - eIDAS defines the trust services that issue the website-authentication and electronic-seal certificates open-banking providers present.
  * **The identity behind the auth stack** - Where FAPI and mTLS are the *mechanism*, eIDAS certificates are the *identity* they carry — the difference between an anonymous TLS client and an accredited AISP or PISP.
  * **Being modernized (eIDAS 2.0)** - The regulation is evolving toward EU Digital Identity Wallets, extending the same trust model to individuals.

eIDAS is a good reminder that open banking is as much an identity problem as an API problem. A machine-readable contract and a bank-grade auth handshake mean little if you cannot prove who is calling; eIDAS is the regulation that makes third-party identity a verifiable fact rather than a claim, and it is the trust anchor the European standards in my catalog lean on.
