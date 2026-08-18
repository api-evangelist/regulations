---
papers:
- title: The State of Supply Chain APIs
  url: https://reports.apievangelist.com/reports/state-of-supply-chain-apis/
  note: A rebuttable presumption that puts the evidentiary burden on the importer — and still names no
    exchange format for the evidence.
name: Uyghur Forced Labor Prevention Act
kind: statute
jurisdiction: United States
slug: uflpa
title: Uyghur Forced Labor Prevention Act (UFLPA)
description: US law establishing a rebuttable presumption that any goods mined, produced or manufactured
  wholly or in part in the Xinjiang Uyghur Autonomous Region, or by entities on an associated list, are
  made with forced labor and are therefore prohibited from entry into the United States.
tags:
- Supply Chain
- Human Rights
- Customs
- Trade Compliance
- United States
- Regulation
common:
- type: Website
  url: https://www.cbp.gov/trade/forced-labor/UFLPA
url: https://www.cbp.gov/trade/forced-labor/UFLPA
yearCreated: 2021
alternativeNames:
- UFLPA
- Public Law 117-78
companyCount: 2
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read of qualified job corpora, hardened word-boundary matcher,
  needles screened and confirmed against sampled matched text
companyCountSource: insights jobs corpus, via the insights-work regulations vocabulary
precision: 95
precisionGrade: high
precisionBasis:
- 'acronym-shape -5: shortest bare needle is 5 characters, halved — it neither collides nor appears in
  the corpus frequency table'
---

The **Uyghur Forced Labor Prevention Act** inverts the usual burden at the US border. Goods with a
nexus to the Xinjiang Uyghur Autonomous Region are presumed to be made with forced labor and are
excluded, and it falls to the importer to rebut that presumption with clear and convincing evidence
of the supply chain behind the shipment.

  * **Rebuttable presumption** - Detention is the default; admissibility is something the importer proves.
  * **Entity List** - A maintained list of producers and exporters whose goods trigger the presumption.
  * **Traceability to raw material** - Rebutting typically requires documentation back to the cotton bale, the polysilicon batch or the ore, several tiers above the direct supplier.
  * **Enforced by CBP** - US Customs and Border Protection issues detentions and publishes statistics.

UFLPA is the most demanding evidentiary regime in this catalog in terms of how far up the chain the
data has to reach — and, characteristically for supply chain, it names no format for that data.
Importers assemble it as documents, per detention, largely by email. *The State of Supply Chain APIs*
places it alongside [CSDDD](/store/csddd/) and [LkSG](/store/lksg/) in the pattern that explains this
market's contract quality: regulation that demands deep supply chain knowledge, and specifies no
interoperable way for the companies who hold it to pass it along.
