# Operator Worklist — corpus cleanup before a fresh Phase 1

Date: 2026-09-17
Owner: operator (not an agent task)
Status: working document. Check items off as you go.

## What this is

Phase 1 was run to characterise the corpus. This document re-reads that same
evidence as a **work list**: what to retire, what to consolidate, what to fix,
and what must not be touched. It is derived by plain code from
`evidence/phase-1/phase1-table.json` (71 rows) and the 15 execution-triage
entries in `evidence/phase-4-triage/`.

Nothing here is a recommendation to delete. Items are sorted by how cheap the
decision is, not by how confident anyone is that the repo is disposable.

**Before starting, read §7.** Consolidation done without a ledger will
contaminate the one question this investigation still has open.

---

## 1. Empty shells (14) — cheapest decisions

Zero bytes on every ref. `409 Git Repository is empty` on commits, 0 branches,
0 tags, `main` and `master` both probed. All created 2026-09-11.

| Repo | Live counterpart, if any |
|---|---|
| `ICEBERG` | `ICEBURG` (67kb, real, note the spelling) |
| `ICEBERG-SIM` | same |
| `Anvil.clean` | `ANVIL` (77kb, real) |
| `FORTRESS1` | `fortress-kernel` (56kb, real) |
| `TBCA1` | `TBCA` (73kb, ambiguous, BROKEN) |
| `TRIAD-PLUS-42` | `Triad-42` (123kb, 105/105 tests pass) |
| `GSA-2` | `GSA` / `GSA-815` / `GSA-GOVERNANCE-CORE` |
| `GSA-GATEWAY1` | same, and see `VANGUARD` in §2 |
| `GOVERNANCE-CONTROL-PLANE` | `Governance_Gateway` (45/45 tests pass) |
| `GLCM1` | none found |
| `TAKEOUT1` | none found |
| `RADAR` | none found |
| `STRIDE` | none found |
| `VSA` | dossier exists inside `Gemini_Extraction` |

**Carry the naming convention forward before deleting.** Five of these use the
`1` suffix (`FORTRESS1`, `GSA-GATEWAY1`, `TAKEOUT1`, `TBCA1`, `GLCM1`), which
operator testimony T1 in `evidence/phase-1/operator-decisions.json` records as
a deliberate convention. That testimony is the only thing preserving the
meaning of the suffix. If these repos go, T1 becomes the sole record, so do not
also let T1 go.

`ICEBURG` vs `ICEBERG`: the misspelled one is the real, populated repo. Worth
deciding the canonical spelling now, because the `C(0)` thread, the recovery
archives, and several PROVENANCE files all refer to "Iceberg" in prose.

---

## 2. Self-declared retired

| Repo | Evidence |
|---|---|
| `VANGUARD` | `.ghost_archive` on main reads **"Retired: content folded into GSA-GATEWAY. Kept as a record."** Default-branch payload is a 46-line stub, zero imports, six undefined names, one file collapsed to a single unparseable line. Phase 1's Opus verifier overturned the inspector's SUBSTANTIVE_SYSTEM label to SPECIMEN_OR_DATA_CORPUS. |

This one already tells you what it is. The only question is whether "kept as a
record" still needs its own repo.

---

## 3. Consolidation candidates, by signal

Repos carrying `DUPLICATED` or `SUPERSEDED` state signals from Phase 1
inspection. These are where merging is most likely to pay off.

**DUPLICATED:** `GEMS`, `GSA-GOVERNANCE-CORE`, `OBSERVE`, `TOUCHSTONE`,
`innovation_os`, `synapsis`, `ARCHIVE`, `CITADEL`, `CODE`, `Claude_History`,
`CoPilot_History`, `Data_files`, `EDDP`, `Gemini_History`

**SUPERSEDED:** `TOUCHSTONE`, `VANGUARD`, `content-polish-pipeline`,
`synapsis`, `ARCHIVE`, `CODE`, `Data_files`, `Gemini_History`,
`GSA-Master-Kernel`

