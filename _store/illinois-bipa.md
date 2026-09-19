---
name: Illinois Biometric Information Privacy Act
kind: statute
jurisdiction: United States (Illinois)
scope: horizontal
countries:
- united-states
regions:
- north-america
industries:
- artificial-intelligence
- cybersecurity
- human-capital-management
- retail
- technology
- healthcare
slug: illinois-bipa
title: Biometric Information Privacy Act (740 ILCS 14)
description: BIPA requires written consent before collecting a fingerprint, faceprint, voiceprint, retina
  or hand scan, mandates a published retention and destruction schedule, bans selling biometric data,
  and — uniquely — gives individuals a private right of action with statutory damages per violation. It
  is the most financially consequential technology statute in the United States, and it is a state law
  about fingerprints.
tags:
- Biometrics
- Consent
- Private Right of Action
- Retention
- United States
- Regulation
common:
- type: Legislation
  url: https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=3004
url: https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=3004
yearCreated: 2008
alternativeNames:
- BIPA
- 740 ILCS 14
- Illinois BIPA
companyCount: 1
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

**BIPA** is the answer to a question I get constantly: what is the actual regulatory risk of operating in the United States, given there is no federal privacy law? It is not a regulator. It is this statute, and the plaintiffs' bar that has been enforcing it since 2019.

  * **Informed written consent before collection** - A written release, with notice of the specific purpose and the retention period. Not a privacy policy. A release.
  * **A published retention and destruction schedule** - Destroy when the purpose is satisfied or within three years of last interaction, whichever comes first, and publish the policy.
  * **No sale, lease or profit from biometric identifiers** - Flatly.
  * **Reasonable standard of care in storage and transmission** - At least as protective as how you treat other confidential data.
  * **A private right of action with statutory damages** - $1,000 per negligent violation, $5,000 per reckless or intentional one. This is the whole story.

The Illinois Supreme Court held in *Cothron* that a violation accrues on **each** scan or transmission, not once per person, which is how a workplace fingerprint time clock becomes a nine-figure exposure. The legislature amended the statute in 2024 to limit accrual to one claim per person per method, which capped the tail risk without changing the underlying duty. Settlements in the hundreds of millions have been ordinary.

What makes BIPA structurally important rather than merely expensive is the private right of action. Every other privacy regime in this catalog depends on a regulator having capacity, appetite and jurisdiction. BIPA depends on none of those. Enforcement scales with plaintiff-side economics, which is to say it scales without limit, and it reaches companies no regulator would ever have prioritised.

The scope question that catches API providers is what counts. A faceprint derived from a photograph is covered even though the photograph is not. A voiceprint derived from a call recording is covered. Companies that process media on behalf of customers have been sued on the theory that extracting embeddings from faces or voices is collecting biometric identifiers, regardless of whether they knew whose face it was. Any pipeline that turns a face or a voice into a vector should assume it is in scope until counsel says otherwise.

For the catalog, this is the regime where the gap between stated and provable posture is widest and most expensive. Consent state, retention period, destruction event and purpose limitation are all things a record can carry and an API can expose; almost universally they live in a policy document and an internal spreadsheet. Texas and Washington have their own biometric statutes without a private right of action, and Colorado added biometric provisions — but Illinois is where the money is, and it will stay that way until Congress acts, which it has not in seventeen years of trying.
