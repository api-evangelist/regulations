# API Evangelist Regulations

The regulations, rules, and legal frameworks that govern API operations across
regulated industries — the laws behind the machine-readable standards catalogued
at [standards.apievangelist.com](https://standards.apievangelist.com).

Published at **[regulations.apievangelist.com](https://regulations.apievangelist.com)**.

Where a **Standard** is the technical, machine-readable contract (OpenAPI, FAPI,
the UK Open Banking Read/Write spec), a **Regulation** is the law or mandated
framework that requires it (PSD2, the CMA Open Banking Order, Dodd-Frank §1033,
Australia's Consumer Data Right, Canada's Consumer-Driven Banking framework).

This is a Jekyll site: one file per regulation in `_store/<slug>.md`, rendered by
`_layouts/store.html`, listed on `index.html`. Each entry links to:

- the **standards that implement it** (`standards:` frontmatter → standards.apievangelist.com),
- the **API Evangelist papers that reference it** (`papers:` frontmatter → papers.apievangelist.com), and
- the **blog posts** that discuss it (`posts:` frontmatter).

Deploys via GitHub Pages on push to `main` — no build step. Mirrors the structure
of the [api-evangelist/standards](https://github.com/api-evangelist/standards) repo.
