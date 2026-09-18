---
headers:
- name: content-security-policy
  basis: evidentiary
  observable: edge
name: EU Cyber Resilience Act
kind: statute
jurisdiction: European Union
scope: horizontal
countries:
- austria
- belgium
- denmark
- estonia
- finland
- france
- germany
- ireland
- italy
- netherlands
- poland
- portugal
- spain
- sweden
regions:
- europe
- dach
- france-iberia
- nordics
- benelux
- italy-southern-europe
- cee
industries:
- cybersecurity
- iot
- developer-tools
- enterprise-software
- semiconductors-hardware
- technology
slug: eu-cyber-resilience-act
title: EU Cyber Resilience Act (CRA)
description: The EU Cyber Resilience Act is the first horizontal law to impose cybersecurity obligations
  on products with digital elements across their whole lifecycle — secure-by-design and secure-by-default
  requirements, a mandatory coordinated vulnerability disclosure policy, vulnerability handling and security
  updates for the support period, an SBOM for the top-level dependencies, and reporting of actively exploited
  vulnerabilities and severe incidents to ENISA. Unlike the sectoral data mandates, it compels no API;
  it compels a set of provable processes, several of which are naturally expressed as machine-readable
  artifacts.
tags:
- Cybersecurity
- Vulnerability Disclosure
- SBOM
- Product Security
- Incident Reporting
- Europe
- Regulation
common:
- type: Legislation
  url: https://eur-lex.europa.eu/eli/reg/2024/2847/oj
- type: Regulator
  url: https://www.enisa.europa.eu/
url: https://eur-lex.europa.eu/eli/reg/2024/2847/oj
yearCreated: 2024
alternativeNames:
- Cyber Resilience Act
- CRA
- Regulation (EU) 2024/2847
companyCount: null
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 0
precisionGrade: unmeasurable
precisionBasis:
- 'human verdict: `cra` is the Community Reinvestment Act in every sampled banking posting ("assists with
  CRA donations sponsorships", "the bank s CRA goals"). Stoplisted.'
standards:
- title: CycloneDX  # wired by scripts/wire_standards_links.py
  url: https://standards.apievangelist.com/store/cyclonedx/
  note: The CRA requires a software bill of materials covering at least the top-level dependencies;
    CycloneDX is one of the two formats the market actually ships.
- title: SPDX  # wired by scripts/wire_standards_links.py
  url: https://standards.apievangelist.com/store/spdx/
  note: The other SBOM format a CRA conformity assessment will accept, and the one with the deeper
    licensing model.
- title: security.txt  # wired by scripts/wire_standards_links.py
  url: https://standards.apievangelist.com/store/security-txt/
  note: The CRA obliges a coordinated vulnerability disclosure policy and a contact point for reporting;
    RFC 9116 is how that becomes machine-readable.
---

The **EU Cyber Resilience Act** does for product security what the AI Act does for AI: it regulates a horizontal property of software rather than a sector, and it attaches duties to whoever places a product with digital elements on the EU market. For an API provider, the important thing is that several of its obligations are not postures — they are artifacts somebody can ask you to produce.

  * **A coordinated vulnerability disclosure policy is mandatory** - Manufacturers must have a policy and a single point of contact for reporting vulnerabilities. This is the obligation that turns a published disclosure policy from good manners into a legal requirement.
  * **Vulnerability handling across the support period** - Identify, document, and remediate vulnerabilities without delay, and distribute security updates for the declared support period.
  * **An SBOM covering top-level dependencies** - Machine-readable in practice, which is why CycloneDX and SPDX matter here rather than as an engineering nicety.
  * **Reporting of actively exploited vulnerabilities and severe incidents** - To ENISA and the relevant CSIRT, on a short clock, which presumes you already know what your product does and who is affected.
  * **Secure by design and by default** - Including a default configuration that is the secure one, not the convenient one.

Read against an API catalog, the CRA lands on exactly the artifacts this research already scores. A `security.txt` or published vulnerability disclosure policy is the single point of contact the Act requires. An SBOM is a machine-readable dependency contract. Incident reporting on a clock presumes operational transparency — a status surface, a changelog, an audit trail — rather than a quarterly PDF.

That is what makes the cybersecurity cohort's numbers uncomfortable rather than merely ironic. **28% of the cybersecurity industry publishes a vulnerability disclosure policy**, and in threat intelligence — the sub-sector whose product is telling customers about exposed infrastructure and unpatched software — it is two organizations in nine. The Act does not ask whether a company knows how disclosure works. It asks whether the policy is published and the contact point exists, and that is a question answered by an artifact or not answered at all.

Like the [EU AI Act](/store/eu-ai-act/), the CRA compels no interface, which is why the Kin Score folds no Regulatory Posture facet into cybersecurity. It compels **provable process**, and process that has to be proved is process that is cheaper to publish than to reconstruct.
