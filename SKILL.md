---
name: design-patent-search-and-design-around
description: Analyze design patents and industrial-design rights for physical products, explain drawing-based visual scope, separate substantive and marketplace risk, and produce structurally distinct design-around concepts with supplier questions and prototype gates. Use for product-clearance pre-screening, product development, sourcing diligence, or marketplace complaint preparation. Do not use as a substitute for patent counsel, formal FTO, or utility-patent claim analysis.
---

# Design Patent Search And Design Around

Turn a physical-product brief, image set, or commercial-party clue into an evidence-backed design-rights pre-screen, a view-by-view scope explanation, and an actionable redesign brief. The workflow is intended for product managers, industrial designers, sourcing teams, cross-border sellers, and counsel preparing a formal review.

This skill is deliberately broader than Amazon listing research. It can be used for automotive accessories, home and kitchen products, tools, consumer electronics, packaging structures, furniture, industrial components, and other products whose visual appearance matters.

## Purpose And Scope

Use this skill when the user needs one or more of the following:

- search for relevant design patents, registered designs, or industrial-design rights;
- trace likely rights holders through brand, seller, supplier, factory, designer, inventor, assignee, and related entities;
- explain what a complete drawing set appears to claim, including solid-line and broken-line treatment;
- compare a target product with serious candidates across multiple views;
- distinguish substantive infringement risk from marketplace complaint, ownership, and unpublished-application risk;
- create several structurally different design-around directions that preserve required function;
- hand the selected direction to sourcing, engineering, prototype, and attorney-review workstreams;
- re-search the preferred redesign for new collision risks.

Do not use it as a formal legal opinion, a guarantee of non-infringement, a substitute for a freedom-to-operate opinion, or a utility-patent claim chart. A design patent or registered design protects an overall ornamental appearance, not an abstract feature list.

## Implementation Basis And Dependencies

The workflow is based on public patent records, complete drawing sets, ownership and family records, image and text search, product evidence, and a structured visual-comparison method. Feasibility depends on having enough product identity and visual evidence to compare the overall appearance, plus current records for the target jurisdiction.

| Dependency | Why needed | Required | Availability check | Fallback |
| --- | --- | --- | --- | --- |
| Current web access | Search patent records, product pages, ownership, portfolios, and legal-status events | Yes for current conclusions | Open at least one authoritative record and record retrieval date | Produce a historical/limited pre-screen and label freshness limits |
| Official patent or design databases | Confirm publication, drawings, priority, assignee, and status | Yes for serious candidates | Prefer USPTO, WIPO, EUIPO, CNIPA, or the relevant national office | Use aggregators for discovery only and mark facts needing confirmation |
| Product visuals | Compare perspective, top, side, front/rear, end, and distinctive details | Required for visual-risk work | Check image count, clarity, and whether key views are missing | Do not overstate cross-section, end, or connection conclusions |
| Commercial-party clues | Expand beyond the visible listing or brand | Optional but strongly recommended | Record seller, legal entity, supplier, factory, designer, or rights-holder clues | Search by product, image, classification, and title only; reduce ownership confidence |
| Reverse-image or visual search | Find visually related products and patent families | Optional | Verify the selected search service is available before relying on it | Use feature vocabulary, classifications, portfolios, and citations |
| Image-generation capability | Create concept boards and annotated concept guidance | Optional | Check that an image tool is available | Deliver a text-only design-around brief with multi-view requirements |
| User authorization | Needed before external writes such as supplier outreach, platform filings, or repository publication | Conditional | Confirm the user explicitly authorized the action | Draft the artifact but stop before the external mutation |

Never invent database access, legal status, supplier identity, or a search result. When a dependency is unavailable, state what was not checked and lower the confidence of the affected conclusion.

## Inputs

Provide as many of these as available. Missing optional inputs do not automatically block a pre-screen, but every material assumption must be recorded.

