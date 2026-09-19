---
name: California Transparency in Frontier AI Act
kind: statute
jurisdiction: United States (California)
scope: sectoral
countries:
- united-states
regions:
- north-america
industries:
- artificial-intelligence
- cloud-data-platform
- technology
slug: california-sb-53
title: Transparency in Frontier Artificial Intelligence Act (SB 53)
description: SB 53 is the first US law requiring public, standardised safety disclosures from developers
  of frontier AI models — those trained above 10^26 FLOPs. Large frontier developers must publish a frontier
  AI framework, publish transparency reports on model release, and report critical safety incidents to
  California's Office of Emergency Services, with penalties to $1 million per violation. It reaches perhaps
  a dozen companies and sets the template everyone else will be measured against.
tags:
- Artificial Intelligence
- Frontier Models
- Safety Disclosure
- Incident Reporting
- United States
- Regulation
common:
- type: Legislation
  url: https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB53
url: https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB53
yearCreated: 2025
alternativeNames:
- SB 53
- TFAIA
- Transparency in Frontier Artificial Intelligence Act
standards:
- title: ISO/IEC 42001 (AI Management System)
  url: https://standards.apievangelist.com/store/iso-42001/
  note: SB 53 requires a published frontier AI framework describing how national and international standards
    are incorporated — which is the question 42001 answers.
companyCount: 1
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 95
precisionGrade: high
precisionBasis:
- 'acronym-shape -5: shortest bare needle is 5 characters, halved — it neither collides nor appears in
  the corpus frequency table'
---

**SB 53** is narrow by design and important anyway. Signed 25 September 2025, operative from 1 January 2026, it applies to *frontier developers* — those training foundation models above 10^26 integer or floating-point operations, counting subsequent fine-tuning and material modification — with the heaviest duties reserved for "large frontier developers" above a revenue threshold. That is a population you can count on your fingers.

  * **Publish a frontier AI framework** - How the developer identifies, assesses and mitigates catastrophic risk, how it incorporates national and international standards, and how it governs the decision to deploy.
  * **Publish a transparency report at release** - Model characteristics, intended uses, restrictions, and the catastrophic-risk assessment performed.
  * **Report critical safety incidents** - To the California Office of Emergency Services, on a defined clock.
  * **Whistleblower protections** - For employees raising catastrophic-risk concerns, which is the provision that will produce the first real test of the statute.
  * **Civil penalties to $1 million per violation** - Enforced by the Attorney General.

I want to separate two things that get conflated. As a *regulation of catastrophic risk*, SB 53 is modest — it compels disclosure of a framework, not the adequacy of one, and a developer who publishes a thin framework and follows it has complied. As a *standardisation event*, it is significant, because it is the first time anyone has legally required these documents to exist in public, in a comparable form, on a schedule tied to release.

That comparability is the thing I care about. Frontier labs have published model cards and system cards voluntarily for years, and the result has been a genre with no shared schema, no required fields, no release-time guarantee, and no way to diff one against the next. Once a document is legally required at release, it acquires a version history, and a version history is what makes a claim checkable. The first time a transparency report contradicts the previous one, somebody will notice, and they will only notice because both exist.

The companion statute matters more for everyone else. **AB 2013**, effective the same day, requires *any* developer of a generative AI system made available to Californians to publish a summary of the data used to train it. That is not a frontier obligation — it is the broadest AI disclosure requirement currently in force in the United States, and it catches small companies and fine-tuners that SB 53 never touches. If you are trying to work out which single US AI provision is most likely to apply to you, it is AB 2013, not this one.

For the catalog, both point the same direction: the durable, survivable AI obligations are disclosure obligations, and disclosure obligations are the ones an API provider can actually satisfy in a machine-readable way if anyone builds the schema.
