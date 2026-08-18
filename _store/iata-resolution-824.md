---
papers:
- title: The State of Australian Travel APIs
  url: https://reports.apievangelist.com/reports/state-of-australian-travel-apis/
  note: The gate an agent cannot pass — Virgin Australia's agency terms require IATA or ATIS accreditation
    and mandate GDS access for BSP sales, at the airline's absolute discretion.
- title: The State of US Travel APIs
  url: https://reports.apievangelist.com/reports/state-of-us-travel-apis/
  note: Across forty organizations researched, only seven are self-serve; thirteen gate behind a commercial
    agreement and seven more behind accreditation or a licence.
standards:
- title: IATA BSP and ARC
  url: https://standards.apievangelist.com/store/iata-bsp/
  note: The settlement machinery accreditation under this resolution admits an agency to.
name: IATA Resolution 824
slug: iata-resolution-824
title: IATA Resolution 824 (Passenger Sales Agency Agreement)
kind: industry-policy
jurisdiction: International
description: Resolution 824 establishes the Passenger Sales Agency Agreement — the standard contract between
  IATA member airlines and accredited travel agencies, and the basis of the accreditation regime that
  determines who may issue airline tickets at all. It is industry rule rather than law, and it is the
  single most binding access control in travel distribution.
tags:
- Travel
- Aviation
- Accreditation
- Distribution
- Industry Policy
- IATA
common:
- type: Website
  url: https://www.iata.org/en/programs/accreditation-travel/
url: https://www.iata.org/en/programs/accreditation-travel/
yearCreated: 1979
alternativeNames:
- Resolution 824
- PSAA
- Passenger Sales Agency Agreement
- IATA accreditation
companyCount: 0
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

Resolution 824 is the reason travel is the least agent-reachable sector in the API Evangelist series, and
it is not a technical obstacle at all.

The resolution establishes the **Passenger Sales Agency Agreement** and the accreditation regime beneath
it. An IATA, ARC, TIDS or equivalent number is what permits an agency to issue a ticket and settle
through [BSP or ARC](https://standards.apievangelist.com/store/iata-bsp/). No amount of API access substitutes for it, and no API key confers
it.

*   **Accreditation is the precondition** - not documentation, not a developer account. A number.
*   **Airlines retain discretion** - ticketing authority can be granted, refused, suspended and revoked
    under the agreement.
*   **Enforced financially** - [Resolution 850m](https://regulations.apievangelist.com/store/iata-resolution-850m/) Agency Debit Memos are how
    breaches are actually punished.

## The binding constraint on the agentic turn

An agent can parse an OpenAPI, follow a discovery document and invoke an MCP tool. **It cannot obtain
IATA accreditation.**

The four *State of Travel APIs* reports measured how much of the sector sits behind that kind of gate.
Across forty newly researched organizations: **thirteen gate access behind a commercial agreement, seven
more behind accreditation or a licence, three are partner-only, three require application approval — and
only seven are self-serve.**

The airline terms make the mechanism explicit:

- **Virgin Australia's** Travel Agent Main Agreement requires current IATA or ATIS accreditation and
  states *"You must have GDS access for BSP Sales"*, with refusal at Virgin's absolute discretion,
  third-party credit assessment, and removal of ticketing authority after sixty days of inactivity.
- **Jetstar** restricts registered agents to its API, GDS and Agent Hub, making commercial booking
  through its own consumer website an express breach of the agency terms.
- **Rex** ties commission to logged-in portal sessions and fixes the accreditation number permanently at
  registration — an identifier the customer can never move.
- **Porter** reserves immediate termination at sole discretion with no notice period, claims ownership of
  all PNR data, and revokes data rights on suspension.

## Why it belongs in a regulations catalog

Because it functions as one. A reader assessing whether a travel API is usable will find the
specification, the authentication scheme and the rate limits documented, and will discover only at
contracting that **the actual gate is a private industry agreement with a discretionary approval step.**

This is the same lesson US real estate teaches through [IDX](https://regulations.apievangelist.com/store/idx-policy/) and
[VOW](https://regulations.apievangelist.com/store/vow-policy/) agreements, and it generalises: **in intermediated industries, the access rule is
private, the technical surface is public, and only the first one decides whether anything can be built.**
