> **CONFIDENTIAL DRAFTS.** This repository holds working drafts. Several of
> them draw on the private library and on `wking53214/CNS`, whose NOTICE
> forbids disclosing class shapes, module layout, its evidence directory, and
> its existence as the source of shared contracts. **No draft here is cleared
> for publication as written.** Each paper carries a `REDACTION.md` naming
> exactly what must change before it leaves this repository.

# WhitePapers

Drafts, with their evidence attached.

## Papers

| paper | status | subject |
|---|---|---|
| [`papers/conversational-archaeology/`](papers/conversational-archaeology/) | **first draft** | Rebuilding a dead system from archived design conversations, and using an independently measured schema to verify the rebuild is a reconstruction rather than a fabrication. |

## House rules

These exist because the subject matter is evidence-handling, and a paper
about evidence-handling that handles its own evidence carelessly is worthless.

**1. Every figure is traceable to something runnable.** Not to a memory of a
result. Each paper's `FIGURES.md` records, per number, the command that
produces it and the file it came from. A figure whose command no longer runs
is marked stale, not quietly kept.

**2. Author-reported and independently verified figures are distinguished.**
A number measured by whoever ran the original work is not the same kind of
claim as one re-measured afterwards. Papers here mark which is which, per
figure.

**3. Uncertainty is quoted, not implied.** Small samples get intervals. A
point estimate standing alone, where n is 37, is a rhetorical device rather
than a measurement.

**4. The A/U convention, inherited from the library's own audits.** **A** for
a claim proven from a surviving artifact, **U** for one that cannot be
established. A draft that cannot separate what it recovered from what it
inferred does not go out.

**5. Redaction is a file, not a memory.** Every paper carries a
`REDACTION.md`. If a paper cannot state what in it is confidential, it is not
ready to be shown to anyone.