| Input | Requirement and format | Used by | Validation and missing-input behavior | Sensitivity |
| --- | --- | --- | --- | --- |
| `target_product` | Required. Product URL, ASIN/SKU/model, or a concise physical-product description | Identity normalization and search plan | Resolve the product and list unresolved identity conflicts; ask only when multiple products cannot be separated | May contain commercial links or private SKU data |
| `product_visuals` | Required for a visual-risk conclusion. PNG/JPG/PDF or accessible image URLs; perspective plus any available top, side, front/rear, end, installed, and detail views | Scope comparison and concept generation | Note missing views; do not infer hidden geometry as fact | May contain confidential product photos |
| `jurisdiction_and_cutoff` | Required. Country/region and search cutoff date; default cutoff is the execution date only when the user accepts it | Database routing and status interpretation | Reject ambiguous jurisdiction for a legal-status conclusion; produce a multi-jurisdiction plan when needed | Legal/commercial scope |
| `commercial_parties` | Optional. Brand, seller, legal entity, supplier, factory, designer, inventor, assignee, parent, affiliate, or suspected rights holder in any language | Entity and portfolio expansion | Preserve original spelling and transliterations; label unverified matches | May include personal or supplier information |
| `known_rights` | Optional. Patent/design numbers, complaint notices, attorney letters, platform case IDs, or prior reports | Candidate validation and risk triage | Validate against an authoritative record; do not treat user labels as status facts | Potentially privileged or confidential |
| `design_constraints` | Required for design-around work. Functions to retain, parts that may change, material, process, fitment, load, cost, tooling, packaging, and launch constraints | Design-around and supplier handoff | Separate must-keep, preferred, and negotiable constraints; ask when a constraint conflicts with the requested redesign | May reveal trade secrets or targets |
| `requested_deliverables` | Required. Search memo, full report, comparison matrix, concept board, annotated views, supplier questions, or attorney handoff | Output packaging | Default to a concise evidence memo plus design-around brief when unspecified | User preference |

Use [references/intake-and-deliverables.md](references/intake-and-deliverables.md) for the copy-paste intake form and output contract.

## Outputs

Unless the user narrows the request, produce a package containing:

1. **Executive conclusion**: scope, search cutoff, confidence, and a clear statement of what was not established.
2. **Target record**: product identity, jurisdiction, commercial parties, visual inventory, and assumptions.
3. **Search log**: exact terms, image searches, classifications, parties, databases, date range, filters, and negative-result limits.
4. **Candidate register**: publication/grant number, title, article of manufacture, applicant/assignee, inventor/designer, priority, family, current status, and source links.
5. **Drawing-based scope note**: overall silhouette, visual rhythm, proportions, transitions, supports, ends, openings, ornamentation, line conventions, and relevant specification language.
6. **View-by-view comparison matrix**: perspective, top, side, front/rear, end, installed relationship, and other material views.
7. **Separate risk conclusions**: substantive infringement, marketplace complaint, ownership uncertainty, unpublished-application, and residual prior-art risk.
8. **Design-around brief**: three structurally different directions, the high-salience relationships changed, functional trade-offs, and supplier questions.
9. **Preferred concept guidance**: multi-view concept requirements, numbered changes, and a "do not revert" list for engineering and cost-down.
10. **Second-pass search note**: new risks introduced by the selected concept and whether another iteration is needed.
11. **Attorney handoff**: evidence gaps, formal FTO questions, and the records a qualified attorney should verify.

For structured delivery, use Markdown, HTML, DOCX, or a dated evidence folder. The output is successful only when another reviewer can trace each material conclusion to evidence, inference, or assumption. Partial results must clearly identify missing views, stale records, unverified ownership, unavailable tools, and skipped searches.

## Workflow

