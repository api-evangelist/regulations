---
headers:
- name: consent-id
  basis: mandated
  observable: credentialed
  standard: berlin-group-nextgenpsd2
  note: A consent — a legal artifact with a lawful basis behind it — reduced to an identifier in a request
    header. Read alongside [[gdpr]].
- name: digest
  basis: mandated
  observable: credentialed
  standard: berlin-group-nextgenpsd2
- name: psu-id
  basis: mandated
  observable: credentialed
  standard: berlin-group-nextgenpsd2
- name: psu-ip-address
  basis: mandated
  observable: credentialed
  standard: berlin-group-nextgenpsd2
- name: signature
  basis: mandated
  observable: credentialed
  standard: http-message-signatures
  note: Berlin Group requires signed requests; the signature travels here.
- name: tpp-signature-certificate
  basis: mandated
  observable: credentialed
  standard: berlin-group-nextgenpsd2
- name: x-fapi-auth-date
  basis: mandated
  observable: credentialed
  standard: fapi
- name: x-fapi-customer-ip-address
  basis: mandated
  observable: credentialed
  standard: fapi
- name: x-fapi-customer-last-logged-time
  basis: mandated
  observable: credentialed
  standard: fapi
- name: x-fapi-interaction-id
  basis: mandated
  observable: credentialed
  standard: fapi
  note: Carried into PSD2 implementations through the FAPI security profile.
- name: deprecation
  basis: evidentiary
  observable: contract
  standard: http
  note: The RTS testing and change-notification windows have to be signalled somehow.
- name: retry-after
  basis: evidentiary
  observable: edge
  note: RTS Article 32 requires a dedicated interface to perform at least as well as the customer interface
    and not obstruct. How a provider throttles a TPP is a regulatory question, and this header is where
    it surfaces.
- name: sunset
  basis: evidentiary
  observable: edge
  standard: http
posts:
- title: Federated Convergence With Mastodon, Enterprise API Governance, and Government Regulation
  url: https://apievangelist.com/2023/01/08/federated-convergence-with-mastodon-enterprise-api-governance-and-government-regulation/
  date: 2023-01-08
- title: Looking Through a Federated Lens Across Mastodon, FHIR, and PSD2/3
  url: https://apievangelist.com/2023/01/08/looking-through-a-federated-lens-across-mastodon-fhir-and-psd23/
  date: 2023-01-08
- title: The PSD2 Sandbox From Banking API Provider bunq
  url: https://apievangelist.com/2019/10/29/the-psd2-sandbox-from-banking-api-provider-bunq/
  date: 2019-10-29
- title: US Companies Getting Ahead Of EU Regulations
  url: https://apievangelist.com/2018/03/07/us-companies-getting-ahead-of-eu-regulations/
  date: 2018-03-07
- title: A Regulatory Subway Map For PSD2
  url: https://apievangelist.com/2018/02/03/a-regulatory-subway-map-for-psd2/
  date: 2018-02-03
- title: The Role of European Banking Authority (EBA) When It Comes To PSD2
  url: https://apievangelist.com/2018/01/23/the-role-of-european-banking-authority-eba-in-regards-to-psd2/
  date: 2018-01-23
papers:
- title: The OpenID Connect Standard
  url: https://reports.apievangelist.com/reports/the-openid-connect-standard/
  note: One of the few regimes compelling FAPI-profiled OIDC; the mandated markets declare identity in
    the contract and the other 99% do not.
- title: The OAuth 2.0 Standard
  url: https://reports.apievangelist.com/reports/the-oauth-2-standard/
  note: One of the few regimes that genuinely compels OAuth and FAPI — and, characteristically, stops
    exactly at the regulatory line.
- title: The State of UK Banking APIs
  url: https://reports.apievangelist.com/reports/state-of-uk-banking-apis/
  note: The legal basis of the UK's write surfaces — payment initiation and confirmation of funds — that
    make UK banking APIs actionable, not read-only.
standards:
- title: UK Open Banking Standard
  url: https://standards.apievangelist.com/store/uk-open-banking-standard/
  note: The OBIE Read/Write specification implements PSD2's access-to-account obligation in the UK.
- title: Berlin Group NextGenPSD2
  url: https://standards.apievangelist.com/store/berlin-group-nextgenpsd2/
  note: The XS2A framework most EU banks implement to satisfy PSD2's dedicated-interface requirement.
name: PSD2
kind: directive
jurisdiction: European Union / United Kingdom
slug: psd2
title: Revised Payment Services Directive (PSD2)
description: PSD2 is the European Union directive that opened bank payment accounts to licensed third
  parties, mandating that banks provide access to accounts (XS2A) for account-information and payment-initiation
  services under strong customer authentication. It is the legal foundation of open banking across the
  EU and, as retained law, the UK — implemented technically by the OBIE standard in the UK and the Berlin
  Group NextGenPSD2 framework across the continent.
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
companyCount: 15
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 65
precisionGrade: medium
precisionBasis:
- 'acronym-shape -10: shortest bare needle is 4 characters, halved — it neither collides nor appears in
  the corpus frequency table'
- 'bare-channel -25: 100% of matching companies were reached only on the bare word (15 bare vs 0 phrase)'
---

**PSD2** — the Revised Payment Services Directive — is the European law that pried open bank payment accounts. It requires banks (account servicing payment service providers) to let licensed third parties, with the customer's consent, access account information and initiate payments, and it banned the credential-sharing screen-scraping the fintech ecosystem had quietly run on.

  * **Access to Account (XS2A)** - The core obligation: banks must expose an interface for Account Information Services (AIS) and Payment Initiation Services (PIS), so a third party can read balances and transactions and move money under consent.
  * **Payment initiation, not just data** - PSD2 gave the ecosystem something to *do*, not just something to read — the write surface that distinguishes European and UK open banking from read-only regimes.
  * **Retained in UK law** - Post-Brexit, PSD2 continues as retained UK law, which is why the UK's OBIE standard and the EU's Berlin Group framework are two implementations of one directive.

PSD2 is the regulation I hold up as the one that worked — with a caveat. Where a market paired it with conformance and a delivery body (the UK), it produced working, actionable APIs; where it was implemented as a framework each bank profiled locally (much of the continent), it multiplied into national and per-bank flavors. The law was right; the execution decided the result.
