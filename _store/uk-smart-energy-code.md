---
name: Smart Energy Code
slug: uk-smart-energy-code
title: Smart Energy Code (Smart DCC)
kind: regulator-guidance
jurisdiction: Great Britain
description: The Smart Energy Code is the multiparty contract governing Great Britain's smart-metering
  infrastructure. It binds energy suppliers, network operators and other parties to a common set of technical
  and operational rules, and licenses the Data Communications Company (DCC) as the monopoly operator carrying
  smart-meter traffic under the DUIS, GBCS, SMETS2 and SMKI specifications. It is an infrastructure mandate,
  not a consumer data right.
tags:
- Energy
- United Kingdom
- Smart Metering
- Infrastructure
- Regulation
common:
- type: Website
  url: https://smartenergycodecompany.co.uk/
- type: Operator
  url: https://www.smartdcc.co.uk/
url: https://smartenergycodecompany.co.uk/
yearCreated: 2013
alternativeNames:
- SEC
- Smart DCC
- DCC Licence
- SMETS2
- DUIS
- GBCS
- SMKI
companyCount: null
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 0
precisionGrade: unmeasurable
precisionBasis:
- 'human verdict: `sec` is the Securities and Exchange Commission throughout ("big 4 SEC clients", "applies
  gaap SEC regulations", "gdpr soc2 finra SEC guidelines"), 28% of sampled corpora. Stoplisted.'
---

**The Smart Energy Code** is the answer to a question the UK energy report keeps returning to: Britain
clearly mandated *something* in energy data, so what was it?

The SEC is a multiparty code binding suppliers, networks and service users to common rules for smart
metering, with the **Data Communications Company** licensed as the single operator of the national
communications layer. The technical specifications underneath it — **DUIS** for the user interface,
**GBCS** for the message set, **SMETS2** for the meters, **SMKI** for the key infrastructure — define an
XML web service that is genuinely machine-readable and genuinely closed.

*   **Access by party status, not by credential** - to reach smart-meter data you become a SEC party in
    the appropriate role. There is no developer signup, no API key, and no self-serve path.
*   **A monopoly by design** - the DCC is licensed to be the only operator. That is a deliberate policy
    choice about reliability and interoperability, and it is the opposite of a competitive API market.
*   **Infrastructure, not portability** - the code governs how meter traffic moves between licensed
    parties. It confers no right on a consumer to send their own data to a third party.

## What it produced, and what it did not

*The State of UK Energy APIs* found something counterintuitive: **eighteen of twenty-six UK organizations
carry a live, verified mandate — more than Australia's fourteen — and only four publish a consumer-data
API, against Australia's thirteen.**

Britain has more mandates and a fraction of the consumer APIs, because its mandates were pointed at pipes.

The consequence is a market where consented consumer data had to be built as a *business* rather than
delivered as a right. **Hildebrand** and **n3rgy** exist to obtain a customer's authorisation and broker
their smart-meter data onward, and they are why Britain leads the entire energy study on
`consent_identity` at 46% — more than double mandated Australia and fifteen times the United States.

Great Britain does have the legal machinery for a consumer energy data right. DESNZ ran a call for
evidence on an energy smart-data scheme that closed in March 2025 with no government response, and no
secondary legislation has followed under the Data (Use and Access) Act 2025. **The instrument exists and
has not been used.**

Read alongside [Ofgem's Data Best Practice Guidance](https://regulations.apievangelist.com/store/ofgem-data-best-practice/),
which is the *other* half of Britain's answer — an open-data obligation aimed at network operational data,
and the reason the DNOs out-publish every mandated market in the study. Britain did not decline to
mandate. It mandated the infrastructure and the network data, and left the customer's own data alone.
