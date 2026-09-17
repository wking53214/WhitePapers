# Phase 1 — Corpus Discovery

Session: https://claude.ai/code/session_01Noy6zmvbm6oPm6ZxtfM3mL
Date: 2026-09-16
Status: **CLOSED WITH RECORDED GAPS.** Every repository is enumerated,
inspected, and verified by at least one adversarial agent. The completeness
critic found material gaps (§6) that are carried into Phase 4 scoping rather
than hidden. Phase 1 stops here for operator triage, as agreed.

Labels follow `papers/super-prompt/AGENT-TASK-SPEC.md` §1. Every figure below
is derived by plain code from the JSON files in `evidence/phase-1/`; the
master row set is `evidence/phase-1/phase1-table.json`.

## 1. What was done

| Step | Method | Model | Evidence file |
|---|---|---|---|
| Enumeration A | `Claude_Code_Remote.list_repos`, limit 200, `has_more:false` | n/a (tool) | `corpus-enumeration.raw.json` |
| Enumeration B | GitHub Search API `user:wking53214`, `total_count:71`, `incomplete_results:false` | n/a (tool) | `corpus-enumeration.github-search.json` |
| Attachment | `add_repo` read access for 69 private repos; `sentinel_os` (public) attached with credentials after its first inspection failed for lack of attachment | n/a | `repo-attachment.json` |
| Inspection | one read-only agent per repo, GitHub API only, no clones; root tree, every branch, README/NOTICE/PROVENANCE, manifests, tests, CI, commits (main), tags, cross-repo mentions | claude-fable-5-1, xhigh (ultracode) | `inspections-and-verdicts.partial-run3.json`, `targeted-verify.run4.json` (sentinel_os) |
| Verification, REFUTE lens | independent agent re-fetches ≥3 cited sources, tries to overturn the classification | claude-fable-5-1 (27 repos); claude-opus-5 (29 repos) | same files; `refute-eligible.opus.json`; `refute-sentinel_os.opus.json` |
| Verification, COST_OF_EXCLUSION lens | for every EMPTY / EXCLUDED / AMBIGUOUS row: what would sidelining lose; empties re-probed on every ref | claude-fable-5-1 (28 repos) | same files |
| Completeness critic | audits the merged table only, no GitHub calls | claude-opus-5 | `critic.opus.json` |
| RUN-B reconciliation | plain code, outside all agent prompts | n/a | `runb-reconciliation.json` |

Agents never received `OPERATOR-BRIEF.md`, RUN-B, or the `C(0)` state
(see `PHASE-0-capability-reconnaissance.md` §5).

## 2. Corpus

Both enumerations agree exactly: **71 repositories**, 0 archived, 0 forks,
69 private, 2 public (`WhitePapers`, `sentinel_os`). 37 were created before
2026-09-11; **34 were created on 2026-09-11/12**, and many of those carry
`claude/*-repo-recreation-*` branches, so the corpus as it stands is
substantially a product of sessions in the days before this investigation
[INFERENCE from branch names and creation dates; not yet verified].

## 3. Classification (inspector labels, after verification)

| Eligibility | Count | Repos |
|---|---|---|
| ELIGIBLE | 43 | 39 substantive systems, 3 docs/papers (`ARLF`, `SOONG_protocol`, `WhitePapers`), 1 specimen corpus (`TOUCHSTONE`) |
| AMBIGUOUS_INVESTIGATE (mixed transcripts + tooling) | 12, **14 pending §9.B** | `ARCHIVE`, `ChatGPT_History`, `CITADEL`, `Claude_History`, `CODE`, `CoPilot_History`, `Data_files`, `Ecology`, `EDDP`, `Gemini_Extraction`, `Gemini_History`, `TBCA` — plus `GSA-Master-Kernel` and `KAGGLE`, held here provisionally, see below |
| EMPTY (no content on any ref; 409 "Git Repository is empty" on commits, 0 branches, 0 tags; `main` and `master` both probed) | 14 | `Anvil.clean`, `FORTRESS1`, `GLCM1`, `GOVERNANCE-CONTROL-PLANE`, `GSA-2`, `GSA-GATEWAY1`, `ICEBERG`, `ICEBERG-SIM`, `RADAR`, `STRIDE`, `TAKEOUT1`, `TBCA1`, `TRIAD-PLUS-42`, `VSA` |
| EXCLUDED_CONVERSATION_ARCHIVE | 0 as-agent-recorded, 2 pending | The agent record (inspection + verifier) classified `GSA-Master-Kernel` and `KAGGLE` `EXCLUDED_CONVERSATION_ARCHIVE`. Operator decision §9.B holds both open as `AMBIGUOUS_INVESTIGATE` pending a read of their unread transcript/artifact files, so neither is dropped from scope by a later phase before that read happens. See `evidence/phase-1/operator-decisions.json`. |

Access: 71/71 OK after the `sentinel_os` re-inspection.

## 4. Verification outcome