1. **Normalize the target.** Build a target record and an image inventory. Separate product identity from seller claims and distinguish visible appearance from assumed construction.
2. **Lock scope.** Record jurisdiction, cutoff date, search languages, legal-status sources, and whether the task is pre-screening, complaint preparation, design development, or supplier diligence.
3. **Build independent search routes.** Combine full-product and local-feature image search, title and synonym search, Locarno/CPC/US classification search, applicant/assignee/inventor/designer search, portfolio and related-application search, citation-chain search, and product-family search.
4. **Validate serious candidates.** Confirm the complete drawing set, line conventions, specification, family, assignments, prosecution/status events, cited art, and relevant foreign counterparts from primary records.
5. **Explain the visual scope.** Describe the claimed ornamental arrangement as a whole. Distinguish solid-line claimed portions from broken-line or environmental portions. Compare all material views and consider prior-art crowding.
6. **Separate risk types.** Do not collapse substantive risk, marketplace complaint risk, ownership uncertainty, and unpublished-application risk into one score. Explain the evidence and uncertainty behind each.
7. **Create design-around directions.** Change several high-salience relationships together: primary architecture, silhouette, component relationship, spacing/proportion, end treatment, support/transition geometry, openings, and installed relationship. Reject cosmetic-only changes.
8. **Test feasibility.** Map each direction to function, material, process, tooling, load, cost, packaging, supplier capability, and future design-filing potential.
9. **Generate and annotate concepts.** When image generation is available, create three directions and a preferred multi-view concept. Use patent drawings as "move away from" references, not style references. Mark core changes and features that must not be restored during cost-down.
10. **Run a second-pass search.** Search the preferred architecture and its new feature vocabulary for adjacent designs and different patent families. Revise if the redesign creates a new collision.
11. **Freeze the handoff.** Deliver the evidence package, assumptions, remaining questions, supplier evidence requests, prototype gates, and attorney-review recommendation.

For the detailed procedure, read [references/workflow.md](references/workflow.md). For a concrete synthetic example, read [references/example-generic-product.md](references/example-generic-product.md).

## Risk And Evidence Rules

- Treat public-record findings as a pre-screen, not a legal conclusion.
- Cite primary patent/design-office records for publication data, drawings, ownership, prosecution, and status whenever available.
- Keep facts, inferences, and assumptions in separate columns or clearly labeled paragraphs.
- A shared concept, feature name, tube count, step count, color, or isolated cross-section is not by itself the protected design.
- A changed feature is not an automatic safe harbor; overall visual impression and prior art still matter.
- A weak, expired, challenged, or ownership-uncertain right may still create marketplace complaint cost.
- Unpublished applications, delayed updates, transfers, licenses, and incomplete supplier identities remain residual risks.
- Generated images are concept guidance, not engineering drawings, manufacturing instructions, or evidence of clearance.
- Do not expose private credentials, privileged legal advice, confidential supplier information, or unredacted customer data in a public report.

## Stopping Conditions And Error Handling

Stop or return a limited result when:

- the product cannot be uniquely identified after reasonable normalization;
- the jurisdiction is unknown and a legal-status conclusion would be misleading;
- primary records cannot be retrieved and the user requests a high-confidence legal conclusion;
- key visual views are missing and the requested conclusion depends on hidden geometry;
- a required external mutation (supplier message, platform response, repository publication, or filing) lacks explicit authorization;
- the generated concept is too similar to a serious candidate or cannot be mapped to the stated functional constraints.

When stopping, preserve the search log and explain the exact next input or verification step needed. Never fill a missing fact with a confident guess.

## Example Trigger Patterns

This skill should activate for requests such as:

- “帮我做一个实体产品的外观专利预筛，并给出三套设计规避方向。”
- “Check whether this product looks close to the cited design patents and prepare supplier questions.”
- “把这个家居产品的外观风险拆成实质侵权、平台投诉和权属风险。”

It should not activate for a pure utility-patent claim chart, a generic market-size report, or a request to copy a patented product more closely.

## Definition Of Done

The run is complete when the evidence trail, view-level comparison, separate risk conclusions, structurally distinct redesign directions, supplier/prototype handoff, and second-pass search note are all present or explicitly marked as unavailable. Validate the package structure with the Codex skill validator and run the trigger checks in [tests/trigger-cases.md](tests/trigger-cases.md).
