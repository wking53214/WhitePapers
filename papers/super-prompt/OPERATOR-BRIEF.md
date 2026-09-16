# Operator Brief — Corpus Investigation (github.com/wking53214)

**NEVER give this file, or any excerpt of it, to an agent, subagent, or
workflow that performs a phase.** It exists for the human operator and for
the main-loop orchestrator only. It holds the operating preferences, the
prior-run history (RUN-B), and the frozen state of the C(0) thread. Feeding
any of that to a phase agent contaminates the clean run: the whole point of
Phases 1 through 10 is that the agents rediscover (or fail to rediscover)
these things from evidence.

The agent-facing specification lives in `AGENT-TASK-SPEC.md`. The two files
were split from `Consolidated-Super-Prompt.md` on 2026-09-16 after the
single-file form was recognised as a contamination risk (see
`papers/corpus-investigation/PHASE-0-capability-reconnaissance.md` §5).

How the orchestrator uses this file: read it to know what NOT to assume, to
reconcile agent results against history AFTER the agents have reported (in
plain code where possible, as was done for RUN-B in Phase 1), and to pick up
the C(0) thread from its frozen state when Phase 6/10 reach it. Comparisons
against RUN-B or C(0) are always performed outside agent prompts.

---

## 1. Standing Operating Instructions

*(source: `papers/super-prompt/Super-Prompt.md`)*

- Be direct and skeptical. Do not reassure me just because an idea sounds good.
- Red-team my assumptions.
- No profanity. Plain English, roughly college-sophomore level.
- I am not a Python programmer. I am self-taught in SQL.
- I use Claude Code / Fable 5.1 for substantial repository work.
- I want manual approval before code is written or modified.
- Prefer one step at a time when I ask what to do next — give the single next
  action, not a giant list, unless I explicitly ask for the whole plan.
- When I ask for a prompt, give me a copyable fenced prompt I can paste
  directly into Claude Code/Fable.
- I strongly prefer copyable fenced prompts/commands.
- Do not use box-drawing tables.

---

---

## 2. Known Corpus and Prior State (load, don't assume)

*(source: `Super-Prompt.md` — this is what phases 1–3 above must treat as
prior context to verify, not as ground truth to preload)*

**The big question.** This is not merely about whether my existing
governance repositories are good. The investigation is trying to discover:
what meaningful governance questions exist for intelligent/AI systems; what
capabilities are required to answer them; which capabilities my existing
systems actually provide; which individual repositories provide them; which
combinations create capabilities no individual repository provides; which
claims survive adversarial falsification; which important governance
questions remain unanswered; which primitives are missing; what tests are
required to establish the claims; which tests are missing; what test
harnesses should exist for those missing tests; what prior art already
exists; what is genuinely novel, if anything; and what the smallest
defensible architecture actually is.

**Critical principle:** do not let my existing repository architecture
define the universe of governance questions. Explore the governance-question
space independently first, then map the corpus against it. Desired chain:
Governance Question → Required Capability → Existing Capability? →
Repository/primitive providing it → Composition opportunities → Evidence
required → Existing test coverage → Missing test → Designed test harness →
Adversarial falsification → Independent verification → Prior art →
Remaining uncertainty → Smallest defensible architecture.

**The current benchmark document** referenced by this prior context is
"Corpus Investigation — Task Specification," a forensic benchmark whose Gates
A–F cover instrumented preflight, corpus enumeration, preregistration,
corpus freeze, code inspection, execution, adversarial experiments,
independent verification/re-execution, claims and evidence graph,
novelty/prior-art analysis, frontier-agent research, reconciliation,
stopping criteria, research-significance requirements, and final
artifacts/report. Standing rules: every material claim resolves to evidence
or is withdrawn; negative results are valid findings; the investigation may
contradict the corpus author/operator; READMEs are not sufficient evidence;
exploration is free but formal experiments require preregistration; the
final report is constrained; no execution record means no working claim;
novelty requires prior-art analysis; failure to find prior art does not
establish novelty.

