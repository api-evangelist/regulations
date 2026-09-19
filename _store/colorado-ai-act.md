---
name: Colorado AI Act
kind: statute
jurisdiction: United States (Colorado)
scope: horizontal
countries:
- united-states
regions:
- north-america
industries:
- artificial-intelligence
- human-capital-management
- banking
- insurance
- healthcare
- education
- real-estate
slug: colorado-ai-act
title: Colorado AI Act (SB 24-205, repealed and replaced by SB 189)
description: 'Colorado passed the first US comprehensive algorithmic-discrimination law, delayed it twice,
  then repealed and replaced it with a narrower automated-decision statute arriving 1 January 2027 — with
  the deployer risk-management and impact-assessment duties removed. It is the most instructive entry
  in this catalog''s AI section precisely because it failed: it is the clearest available evidence of
  which AI obligations survive contact with a legislature and which do not.'
tags:
- Artificial Intelligence
- Algorithmic Discrimination
- Automated Decisions
- Impact Assessment
- United States
- Regulation
common:
- type: Legislation
  url: https://leg.colorado.gov/bills/sb24-205
url: https://leg.colorado.gov/bills/sb24-205
yearCreated: 2024
alternativeNames:
- SB 24-205
- Colorado Artificial Intelligence Act
- CAIA
- SB 189
companyCount: 32
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 67
precisionGrade: medium
precisionBasis:
- 'acronym-shape -10: shortest bare needle is 4 characters, halved — it neither collides nor appears in
  the corpus frequency table'
- 'bare-channel -23: 97% of matching companies were reached only on the bare word (32 bare vs 1 phrase)'
---

The **Colorado AI Act** was, when it passed in May 2024, the most ambitious AI statute in the United States and the closest anything in America had come to the EU AI Act's structure. It is now the most useful cautionary tale in this catalog, and I would rather carry the entry with its failure recorded than quietly drop it.

What it originally required, for "consequential decisions" in employment, lending, housing, education, healthcare, insurance and legal services:

  * **A duty of reasonable care against algorithmic discrimination** - On both developers and deployers, which was the structural innovation.
  * **Developer disclosures to deployers** - Known limitations, training-data summaries, evaluation results, intended uses. A documentation handoff, legally required, along a commercial supply chain.
  * **Deployer risk management and impact assessments** - Annual reviews, aligned to a recognised framework such as NIST AI RMF.
  * **Consumer notice and a right to appeal** - Told that an AI system was involved, and able to ask for human review.
  * **Attorney-General enforcement** - No private right of action.

Then it was delayed to 30 June 2026, delayed again to 1 January 2027, and in the same breath rewritten. SB 189 stripped out the deployer risk-management and impact-assessment duties — the compliance machinery — and left a narrower automated-decision law.

The lesson is in *which half* survived. Disclosure obligations survived. Notice-to-the-consumer survived. What did not survive was the continuing internal-process obligation: the annual assessment, the documented risk programme, the thing that costs money every year rather than once. That is the same split visible in the EU, where the Digital Omnibus deferred high-risk conformity assessment by sixteen months while leaving the Article 50 transparency duties untouched on their original date.

Two conclusions follow, and I hold both. First, **transparency obligations are the durable ones** — they are cheap to comply with, easy to enforce, and hard to argue against in public — so a company deciding where to invest ahead of certainty should invest in being able to say what a system is, what it was trained on, and when a human can intervene. Second, the durable obligations are exactly the ones an API contract can carry. A model card is a document. A training-data summary is a document. An appeal path is an endpoint. An "AI was involved in this decision" disclosure is a response field.

The part that was removed is also the part that was never going to be machine-readable, which is why its removal changes less about what I can score than the headlines suggest. Colorado did not stop requiring AI accountability. It stopped requiring the paperwork and kept requiring the disclosure — and disclosure is the half that shows up in a contract.
