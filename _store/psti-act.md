---
name: UK Product Security and Telecommunications Infrastructure Act
kind: statute
jurisdiction: United Kingdom
scope: sectoral
countries:
- united-kingdom
regions:
- united-kingdom-ireland
industries:
- iot
- consumer-goods
- cybersecurity
- semiconductors-hardware
- hvac-building-automation
- telecommunications
slug: psti-act
title: Product Security and Telecommunications Infrastructure Act 2022 (c. 46)
description: 'The PSTI Act and its 2023 security regime make three baseline security requirements
  legally binding on consumer connectable products sold in the UK: no universal default passwords, a
  published vulnerability disclosure policy, and a published minimum security update period. It is
  small, it is enforced, and it is the first regime anywhere to make a machine-readable security
  commitment a condition of sale — which is the model the EU Cyber Resilience Act then scaled up.'
tags:
- Product Security
- IoT
- Vulnerability Disclosure
- Security Updates
- United Kingdom
- Regulation
common:
- type: Legislation
  url: https://www.legislation.gov.uk/ukpga/2022/46
- type: Regulator
  url: https://www.gov.uk/government/collections/the-product-security-and-telecommunications-infrastructure-psti-bill-factsheets
url: https://www.legislation.gov.uk/ukpga/2022/46
yearCreated: 2022
alternativeNames:
- PSTI
- PSTI Act
- PSTI Act 2022
companyCountStatus: pending-corpus-pass
standards:
- title: security.txt  # wired by scripts/wire_standards_links.py
  url: https://standards.apievangelist.com/store/security-txt/
  note: PSTI requires a published vulnerability disclosure policy with a working contact — exactly what
    security.txt exists to publish.
---

The **PSTI Act** is the smallest regime in this catalog that I would call genuinely important, and the reason is its shape rather than its size. Three requirements, in force since April 2024 for consumer connectable products placed on the UK market:

  * **No universal default passwords** - Passwords must be unique per device or set by the user at initialisation. The single most-exploited class of consumer IoT weakness, legislated out of existence in one sentence.
  * **A published vulnerability disclosure policy** - The manufacturer must publish how to report a security issue, and must provide status updates to the reporter. A contact point, publicly stated, with an acknowledgement obligation behind it.
  * **A published minimum security update period** - The manufacturer must state, at point of sale, how long the product will receive security updates. Not promise a duration — *state* one, which can lawfully be short, but cannot lawfully be unstated.

The third is the innovation. Regulators had spent a decade trying to legislate that connected products be secure, which is unenforceable because security is not a state you can inspect for. PSTI legislates something adjacent and completely checkable: that the manufacturer has made a public, dated, falsifiable commitment about support. A regulator does not need to assess your firmware. It needs to read your website and compare it to your shipping history.

That is why I keep pointing at this Act when people ask how regulation could ever reach the parts of software that matter. The answer PSTI found is that you do not regulate the quality — you regulate the *declaration*, and you make the declaration public, structured and comparable. Once it is public, the market does work the regulator cannot.

For the catalog this maps almost exactly onto signals I already look for. A vulnerability disclosure policy is `/.well-known/security.txt` plus a documented process. A support lifetime is a lifecycle declaration with a date in it. Both are observable from outside, both are cheap to publish, and both are absent across most of the catalog. The Cyber Resilience Act takes the same two ideas and makes them apply to essentially all commercial software sold into the EU with a product-level conformity regime behind them — but PSTI got there first, on a narrower class of product, and it has the advantage of already being in force with enforcement history to look at.

If you ship a consumer connected product into the UK, the compliance artefact is a statement of compliance, and the three requirements above are the whole of it. If you ship software rather than hardware, PSTI does not reach you — but read it anyway, because it is the clearest short statement of what the next five years of product-security regulation is going to ask you to publish.
