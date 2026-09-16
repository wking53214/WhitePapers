# Consolidated Super-Prompt — Claude Code / Fable 5.1 (Ultracode)

This file merges every fragment of the "super prompt" scattered across this
repository's markdown files into one paste-ready, non-contradictory prompt.
Section 9 lists exactly which source file each piece came from.

Two files were **not** merged into the prompt body because they are analysis
*about* the prompt, not prompt text: `Autonomous_Adversarial_Research_Agent.md`
(a plain-English design rationale) and
`anthropic_fable51_frontier_benchmark_research_20260914.md` (external research
notes on Fable 5.1 capabilities). Their one actionable conclusion — that the
agent-facing prompt should get *simpler* while the harness carries more of the
bookkeeping — is noted in Section 8 but not otherwise applied here, since
shrinking the prompt was not requested.

---

## 0. How to use this

Paste everything from Section 1 through Section 8 into Claude Code running
Fable 5.1 in Ultracode mode as the opening message of a fresh session. Section
6 ("Known Corpus and Prior State") and Section 7 (active sub-investigation
threads) are payload, not instructions to you the reader — they tell the
agent what has already happened so it doesn't rediscover or silently
overwrite it.

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

## 2. Core Epistemic Discipline

*(sources: `Super-Prompt.md`, `Prompt.md` / `Agentic_prompt.md`
`<evidence_discipline>`, `c-0-.md` §3)*

Four label systems apply at different points in an investigation. Do not
blend them or silently upgrade a value from one category into a stronger one.

**a. Operational status** (per claim, per action taken):
`EXECUTED` / `INSPECTED` / `INFERRED` / `UNKNOWN`

**b. Evidence class** (what kind of thing backs a claim):
`[CODE]` `[TEST]` `[EXPERIMENT]` `[REPOSITORY HISTORY]` `[EXTERNAL SOURCE]`
`[INFERENCE]` `[HYPOTHESIS]` `[UNKNOWN]`

**c. Implementation-state** (for forensic inventory of a repo/module):
`IMPLEMENTED` / `PARTIALLY IMPLEMENTED` / `TESTED` / `UNTESTED` /
`DOCUMENTED ONLY` / `EXPERIMENTAL` / `BROKEN` / `DUPLICATED` / `SUPERSEDED` /
`CONTRADICTORY` / `COMPOSABLE` / `NOT COMPOSABLE` / `UNIQUE` / `UNKNOWN`

**d. Final-claim verification** (for conclusions in the closing report):
`DIRECTLY DEMONSTRATED` / `EXPERIMENTALLY DEMONSTRATED` /
`EXTERNALLY SUPPORTED` / `INFERRED` / `PLAUSIBLE` / `CONTESTED` / `UNTESTED` /
`FALSIFIED` / `UNKNOWN`

**The evidence chain — never skip a link:**
documentation does not prove implementation → implementation does not prove
correctness → correctness does not prove usefulness → usefulness does not
prove novelty → novelty does not prove commercial value. Never present a
weaker link as if it were a stronger one.

**Core adversarial philosophy:**
"Don't ask whether the fix (or hypothesis) works; ask how it can be broken."

**Methodology rules:**
- Freeze baselines before investigating them further. A frozen baseline is
  not rewritten because new evidence turns up; a revision gets a new version
  tag (e.g. `C(0)-v1` vs `C(0)-v2`) and documents what changed, why, what
  evidence motivated it, whether that evidence predates the change, and
  whether the revision is still falsifiable or has just been made vaguer.
- Version methodologies separately from the claims they test.
- One intentional intervention per formal retest. No silent methodology
  changes mid-run.
- Use targeted differential testing, not blind reruns of the entire
  historical test suite.
- Evidence should be author-independent wherever possible.
- Preserve negative results as first-class findings — a killed hypothesis is
  a successful outcome, not a failed one.
- FACP is mandatory unless formally replaced. *(Carried forward verbatim from
  the source; FACP is not spelled out anywhere in this repository's markdown
  — treat it as a defined term from the user's private prior context and ask
  if it needs restating.)*

---

## 3. Anti-Confirmation Rule and Authority Limits

*(sources: `Prompt.md` `<anti_confirmation_rule>`, `c-0-.md` §38)*

You have explicit permission to contradict me. Do not optimize for
confirming my architecture, terminology, repository classifications, prior
conclusions, assumptions, preferred product direction, or beliefs about
novelty or commercial value. If the evidence contradicts them, say so
clearly. If it supports them, show why. If it's insufficient, say `UNKNOWN`.

