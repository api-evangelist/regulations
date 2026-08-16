---
papers:
- title: The State of Australian Real Estate APIs
  url: https://reports.apievangelist.com/reports/state-of-australian-real-estate-apis/
  note: "The statute behind PEXA — the top-scoring Australian organization (60.1) and the only mandated machine-readable rail in the four-market study, holding the sole idempotency implementation across 101 organizations."
name: Electronic Conveyancing National Law
slug: electronic-conveyancing-national-law
title: Electronic Conveyancing National Law (ECNL)
kind: statute
jurisdiction: Australia (state and territory)
description: >-
  The Electronic Conveyancing National Law is the uniform legislation, enacted state by state across
  Australia, that authorises electronic lodgement and settlement of property transactions. It establishes
  Electronic Lodgement Network Operators (ELNOs) as regulated infrastructure and empowers the Australian
  Registrars' National Electronic Conveyancing Council (ARNECC) to issue the Model Participation Rules and
  Model Operating Requirements that bind them. Most states now require mainstream conveyancing to settle
  electronically under it.
tags:
- Real Estate
- Australia
- Conveyancing
- Infrastructure
- Regulation
common:
- type: Regulator
  url: https://www.arnecc.gov.au/
- type: Model Participation Rules
  url: https://www.arnecc.gov.au/regulation/model-participation-rules/
url: https://www.arnecc.gov.au/
yearCreated: 2012
alternativeNames:
- ECNL
- ARNECC Model Participation Rules
- Model Operating Requirements
- Electronic Lodgement Network Operator
- ELNO
---

The **Electronic Conveyancing National Law** is the most instructive mandate in the real estate study, and
the reason is what it chose to compel.

Australia did not standardise a listing schema. It made **electronic settlement** the way property changes
hands, established ELNOs as regulated infrastructure under uniform national law, and left ARNECC to write
the Model Participation Rules that govern who may operate one and how.

*   **Uniform law, state enactment** - A single legislative template adopted across jurisdictions, giving
    national consistency without a federal takeover of land titles.
*   **Regulated operators, not a government platform** - ELNOs are private operators bound by public rules,
    supervised by the state Registrars collectively through ARNECC.
*   **Effectively compulsory** - Most states now require mainstream conveyancing to settle electronically,
    which is what turned a permission into a rail.

The measured outcome is the point. *The State of Australian Real Estate APIs* found **PEXA** — the dominant
ELNO — topping the market at **60.1** with an agent-readiness of **86.5**, publishing seven specifications
covering workspaces, participants, documents and settlement events, and holding **the only idempotency
implementation found across all 101 organizations in the four-market study.** In a market that transfers
title, exactly one participant publishes a mechanism to prevent a duplicate transaction, and it is the one
the law made into infrastructure.

Set that against the United States, which mandated the
[RESO Web API](https://standards.apievangelist.com/store/reso-web-api/) and
[Data Dictionary](https://standards.apievangelist.com/store/reso-data-dictionary/) — a *schema* — through
[NAR Policy Statement 7.90](https://regulations.apievangelist.com/store/nar-policy-statement-790/) and left
distribution licensed. That mandate returned about two points of measured API quality and produced certified
endpoints that answer 401.

**The transferable lesson: if you are going to compel something, compel the rail, not the vocabulary.** A
schema mandate produces conformance. A rail mandate produces traffic, and traffic produces the operational
maturity — idempotency, events, published limits — that conformance never asks for.

The honest qualifier: PEXA's API is not open either. It serves subscribers to a regulated network, and
access runs through participation rules rather than a developer signup. Australia did not produce an open
property ecosystem. It produced working infrastructure, which is more than the schema mandate managed.