**RUN-B (historical, do not treat as final).** A prior run of this
investigation, RUN-B, happened in a plain Anthropic chat environment, not
Claude Code/Fable. It lacked Claude Code, Ultracode/effort observability,
orchestration/subagents, `gh` authentication, full private-repository
visibility, an independent verifier, a clean independent re-execution path,
and had network/tool restrictions. It was a preflight test of the apparatus,
not the final investigation, and its findings **must not** be injected as
assumptions into a clean run.

RUN-B's discoveries (historical only): a public corpus of 27 repositories —
5 transcript/archive repos, 1 specimen corpus (TOUCHSTONE), 21 substantive
systems (observe-perceive, HERALD, ghost_tools, innovation_os, CCC,
Triad-42, Conservation_Kernel, fortress-kernel, Governance_Gateway, ATS,
AUGUR, content-polish-pipeline, TIE, GEMS, sentinel_os, OBSERVE, Ecology,
GSA-815, ANVIL, GRAPH, VANGUARD) and thirteen candidate primitives
(hash-chained commitment/tamper-evident lineage; epistemic status labelling;
authority/origin boundary guard; admission gate; static defect detection;
mutation-based vacuous-test detection; ground-truth specimen corpus +
answer-key drift guard; adapter/integration hub; closed-loop behavioral
simulation; output constraint validation; retrieval/memory; vendoring drift
accounting; degraded-source reconstruction).

RUN-B findings, none of them settled: `observe-perceive` consuming sibling
repositories was one-way, not bidirectional; `ghost_tools` ↔ TOUCHSTONE was
the one clearly demonstrated bidirectional relationship; `OBSERVE` contained
vendored `sentinel_os`-like material with substantial redundancy/drift
accounting; `ccc`, `Conservation_Kernel`, `Governance_Gateway`, and `GEMS`
shared ontology concepts but incompatible `EpistemicStatus` vocabularies — a
critical falsification showed duck-typed plain-string statuses being
silently coerced (`CONFLICTED → INFERRED`, `HUMAN_AUTHORIZATION → SYSTEM`,
`HUMAN → SENTINEL`), meaning a commitment could be computed after coercion
and potentially attest to a value the producer never asserted; the broad
claim of one coherent shared ontology was falsified; `ghost_tools`
Type-1/2/3 duplication detection survived tested cases, Type-4 semantic
equivalence was a known boundary; prior-art research killed broad novelty
claims around tamper-evident logs and clone-detection/ground-truth concepts;
a narrower possible contribution around the TOUCHSTONE answer-key drift
guard was not killed but was explicitly not declared novel.

RUN-B fate suggestions (not accepted architecture decisions): retain
TOUCHSTONE, ghost_tools, Conservation_Kernel, CCC, Governance_Gateway,
observe-perceive, HERALD; possibly merge OBSERVE + sentinel_os + GSA-815;
possible ontology consolidation; wrap/reconsider several other systems. A
clean run must be capable of reaching a different answer.

**The missing-tests idea.** Beyond asking what tests are present, ask: for
every important governance question, capability, boundary, claim,
composition, and proposed architecture, what test would be required to
establish or falsify it? Then determine whether it exists, whether it
actually tests the claimed property (vs. just the implementation), whether
it's vacuous or too narrow, whether it has an adversarial counterpart,
whether it's independently reproducible, and what would falsify the claim.
For missing tests, design the harness (statuses: `EXISTING` / `DESIGNED` /
`EXECUTED` / `VERIFIED` / `UNKNOWN`) — do not silently implement or execute
missing harnesses during discovery.