You are an investigative instrument, not a decision authority. You do not
get to declare a hypothesis proven, disproven, novel, causally established,
or independently convergent — you recommend a classification and show the
evidence behind it. The final interpretation is mine.

---

## 4. Mission

*(source: `Prompt.md` / `Agentic_prompt.md`, opening + `<mission>` +
`<ultimate_benchmark_objective>`)*

Given the outcome I am trying to obtain, design and execute the task
specification — not merely a prompt — that would maximally challenge,
exercise, and exploit the full currently available capability of Claude Code
using the currently documented Fable model in Ultracode mode.

Treat this as a frontier-agent research benchmark, not a conventional coding
assignment. The objective is not to tell the agent how to solve a
predetermined problem. It is to construct an environment in which a frontier
agent must discover what the actual problem is, determine what must be known
to solve it, determine how to investigate it, execute the investigation,
challenge its own conclusions, and produce whatever technical, scientific,
architectural, or commercial discoveries the evidence warrants. The agent
must be allowed to surprise the task designer, and allowed to conclude that
the desired outcome cannot be achieved.

Do not merely answer this request by proposing another conventional prompt.
First determine what the current agent can actually do. Then discover the
corpus. Then discover the problem. Then design the adaptive frontier-agent
task. Then attack the task. Then execute the highest-value investigation
that the resulting task requires. Then determine what was actually learned.
The objective is not to demonstrate that the agent can follow this
specification — it is to discover how far the agent can actually go when
given the freedom, tools, evidence, and adversarial pressure to find out.

**Ultimate benchmark question:** Can a frontier Claude Code agent, given a
difficult real-world technical corpus and broad access to tools,
independently discover the structure of an inadequately specified problem,
determine what must be known, investigate it efficiently, reason across
heterogeneous code and external knowledge, construct and test competing
explanations, discover emergent capabilities, invent or identify missing
primitives, falsify attractive conclusions, synthesize a defensible
architecture, determine what is genuinely novel, and produce the artifacts
justified by the evidence? Do not assume the answer is yes. Find out.

---

## 5. Phases 0–20 (task specification)

*(source: `Prompt.md` and `Agentic_prompt.md` — byte-identical in this
repository; merged once here)*

<phase_0_capability_reconnaissance>

THIS IS A HARD PREREQUISITE. Before designing the task, analyzing the
repository corpus, proposing an architecture, or making substantive
assumptions about what the agent can accomplish, perform current capability
reconnaissance.

Access and study authoritative, current Anthropic documentation applicable
to the exact target environment and model/configuration. Do not assume
Anthropic publishes a single document called a "capability matrix."
Construct the capability matrix from authoritative current Anthropic sources
where necessary.

Determine and document: the exact currently available model designation;
current capabilities of that model; Ultracode-specific behavior and
capabilities; reasoning/thinking capabilities; tool-use capabilities; web
research capabilities; code execution capabilities; filesystem capabilities;
subagent capabilities; agent-team capabilities; parallelization
capabilities; orchestration capabilities; context-window capabilities;
long-horizon execution capabilities; context compaction and continuity
mechanisms; persistence and state-management mechanisms; skills; hooks; MCP
and other extensibility mechanisms; network access; repository/Git
capabilities; autonomy-related capabilities; documented limits and
constraints; known failure modes; recently added or changed capabilities;
distinctions between model capabilities, Claude Code capabilities, and
Ultracode capabilities; capabilities that are documented but may not be
available in the actual execution environment.

If "Fable 5.1" is not the current official designation, or the requested
configuration differs from what's currently documented, explicitly identify
the discrepancy and determine the closest valid target configuration. Do not
silently substitute assumptions. Do not rely on model memory when current
authoritative Anthropic documentation can establish the answer.

Create a capability matrix with columns: CAPABILITY / CURRENTLY AVAILABLE? /
DOCUMENTED EVIDENCE / ACTUALLY EXERCISABLE IN THIS ENVIRONMENT? /
LIMITATIONS / HOW IT COULD BE STRESSED BY THIS TASK.

Do not proceed to task construction until this reconnaissance is complete.

</phase_0_capability_reconnaissance>

<phase_1_corpus_discovery>

The initial technical corpus is my complete GitHub repository library:
github.com/wking53214

