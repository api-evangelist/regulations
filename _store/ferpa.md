---
papers:
- title: The State of Education & EdTech APIs
  url: https://papers.apievangelist.com/papers/state-of-education-apis/
  note: The delegation statute of US education — a parent for a child, an institution for both — in a
    market describing consent and delegated identity at 3.3%.
name: FERPA
kind: regulation
jurisdiction: United States
slug: ferpa
title: Family Educational Rights and Privacy Act (FERPA)
description: FERPA is the United States statute governing the privacy of student education records. It
  gives parents, and students once they turn eighteen, the right to inspect and seek correction of those
  records, and it restricts disclosure without consent — with exceptions for school officials with a legitimate
  educational interest, and for vendors operating under the school official exception.
tags:
- Privacy
- Education
- Student Data
- United States
- Regulation
common:
- type: Regulator
  url: https://studentprivacy.ed.gov/
- type: Legislation
  url: https://www.ecfr.gov/current/title-34/subtitle-A/part-99
url: https://studentprivacy.ed.gov/ferpa
yearCreated: 1974
alternativeNames:
- Family Educational Rights and Privacy Act
- 20 U.S.C. § 1232g
- Buckley Amendment
standards:
- title: WCAG
  url: https://standards.apievangelist.com/store/wcag/
  note: 'Unrelated in subject, related in pattern: both are obligations institutions meet without publishing
    a machine-readable artifact.'
---

**FERPA** is the statute every American EdTech contract is written against, and its central mechanism is consent and delegation rather than security. A school may share records with a vendor acting as a *school official*, under direct control, for a defined purpose — which is a delegation of authority, negotiated in a contract and described nowhere machine-readable.

  * **Inspection and correction** - Parents and eligible students may see the record and challenge what is in it.
  * **Consent before disclosure** - The default is no disclosure, with enumerated exceptions rather than a general permission.
  * **The school official exception** - How vendors lawfully hold student data: under the institution's direct control, for a defined purpose.
  * **Directory information** - A carve-out institutions define themselves, with an opt-out — one of the few places a student choice becomes data.
  * **Enforcement through funding** - The remedy is federal funding, not a private right of action, which shapes how seriously it is treated.

FERPA governs disclosure and asks nothing about interfaces, which is the pattern this research has recorded in every regulated market. Its distinctive feature is that the permission it turns on is **delegated** — a parent for a child, an institution for both, a vendor under the institution's control. [The State of Education & EdTech APIs](https://papers.apievangelist.com/papers/state-of-education-apis/) measures consent and delegated identity as a legible surface at 3.3% of the education market. In the sector where the data subject is most often a minor and the authority is always delegated, that surface is effectively absent.
