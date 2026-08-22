---
name: BSA / AML
kind: regulation
jurisdiction: United States
slug: bsa-aml
title: Bank Secrecy Act and US AML obligations
description: The Bank Secrecy Act and the anti-money-laundering rules built on it require US financial
  institutions — including money services businesses, which is how they reach crypto firms — to identify
  their customers, monitor for suspicious activity, keep records and file reports with FinCEN. It is the
  regime that turns identity verification and transaction monitoring from a product decision into a legal
  obligation.
tags:
- Anti-Money Laundering
- Financial Crime
- KYC
- United States
- Regulation
common:
- type: Regulator
  url: https://www.fincen.gov/
- type: Legislation
  url: https://www.fincen.gov/resources/statutes-and-regulations/bank-secrecy-act
url: https://www.fincen.gov/resources/statutes-and-regulations/bank-secrecy-act
yearCreated: 1970
alternativeNames:
- Bank Secrecy Act
- BSA
- AML
- FinCEN rules
- Anti-Money Laundering
companyCount: 148
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 80
precisionGrade: high
precisionBasis:
- 'human verdict: Sampled 150 corpora and confirmed REAL on both needles: "ensuring that the firm is in
  compliance with applicable kyc cdd and AML rules and regulations", "compliance BSA aml fair lending
  cecl". `AML` was revoked from Azure Machine Learning rather than stoplisted, so this record keeps it
  — see _data/alias-overrides.yml.'
---

**BSA and the AML rules** are why a crypto exchange asks for a passport. Registering as a money services business brings customer identification, sanctions screening, transaction monitoring, recordkeeping and suspicious activity reporting — a set of obligations that generate enormous volumes of machine-processed data and almost no published interfaces.

  * **Customer identification** - Know-your-customer programmes as a legal minimum rather than a risk preference.
  * **Sanctions screening** - OFAC list checking on parties and, in this market, on wallet addresses.
  * **Transaction monitoring and SARs** - Suspicious activity detection and reporting, on timelines that reward automation.
  * **Recordkeeping** - Retention obligations that shape what a platform must be able to reconstruct.
  * **Reaches non-banks** - The money services business definition is what pulls exchanges, custodians and payment firms into scope.

In *The State of Blockchain & Crypto APIs* this regime explains a segment: compliance, identity and risk vendors exist because these obligations do, and the market's institutional tier — custody, stablecoins, regulated payments — publishes idempotency and error semantics at the highest rates in the cohort, because it answers to supervisors who ask what happened and when. The same tier publishes scopes at a fraction of that rate, which is the report's open question rather than its conclusion.
