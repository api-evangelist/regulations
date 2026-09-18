---
name: US State and Local Employment AI Laws
kind: statute
jurisdiction: United States (state and municipal)
scope: sectoral
countries:
- united-states
regions:
- north-america
industries:
- human-capital-management
- artificial-intelligence
- professional-services
- enterprise-software
slug: us-state-employment-ai-laws
title: US Employment AI Laws (Illinois HB 3773, NYC Local Law 144, Maryland, Utah)
description: 'Employment is where US AI regulation actually bit first. Illinois HB 3773 amends the
  Human Rights Act to reach AI in employment decisions; New York City Local Law 144 requires an
  independent annual bias audit of automated employment decision tools with the results published;
  Maryland and Illinois regulate facial analysis in interviews; Utah requires disclosure of generative
  AI in regulated occupations. Local Law 144 is the only US regime that requires a published, structured,
  third-party-verified statistic about a model''s behaviour.'
tags:
- Artificial Intelligence
- Employment
- Bias Audit
- Automated Decisions
- United States
- Regulation
common:
- type: Legislation
  url: https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page
url: https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page
yearCreated: 2021
alternativeNames:
- Local Law 144
- LL 144
- NYC AEDT law
- Illinois HB 3773
- AI hiring laws
companyCountStatus: pending-corpus-pass
---

Long before anyone passed a general AI statute, US regulators reached AI through **employment**, and that body of law is still the most operationally demanding thing on the books. It is also the only place where a US law requires a company to publish a number about how its model behaves.

  * **NYC Local Law 144** - An automated employment decision tool used to screen candidates in New York City must undergo an **independent bias audit** within the prior year, and a **summary of results must be published on the employer's website**. Candidates must be notified at least ten business days in advance and told what qualifications the tool assesses.
  * **Illinois HB 3773** - Amends the Illinois Human Rights Act so that using AI that has a discriminatory effect in recruitment, hiring, promotion, discipline or discharge is a civil rights violation, and using zip code as a proxy for a protected class is expressly prohibited. Effective 1 January 2026.
  * **Illinois AI Video Interview Act** - Consent, explanation and deletion rights where AI analyses video interviews, plus demographic reporting where AI alone determines who advances.
  * **Maryland** - Consent required for facial recognition during interviews.
  * **Utah AI Policy Act** - Disclosure that a user is interacting with generative AI, on request generally and proactively in regulated occupations.

Local Law 144 deserves the attention. Every other transparency obligation in this catalog asks a company to describe itself — publish a framework, summarise training data, state a policy. LL 144 asks for a **selection rate and impact ratio, by race/ethnicity and sex, computed by an independent auditor, published at a URL**. That is a measured statistic about model behaviour, externally verified, in public, refreshed annually. There is nothing else like it in American law.

It has not worked as well as it should, and the reason is instructive. The published summaries live at inconsistent URLs in inconsistent formats, often a PDF or a paragraph buried in a careers page, with no registry, no schema and no required identifier tying an audit to the tool it audited. Researchers trying to study compliance have had to find the disclosures by crawling. A requirement to publish a number, without a requirement about *where* or *in what shape*, produces data nobody can aggregate.

That is the single clearest lesson this catalog has for anyone drafting the next one, and it generalises well beyond hiring. Disclosure obligations survive the legislative process — that is the pattern across Colorado, California and the EU. But a disclosure obligation without a location and a schema produces compliance without transparency. The fix is small and nobody has made it: say the artefact goes at a well-known path, say what fields it carries, and the same law starts producing a dataset instead of a scavenger hunt.