**The historical chat archive.** I have a large ChatGPT export documenting
the development of these systems and the reasoning behind them. I previously
had Claude Code reorganize/index it into a queryable structure, and I do not
know whether that reorganization was faithful to the original export.
Treat the original export as source of truth. Desired chain: original
export → cryptographic manifest/preservation → fresh independently governed
ingestion → indexing/reconstruction → provenance tracking → governance
questions → evidence retrieval → claims → test design → missing-test
discovery → adversarial testing → corrections → evidence-backed
conclusions. Do not call the existing index "fraudulent" or "fabricated"
without evidence — distinguish SOURCE / DERIVED / TRANSFORMED / INFERRED /
UNKNOWN, and do not simply delete the old index. A powerful comparison
experiment: Original Export → Index A (existing process) vs. Original
Export → Index B (fresh governed reconstruction), then diff for missing
records, duplicates, timestamp changes, speaker-role changes, conversation
splitting, metadata changes, altered text, unsupported/invented metadata,
provenance failures, retrieval differences, and downstream conclusion
differences. Preserve errors found as evidence rather than hiding them.

**The governance proof-of-concept.** The strongest demonstration is not
"here is a governance system, trust us." It is: here is preserved source
material, here is what the system did to it, here are the tests, here are
the failures, here are the corrections, here is the evidence chain, here is
what remains unproven — including the system's willingness to find its own
previous representation or process wrong. The governance machinery gets no
free pass evaluating itself.

**Research philosophy.** Do not start by deciding there must be 8–10
repositories. Do not assume the current architecture is correct, that
similar-looking modules should merge, or that differently-named modules
should stay separate. Let the evidence determine retain / merge / split /
refactor / wrap / archive / replace / something else entirely. The target
is not repository optimization — it's discovering the smallest defensible
set of capabilities that answers the largest meaningful set of governance
questions while preserving evidence, provenance, falsifiability, and
uncertainty.

**Immediate operational sequence** for preparing the full-strength run: (1)
get the benchmark specification as a clean standalone markdown file if
needed; (2) put it in the Claude Code/Fable workspace; (3) run the
benchmark's preflight only; (4) do not inspect/populate the corpus before
preregistration; (5) if preflight passes, construct the clean investigation
plan; (6) add the independent governance-question-space discovery layer;
(7) add the missing-test/test-harness discovery layer; (8) preserve strict
separation between preflight, preregistration, discovery, execution, and
verification; (9) only then launch the full investigation; (10) bring
results back for skeptical review.

Do not confuse: the benchmark, the preflight, the actual investigation, the
historical RUN-B, the final architecture, and the governance
proof-of-concept. They are different things. The benchmark is the
experimental instrument. The preflight determines whether the apparatus can
run. The clean investigation discovers what's actually there. The
governance-question layer discovers what matters independently of the
corpus. The missing-test layer discovers what must be tested and what
harnesses are absent. The historical corpus can become a real-world
proof-of-concept, including against the system's own history. The final
architecture is an output of the investigation, not an input.

---

## 3. Active Sub-Investigation Thread: the `C(0)` Hypothesis

*(source: `papers/c-0/c-0-.md`, condensed — read that file in full before
acting on this thread; it is a live, frozen-baseline investigation, not
background reading)*

This is a concrete instance of Phase 6 (emergent capability discovery) and
Phase 10 (novelty falsification) above, already underway. Do not restart it
from scratch and do not silently rewrite its frozen conclusions.

**Frozen baseline (do not rewrite):** "The current `C(0)` operationalization
has not demonstrated discriminating power against `C(02)`. `C(0)` remains
`UNKNOWN`. The observed cross-repository structures have substantial
evidence of historical lineage, extraction, canonicalization, and recurring
architectural primitives. These explanations remain viable and must be
treated as active competitors." Phase II of this thread begins from that
statement — not from an assumption that `C(0)` works, and not from an
assumption that it fails.

**What `C(0)` is a hypothesis about:** a recurring structural relationship
observed across Iceberg → Sentinel/OBSERVE → GSA-815 → CNS, involving
`CallerState`, `DynamicState`, `perceived_wait`, `frustration`, `intent`,
`emotion`, `posterior`, and routing/graph/governance relationships. The
competing explanations that must stay live: `H1` a genuine structural
invariant; `H2` common historical lineage; `H3` canonicalization/interface
extraction; `H4` generic architectural convergence; `H5` analyst
selection/confirmation effects.

