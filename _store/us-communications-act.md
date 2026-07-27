---
papers:
- title: The State of Telecom APIs
  url: https://papers.apievangelist.com/papers/state-of-telecom-apis/
  note: "The FCC publishes real public REST APIs over its own data and out-publishes Deutsche Telekom, Comcast, BT, Vodafone, T-Mobile and AT&T — the regulator beating the regulated, again."
name: US Communications Act
kind: statute
jurisdiction: United States
slug: us-communications-act
title: US Communications Act and FCC Authority
description: >-
  The Communications Act of 1934, as amended by the Telecommunications Act of 1996, is the statutory basis for US telecommunications regulation and the Federal Communications Commission's authority. It governs spectrum licensing, carrier obligations, interconnection, universal service and customer proprietary network information (CPNI) — and requires no carrier to expose a network API to anybody.
tags:
- Telecommunications
- United States
- Regulation
- Spectrum
- Privacy
common:
- type: Website
  url: https://www.fcc.gov/
- type: Regulator
  url: https://www.fcc.gov/general/rules-regulations-title-47
url: https://www.fcc.gov/
yearCreated: 1934
alternativeNames:
- Communications Act of 1934
- Telecommunications Act of 1996
- FCC
- Federal Communications Commission
- CPNI
jurisdiction: United States
---

US telecom regulation is extensive and old, and none of it points at the thing this research measures.

  * **Spectrum and licensing** - The core of the regime: who may transmit, where, and on what terms.
  * **Interconnection** - Carrier-to-carrier obligations that shaped the wholesale market, and which have no
    developer-facing analogue.
  * **CPNI** - Customer proprietary network information rules restrict how carriers use and disclose subscriber
    data, which bears directly on the network APIs that expose exactly that data.
  * **No network-API mandate** - Nothing obliges an operator to publish SIM swap, number verification, device
    location or quality-on-demand as a callable contract.

CPNI is the part API practitioners should read closely. The CAMARA identity verbs — number verification, SIM swap,
device location — are built on precisely the subscriber information CPNI governs, which is why consent design is
the make-or-break element of network APIs rather than an afterthought. *The State of Telecom APIs* also recorded
the pattern this catalog keeps finding: the FCC's own public APIs are more usable than most of the carriers it
regulates.
