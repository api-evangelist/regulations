---
name: Australia Cyber Security Act 2024
kind: statute
jurisdiction: Australia
scope: horizontal
countries:
- australia
regions:
- anz
industries:
- cybersecurity
- iot
- consumer-goods
- technology
- enterprise-software
- semiconductors-hardware
slug: australia-cyber-security-act
title: Cyber Security Act 2024 (Cth)
description: 'Australia''s first standalone cyber security statute does three things: it creates
  mandatory security standards for smart devices, it requires businesses above a turnover threshold to
  report ransomware and cyber extortion payments within 72 hours, and it establishes a Cyber Incident
  Review Board with a limited-use protection so information given to government during an incident
  cannot be turned against the victim. The ransomware payment reporting obligation is the first of its
  kind at national scale.'
tags:
- Cybersecurity
- Ransomware
- IoT Security
- Incident Reporting
- Australia
- Regulation
common:
- type: Legislation
  url: https://www.legislation.gov.au/C2024A00108/latest/text
- type: Regulator
  url: https://www.cyber.gov.au/
url: https://www.cyber.gov.au/
yearCreated: 2024
alternativeNames:
- Cyber Security Act 2024
- Australian Cyber Security Act
- Ransomware payment reporting
companyCountStatus: pending-corpus-pass
standards:
- title: security.txt  # wired by scripts/wire_standards_links.py
  url: https://standards.apievangelist.com/store/security-txt/
  note: The smart-device standards carry the same vulnerability-disclosure requirement the UK's PSTI Act
    established.
- title: CycloneDX  # wired by scripts/wire_standards_links.py
  url: https://standards.apievangelist.com/store/cyclonedx/
  note: Component transparency for connectable products, converging with the CRA.
---

The **Cyber Security Act 2024** is short, and two of its three parts are more interesting than their length suggests.

  * **Security standards for smart devices** - Mandatory minimum standards for relevant connectable products supplied in Australia, with a statement of compliance. The same three-requirement pattern the UK's PSTI Act established: no universal default passwords, a vulnerability disclosure policy, a stated support period.
  * **Ransomware payment reporting** - Businesses above the turnover threshold (AUD 3 million) and critical infrastructure entities must report a ransomware or cyber-extortion payment to government **within 72 hours**. Reporting began 30 May 2025.
  * **A Cyber Incident Review Board** - Conducting no-fault post-incident reviews, modelled on transport safety investigation.
  * **Limited use protections** - Information voluntarily given to the National Cyber Security Coordinator during an incident is restricted in how it can be used against the provider. This is the provision that makes the rest workable.

The ransomware payment reporting is genuinely novel and worth understanding on its own terms. Governments have wanted this data for years and have not been able to get it, because the population that pays is precisely the population least willing to tell anyone. Australia's answer was not to ban payment — which pushes it underground — but to make reporting mandatory and pair it with a limited-use protection, so that the act of reporting does not hand a regulator the evidence for a separate enforcement action.

Whether that bargain holds is the thing to watch. It is the same bargain aviation made with no-fault incident reporting, and aviation's version works because the protection is credible and has been tested. Cyber has no comparable track record, and the first time reported information appears to surface in an unrelated enforcement action, reporting rates will tell you what people concluded.

The smart-device standards matter for a different reason: convergence. The UK legislated three requirements in 2022, the EU is scaling the same ideas across essentially all software with the Cyber Resilience Act by December 2027, and Australia has now adopted the pattern. A manufacturer shipping into all three markets faces one engineering task — publish a vulnerability disclosure policy, publish a support period, eliminate default credentials — and three conformity processes.

For this catalog the first two are directly observable from outside, which is unusual for anything regulatory. A vulnerability disclosure policy is `/.well-known/security.txt` and a documented process. A support period is a lifecycle declaration with a date. Both can be fetched, neither can be faked, and across the catalog they are mostly absent. That combination — mandated, cheap, machine-readable, and missing — is exactly what a scored check should be aimed at.