84 verdicts over 71 rows (56 REFUTE, 28 COST_OF_EXCLUSION; 55 by Fable 5.1,
29 by Opus 5). 67 rows AGREED. Four rows did not:

| Repo | Status | What the verifier found | Recommended label (critic's judgement, for operator decision) |
|---|---|---|---|
| `ARCHIVE` | CONTESTED (REFUTE upheld, COST_OF_EXCLUSION overturned; both Fable) | No tooling exists anywhere in the repo, so "MIXED" is a rule misapplication; it is one Gemini transcript plus verbatim-extracted, unrepaired code payloads, i.e. a specimen. Both verifiers agree it must stay in scope. | `SPECIMEN_OR_DATA_CORPUS` / `ELIGIBLE`, keep CONTESTED flag |
| `ARLF` | CORRECTED (Fable REFUTE) | The non-default branch `claude/arlf-repo-recreation-68ldf3` carries a runnable dependency-free Python reference implementation (8 modules) and 5 test modules; the inspector saw only `main` (docs only). Eligibility unchanged. | `ELIGIBLE`; purpose stays DOCS_OR_PAPERS on `main` but the row must record the branch content; `tests_dir=false` is wrong at repo level |
| `VANGUARD` | CORRECTED (Opus REFUTE) | The whole default-branch payload is a 46-line stub with zero imports and six undefined names, plus one file collapsed to a single unparseable line; `.ghost_archive` reads "Retired: content folded into GSA-GATEWAY. Kept as a record." The inspector's own state signals (BROKEN, SUPERSEDED) contradict its SUBSTANTIVE_SYSTEM label. | `SPECIMEN_OR_DATA_CORPUS` / `ELIGIBLE`, confidence MEDIUM |
| `WhitePapers` | CORRECTED (Opus REFUTE, confidence only) | 88,219,384 of ~88.5 MB is one unread file, `papers/co-v-co2-test/co.v.co2.test.md`; the branch SHA cited had moved (this investigation's own commits); `papers/corpus-investigation/` exists only on the working branch. Labels stand. | `DOCS_OR_PAPERS` / `ELIGIBLE`, confidence MEDIUM until the 88 MB file is characterised |

Repo-level facts that surfaced during verification and matter downstream:
`sentinel_os/governance_loop_guard.py` states in code that it was "salvaged
from the STRIDE repo (stride-formatted-audited.py) before its deletion from
GitHub, 2026-08-20", an in-repo explanation for `STRIDE` being empty
[INSPECTED by the Opus verifier]. `sentinel_os` is the largest system by
history (284 commits, ~60 test files, CI, 8 branches, pins `CNS`,
`Conservation_Kernel`, `DIT` by commit SHA in `requirements.txt`).

## 5. Name-collision groups

All 17 groups remain **OPEN** after Phase 1. Phase 1 could establish only
in-repo statements (author claims) and empties; it could not establish
lineage. The best-evidenced edges, all still author claims pending Phase 4
checks: `CODE` → `content-polish-pipeline` (bidirectional PROVENANCE),
`synapsis` → `Ecology` (salvage claim plus an unopened
`corpus/synapsis-master.zip`, 18.2 MB), `Data_files` → `EDDP` (claimed shared
commit `6dd34d3`), `GSA-815` → `GSA-Master-Kernel` (split-out claim on both
sides), `AUGUR` renamed from a "FORTRESS" (which one is not established),
`VANGUARD` "folded into GSA-GATEWAY" while `GSA-GATEWAY1` is empty and
`TOUCHSTONE` claims to be the renamed `GSA-GATEWAY`. Full per-group notes:
`critic.opus.json`.

## 6. Gaps the critic found (verbatim severity; full text in `critic.opus.json`)

HIGH:
1. **Commit counts are main-branch only but labelled EXACT.** Proven wrong for
   `ARLF` (7 on a non-default branch vs 6 recorded). Any chronology built on
   this column is unsafe. The rebuilt table names the field
   `commit_count_main` for this reason.
2. **Both exclusions rest on unread files and a single lens.**
   `GSA-Master-Kernel`'s 178 KB transcript and 15 `.py` artifacts were never
   opened; its exclusion is MEDIUM confidence from README/PROVENANCE claims.
   `KAGGLE`'s `claude/*` branches were never listed.
3. **Substantive rows holding unread conversation material** at the exact
   MIXED boundary: `Resume_OS` (a 1.02 MB transcript), `innovation_os`,
   `SAGE-K`, `Ecology`, `OBSERVE`, `CCC`, `GSA`.
4. **One 88.2 MB unread file** in `WhitePapers`, the repo hosting this
   investigation.
5. **Non-default branches not enumerated in 16 repos**; per-row booleans are
   main-only and demonstrably wrong at repo level (`ARLF`, `PERCEIVE` whose
   `main` is empty, `wizzle`).
6. **Purposes rest on author claims never executed or cross-checked**; 35 of
   71 rows say tests/behaviour were not executed. The whole "reconstructed
   from transcript" family (`AC-HCCSE`, `ICEBURG`, `DGK`, `TIE`, `UTEP`,
   `ZTGKT`, `URE`, `SAGE-K`, `HTTP`, `PERCEIVE`) cites transcript line
   numbers in the history repos that nobody followed.
7. **Five empty repos are named inside other repos' content** (`VSA` by seven
   repos, `STRIDE` by five, `GSA-GATEWAY1`/`GSA-GATEWAY`, `ICEBERG`, `RADAR`)
   and Phase 1 recorded the mentions without locating the referenced material.