Two specific observations from execution triage:

- `content-polish-pipeline` is marked SUPERSEDED, and `ghost_tools` already
  carries a **vendored copy** of its "polish" quality gate. The dependency
  direction is already established.
- `GEMS` carries a second, explicitly unwired implementation in `transport/`
  (the `gems_transport` package). Two implementations, one unreferenced.

The largest repos by size are also the most likely to hide duplication:
`Claude_History` (149MB), `ChatGPT_History` (92MB), `Gemini_Extraction` (65MB),
`WhitePapers` (21MB, see §6), `Ecology` (19MB), `synapsis` (15MB),
`Data_files` (11MB), `EDDP` (10MB), `CoPilot_History` (11MB).

---

## 4. Do not delete: the evidentiary substrate

These are the source material for provenance claims made by other repos. At
least twelve repos state in their own `PROVENANCE.md` that they were
reconstructed by mining these archives after an original was lost: `AC-HCCSE`,
`DGK`, `HTTP`, `ICEBURG`, `PERCEIVE`, `SAGE-K`, `ZTS`, `ZTGKT`, `UTEP`, `GEMS`,
`ATS`, `GSA`.

| Repo | Why it must survive |
|---|---|
| `Gemini_Extraction` | 30.7MB byte-preserved export with recorded SHA-256, plus derived evidence/chronology ledgers and 8 per-system dossiers |
| `ChatGPT_History` | raw export plus a **re-runnable extraction pipeline with credential and phrase redaction** |
| `Claude_History`, `CoPilot_History`, `Gemini_History` | cited as provenance by multiple reconstructions |
| `ARCHIVE`, `CITADEL`, `CODE`, `Data_files`, `EDDP` | transcripts plus verbatim-extracted code payloads; Phase 1 verifiers explicitly ruled these must stay in scope |
| `TOUCHSTONE` | answer-key corpus, 26/26 manifest claims verified intact by execution |
| `GSA-Master-Kernel`, `KAGGLE` | held open as AMBIGUOUS by operator decision §9.B pending a read of their unread files, not yet performed |

Prefer **archive** over **delete** for anything in this section. Archiving is
reversible; GitHub deletion mostly is not.

---

## 5. Concrete fixes found by running the code

These are not inferences from READMEs. Each was produced by executing the repo.
All 15 triage entries are in `evidence/phase-4-triage/`.

### Broken as committed

| Repo | Item |
|---|---|
| `composition-engine` | `src/cns/gate.py` **was never committed**. `pytest` cannot collect at all (`ModuleNotFoundError: No module named 'cns.gate'`), so the README's "All 21 tests passing" is false as committed. Separately, `SwizzleAdapter.invoke()` and `GhostToolsAdapter.invoke()` return the constant strings `"escaped"` and `"reasoned"` for **every** input including `None`. No packaging manifest of any kind. |
| `GRAPH` | Phase 1 state signals: PARTIALLY IMPLEMENTED, UNTESTED, **BROKEN**, EXPERIMENTAL. Not execution-triaged. |

### Documentation drift (code is fine, docs are stale)

This pattern recurred in at least seven repos. In every case the code was
better than the documentation claimed.

| Repo | Drift |
|---|---|
| `sentinel_os` | README **badly understates** the repo: actual 967 passed, 22 skipped, 0 failed |
| `SWIZZLE` | README header says v0.4.0, installed version is 0.7.1. Three conflicting test counts on record (343, 109, 661); actual is **788 passing** |
| `ghost_tools` | README says v1.5.0, only git tag is v1.6.0, pyproject and CHANGELOG say 1.7.0 |
| `HERALD` | README claims 312 tests; actual is **365 passing** |
| `Triad-42` | README is a stale snapshot predating the last upgrade round; `ENHANCEMENT_REJECTION.md` is the accurate document |
| `GSA-815` | README "Running it" section never mentions the `PYTHONPATH` / vendor-path requirement that `api_server_resilient.py` needs. Also no Dockerfile despite deployment framing |
| `observe-perceive` | test count moves 580 → 676 only once the full 7-package chain resolves |

