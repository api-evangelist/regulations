---
name: Australia Spam Act 2003
kind: statute
jurisdiction: Australia
scope: horizontal
countries:
- australia
regions:
- anz
industries:
- marketing-advertising
- e-commerce-platform
- communications-platform-as-a-service-cpaas
- retail
- technology
slug: spam-act-2003
title: Spam Act 2003 (Cth)
description: 'The Spam Act prohibits sending commercial electronic messages to Australian addresses
  without consent, requires accurate sender identification and a functional unsubscribe honoured within
  five working days, and is enforced by ACMA with civil penalties that have repeatedly run into the
  millions. It sits between CAN-SPAM''s opt-out permissiveness and CASL''s strictness, and ACMA enforces
  it more consistently than either.'
tags:
- Anti-Spam
- Consent
- Electronic Messages
- Unsubscribe
- Australia
- Regulation
common:
- type: Legislation
  url: https://www.legislation.gov.au/C2004A01214/latest/text
- type: Regulator
  url: https://www.acma.gov.au/avoid-sending-spam
url: https://www.acma.gov.au/avoid-sending-spam
yearCreated: 2003
alternativeNames:
- Spam Act
- Spam Act 2003
- ACMA spam rules
companyCountStatus: pending-corpus-pass
---

The **Spam Act 2003** is the oldest statute in this catalog's messaging group and the most consistently enforced. Three requirements, which have not changed in two decades:

  * **Consent** - Express or inferred. Inferred consent is narrower than most senders assume: a conspicuously published work address with no statement against unsolicited messages, or an existing relationship where the message is relevant to it. Inferred consent does not arise from a purchase alone in every circumstance, and it does not last indefinitely.
  * **Identify** - Accurate sender identification and contact details, valid for at least 30 days after sending.
  * **Unsubscribe** - A functional facility, honoured within **five working days** — shorter than CASL's ten business days and CAN-SPAM's ten calendar days — and free to use.

It covers email, SMS, MMS and instant messaging. It does not cover voice calls, which sit under the Do Not Call Register Act.

ACMA's enforcement record is the reason to take it seriously. The regulator has issued multi-million-dollar infringement notices against major Australian brands — banks, telcos, airlines, retailers — and the fact patterns are almost always the same two failures: unsubscribe requests not actually honoured within the window, and consent records that could not be produced when asked. Neither is a strategic compliance failure. Both are data-plumbing failures.

That is what makes this entry belong in an API catalog rather than a marketing compliance guide. The three obligations decompose cleanly into machine state: a consent record with a type, source and timestamp; a sender identity block; and an unsubscribe with a latency guarantee. The chronic failure mode is architectural — a suppression list that lives in one system while a campaign is sent from another, or a customer-data platform that re-imports a suppressed address from a source that never saw the opt-out. The five-day clock is missed by systems that never had a single authoritative answer to "may we message this address?"

For a CPaaS, email delivery or marketing automation provider, there is a product opportunity here that most have taken only partly. The obligation belongs to the sender, but the sender is using your API, and the difference between a platform that enforces suppression at send time across every channel and one that trusts the caller to have checked is the difference between a customer who passes an ACMA inquiry and one who does not. Suppression state, consent provenance and unsubscribe latency are all things an API can expose, guarantee and prove — and the providers who do it well rarely document it as the compliance feature it is.

Australia, Canada and the United States all regulate this, all with different clocks and different consent standards. The intersection is not complicated: express consent with a record, and honour opt-outs within five working days everywhere. Build to that and the jurisdiction question stops mattering.
