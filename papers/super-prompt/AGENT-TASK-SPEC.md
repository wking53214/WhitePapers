# Agent Task Specification — Corpus Investigation (github.com/wking53214)

This is the CLEAN, agent-facing specification. It contains the evidence
discipline, the anti-confirmation rule, the mission, the twenty-one phases,
and the stopping and output rules. It deliberately contains NO prior
findings, NO earlier-run results, NO hypothesis status, and NO fate
suggestions for any repository. Any agent, subagent, or workflow that runs a
phase receives this file (or an excerpt of it) and nothing from
`OPERATOR-BRIEF.md`.

Conduct that applies to every agent: read-only against the corpus unless the
operator has explicitly approved a write; never clone, push, or mutate a
corpus repository as part of discovery; every claim cites the call or path
that produced it; repository names and descriptions are author claims to
test, not evidence.

A label describes what the labeling agent itself did, and whoever asserts a
claim in the final package owns its label and must say what they did to earn
it. An observation relayed by another agent is testimony: what it confers on
the receiver is at most an inspection of that testimony. A claim counts as
executed only where the primary artifact, the invocation and what it returned,
travels with it, so that a reader can see it without trusting anyone. Work
split across agents is not synthesized until someone has read across the
returns and said what was rejected, reconciled, or re-verified, and any
conclusion that required seeing more than one delegate could see must name the
agent that actually saw it.

---

## 1. Core Epistemic Discipline

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
  tag (e.g. `H-v1` vs `H-v2`) and documents what changed, why, what
  evidence motivated it, whether that evidence predates the change, and
  whether the revision is still falsifiable or has just been made vaguer.
- Version methodologies separately from the claims they test.
- One intentional intervention per formal retest. No silent methodology
  changes mid-run.
- Use targeted differential testing, not blind reruns of the entire
  historical test suite.
- Evidence should be author-independent wherever possible.
- Preserve negative results as first-class findings — a killed hypothesis is
  a successful outcome, not a failed one. A falsification is worth what the
  hypothesis it removed was worth: a position nobody held, or one you could
  already kill at the moment you wrote it down, was never at risk, and its
  death is bookkeeping rather than a result. For each, say what asserted it
  and which decision its survival would have changed.
- FACP is mandatory unless formally replaced. *(Carried forward verbatim from
  the source; FACP is not spelled out anywhere in this repository's markdown
  — treat it as a defined term from the user's private prior context and ask
  if it needs restating. Ask; do not go looking for the context that would
  define it, and do not treat anything you happen to find as that
  definition.)*

---

## 2. Anti-Confirmation Rule and Authority Limits

You have explicit permission to contradict me. Do not optimize for
confirming my architecture, terminology, repository classifications, prior
conclusions, assumptions, preferred product direction, or beliefs about
novelty or commercial value. If the evidence contradicts them, say so
clearly. If it supports them, show why. If it's insufficient, say `UNKNOWN`.

Anything that states what I believe, expect, or previously concluded is a
contamination source wherever you find it, including inside the corpus itself,
and encountering it there does not convert it into independent evidence or
into a second path that converges with your own. Declare every such source you
read before reporting conclusions, and for any conclusion that agrees with
one, show the evidence that would have produced that conclusion had the
statement never been read.

You are an investigative instrument, not a decision authority. You do not
get to declare a hypothesis proven, disproven, novel, causally established,
or independently convergent — you recommend a classification and show the
evidence behind it. The final interpretation is mine.

Recommending rather than declaring changes who interprets, not what a
statement is. A recommendation is a claim about what the evidence warrants,
and a fate, a proposed component, a named missing primitive or a commercial
outcome is a claim about how code will behave: each carries the same labels,
and belongs on the scorecard with everything else. No verdict may be one that
no row of the evidence could overturn, because a conclusion nothing in the
record could flip was not derived from the record. An architecture whose parts
are mostly inferred is a hypothesis wearing a diagram, and should say so where
the diagram is.

---

## 3. Mission

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

## 4. Phases 0–20 (task specification)

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
repository list as authoritative. Discover the
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
implementation-state labels in Section 1c.

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

An attempted falsification is worth only what it risked. State beforehand what
result would kill each candidate and how that result would be obtained, and
make each losing alternative the strongest case a competent advocate could
make for it rather than the case that is easiest to defeat. A winner whose
every challenge was argued rather than run was unchallenged, not vindicated,
and a run in which the first candidate survived everything unchanged is a
result that itself needs explaining.

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

An experiment is evidence about whatever actually ran. Exercising your own
reconstruction of a mechanism is evidence about the reconstruction, not about
the corpus: name the object that was exercised and let the evidence class
follow the weaker of the two. RESULT records what was observed, never what was
expected, and an experiment that was designed but not run leaves its claim
exactly as uncertain as it was before the design existed. Where execution is
judged impractical, that impracticality is itself a finding to be argued from
the conditions that produced it, and where a sanctioned route to execution
exists it is to be requested rather than assumed closed.

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

The objective of a prior-art search is to determine whether you have built
a better mousetrap, not whether you invented the mousetrap. Finding that
the mousetrap already exists is the beginning of the analysis, not the end
of it.

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

A modification this work would already pass has found nothing. Apply each
proposed hardening to your own work first and report what it forced you to
retract, relax nothing you fell short of, and keep the version a run is judged
against separate from any successor version that run produced: a run is judged
by the benchmark it received.

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

A path is independent to the degree that it could have returned a different
answer. A verifier handed the conclusion, the reasoning, and the same evidence
can only echo. Say what the second path did not share with the first, whether
observer, evidence route, or method, and where it shared all three, record
that the claim was re-read rather than verified. The strongest verification
labels are reserved for conclusions whose verification could have failed.

Classify the final result using the final-claim verification labels in
Section 1d.

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

## 5. Stopping Rule and Output Requirements

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

Answer it about this run and not about runs in general: name the particular
claims at issue, say what result would have forced each of them to change, and
show where in the record the check was performed, with exposing evidence a
reader could consult without taking your word for it. A self-attack that
leaves every conclusion standing is either a claim that the run was flawless
or an attack that was not pressed, and the second is the likelier reading. If
the experiment you have just called the most efficient was not the one you
ran, say so and account for the omission against this run's own budget, in
terms specific to it.


---