### Unsupported claims to retract

| Repo | Item |
|---|---|
| `Governance_Gateway` | The "105 attacks / 5 exposed issues / supports a white paper" claim has **zero supporting evidence anywhere in the repo**. The adversarial test file contains 25 executable cases after parametrize expansion. The 45 tests that do exist are real and pass. Retract the 105 claim; keep the component. |
| `innovation_os` | 309/309 tests pass but `Perceiver.perceive()` is a confirmed pass-through stub, the MVP demo is scripted around a near-no-op pipeline, and the one real logic module (`IdeationEngine`) is disconnected from everything. 351 files, 13,528 lines, 86 files under 10 lines, under 65 version tags. Do not include in any "N for N working systems" summary. |

### Small real defects

| Repo | Item |
|---|---|
| `Ecology` | 2 failing tests, a genuine provenance-ledger drift. Fix is to rerun `scripts/corpus_origin.py` |
| `CCC` | a malformed `epistemic_status` raises an unhandled `AttributeError`; a clear `TypeError` would be better. Robustness only, it fails loudly rather than silently |
| `HERALD` | `herald/gate.py` `submit()` checks only `claim.confidence >= threshold`. `claim.opacity_flags` is read only for the human-facing log string, never for admission |
| `ghost_tools` | SWIZZLE named **0 of 10** disguised defects, roughly half of those gaps undisclosed in ghost_tools' own docs. Each escape was control-verified. See `evidence/phase-4-triage/swizzle.json` |

---

## 6. Outstanding from earlier in this session

- `WhitePapers`: `papers/co-v-co2-test/co.v.co2.test.md` is 88,219,384 bytes, of
  which line 553 alone is 80,111,004 bytes: an incidentally captured raw
  ChatGPT export containing 863 distinct `conversation_id`s. The repo was made
  private, which contains it. **The file is still in git history on `main`.**
  Purging it requires `git filter-repo` plus a force push and has not been
  done. This is the single largest item in the repo by an order of magnitude.

---

## 7. The consolidation ledger — read before merging anything

Merging repos and extracting shared code into common packages **creates new
instances of H2 (common lineage) and H3 (canonicalization)**, dated September
2026. A fresh Phase 1 would observe the resulting shared contracts and have no
way to distinguish them from structures that arose organically.

This is not hypothetical. It is structurally identical to the `cns.caller`
extraction analysed in `papers/c-0/c-0-.md` §45, which is currently the
strongest evidence *against* `C(0)`. And it has already happened once without
being recorded: Phase 1 observed that 34 of 71 repos were created on
2026-09-11/12 carrying `claude/*-repo-recreation-*` branches, and could only
flag it as an unverified inference.

**Keep a ledger as you work.** For each move: what moved, from where, to where,
when, and why. Then a fresh Phase 1's structural findings can be netted against
deliberate moves rather than confounded by them.

The habit already exists in this corpus. `TIE`'s `recovery/DECISION_LEDGER.md`
and `recovery/ARTIFACT_PROVENANCE.md`, and the `PROVENANCE.md` convention used
across the reconstructed repos, are the same discipline. Apply it to yourself.

---

## 8. Re-running Phase 1 afterwards

Phase 1 cost one phase against a 71-repo corpus. A post-cleanup corpus will be
smaller, so a fresh run should be cheaper and will produce a cleaner baseline.

Two things to preserve across the re-run:

1. **The current Phase 1 record is a dated snapshot, not a stale artifact.**
   Keep it. The delta between old and new Phase 1 is itself evidence about what
   consolidation did, and is the check on §7.
2. **The 15 execution-triage entries record `head_sha` at time of test.** If you
   change those repos, the SHAs move and the entries stop describing the current
   state. That is expected and fine. Do not edit them to match; they are dated
   observations.
