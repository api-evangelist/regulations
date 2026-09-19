---
name: Texas Responsible AI Governance Act
kind: statute
jurisdiction: United States (Texas)
scope: horizontal
countries:
- united-states
regions:
- north-america
industries:
- artificial-intelligence
- government
- healthcare
- financial-services
- human-capital-management
slug: texas-traiga
title: Texas Responsible Artificial Intelligence Governance Act (HB 149)
description: 'TRAIGA took effect 1 January 2026 as an intent-based AI statute: rather than imposing risk-management
  duties on classes of system, it prohibits developing or deploying AI with the intent to manipulate behaviour,
  conduct social scoring, unlawfully discriminate, or uniquely identify people without consent. Its most
  consequential design choice is a safe harbour for substantial compliance with the NIST AI Risk Management
  Framework — the first US law to give a voluntary standard legal effect.'
tags:
- Artificial Intelligence
- Prohibited Practices
- NIST AI RMF
- Safe Harbor
- United States
- Regulation
common:
- type: Legislation
  url: https://capitol.texas.gov/BillLookup/History.aspx?LegSess=89R&Bill=HB149
url: https://capitol.texas.gov/BillLookup/History.aspx?LegSess=89R&Bill=HB149
yearCreated: 2025
alternativeNames:
- TRAIGA
- HB 149
- Texas HB 149
standards:
- title: ISO/IEC 42001 (AI Management System)
  url: https://standards.apievangelist.com/store/iso-42001/
  note: TRAIGA's safe harbour runs to the NIST AI RMF specifically; ISO/IEC 42001 is the certifiable sibling
    organisations pair with it.
companyCount: 1
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---

**TRAIGA** is the US answer to the EU AI Act that nobody expected to come from Texas, and it took a genuinely different route. Where the EU sorts systems by risk tier and attaches duties to the tier, TRAIGA attaches liability to **intent**. Signed 22 June 2025, in effect 1 January 2026.

  * **Prohibited purposes, not prohibited categories** - Developing or deploying an AI system with the intent to incite self-harm or crime, to manipulate behaviour in ways that circumvent informed decision-making, to conduct government social scoring, to uniquely identify individuals from biometric data without consent, or to unlawfully discriminate against a protected class.
  * **Intent is the element** - Disparate impact without intent is expressly not enough for the discrimination provision. This is the whole design, and it is what made the bill passable.
  * **A NIST AI RMF safe harbour** - An organisation substantially complying with the NIST AI Risk Management Framework gets an affirmative defence. A voluntary framework, given teeth by being the thing that protects you.
  * **Attorney-General enforcement with a cure period** - Civil penalties from $10,000 to $200,000 per violation, with notice and an opportunity to fix.
  * **A regulatory sandbox and an AI Council** - Time-limited authorisation to test systems outside the ordinary rules.

The safe harbour is the provision with the longest reach, and I do not think its significance is widely appreciated outside of compliance teams. NIST AI RMF was published as guidance — genuinely voluntary, deliberately non-prescriptive, adopted mostly by organisations that already wanted to do the work. TRAIGA converts it into the cheapest available insurance policy in the state of Texas. That changes the economics of adopting it for every company that was previously treating it as optional, and it does so without the legislature having to write a single technical requirement itself.

That mechanism — legislate the liability, point at an external standard for the defence — is one I expect to see copied, and it is the most API-relevant thing in the statute. It means the operative compliance artefact is not defined by law at all. It is defined by NIST, revised by NIST, and whatever machine-readable expression the AI governance community builds around NIST AI RMF becomes, in Texas, legally load-bearing.

For the catalog the practical question is what a provider can publish that evidences substantial compliance. Today, essentially nothing standardised: RMF conformance is an internal programme with internal documents. If there is a gap worth someone building a specification into, it is this one — a declarative, publishable profile of AI RMF conformance that a customer, a partner or an Attorney-General can retrieve rather than request. Texas just created the demand for it.