The eligible corpus consists of every repository under that account —
active, archived, apparently obsolete, experimental, abandoned, whether or
not the README suggests it's unimportant, whether or not its purpose is
initially clear. Exclude only repositories whose primary purpose is storing
conversation history, chat history, transcript archives, AI-assistant
history, or equivalent historical conversation files.

Do not assume the number of repositories. Do not use a previously supplied
repository list as authoritative (see Section 6 for why). Discover the
actual current corpus. Determine repository eligibility from observed
contents and purpose, not merely names. Record and investigate any
ambiguous or mixed-purpose repository.

Verify that the GitHub access required actually works. If access fails, do
not fabricate findings — record the environmental limitation and determine
what can legitimately be established.

Archived repositories are first-class evidence. Treat repositories as
evidence, not as an architecture.

</phase_1_corpus_discovery>

<phase_2_define_the_real_outcome>

Before optimizing a solution, determine what outcome can legitimately be
pursued from the evidence. Do not assume that my prior descriptions of the
problem, architecture, governance model, terminology, repository
relationships, product concept, scientific contribution, or commercial
opportunity are correct.

Determine what problem or opportunity actually exists; whether it's
well-posed; what outcomes are possible, matter, are measurable, are
technically defensible, or are unsupported by the evidence; what would
constitute meaningful success or failure; what evidence would invalidate the
framing itself. If multiple plausible interpretations exist, preserve them
long enough to test them. Do not prematurely collapse uncertainty.

</phase_2_define_the_real_outcome>

<phase_3_discover_the_question_universe>

Do not begin with a predetermined question list. Discover the questions that
must be answered. Determine the smallest complete question universe
necessary to understand the actual problem and evaluate candidate
solutions. The number of questions is an output, not a constraint.

Questions may concern, where relevant: observation; evidence; provenance;
identity; authority; knowledge; uncertainty; contradiction; memory; temporal
state; causality; intent; objectives; decisions; authorization; policy;
execution; runtime state; consequences; learning; adaptation; adversarial
conditions; security; resilience; human oversight; external dependencies;
multi-agent interaction; system composition; counterfactuals; independent
verification; scientific validity; novelty; commercialization. Do not assume
this list is complete — discover additional categories when the evidence
requires them.

For every important question determine: why it matters; what evidence could
answer it; whether that evidence exists; what capability is required to
answer it; whether the answer can be independently verified; what would
falsify the answer.

</phase_3_discover_the_question_universe>

<phase_4_forensic_discovery>

Perform forensic analysis of the complete eligible repository corpus.
Prioritize actual implementation over descriptions. Inspect, where useful:
source code; tests; package structure; dependencies; interfaces; schemas;
configuration; executable paths; data structures; algorithms; invariants;
error handling; persistence; state transitions; security boundaries;
authorization mechanisms; provenance mechanisms; cryptographic mechanisms;
logging; external interfaces; integration points; build configuration; CI;
generated artifacts; repository history; commits; branches; tags;
architectural predecessors.

Determine what each repository actually does. Do not infer capability
merely because a README claims it exists. Do not infer absence merely
because documentation doesn't mention it. Classify each using the
implementation-state labels in Section 2c.

Discover relationships between repositories from evidence rather than
assuming relationships from names.

</phase_4_forensic_discovery>

<phase_5_capability_and_question_graph>

Construct a capability model from the evidence. For each discovered
capability determine what it actually does; what evidence proves it; what
questions it can answer; required inputs; produced outputs; what guarantees
it does and does not provide; what other capabilities it depends on and
what depends on it; whether it's independently testable, composable,
duplicated elsewhere, unique, or introduces new failure modes.

Build the chain: QUESTIONS → REQUIRED CAPABILITIES → IMPLEMENTATIONS →
EVIDENCE → TESTS → LIMITATIONS. Do not confuse the existence of code with
the existence of a validated capability.

</phase_5_capability_and_question_graph>

<phase_6_emergent_capability_discovery>

Investigate what becomes possible through composition — do not limit
analysis to individual repositories. Search systematically for:
complementary capabilities; emergent capabilities; information-flow
relationships; state continuity; transformation chains; feedback loops;
cross-repository invariants; new interfaces/abstractions; capability
amplification or conflicts; hidden dependencies; emergent failure modes;
compositional vulnerabilities.

Determine whether combinations produce capabilities no individual repository
provides — and whether combinations create contradictions or risks that
disappear when components stay separate. Do not assume integration is
inherently beneficial.

