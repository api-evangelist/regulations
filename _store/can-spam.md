---
papers:
- title: The State of Marketing & Advertising APIs
  url: https://papers.apievangelist.com/papers/state-of-marketing-advertising-apis/
  note: The obligations behind the suppression list — and across 2,925 specification documents from that
    market's best publishers, `suppression` and `preferences` appear as resources zero times.
name: CAN-SPAM
kind: regulation
jurisdiction: United States (with UK and Canadian equivalents)
slug: can-spam
title: CAN-SPAM Act (with PECR and CASL)
description: 'CAN-SPAM sets the United States rules for commercial email: accurate headers and subject
  lines, identification as an advertisement, a physical postal address, and a working unsubscribe honoured
  promptly. Its UK and Canadian counterparts, PECR and CASL, are stricter — both require consent before
  sending rather than an opportunity to opt out afterwards.'
tags:
- Email Marketing
- Consent
- Unsubscribe
- Marketing
- United States
- Regulation
common:
- type: Regulator
  url: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
- type: Legislation
  url: https://www.congress.gov/bill/108th-congress/senate-bill/877
url: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
yearCreated: 2003
alternativeNames:
- CAN-SPAM Act
- PECR
- CASL
- Canada Anti-Spam Legislation
- Privacy and Electronic Communications Regulations
---

**CAN-SPAM, PECR and CASL** are the rules under the send button. The American version is opt-out: you may email a stranger provided you identify yourself and honour an unsubscribe. The British and Canadian versions are opt-in: consent comes first, and CASL's penalties are severe enough that most senders operate to it globally rather than maintain two systems.

  * **A working unsubscribe** - Honoured within a fixed window, and the one obligation every regime in this family shares.
  * **Truthful routing and subject lines** - Headers and subjects must not misrepresent origin or content.
  * **Identification and postal address** - The sender must be reachable outside the channel used to send.
  * **Consent before sending, outside the US** - PECR and CASL invert the default, which is why suppression state has to be portable.
  * **Liability that follows the list** - Using a platform does not transfer the obligation; the sender remains responsible for the list it uploaded.

This family produces the single most under-published artifact in the marketing stack. Every obligation here is about state — who consented, who withdrew, who must never be contacted again — and that state has to be honoured across every platform a business integrated. [The State of Marketing & Advertising APIs](https://papers.apievangelist.com/papers/state-of-marketing-advertising-apis/) reads 2,925 specification documents from the 244 best-published companies in that market and finds `suppression` and `preferences` published as resources exactly zero times, and `unsubscribe` once. The compliance work is being done; it simply is not described anywhere a machine can read it.
