---
name: US State Comprehensive Privacy Laws
kind: statute
jurisdiction: United States (state, 20 in effect)
scope: horizontal
countries:
- united-states
regions:
- north-america
industries:
- technology
- marketing-advertising
- data-analytics
- e-commerce-platform
- retail
- artificial-intelligence
slug: us-state-comprehensive-privacy-laws
title: US State Comprehensive Consumer Privacy Laws
description: 'In the absence of a federal privacy statute, twenty US states have comprehensive consumer
  privacy laws in effect and twenty-four have enacted one. They converge on six rights — access,
  deletion, correction, portability, opt-out and non-discrimination — and diverge on thresholds,
  cure periods, sensitive-data handling, universal opt-out signals and who enforces. The practical
  consequence for an API provider is that the obligation is one obligation and the compliance surface
  is twenty, and only a few of the differences are actually machine-visible.'
tags:
- Privacy
- Consumer Rights
- Opt-Out
- Data Portability
- United States
- Regulation
common:
- type: Legislation
  url: https://iapp.org/resources/article/us-state-privacy-legislation-tracker/
url: https://iapp.org/resources/article/us-state-privacy-legislation-tracker/
yearCreated: 2018
alternativeNames:
- State Privacy Laws
- US State Privacy Patchwork
- Comprehensive Consumer Data Privacy Acts
companyCountStatus: pending-corpus-pass
---

The **US state privacy patchwork** is catalogued here as a single entry because that is how companies actually experience it. Nobody builds a Connecticut data-subject-request flow and a separate Montana one. They build one flow to the strictest common denominator and then carry a table of the exceptions.

Twenty laws are in effect. California, Virginia, Colorado, Connecticut and Utah came first; Texas, Oregon, Montana, Florida, Delaware, Iowa, Nebraska, New Hampshire, New Jersey, Tennessee, Minnesota and Maryland followed; Indiana, Kentucky and Rhode Island all took effect on 1 January 2026. Alabama, Louisiana, Oklahoma and Vermont enacted during 2026 and are queued.

  * **The six rights are effectively universal** - Access, deletion, correction, portability, opt-out of sale/targeted advertising/profiling, and non-discrimination for exercising them.
  * **Thresholds differ and they matter most to small companies** - Record counts, revenue tests and whether revenue from selling data pulls you in regardless of size. A company under every threshold in eighteen states can be squarely in scope in two.
  * **Universal opt-out signals are the machine-readable part** - Colorado, California, Connecticut, Texas and others require honouring browser-level opt-out signals. This is the one provision in the whole patchwork expressed as a protocol rather than as a process.
  * **Maryland is the outlier worth reading** - It imposes data-minimisation duties rather than only consent duties, which is a different and harder obligation.
  * **Cure periods are closing** - Early laws gave a window to fix a violation before enforcement. The newer ones increasingly do not, and several sunset the cure period on a schedule.

The thing I would tell an API provider is that almost none of this is where their actual US risk sits. State privacy enforcement has been modest and mostly directed at consumer-facing companies with obvious dark patterns. The genuine exposure in the United States is **private litigation**: Illinois BIPA for anything touching biometrics, the California Invasion of Privacy Act and its state analogues for pixels, session replay and chat-widget interception, and the Video Privacy Protection Act for anything that looks like video viewing history. Those produce class actions with statutory damages, which is a structurally different threat from a regulator with a cure period.

From a catalog perspective the patchwork is frustrating precisely because it is so nearly machine-readable and so rarely made so. A data-subject-request endpoint is an API. A universal opt-out signal is a header. A retention period is a number. A "do not sell" state is a flag on a record. Every one of these is expressible in a contract, and the overwhelming majority of providers express all of them in a privacy policy written for a lawyer to read once. The Global Privacy Control is the single counterexample — a real, adopted, legally recognised machine-readable signal — and it is worth noting how much work it took to get one.