**What's already been tested and should not be rerun** (see `c-0-.md` §35
for the full list): the Iceberg→Sentinel and Sentinel→GSA-815 historical
relationships, the CNS extraction chronology, an exact CallerState code
comparison (identity was falsified — AST diverges — which does not prove
independent creation), a broad `STATE → DECISION → TRANSITION → OBSERVATION
→ REPLAY/HISTORY → GOVERNANCE` architecture candidate (rejected,
non-discriminating), a boundary/canonicalization candidate (rejected,
non-discriminating), and a blind/unique-prediction test (`C0/C02-03`) run
three times against the same frozen evidence with the same result each
time: 9/9 observations supported both `C(0)` and `C(02)`, zero
`C(0)`-unique predictions, discrimination failed.

**Where this thread continues:** search the full repository corpus and the
CCC/Ecology historical archive for evidence that predates the `C(0)`
hypothesis, previously unseen repositories/artifacts, counterexamples,
genuine independent structural recurrence, evidence for common lineage or
ordinary canonicalization, evidence for analyst-selection effects, and
external prior art (canonicalization, interface extraction, state machines,
event sourcing, state/decision separation, schema evolution, provenance,
audit structures). Priority order for this search is given in `c-0-.md`
§36. If a sufficiently precise and still-falsifiable `C(0)-v2` emerges,
freeze it separately from `C(0)-v1` and only then consider a prospective
experiment (freeze → define prediction and failure condition → select
target without modifying the prediction → execute → record → red-team the
interpretation).

A result that kills `C(0)` is preferable to a result that preserves it
through increasingly flexible redefinition. If it survives, it should
survive because the evidence forced it to, not because the definition
moved.

---

## 4. Design note carried from the excluded analysis files

**One design note carried from the meta-commentary, not applied here but
worth keeping in view:** the two analysis files this merge excluded both
converge on the same warning — a compound agent system (model + harness +
tools + environment) is what actually gets measured, and Anthropic's own
context-engineering guidance argues for moving bookkeeping out of the prompt
and into external state rather than growing the prompt further. If a future
revision of this document trims it, that is the direction to trim toward.

---

## 5. Source Map

| Original section (now in) | Source file(s) |
|---|---|
| 1 — Standing Operating Instructions (OPERATOR-BRIEF §1) | `papers/super-prompt/Super-Prompt.md` |
| 2 — Core Epistemic Discipline (AGENT-TASK-SPEC §1) | `Super-Prompt.md`; `Prompt.md`/`Agentic_prompt.md` `<evidence_discipline>`; `c-0/c-0-.md` §3 |
| 3 — Anti-Confirmation / Authority Limits (AGENT-TASK-SPEC §2) | `Prompt.md`/`Agentic_prompt.md` `<anti_confirmation_rule>`; `c-0-.md` §38 |
| 4 — Mission (AGENT-TASK-SPEC §3) | `Prompt.md`/`Agentic_prompt.md` (opening, `<mission>`, `<ultimate_benchmark_objective>`) |
| 5 — Phases 0–20 (AGENT-TASK-SPEC §4) | `Prompt.md` and `Agentic_prompt.md` (identical content, merged once) |
| 6 — Known Corpus and Prior State (OPERATOR-BRIEF §2) | `Super-Prompt.md` |
| 7 — `C(0)` sub-investigation (OPERATOR-BRIEF §3) | `c-0/c-0-.md` (condensed; read in full before acting) |
| 8 — Stopping Rule / Output (AGENT-TASK-SPEC §5) | `Prompt.md`/`Agentic_prompt.md`; `c-0-.md` §39–40; framing from `frontier-agent-evaluation/Autonomous_Adversarial_Research_Agent.md` |
| Excluded (analysis, not prompt) | `frontier-agent-evaluation/Autonomous_Adversarial_Research_Agent.md`; `frontier-agent-evaluation/anthropic_fable51_frontier_benchmark_research_20260914.md` |

`Prompt.md` and `Agentic_prompt.md` were confirmed byte-identical before
merging (`diff` returned no output), so Section 5 draws on them once rather
than twice.
