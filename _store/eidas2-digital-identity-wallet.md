---
name: eIDAS 2 / EU Digital Identity Wallet
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
- cybersecurity
- government
- banking
- financial-services
- technology
- legal-compliance
slug: eidas2-digital-identity-wallet
title: eIDAS 2 — European Digital Identity Framework (Regulation (EU) 2024/1183)
description: 'eIDAS 2 amends the original eIDAS Regulation to create the European Digital Identity Wallet
  — a member-state-issued wallet every EU citizen and resident must be offered, and which large online
  platforms and regulated sectors must accept for authentication. Unlike most of this catalog it does
  not restrict an interface or merely require one: it specifies a protocol stack, which makes it the most
  concretely machine-readable obligation in EU law.'
tags:
- Identity
- Authentication
- Verifiable Credentials
- Trust Services
- Europe
- Regulation
common:
- type: Legislation
  url: https://eur-lex.europa.eu/eli/reg/2024/1183/oj
- type: Regulator
  url: https://digital-strategy.ec.europa.eu/en/policies/eudi-wallet
url: https://eur-lex.europa.eu/eli/reg/2024/1183/oj
yearCreated: 2024
alternativeNames:
- eIDAS 2
- eIDAS 2.0
- EUDI Wallet
- European Digital Identity Wallet
- Regulation (EU) 2024/1183
companyCount: 5
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 90
precisionGrade: high
precisionBasis:
- 'acronym-shape -10: shortest bare needle is 4 characters, halved — it neither collides nor appears in
  the corpus frequency table'
---

**eIDAS 2** is the regulation that turns European digital identity from a patchwork of national schemes into a wallet with a specification behind it. The original eIDAS created trust services and mutual recognition of national eIDs; the amendment creates the **European Digital Identity Wallet**, obliges every member state to offer one, and — the part that reaches companies who have never thought about trust services — obliges a defined set of relying parties to *accept* it.

  * **Member states must offer a wallet** - The obligation runs to the state, with the operative deadline landing at the end of 2026. Several are already piloting.
  * **Large platforms must accept it** - Very Large Online Platforms under the DSA must accept the wallet for authentication where they ask users to authenticate. So do regulated sectors — banking, telecoms, transport, health, education — wherever strong user authentication is required by law.
  * **Selective disclosure is the design premise** - A user proves they are over 18 without disclosing a birth date, or proves residency without disclosing an address. The credential format carries the attribute; the holder chooses what to release.
  * **Qualified Electronic Attestation of Attributes** - The wallet carries not just identity but attested claims from qualified providers, which is the mechanism that makes it useful commercially rather than only civically.
  * **A specified stack, not a stated outcome** - Implementing acts and the Architecture and Reference Framework pin down the protocols and credential formats. This is the unusual part.

That last point is why this entry matters more than its current visibility suggests. Almost every regime in this catalog tells a company what must be true and leaves the interface to them — which is precisely why so little of compliance is machine-readable, and why the Kin Score finds so little to score. eIDAS 2 tells them what protocol to speak. It is the closest thing EU law has produced to a mandated API contract outside of open banking, and unlike open banking it is horizontal: the wallet is the same wallet at a bank, a telco, a university and a marketplace.

The practical convergence worth naming is with age assurance. Three of the five jurisdictions I track now require platforms to establish that a user is over a threshold, and every one of them has run into the same objection — that verifying age means collecting identity documents, which creates a data-protection liability out of a child-safety duty. Selective disclosure is the standing answer to that objection, and eIDAS 2 is the only place it exists as deployed infrastructure with a legal mandate behind it rather than as a whitepaper.

For an API provider the question is narrow and answerable: when a relying party presents a wallet credential, is there an endpoint that can verify and consume it, and is the attribute model documented well enough that an integrator can tell which claims are accepted? Today almost nobody publishes that. It is a good early candidate for a scored check, because unlike most regulatory posture it is observable from outside.
