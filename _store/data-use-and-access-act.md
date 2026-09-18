---
name: Data (Use and Access) Act 2025
kind: statute
jurisdiction: United Kingdom
scope: horizontal
countries:
- united-kingdom
regions:
- united-kingdom-ireland
industries:
- technology
- data-analytics
- artificial-intelligence
- marketing-advertising
- banking
- financial-services
- healthcare
slug: data-use-and-access-act
title: Data (Use and Access) Act 2025 (c. 18)
description: 'The DUAA amends UK GDPR, the Data Protection Act 2018 and PECR, replaces the ICO with the
  Information Commission, and creates statutory smart-data schemes that generalise the open-banking
  model to any sector a regulation names. It is the point at which UK data protection stops being a
  copy of the EU''s and starts being a different regime, which is a problem for anyone whose compliance
  model assumed the two moved together.'
tags:
- Data Protection
- Smart Data
- Automated Decisions
- Data Portability
- United Kingdom
- Regulation
common:
- type: Legislation
  url: https://www.legislation.gov.uk/ukpga/2025/18
- type: Regulator
  url: https://ico.org.uk/
url: https://www.legislation.gov.uk/ukpga/2025/18
yearCreated: 2025
alternativeNames:
- DUAA
- DUAA 2025
- Data Use and Access Act
companyCountStatus: pending-corpus-pass
---

The **Data (Use and Access) Act 2025** is the UK's answer to a question it had been avoiding since Brexit: whether to keep UK GDPR as a near-identical twin of the European regime, or to diverge and accept the cost. It diverged — carefully, in places that matter operationally more than they matter rhetorically.

  * **Recognised legitimate interests** - A defined list of purposes that need no balancing test, which changes the shape of the lawful-basis analysis rather than its outcome.
  * **Automated decision-making loosened** - The Article 22 prohibition narrows to decisions involving special category data, with safeguards rather than a general bar elsewhere. This is the single largest practical divergence from the EU, and it lands precisely where AI deployment sits.
  * **Research provisions widened** - A broader consent model for scientific research, including commercial research.
  * **The ICO becomes the Information Commission** - A board-governed body rather than a corporation sole.
  * **Smart data schemes** - The part almost nobody outside financial services has read.

That last one is why this entry is in an API catalog rather than only in a privacy briefing. The Act creates a **statutory power to establish smart-data schemes** in any sector a regulation designates: a duty on data holders to release customer and business data to authorised third parties at the customer's request, with an accreditation regime and an interface obligation. It is the open-banking pattern, generalised, with the legislation written once and the sector chosen later.

I have spent years arguing that the CMA Open Banking Order was the most consequential API regulation ever made in the UK, and that its real significance was never banking — it was the demonstration that a regulator could compel a working, documented, conformance-tested interface across an entire industry and have it actually ship. The DUAA is the machinery for doing that again without new primary legislation. Energy and telecoms are the obvious first candidates.

The divergence problem is real for anyone operating on both sides. A company serving UK and EU users now has two data-protection regimes that share a vocabulary and disagree on substance, and the disagreement is worst exactly where automated decisions are made — which is to say, in the products everyone is currently building. The comfortable answer, comply with the stricter of the two, works until a UK smart-data scheme obliges a disclosure the EU analysis would have declined to make.

There is also a quiet amendment worth knowing about: section 124 touches the Online Safety Act's information-retention provisions, and other DUAA provisions add requirements for services likely to be accessed by children. The two Acts are being read together by Ofcom and the ICO, which means a children's-data question can arrive from either regulator.