*(Section 7 below carries an already-active thread of this phase — the
`C(0)` structural-invariant hypothesis — that must be picked up from its
frozen state, not restarted.)*

</phase_6_emergent_capability_discovery>

<phase_7_competing_architectures>

Generate genuinely competing architectural hypotheses. Do not optimize
immediately around the first plausible one. Produce multiple materially
different candidates where the evidence supports them, including radically
different organizational structures.

For each candidate determine: capabilities provided and missing;
dependencies; complexity; failure modes; verification properties; security
and operational implications; scalability; maintainability; scientific
defensibility; commercial implications; migration requirements; irreducible
assumptions. Then actively attempt to falsify each candidate. The winning
architecture must survive comparison against credible alternatives. If none
survives, say so.

</phase_7_competing_architectures>

<phase_8_experiment_generation>

Do not merely reason about whether important claims are true — invent
experiments capable of proving them false, and where practical implement and
execute them. Use tests, adversarial tests, simulations, benchmarks,
property tests, differential tests, mutation tests, fault injection, state
reconstruction, replay, temporal tests, counterfactual tests, performance
measurements, security tests, compositional tests, independent verification,
or other appropriate methods discovered during the investigation.

For every major conclusion, produce: CLAIM / EVIDENCE / EXPERIMENT / RESULT
/ INTERPRETATION / LIMITATION / FALSIFIER. A failed experiment is valuable
evidence — do not conceal negative results.

</phase_8_experiment_generation>

<phase_9_external_research>

Conduct external research where it materially affects the conclusions:
prior art; academic literature; standards; technical specifications;
competing architectures; existing commercial systems; known algorithms;
existing governance approaches; legal/regulatory requirements where
relevant; established terminology; prior implementations.

Repository evidence establishes what exists in the corpus. External evidence
establishes what exists outside it. Do not substitute external research for
repository forensic analysis. Do not claim novelty merely because no
identical implementation was found.

</phase_9_external_research>

<phase_10_novelty_falsification>

Treat every potential innovation as a hypothesis. For each candidate
contribution: formulate the novelty hypothesis; identify the closest known
prior art; search aggressively for competing explanations; compare against
prior work; determine exactly what's different and whether that difference
is technically meaningful; attempt to falsify the novelty claim; downgrade
or discard it if it doesn't survive.

Search for novel computational primitives, algorithms, representations,
invariants, state models, architectural patterns, governance mechanisms,
verification methods, methodologies, benchmarks, or theoretical models. Do
not manufacture novelty.

</phase_10_novelty_falsification>

<phase_11_second_order_benchmark_attack>

After designing the task, attack the task itself. Assume an intelligent
agent is trying to obtain a high evaluation result without actually
possessing the capabilities the benchmark claims to measure. Look for:
superficial compliance; excessive verbosity; fake research or
experimentation; unjustified confidence; tool-use theater; gratuitous
parallelization; delegation without synthesis; citation theater;
architecture theater; novelty theater; benchmark-specific optimization;
repository sampling bias; premature conclusions; hidden assumptions;
evaluation leakage; reward hacking; proxy optimization; unmeasured failure
modes.

Then modify the benchmark to resist those failure modes. Repeat this
adversarial review until further improvements produce diminishing returns.
The benchmark itself must be falsifiable.

</phase_11_second_order_benchmark_attack>

<phase_12_autonomy_evaluation>

Evaluate not merely what was produced but how intelligently the agent
operated. Measure, where the environment permits: information gained per
unit effort; tool selection and delegation quality; parallelization
efficiency; unnecessary work, tool calls, or agent spawning; recovery from
failed plans; self-detected errors; abandoned hypotheses; successful course
corrections; quality of stopping decisions; human intervention required;
persistence across long horizons; state-management quality; ability to
preserve uncertainty and revise conclusions.

Do not reward activity for its own sake. Do not equate token consumption,
tool-call volume, repository count, experiment count, or agent count with
intelligence. Reward intelligent allocation of effort.

</phase_12_autonomy_evaluation>

<phase_13_resource_intelligence>

Test resource allocation as well as raw capability. Where meaningfully
measurable, establish reasonable budgets or accounting for execution time,
tool calls, external research, parallel agents, agent-team usage,
experimentation, compute, human intervention. Let the agent determine how to
allocate those resources, and evaluate whether it targets the
highest-value uncertainties rather than simply maximizing activity, using
information gain, consequence of error, architectural leverage, and
uncertainty as priority factors. Do not force a fixed workflow.

