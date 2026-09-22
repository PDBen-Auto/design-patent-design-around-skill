# Design Patent Search And Design Around Skill

[中文说明](README.md)

[![Release](https://img.shields.io/github/v/release/PDBen-Auto/design-patent-design-around-skill?display_name=tag&style=flat-square)](https://github.com/PDBen-Auto/design-patent-design-around-skill/releases/latest)
[![Validation](https://img.shields.io/github/actions/workflow/status/PDBen-Auto/design-patent-design-around-skill/validate.yml?branch=main&style=flat-square&label=validation)](https://github.com/PDBen-Auto/design-patent-design-around-skill/actions/workflows/validate.yml)
[![skills.sh](https://skills.sh/b/PDBen-Auto/design-patent-design-around-skill)](https://skills.sh/PDBen-Auto/design-patent-design-around-skill/design-patent-search-and-design-around)
[![License](https://img.shields.io/badge/license-source--available-59636e?style=flat-square)](LICENSE)

**A design-patent and industrial-design pre-screening workflow for physical products.** It connects product visuals, complete drawing sets, rights-holder research, risk separation, design-around concepts, supplier questions, prototype gates, and a second-pass collision search.

## What it solves

Most product IP checks stop at a keyword list or an image-similarity result. Product teams still need to know what the complete drawing set appears to protect, which risks are substantive versus marketplace or ownership risks, and what can be changed without breaking the product brief. This Skill turns that gap into a reviewable development workflow.

## What you get

- Primary-record candidate register with publication, family, assignee, status, and source links.
- Drawing-based visual scope explanation, including solid-line and broken-line treatment.
- View-by-view comparison across perspective, top, side, front/rear, end, and installed relationships.
- Separate substantive, marketplace complaint, ownership, unpublished-application, and residual-risk conclusions.
- Three structurally distinct design-around directions mapped to function, tooling, cost, supplier capability, and prototype gates.
- A preferred-concept handoff, do-not-revert list, second-pass search note, and attorney-review questions.

## Install

```bash
npx skills add PDBen-Auto/design-patent-design-around-skill --skill design-patent-search-and-design-around
```

Manual Codex installation:

```bash
git clone https://github.com/PDBen-Auto/design-patent-design-around-skill.git
cp -R design-patent-design-around-skill "$HOME/.codex/skills/design-patent-search-and-design-around"
```

The latest signed package is available from [GitHub Releases](https://github.com/PDBen-Auto/design-patent-design-around-skill/releases/latest).

## Example request

> Pre-screen this home-organization product for US design-patent risk. Compare the product images with serious candidates across all available views, separate substantive and marketplace risk, produce three structurally different design-around directions, and list supplier and prototype gates. Mark everything that still requires patent counsel.

## Best-fit users

Product managers, industrial designers, R&D engineers, sourcing teams, cross-border sellers, and attorneys preparing a formal review. It is useful for automotive accessories, home and kitchen products, tools, consumer electronics, furniture, packaging structures, and other products where overall visual appearance matters.

## Boundaries

This is a public-record pre-screen and product-development workflow. It is not a patent attorney opinion, formal FTO, litigation strategy, or non-infringement guarantee. Generated images are concept guidance, not engineering drawings or manufacturing instructions.

## Related PDBen-Auto Skills

- [Amazon Review Intelligence](https://github.com/PDBen-Auto/amazon-review-intelligence-skill)
- [SellerSprite Amazon Market Research BI](https://github.com/PDBen-Auto/sellersprite-amazon-market-research-bi-skill)
- [Amazon Product Decision Gateway](https://github.com/PDBen-Auto/amazon-product-decision-suite)

## License

This repository is source-available for inspection and evaluation. All rights are reserved; see [LICENSE](LICENSE).
