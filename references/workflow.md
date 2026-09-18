# Generic Physical-Product Workflow

This reference turns the entry-point rules into a repeatable operating procedure. It is intentionally product-agnostic: adapt the feature vocabulary and evidence sources to the target category.

## 1. Target Record

Create one record before searching:

```text
Target ID:
Product / model / SKU:
Product category and use:
Target jurisdiction(s):
Search cutoff:
Brand / seller / legal entity:
Supplier / factory / designer / suspected rights holder:
Product family or variants:
Available views:
Must-keep functions:
Changeable and non-changeable structures:
Evidence gaps:
```

Do not merge multiple variants into one target. Record whether an image shows the product itself, a render, an installation context, or a copied listing image.

## 2. Visual Feature Vocabulary

Describe appearance without assuming legal scope. Useful buckets include:

- primary body: tube, plate, shell, box, lattice, segmented rail, capsule, or hybrid;
- silhouette: straight, tapered, stepped, bowed, faceted, asymmetrical, or interrupted;
- component relationship: integrated, suspended, cantilevered, nested, overlapping, or modular;
- proportions: length-to-height, spacing, offset, front/rear balance, and symmetry;
- transitions: returns, chamfers, radii, folds, gussets, bridges, and connectors;
- voids and openings: slots, windows, recesses, cut-outs, and their rhythm;
- surface ornamentation: ribs, bands, perforation, texture, seams, and badges;
- installed relationship: wrap, clearance, mounting points, host-product silhouette, and visible gap.

Use neutral descriptions such as “two offset recessed tread pockets” instead of conclusions such as “the patent protects two steps.”

## 3. Search Matrix

Run at least three independent routes when sources permit:

| Route | Example query | Purpose |
| --- | --- | --- |
| Product text | product category + synonym + jurisdiction | Find candidate records and related products |
| Image / local feature | full product, end detail, connector, opening pattern | Find visually similar records that use different terminology |
| Classification | Locarno, CPC, US class, national design class | Reduce dependence on product naming |
| Rights holder | applicant, assignee, inventor, designer, supplier, factory | Expand beyond the visible seller |
| Portfolio | related applications, family, continuation, division, other sizes | Understand design strategy and claim context |
| Citation / prior art | cited references and independently found earlier designs | Assess crowdedness and scope-narrowing context |
| Product family | other models, vehicles, sizes, markets, archived pages | Identify repeated architecture and earliest disclosure |

Log search terms, filters, date ranges, sources, and negative results. A negative search result is a limit on evidence, not proof of absence.

## 4. Candidate Validation

For every serious candidate, capture:

1. publication, application, grant, and priority identifiers;
2. title and article of manufacture;
3. applicant, inventor/designer, assignee, assignments, and related entities;
4. all drawing sheets and figure descriptions;
5. solid-line, broken-line, boundary-line, shading, and color conventions;
6. family members, foreign priorities, continuations, divisionals, and related filings;
7. cited prior art and non-patent literature;
8. prosecution, cancellation, expiration, reexamination, or other status events;
9. source URLs and retrieval dates.

Use aggregators to discover candidates, but use official records for any high-stakes fact. When a record is unavailable, mark the field “not verified.”

## 5. Drawing-Based Scope Explanation

Use this order in the report:

1. **Claimed versus environmental portions**: state what appears in solid line, broken line, boundary line, or disclaimer language.
2. **Overall impression**: describe silhouette, visual rhythm, proportion, and the relationship among major components.
3. **View map**: explain what perspective, top, side, front/rear, and end views add or rule out.
4. **Crowdedness**: identify earlier designs that make a feature less distinctive without predicting a legal result.
5. **Comparison**: map similarities and differences to the target product across all material views.

Avoid isolated-feature shortcuts. A changed cross-section, slot count, color, or logo is only one data point in the overall visual comparison.

## 6. Risk Register

Keep separate rows for:

- substantive infringement risk;
- marketplace complaint and takedown risk;
- ownership, license, and supplier-chain uncertainty;
- unpublished-application or delayed-publication risk;
- prior-art and validity uncertainty;
- operational risk if engineering restores avoided features.

For each row, write evidence, inference, confidence, open questions, and next action. Prefer labels such as low / medium / high with rationale over an unexplained composite score.

## 7. Design-Around Matrix

Build a matrix before drawing concepts:

| Salience category | Current / candidate arrangement | Preferred redesign move | Function retained? | Manufacturing impact |
| --- | --- | --- | --- | --- |
| Primary architecture |  |  |  |  |
| Component relationship |  |  |  |  |
| Proportion and spacing |  |  |  |  |
| End and transition geometry |  |  |  |  |
| Openings / tread / recesses |  |  |  |  |
| Installed silhouette |  |  |  |  |

Each direction should change several high-salience rows together. Do not call a cosmetic-only variant a design-around.

## 8. Concept And Prototype Gates

For each direction, record:

- the visual relationships intentionally changed;
- what function, strength, fitment, or user experience is retained;
- materials, process, tooling, and supplier capability assumptions;
- the parts that must not be restored during cost-down;
- the view set needed for a second-pass search;
- prototype measurements or user tests that could invalidate the direction.

If image generation is used, request perspective, top, side or installed, and end views. Inspect text, arrows, view consistency, and accidental reintroduction of avoided features.

## 9. Second-Pass Search

Search the preferred design using its new vocabulary, not the original product name alone. Include newly introduced architectures such as plate-style, integrated recess, cantilevered module, segmented rail, capsule, blade, or other relevant forms. Reopen the design-around matrix when a new serious candidate appears.

## 10. Evidence Package

Freeze a dated package containing:

- the final report;
- search log and query list;
- official patent/design records and complete drawings;
- assignment and legal-status records;
- source URLs and retrieval dates;
- comparison boards and generated prompts;
- preferred concept and annotated “do not revert” list;
- supplier evidence requests;
- attorney-review questions;
- a short list of unverified assumptions.
