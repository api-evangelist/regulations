---
papers:
- title: The State of Robotics & Autonomous Systems APIs
  url: https://reports.apievangelist.com/reports/state-of-robotics-apis/
  note: The one obligation in robotics demanding a machine-readable EMISSION rather than a document —
    and the segment around it produced the market's clearest cluster of real interfaces.
name: FAA Part 107 and Remote ID
kind: regulation
jurisdiction: United States
slug: faa-part-107
title: FAA Part 107 and Remote ID
description: Part 107 governs commercial small unmanned aircraft operation in the United States — pilot
  certification, operating limits, and the waiver and authorization process for flying beyond them. Part
  89, the Remote ID rule, requires most drones to broadcast their identity, position and control-station
  location while in flight.
tags:
- Drones
- UAV
- Aviation
- Safety
- United States
- Regulation
common:
- type: Regulator
  url: https://www.faa.gov/uas
- type: Legislation
  url: https://www.ecfr.gov/current/title-14/chapter-I/subchapter-F/part-107
url: https://www.faa.gov/uas/commercial_operators/part_107
yearCreated: 2016
alternativeNames:
- Part 107
- 14 CFR Part 107
- Remote ID
- 14 CFR Part 89
companyCount: 17
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---

**Remote ID is the most interesting rule in robotics for anyone who studies interfaces**, because it does something almost no other safety regime does: it requires a **machine-readable emission** rather than a document. An aircraft must continuously broadcast who it is and where it is, in a defined format, to anyone listening.

  * **Broadcast identity and position** - Serial or session ID, location, altitude, velocity and control-station position, over Bluetooth or Wi-Fi.
  * **LAANC authorization** - Near-real-time airspace authorization delivered through approved API providers rather than by paperwork.
  * **Waivers for extended operations** - Beyond-visual-line-of-sight and other operations run through a defined application process.
  * **An API-shaped ecosystem** - LAANC created a market for airspace-authorization providers that had to integrate programmatically.

[The State of Robotics & Autonomous Systems APIs](https://reports.apievangelist.com/reports/state-of-robotics-apis/) finds this the clearest natural experiment in that market. Where the rule demands data a machine can read, the data appears: the drone and airspace segment produced the market's most visible cluster of real interfaces, and the FAA itself scores 57.1 — ahead of all but three companies in the industry it regulates. Everywhere else in robotics the obligation is a technical file, and technical files do not create APIs.