MEDIUM: 13 rows have `created_at` before their first commit (history-rewrite
signal untested); description-vs-observed discrepancies recorded then dropped
(`GSA-815`'s "governance architecture" description vs an observed Twilio IVR
call-center app); "is this token the corpus repo of that name?" recurs in 12
rows and is the load-bearing question for every lineage hypothesis; PII
state unknown in the six history repos; MIXED_AMBIGUOUS applied inconsistently
(`ARCHIVE` with no tooling vs `Resume_OS`/`innovation_os` with transcripts
labelled substantive); no row was verified by two different models.

## 7. RUN-B, reconciled outside the agents

All 22 repos RUN-B named still exist by exact name. RUN-B counted 27; today
there are 71, of which 34 post-date RUN-B's likely window. At least 10 of the
37 pre-batch repos were absent from RUN-B's count (INFERENCE; RUN-B's date is
UNKNOWN). RUN-B said "public corpus"; today 2 repos are public.
`runb-reconciliation.json`.

## 8. Process record

- Runs: 4 resumptions of the main workflow (usage-limit stops at 05:00,
  13:30, 18:30, 23:30 UTC), 1 targeted Fable run, 2 Opus refuter runs, 1
  Opus critic. Subagent tokens, approximate: Fable 10.3M, Opus 2.7M.
- The first real capacity ceiling hit was **Fable's weekly pool**, not
  context, agent caps, or disk. Verification of 29 rows and the critic moved
  to Opus 5 for that reason; every verdict carries its model.
- Defect found and closed mid-phase: the merged super-prompt would have
  handed RUN-B and `C(0)` to agents; split into agent spec and operator
  brief before any agent could receive it (Phase 0 §5).
- Defect found by the critic and fixed in this record: the first table
  truncated fields and conflated "contested" with "corrected"; the rebuilt
  `phase1-table.json` is full-fidelity and splits the status.
- No repository was cloned, modified, or pushed to during Phase 1.

## 9. Operator decisions before Phase 4

Operating principle applied below, per operator instruction 2026-09-17:
prefer whichever option keeps the most paths open, and weight downstream
consequences above short-term cost or convenience. A closed decision is
expensive to reopen; an open one costs only patience.

A. **Accepted.** The four relabels in §4 close no options — none changes an
   eligibility verdict, all only correct purpose/confidence to match observed
   content. Leaving the old labels in place would be the option-reducing
   choice, since Phase 4 scoping will read whatever label is on record.

B. **Approved, with the two exclusions held open in the interim rather than
   left closed while queued for later.** `GSA-Master-Kernel` and `KAGGLE`
   are reclassified `AMBIGUOUS_INVESTIGATE` (provisional, not a finding) so
   that no downstream phase can read `EXCLUDED` and drop them from scope
   before their cited files are actually read. Revert to `EXCLUDED` or
   confirm `AMBIGUOUS_INVESTIGATE`/`ELIGIBLE` only after that read. P0 order
   stands: the two exclusions and the 88 MB `WhitePapers` file first (both
   bear on whether the corpus boundary and this investigation's own record
   are trustworthy), then the MIXED-boundary repos, then GSA-GATEWAY lineage
   and all-ref commit histories.

C. **Reversed from the prior answer.** The 14 empties are recorded as
   `EMPTY`, fate undetermined, with no suggested disposition attached. The
   earlier "ELIMINATE-candidate" framing was itself a small act of the thing
   this investigation exists to prevent: attaching a fate suggestion ahead
   of the evidence, the same failure this project already flagged in RUN-B's
   fate list. Fate is a Phase 16 output, decided from whatever accumulates
   by then, including patterns like the `sentinel_os` → `STRIDE`
   salvage-then-delete trail, which could make some of these fourteen
   informative rather than disposable.

D. **Elevated from "decide the split" to "design the split to preserve the
   model-attribution question."** Running Phase 4 single-model to save
   budget forecloses, permanently and cheaply, one of the three questions
   this whole project exists to answer (how much of any finding is the
   model versus the harness). That option cannot be recovered after the
   fact. Phase 4 should therefore budget a small, deliberate dual-model
   overlap — the same handful of repos run on both Fable and Opus on
   purpose, tagged accordingly — rather than treating cross-model
   verification as leftover budget, which is where the critic's P3 list had
   filed it.
