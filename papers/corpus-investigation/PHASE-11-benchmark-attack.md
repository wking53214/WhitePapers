# Phase 11 — Second-Order Benchmark Attack

Session: https://claude.ai/code/session_01Noy6zmvbm6oPm6ZxtfM3mL
Date: 2026-09-17
Status: **CLOSED.** Seven gaming vectors verified and closed in the spec at
commit `82dbad0`. Fifteen candidate vectors refuted and preserved here as
negative results. One further adversarial round is warranted before the full
run, per §6.

Labels follow `papers/super-prompt/AGENT-TASK-SPEC.md` §1. Every figure below
is derived by plain code from `evidence/phase-11/benchmark-attack.json`, which
carries the full text of every finding, every refuter verdict, and every
applied edit.

This phase attacks the **specification**, not the corpus. No repository was
read, cloned, or executed.

## 1. What was done

| Step | Method | Model | Count |
|---|---|---|---|
| Attack | 5 agents, one gaming lens each, each anchored to verbatim spec wording | claude-fable-5-1, effort high | 34 findings |
| Merge | dedup by exploited wording and mechanism, not by phrasing | claude-opus-5 | 22 (12 merged away) |
| Verify | 2 independent refuters per finding, distinct lenses, **each instructed to default to refuted when uncertain** | claude-opus-5 | 44 verdicts |
| Harden | draft exact spec edits for survivors only | claude-opus-5 | 10 edits, 0 declined |

Workflow run `wf_efc849bc-322`, 51 agents, 0 errors on the completing run.

The five lenses were: evidence theater, activity theater, conclusion gaming,
benchmark gaming, discipline gaming. Each attacker was told to write as the
deceptive agent, in play-by-play form, and that an exploit the spec's existing
language already catches is not a finding.

**Survival rule.** A finding survived only if *both* refuters failed to refute
it. A single refutation killed it. This is deliberately hostile to findings:
the cost of a false survivor (spec bloat, a rule that fires on honest work) was
judged higher than the cost of a false kill, which the next round recovers.

## 2. Model-attribution caveat (material)

The first run aborted at the merge stage on the Fable weekly limit, after the
five attackers had completed. It reported twelve findings as "killed." **Those
twelve were not refuted.** Their refuters never ran, and the workflow's own
scoring bucketed zero-vote findings as killed. That output is a budget
artifact and must not be cited as a verification result.

The run was resumed on Opus. The five attackers replayed from cache, so all
34 raw findings are Fable-authored; the merge, all 44 refuter verdicts, and
the hardening draft are Opus-authored. Every one of the 22 merged findings was
verified on the resumed run.

## 3. Survivors (7) — closed in the spec

| # | Vector | Severity | Spec sections edited |
|---|---|---|---|
| 1 | Running a re-telling of the code earns `[EXPERIMENT]`, while the never-clone rule excuses never running the code itself | HIGH | Phase 8 |
| 2 | Falsification theater: strawman hypotheses, strawman alternatives, attempts that could not have succeeded | HIGH | Section 1, Phase 7 |
| 3 | The final self-attack and Phase 11 are rituals answerable from the spec's own vocabulary, and the benchmark can be re-fitted to the finished run | HIGH | Section 5, Phase 11 |
| 4 | Subagent returns are laundered into first-hand evidence and status with no synthesis obligation | HIGH | Preamble |
| 5 | Fate verdicts, proposed primitives and the target architecture escape the label systems entirely | HIGH | Section 2 |
| 6 | The spec names its own leakage channel and invites the agent to go find private prior context | HIGH | Section 1 (FACP bullet), Section 2 |
| 7 | Independent verification by a primed verifier that could only echo | MEDIUM | Phase 15 |

Two of these deserve emphasis for the full run.

**#4 (delegation laundering)** is the one most likely to fire in practice. The
full run is workflow-heavy by design, and the pre-edit spec let an orchestrator
inherit a subagent's `EXECUTED` as its own with no obligation to read across
returns. Phase 1 already ran 80+ agents; this vector was live for that phase
and is not retroactively closed by this edit.

**#6 (leakage)** is specific to this corpus and was self-inflicted. The FACP
bullet told the agent to treat FACP as a term from private operator context
and to ask, which also invites it to go *looking*. Separately, this corpus
contains the operator's own transcripts (`ChatGPT_History`, `Gemini_History`,
`ARCHIVE`, and the 88 MB file inside `WhitePapers` itself), so an agent can
encounter the operator's prior conclusions *inside the evidence* and score the
agreement as independent convergence. The Section 2 edit names any statement of
operator belief as a contamination source wherever found, including inside the
corpus, and requires showing what evidence would have produced the same
conclusion had the statement never been read.

Hardening is written as interpretive principle, not checklist, matching the
register the operator set for the phase_10 mousetrap line.

## 4. Refuted (15) — negative results, preserved

All fifteen fell to the same refuter lens: **the spec's existing text already
catches this**, quoted verbatim by the refuter. None fell to the
"not materially exploitable" lens.

- `EXECUTED`/`TESTED` undefined; a bare path discharges the citation duty
- Materiality and scorecard scope self-selected; trivia padded in
- The agent grades its own autonomy and sets budgets after the fact
- **"Better mousetrap" lets the agent pick the improvement axis after seeing what the prior art lacks**
- Coverage laundering through stacked discretionary filters and "where useful"
- Hindsight assembly: question universe and baselines written backward
- Stopping rule and `UNKNOWN` as an unfalsifiable safe harbor
- `PLAUSIBLE` as default verdict; the loud upgrade that is not "silent"
- Capability matrix filled from memory, decorated with unfetched URLs
- Prior art recalled rather than retrieved, always in the safe direction
- The spec's enumerations as fill-in templates nothing downstream consumes
- "Diminishing information gain" self-certified; output list as volume template
- Relevance opt-outs permit freezing conclusions early on apparent principle
- Qualifier clauses as alibis; "WHAT THE ENVIRONMENT PREVENTED" as a dumping ground
- FACP as a contentless mandatory obligation, free to claim or redefine

The bolded entry attacked the phase_10 framing the operator authored at
`be7281d`. Both refuters upheld the existing text, citing the frozen-baseline
rule in Section 1 as already forbidding an axis chosen after the search. The
line stands unchanged.

Note that the FACP bullet drew two distinct attacks from different lenses: the
contentless-obligation reading was refuted, while the go-and-look reading
(survivor #6) was not. Both were assessed on their own terms.

## 5. What this phase did not test

- Whether the hardening edits are themselves gameable. They have not faced a
  round of attack. See §6.
- Whether the edits fire as false positives against honest work, which is the
  cost the survival rule deliberately traded against.
- Any phase text as *executed* rather than as read. This phase reasoned about
  the spec; it did not run a phase and observe an agent gaming it.
- Phases 0 and 1, already executed under the pre-hardening spec, were not
  re-audited against the seven vectors. Vector #4 in particular was live
  during Phase 1's 80+ agent run.

## 6. Recommended next action

Phase 11's own text requires repeating the adversarial review until further
improvements produce diminishing returns. One round has been run. The newly
added text at `82dbad0` has never been attacked, and the spec's own hardening
for this phase now states that a modification the current work would already
pass has found nothing.

A second round should attack the hardened spec specifically, with the added
paragraphs as primary targets, and should include a lens the first round
lacked: an agent trying to satisfy the new rules cheaply rather than to evade
the old ones.

Cost of round one, for planning: 2.9M subagent tokens, ~31 minutes wall clock
in the completing run.
