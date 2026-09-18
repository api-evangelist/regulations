---
name: Canada's Anti-Spam Legislation
kind: statute
jurisdiction: Canada
scope: horizontal
countries:
- canada
regions:
- north-america
industries:
- marketing-advertising
- e-commerce-platform
- technology
- communications-platform-as-a-service-cpaas
- enterprise-software
- developer-tools
slug: casl
title: Canada's Anti-Spam Legislation (S.C. 2010, c. 23)
description: 'CASL is the strictest commercial-messaging law in the world — express opt-in consent,
  prescribed sender identification, a working unsubscribe honoured within ten business days, and
  penalties to CAD 10 million. It also does something no other spam law does: it separately regulates
  the INSTALLATION OF COMPUTER PROGRAMS on another person''s device, which makes it the only statute
  in this catalog that reaches a software updater.'
tags:
- Anti-Spam
- Consent
- Electronic Messages
- Software Installation
- Canada
- Regulation
common:
- type: Legislation
  url: https://laws-lois.justice.gc.ca/eng/acts/E-1.6/
- type: Regulator
  url: https://crtc.gc.ca/eng/internet/anti.htm
url: https://fightspam.gc.ca/
yearCreated: 2010
alternativeNames:
- CASL
- Anti-Spam Law
- An Act to promote the efficiency and adaptability of the Canadian economy
companyCountStatus: pending-corpus-pass
---

**CASL** is routinely described as "Canada's CAN-SPAM", which is wrong in both direction and degree. CAN-SPAM is opt-out and lightly enforced. CASL is opt-in, prescriptive, enforced by three regulators, and carries penalties up to CAD 10 million for an organisation.

On commercial electronic messages:

  * **Express or implied consent, required before sending** - Implied consent exists only in defined circumstances (an existing business relationship, a conspicuously published address relevant to the recipient's role) and most of it expires on a clock.
  * **Prescribed identification** - Who is sending, on whose behalf, with a mailing address and a working contact, in the message.
  * **An unsubscribe mechanism honoured within ten business days** - And functional for at least sixty days after sending.
  * **The burden of proving consent sits on the sender** - Which is a records requirement, not a policy.
  * **It covers email, SMS, and instant messaging** - Any commercial electronic message to an electronic address.

And then section 8, which is the part that belongs in an API catalog:

  * **Installing a computer program on another person's computing device requires express consent** - With enhanced disclosure where the program collects personal information, changes settings, interferes with control of the device, or communicates externally without the user's knowledge.

That provision has no equivalent anywhere else in this catalog. It reaches software updaters, bundled installers, agents, browser extensions, SDK components that self-update, and — on a reading nobody has definitively tested — a good deal of what an autonomous agent installed on a user's machine does. The enhanced-disclosure trigger list reads like a description of ordinary telemetry.

CASL is under-considered by API providers for a specific structural reason: it does not feel like a data-protection law, so it does not get picked up by the privacy review, and it does not feel like a product law, so it does not get picked up by the engineering review. It lands in marketing. Meanwhile the section that would most affect an engineering team sits in a statute nobody in engineering has read.

For anyone building the machine-readable side of this, the artefacts are unusually clean. Consent has a type (express or implied), a source, a timestamp and — for implied consent — an expiry. An unsubscribe is an endpoint with a latency guarantee. A sender identity is a structured block. A software installation disclosure is a manifest of behaviours: what it collects, what it changes, what it talks to. Every one of those is a field. In practice they live in a marketing automation platform and a legal review, and the ten-business-day clock is honoured by hope.

The private right of action in CASL was suspended before it came into force and has never been activated. If it ever is, this becomes the most expensive statute in Canada overnight.
