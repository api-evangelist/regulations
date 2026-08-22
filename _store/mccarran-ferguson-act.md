---
standards:
- title: ACORD
  url: https://standards.apievangelist.com/store/acord/
  note: With no federal rule to force a contract, data exchange fell to a private standards body — and
    stayed in an EDI idiom for fifty years.
name: McCarran-Ferguson Act
kind: statute
jurisdiction: United States
slug: mccarran-ferguson-act
title: McCarran-Ferguson Act (1945)
description: The McCarran-Ferguson Act is the 1945 US statute that delegated the regulation of insurance
  to the states and exempted the business of insurance from most federal law where a state already regulates
  it. It is the reason the United States has no federal insurance regulator, fifty separate insurance
  departments, and nothing resembling PSD2, the CFPB's 1033 rule, or the 21st Century Cures Act for insurance
  data.
tags:
- Insurance
- United States
- Regulation
- Federalism
- Statute
common:
- type: Website
  url: https://www.law.cornell.edu/uscode/text/15/chapter-20
- type: Regulator
  url: https://content.naic.org/
url: https://www.law.cornell.edu/uscode/text/15/chapter-20
yearCreated: 1945
alternativeNames:
- McCarran-Ferguson
- Public Law 79-15
- 15 U.S.C. §§ 1011-1015
companyCount: 0
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---

McCarran-Ferguson is the most consequential regulation in this catalog that mandates nothing at all. It is
an allocation of authority, and the allocation is why American insurance looks the way it does from the outside.

  * **Regulation delegated to the states** - Insurance is regulated by fifty state departments, coordinated —
    not governed — by the National Association of Insurance Commissioners.
  * **A federal exemption, not a federal rule** - Federal law generally yields where a state regulates the
    business of insurance, which forecloses the single-national-mandate path that opened banking and health data.
  * **No open-insurance rule anywhere in the stack** - The CFPB's 1033 rule opened consumer banking data;
    nothing equivalent touches an insurance policy.
  * **Coordination without compulsion** - The NAIC can write model laws, and each state decides whether and how
    to adopt them. There is no mechanism to require a carrier to expose anything to anybody.

This is the law that makes US insurance the control group for every argument about mandates. Scoring seventy-nine
US insurance organizations for *The State of US Insurance APIs* found a sector averaging 29.4 with nothing reaching
the Strong band and exactly one company publishing `bind` as an operation. When people ask what an industry does
when nobody forces it to publish, this is the statute that set up the experiment, and that report is the
result.
