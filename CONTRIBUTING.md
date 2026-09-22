# Contributing

Contributions are welcome for public-record research guidance, generic product examples, supplier handoff checklists, synthetic tests, documentation, and release validation.

## Before opening an issue or pull request

1. Use a generic or fully sanitized product example.
2. Remove unpublished design files, client names, supplier records, attorney material, and private absolute paths.
3. State the jurisdiction, cutoff date, evidence sources, expected result, and remaining uncertainty.
4. Explain the validation performed and distinguish factual corrections from legal interpretation.

## Pull requests

Keep changes focused and run:

```bash
python -m unittest discover -s tests -v
```

Do not add language that presents this Skill as FTO clearance, legal advice, an infringement opinion, or a substitute for counsel. Do not add hidden prompts, telemetry, callbacks, or private case data.

## Releases

Signed release metadata is maintained by the publisher. Do not hand-edit the public manifest or provenance signature in a feature pull request.
