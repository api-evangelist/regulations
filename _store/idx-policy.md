---
papers:
- title: The State of US Real Estate APIs
  url: https://reports.apievangelist.com/reports/state-of-us-real-estate-apis/
  note: "The agreement a developer must execute to display MLS listings — the access layer that a RESO certification says nothing about, and the reason certified endpoints return 401."
name: IDX
slug: idx-policy
title: Internet Data Exchange (IDX)
kind: industry-policy
jurisdiction: United States (trade association / local MLS)
description: >-
  Internet Data Exchange is the National Association of REALTORS policy framework, implemented through
  each local MLS's own rules, that permits participating brokers to display other brokers' listings on
  their public websites. Access requires an executed IDX agreement with the MLS, broker participation,
  and compliance with display, attribution and refresh rules. It is the mechanism through which most
  public US listing data reaches the open web, and it is a contract rather than a statute.
tags:
- Real Estate
- United States
- Industry Policy
- Data Licensing
- Access Control
common:
- type: Website
  url: https://www.nar.realtor/
url: https://www.nar.realtor/
yearCreated: 2000
alternativeNames:
- Internet Data Exchange
- IDX feed
- IDX agreement
---

**IDX is a licence, not a law** — and in US residential real estate it is the instrument that actually
determines whether anyone can reach listing data.

Under NAR policy, implemented through each local MLS's own rules, a participating broker may display other
participants' listings on their public site. To consume that feed a developer executes an IDX agreement with
the MLS, works under broker participation, and accepts rules on how listings are displayed, attributed and
refreshed.

*   **Per-MLS, not national** - There are roughly five hundred MLSs, each with its own agreement and its own
    terms. There is no single contract that unlocks American listing data.
*   **Broker-anchored** - Access derives from broker or agent participation. A developer without that
    relationship generally routes through a reseller who has it.
*   **Display-constrained** - IDX governs what may be shown and how, not merely what may be retrieved.

*The State of US Real Estate APIs* recorded an access gate for every organization researched, and IDX sits
at the centre of the American ladder. The finding that gives this entry its point: **sorted by access model,
average API score runs backwards** — licence-agreement 47.7, self-serve 47.6, application-approval 44.7,
partner-only 37.2, membership-required 32.5, nothing-published 23.0. The most contractually locked tier has
the best contracts.

This is the counterpart to
[NAR Policy Statement 7.90](https://regulations.apievangelist.com/store/nar-policy-statement-790/) and the
reason that mandate returned so little. 7.90 compels the *schema*; IDX governs the *access*. A
RESO-certified endpoint is genuinely conformant and still answers 401 to anyone without an executed
agreement.

For the agentic turn this is the hard edge. An autonomous agent can parse an OData contract and follow a
discovery document. **It cannot execute an IDX agreement or obtain broker sponsorship.** Every access tier
above self-serve in this sector is a human legal process, and in the sixty-seven organizations newly
researched for the study, only four were self-serve — none of them American.