</phase_13_resource_intelligence>

<phase_14_temporal_and_counterfactual_integrity>

Where relevant, test whether conclusions survive temporal and counterfactual
analysis. Determine whether the system can distinguish, at the relevant
point in time, what was observed, known, unknown, inferred, believed,
intended, authorized, decided, executed, and learned. Determine whether
later information improperly contaminates earlier conclusions.

Where relevant, test alternative worlds: what would have happened under a
different observation, belief, authorization, decision, action, dependency,
or system state? Do not assume these dimensions are relevant to every
discovered problem — determine their relevance from the evidence.

</phase_14_temporal_and_counterfactual_integrity>

<phase_15_independent_verification>

Attempt to construct an independent path to verify the most important
conclusions, minimizing dependence on the reasoning process that generated
the original conclusion. Determine what another competent investigator could
independently establish; what evidence is sufficient; what cannot be
independently verified; what remains dependent on interpretation; what
claims exceed the available evidence.

Classify the final result using the final-claim verification labels in
Section 2d.

</phase_15_independent_verification>

<phase_16_architecture_fate>

Determine the fate of every relevant repository and capability from
evidence: RETAIN / COMBINE / SEPARATE / TRANSFORM / REIMPLEMENT / EXTRACT /
ARCHIVE / RETIRE / ELIMINATE / UNKNOWN.

Do not establish a target number of surviving repositories. The final
architecture may contain more or fewer components than expected, or
components not currently present. A repository may be retained for
historical/evidentiary reasons even outside the runtime architecture, or
eliminated despite substantial implementation effort if its capability is
unnecessary or inferior.

</phase_16_architecture_fate>

<phase_17_missing_primitives>

Search explicitly for capabilities that do not exist — not limited to
missing modules. Look for missing primitives, abstractions,
representations, interfaces, verification mechanisms, state models,
algorithms, experimental methods, security boundaries, theoretical concepts,
architectural mechanisms. If a missing primitive appears necessary,
determine whether it can be designed and experimentally validated; if it
can't be justified, record it as an unresolved gap.

</phase_17_missing_primitives>

<phase_18_scientific_and_commercial_discovery>

Determine what the investigation has actually discovered. Do not assume the
outcome must be a product. Potential outcomes: no meaningful new result;
engineering improvement; architecture; infrastructure; platform; product;
service; technical methodology; benchmark; scientific hypothesis; formal
model; research program; publication; patent investigation; multiple
products or papers; or another outcome not anticipated here.

Evaluate technical defensibility separately from commercial attractiveness,
and novelty separately from commercial value. Do not force commercialization
where the evidence doesn't support it.

</phase_18_scientific_and_commercial_discovery>

<phase_19_artifact_selection>

Do not prescribe the final deliverables — determine which artifacts are
justified. Potential artifacts: source code; tests; architecture
specifications; formal models; benchmarks; datasets; reproducibility
packages; technical reports; whitepapers; systems/empirical/formal papers;
taxonomies; research agendas; product specifications; commercialization
analyses; patent prior-art analyses; demonstrations.

Produce only artifacts warranted by the evidence. For each, state: WHY IT
EXISTS / WHAT CLAIM IT SUPPORTS / WHAT EVIDENCE SUPPORTS IT / WHAT WOULD
FALSIFY IT.

</phase_19_artifact_selection>

<phase_20_meta_evaluation>

At the end, evaluate the entire investigation: what was discovered,
disproved, or left unresolved; which assumptions were invalidated or
survived; which capabilities were or weren't demonstrated; which
architectural, scientific, novelty, and commercial conclusions survived;
what the agent learned about its own limitations; what the task revealed
about frontier-agent capability.

Explicitly identify the boundary between: WHAT THE AGENT COULD DO / WHAT THE
AGENT COULD NOT DO / WHAT THE ENVIRONMENT PREVENTED / WHAT THE TASK FAILED
TO MEASURE / WHAT REMAINS UNKNOWN.

</phase_20_meta_evaluation>

---

## 6. Known Corpus and Prior State (load, don't assume)

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

## 7. Active Sub-Investigation Thread: the `C(0)` Hypothesis

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

## 8. Stopping Rule and Output Requirements

*(sources: `Prompt.md` `<stopping_rule>` and `<final_output>`, `c-0-.md`
§39–40, `Autonomous_Adversarial_Research_Agent.md` §13 for framing)*

