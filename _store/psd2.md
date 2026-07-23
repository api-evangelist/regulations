---
papers:
- title: The State of UK Banking APIs
  url: https://papers.apievangelist.com/papers/state-of-uk-banking-apis/
  note: "The legal basis of the UK's write surfaces — payment initiation and confirmation of funds — that make UK banking APIs actionable, not read-only."
standards:
- title: UK Open Banking Standard
  url: https://contracts.apievangelist.com/store/uk-open-banking-standard/
  note: "The OBIE Read/Write specification implements PSD2's access-to-account obligation in the UK."
- title: Berlin Group NextGenPSD2
  url: https://contracts.apievangelist.com/store/berlin-group-nextgenpsd2/
  note: "The XS2A framework most EU banks implement to satisfy PSD2's dedicated-interface requirement."
name: PSD2
slug: psd2
title: Revised Payment Services Directive (PSD2)
description: PSD2 is the European Union directive that opened bank payment accounts to licensed third parties, mandating that banks provide access to accounts (XS2A) for account-information and payment-initiation services under strong customer authentication. It is the legal foundation of open banking across the EU and, as retained law, the UK — implemented technically by the OBIE standard in the UK and the Berlin Group NextGenPSD2 framework across the continent.
tags:
- Finance
- Open Banking
- Payments
- Consent
- Europe
- United Kingdom
- Regulation
common:
- type: Legislation
  url: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32015L2366
- type: Regulator
  url: https://www.eba.europa.eu/
url: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32015L2366
yearCreated: 2015
alternativeNames:
- Revised Payment Services Directive
- Directive (EU) 2015/2366
- PSD2 (EU/UK)
jurisdiction: European Union / United Kingdom
---

**PSD2** — the Revised Payment Services Directive — is the European law that pried open bank payment accounts. It requires banks (account servicing payment service providers) to let licensed third parties, with the customer's consent, access account information and initiate payments, and it banned the credential-sharing screen-scraping the fintech ecosystem had quietly run on.

  * **Access to Account (XS2A)** - The core obligation: banks must expose an interface for Account Information Services (AIS) and Payment Initiation Services (PIS), so a third party can read balances and transactions and move money under consent.
  * **Payment initiation, not just data** - PSD2 gave the ecosystem something to *do*, not just something to read — the write surface that distinguishes European and UK open banking from read-only regimes.
  * **Retained in UK law** - Post-Brexit, PSD2 continues as retained UK law, which is why the UK's OBIE standard and the EU's Berlin Group framework are two implementations of one directive.

PSD2 is the regulation I hold up as the one that worked — with a caveat. Where a market paired it with conformance and a delivery body (the UK), it produced working, actionable APIs; where it was implemented as a framework each bank profiled locally (much of the continent), it multiplied into national and per-bank flavors. The law was right; the execution decided the result.