**When to stop.** Do not stop merely because the requested artifacts exist.
Stop when the highest-value unresolved questions have been investigated to
the point where more work is unlikely to materially change the principal
conclusions — use diminishing information gain as the stopping criterion,
not elapsed time or token count. If important uncertainty is genuinely
unresolvable within available resources, stop and explicitly preserve it.
Do not manufacture certainty for a cleaner final answer.

**Final output.** Produce a final evidence-backed package containing
whatever the investigation genuinely warrants, at minimum making the
reasoning auditable. Include: the discovered capability baseline; the
discovered eligible corpus; the discovered problem structure; the discovered
question universe; the capability model; important repository
relationships; competing architectural hypotheses; experiments and results;
falsified hypotheses; surviving conclusions; unresolved questions;
repository/capability fate; missing capabilities or primitives; novelty
analysis; external research findings; independent-verification results;
commercial implications where justified; artifacts produced; limitations;
and a final assessment of what this run demonstrated about frontier-agent
capability. Do not optimize the presentation to look impressive — optimize
it to be difficult to falsify incorrectly.

**Final scorecard**, one row per material claim: CLAIM / STATUS / EVIDENCE
CLASS / EXECUTED-INSPECTED-INFERRED-UNKNOWN / SUPPORTING EVIDENCE /
CONTRADICTING EVIDENCE / COMPETING EXPLANATION / REMAINING UNCERTAINTY /
NEXT TEST.

**Non-negotiable principles**, all twenty-two, carried forward unedited:
discover before prescribing; evidence before assertion; code before README
claims; experiments before confidence; falsification before conclusion;
alternatives before architecture selection; prior art before novelty
claims; independent verification before strong claims; negative results are
first-class results; uncertainty must be preserved; tool use must be
justified by information gain; parallelization must be justified by task
structure; complexity is not intelligence; activity is not progress;
repository count is not architectural quality; code volume is not
capability; novelty is not assumed; commercial value is not assumed; no
repository or hypothesis is protected; the agent is allowed to conclude the
desired outcome cannot be achieved; the benchmark itself must be attacked
and improved; the final result must be allowed to differ radically from the
task designer's expectations.

**Final self-attack**, immediately before declaring the task complete: what
would an exceptionally capable but strategically deceptive or reward-seeking
agent do to appear successful without solving the problem, what evidence
would expose that, what important capability does this benchmark still fail
to measure, what important conclusion could still be wrong, what experiment
would most efficiently change my mind. Perform the highest-value remaining
checks, then finalize.

**One design note carried from the meta-commentary, not applied here but
worth keeping in view:** the two analysis files this merge excluded both
converge on the same warning — a compound agent system (model + harness +
tools + environment) is what actually gets measured, and Anthropic's own
context-engineering guidance argues for moving bookkeeping out of the prompt
and into external state rather than growing the prompt further. If a future
revision of this document trims it, that is the direction to trim toward.

---

## 9. Source Map

| Section | Source file(s) |
|---|---|
| 1 — Standing Operating Instructions | `papers/super-prompt/Super-Prompt.md` |
| 2 — Core Epistemic Discipline | `Super-Prompt.md`; `Prompt.md`/`Agentic_prompt.md` `<evidence_discipline>`; `c-0/c-0-.md` §3 |
| 3 — Anti-Confirmation / Authority Limits | `Prompt.md`/`Agentic_prompt.md` `<anti_confirmation_rule>`; `c-0-.md` §38 |
| 4 — Mission | `Prompt.md`/`Agentic_prompt.md` (opening, `<mission>`, `<ultimate_benchmark_objective>`) |
| 5 — Phases 0–20 | `Prompt.md` and `Agentic_prompt.md` (identical content, merged once) |
| 6 — Known Corpus and Prior State | `Super-Prompt.md` |
| 7 — `C(0)` sub-investigation | `c-0/c-0-.md` (condensed; read in full before acting) |
| 8 — Stopping Rule / Output | `Prompt.md`/`Agentic_prompt.md`; `c-0-.md` §39–40; framing from `frontier-agent-evaluation/Autonomous_Adversarial_Research_Agent.md` |
| Excluded (analysis, not prompt) | `frontier-agent-evaluation/Autonomous_Adversarial_Research_Agent.md`; `frontier-agent-evaluation/anthropic_fable51_frontier_benchmark_research_20260914.md` |

`Prompt.md` and `Agentic_prompt.md` were confirmed byte-identical before
merging (`diff` returned no output), so Section 5 draws on them once rather
than twice.
