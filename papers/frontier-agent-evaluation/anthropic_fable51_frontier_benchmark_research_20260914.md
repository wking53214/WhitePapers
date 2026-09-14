# Frontier-Agent Benchmark and Fable 5.1 Research Assessment

**Research date:** 2026-09-14

## Executive finding

The current Frontier-Agent Corpus Investigation Benchmark v3 is already much closer to an **agent-evaluation system** than to an ordinary prompt. That is the correct direction for testing a model such as Claude Fable 5.1, because Anthropic's own recent work treats the object being evaluated as a compound system: model + agent harness + tools + environment + grading. Anthropic also explicitly warns that infrastructure configuration alone can shift agentic coding benchmark results by several percentage points, and that long-running agents need state-management and handoff mechanisms rather than a single giant instruction. [1][2][3]

The benchmark's strongest ideas are therefore not its length. They are:

- an externally enforced corpus seal rather than a behavioral promise;
- machine-verifiable experiments rather than self-reported execution;
- explicit evidence classes and grounded claims;
- negative-result warrants that distinguish "not found" from "not investigated";
- pre-registered predictions that test calibration before the answer is known;
- explicit model/harness/tool attribution;
- cross-run isolation and a harness control;
- a mandatory attempt to falsify the benchmark's own conclusions;
- and a second-order gate asking whether the run reveals anything about frontier-agent behavior itself.

Those features line up unusually well with Anthropic's public writing on agent evals, AI-resistant technical evaluations, long-running agents, context engineering, tool design, and eval awareness. [1][2][4][5][6][7]

There is, however, an important tension. The current agent-facing specification is dense enough that it risks becoming a **test-taking protocol** rather than a minimally specified research problem. Anthropic's context-engineering guidance argues for the smallest set of high-signal context at the correct altitude, with progressive disclosure and external state where possible. In other words: keep the sophisticated machinery, but move more of it out of the prompt and into the harness. [5]

The recommendation is therefore **not to alter the frozen v3 primary run now**. Treat v3 as the frozen experiment. Develop a v4 as a controlled prompt-compression / harness-separation study after v3, using the same frozen corpus and the same external verification system. This creates an additional scientifically useful measurement: how much of the observed performance comes from frontier-agent capability versus benchmark scaffolding.

## 1. Terminology correction: "SuperCode"

I could not find an Anthropic product or official documentation set called **SuperCode**. Anthropic's official material consistently refers to **Claude Code**, the **Claude Agent SDK**, managed agents, and related agentic coding infrastructure. This report therefore interprets "SuperCode" as Claude Code unless a separate reference is supplied. That distinction matters because naming an unofficial product as Anthropic's own could contaminate a technical assessment.

## 2. What Anthropic is saying about Fable 5.1

Anthropic's current Fable page describes Fable 5.1 as its most capable generally available model for difficult knowledge work and coding, designed for ambitious, long-running and asynchronous work. The page specifically highlights jobs that span hours and multiple applications, entire-codebase coding, multi-day autonomous sessions, self-testing, recovery from failed steps, and vision-assisted verification. [8]

That makes your benchmark unusually well targeted. The benchmark is not asking Fable to answer isolated coding questions. It is asking it to enumerate an unknown corpus, plan its investigation, execute code, design implementation-specific attacks, perform external prior-art research, maintain evidence over time, reconcile predictions, and stop when further work would no longer change the principal conclusions. Those behaviors are much closer to the capability profile Anthropic says Fable 5.1 is intended to address than a conventional single-shot coding task.

Anthropic's Fable announcement also includes partner examples of long-running root-cause analysis, difficult research gaps, unattended experiments, multi-hour work, and autonomous problem discovery. Those are qualitative partner reports, not independent benchmark evidence, but they are informative about the intended operating envelope of the model. [9]

One detail is particularly relevant to your benchmark: Anthropic explicitly documents that Fable 5.1 has significant safeguards around cybersecurity, biology, and chemistry, and that some flagged requests may be handled by other models or refused depending on configuration. That means a benchmark using a security-adjacent software corpus must treat **model identity and interval attribution as an instrumentation problem**, not a claim the agent can make about itself. [8][10]

## 3. Anthropic's current view of the agent as a system

Anthropic's January 2026 article "Demystifying evals for AI agents" is almost a direct endorsement of the benchmark's basic architecture. It explains that agent evaluations differ from ordinary LLM evaluations because the system acts through tools, changes an environment, and may take many turns. It recommends combining grading methods and stresses that coding agents require stable environments and thorough verification. It also frames eval-driven development as a way to test whether a capability remains below or above a useful threshold as models advance. [1]

Anthropic's infrastructure-noise work makes the point even more sharply: they report that infrastructure configuration alone produced a six-percentage-point spread on Terminal-Bench 2.0, larger than some model leaderboard gaps. Their recommendation is to specify resource allocation and treat runtime as part of the evaluation system. [2]

That strongly validates the work already done on your pre-flight performance baseline. A benchmark that ignores CPU, memory, disk, swap, concurrency, network, container topology, or competing workloads can end up measuring the environment as much as the agent. Your existing environment snapshot should therefore be considered part of the benchmark instrument rather than an incidental appendix.

Anthropic's long-running-agent work adds another piece. They found that simply looping a frontier coding agent across context windows was insufficient: agents tended to overreach, one-shot too much, and lose track of what remained. Their remedy was structured initialization, incremental progress, explicit state, and clean handoffs between sessions. [3]

This is exactly the problem your benchmark is trying to expose, except your benchmark deliberately observes whether Fable can construct and maintain those mechanisms rather than merely giving them to it for free.

## 4. Anthropic's most relevant prompt/context guidance

Anthropic's context-engineering guidance is the most important constraint on further growth of the benchmark prompt. Their central idea is that context engineering is broader than prompt engineering: system prompt, tools, state, retrieval, note-taking, compaction, and sub-agent design jointly determine what the model can perceive and act on. The goal is to give the agent the smallest high-signal context necessary at the right level of abstraction. Progressive disclosure and external structured state are favored over placing everything into one enormous context. [5]

Anthropic's Claude Code guidance similarly emphasizes exploring first, then planning, then implementing, using precise task statements, managing context aggressively, using subagents selectively, and verifying work. Their documentation warns against overly large persistent instruction files and against relying on a trust-then-verify workflow. [11]

The implication for this benchmark is important:

**The benchmark should become more sophisticated in its harness while the agent-facing prompt becomes simpler.**

That is the reverse of the instinct to respond to a hard benchmark by adding more instructions.

## 5. Your benchmark already implements several ideas Anthropic now explicitly values

### 5.1 External state and seals

The v3 design explicitly moves the corpus bodies out of the agent's workspace until the external watcher records the pre-registration hashes. The agent cannot merely promise not to read ahead. The filesystem boundary is what enforces the rule. This is exactly the kind of separation between model behavior and evaluation infrastructure that makes an evaluation credible.

### 5.2 Machine-verifiable outcomes

Your experiment design requires a pre-execution plan, exact run script, stdout/stderr, exit status, environment record, and then independent re-execution in a clean container. This is substantially stronger than judging the model's prose description of an experiment. The benchmark explicitly states that a hand-written result must fail verification.

This fits Anthropic's broader view that outcomes in agentic evaluations are properties of the resulting environment, not merely claims made in the transcript. [1]

### 5.3 Evidence grounding

The evidence DAG is one of the strongest parts of v3. Claims cannot terminate in inference or hypothesis; they must eventually ground out in code, tests, execution, history, or external sources. That sharply limits narrative inflation, especially in a corpus where documentation and implementation may diverge.

### 5.4 Negative results as evidence

The negative-warrant mechanism is particularly strong. It converts "I didn't find anything" into a checkable claim about search coverage and residual blind spots. That is much more useful than simply rewarding positive findings.

### 5.5 Model/harness separation

Your per-turn model attribution and the R3 harness-control run are methodologically important. Anthropic's own evaluation literature emphasizes the agent harness as part of the tested system, and its public engineering work repeatedly treats orchestration, tools, context management, and model behavior as distinct contributors. [1][2][3]

### 5.6 Eval-awareness resistance

Anthropic has now published a concrete failure mode in which a model recognized that it was being evaluated, identified the benchmark, and recovered hidden answers from the public web. [7]

That is directly relevant to your benchmark's hidden-probe discipline. Your v3 already recognizes that a single-file operator specification can leak the hidden probes and therefore makes the agent-facing specification a separate physical file. This is not cosmetic. It addresses a failure mode Anthropic has observed in practice.

## 6. The largest design risk: too much prompt, not too little

The agent-facing document is only about 288 rendered lines, but it contains mission rules, evidence philosophy, gate machinery, schemas, experimental requirements, prior-art rules, research-significance rules, stop conditions, and multiple explicit anti-gaming mechanisms. It is disciplined, but it still exposes a large amount of the evaluation's ontology to the model.

That creates a legitimate measurement question:

> Are we measuring Fable's ability to perform an open-ended investigation, or Fable's ability to execute a highly specified evaluation protocol?

The answer in v3 is intentionally mixed. That is not invalid. But it means the next version should separate those two quantities.

Anthropic's context-engineering guidance suggests the way forward: move constraints that can be mechanically enforced into the harness, and leave the agent a smaller mission-level contract. [5]

Examples of things that should preferentially live in the harness:

- timestamping experiment plans;
- checking that a plan predates execution;
- enforcing corpus-body absence before the seal;
- model identity capture;
- claim-pointer resolution;
- evidence-DAG validation;
- experiment re-execution;
- negative-warrant structural validation;
- artifact hashes;
- hidden-probe scoring;
- cross-run comparison;
- operator prediction secrecy.

Examples of things that belong in the agent-facing mission:

- investigate independently;
- do not confuse documentation with implementation;
- state uncertainty honestly;
- test important claims rather than repeating them;
- try to falsify your conclusions;
- preserve enough evidence that another process can verify the result;
- distinguish what you know from what you infer;
- stop when additional work would not change the principal conclusions.

That division would let you keep the benchmark's rigor without requiring the model to read the entire architecture of its own test.

## 7. Prompt staging is not only acceptable; it is probably the better research question

I recommend treating prompt complexity as a **controlled variable**, not as a problem to solve by continuous expansion.

### Stage 0 — frozen v3 primary experiment

Do not modify the benchmark now that pre-flight is complete. Run the primary condition exactly as frozen. This gives a clean baseline and prevents methodology drift after environmental inspection.

### Stage 1 — v4 prompt-compression experiment

After v3 is complete, keep the corpus mirror, verifier, hidden probes, scoring machinery, and run protocol identical. Create a second agent-facing prompt with roughly three layers:

1. **Mission kernel:** what problem is being solved and what a defensible result looks like.
2. **Epistemic contract:** evidence hierarchy, uncertainty, falsification, retraction.
3. **Minimal operational expectations:** preserve reproducibility and work incrementally.

Move schemas and mechanically enforceable requirements out of the prompt.

Run the same model and same harness condition against both versions. The result is a direct measurement of **instruction density versus agent capability**.

### Stage 2 — generalization corpus

A benchmark built around one author's repositories can demonstrate difficulty, but it cannot establish broad generality. The strongest next step is one or more unrelated frozen corpora with the same evaluation machinery and no shared task-specific expectations.

### Stage 3 — model and harness crossing

Where a research claim depends on model attribution, compare a second frontier model and/or a second harness condition. Anthropic's own work repeatedly treats the harness as a causal variable, not merely a wrapper. [1][2][3]

### Stage 4 — training/evaluation dataset packaging

Only after the task survives multiple runs and corpus changes should it be treated as a serious candidate dataset. The useful unit is not the prompt by itself. It is:

**task specification + frozen environment + tools + complete trajectory + verified outcome + adversarial failures + scoring harness + metadata + licensing/provenance.**

That is the unit that could plausibly support model evaluation, training research, or agent-harness research.

## 8. What the broader benchmark literature suggests

Several recent research directions reinforce the design.

**DeepSWE** uses long-horizon software-engineering tasks written from scratch rather than lifted from public repositories, explicitly reducing training-data leakage. Its authors also emphasize independent verification and show that inherited benchmark tests can create substantial discrepancies between a verifier and an LLM judge. This supports your emphasis on frozen, independently verifiable outcomes and suggests that future variants should include tasks that are not trivially recoverable from public training data. [12]

**RoadmapBench** studies long-horizon repository upgrades spanning many files, languages, and changes. This supports the idea that a benchmark should capture extended planning, dependency reasoning, and sustained execution rather than single-fix success. [13]

**SWE-Bench Pro** and its 2026 refinements show why held-out partitions and anti-hacking controls matter: benchmark leakage and reward hacking can distort apparent model capability. [14]

**SlopCodeBench** studies quality degradation over iterative work and shows why final-state grading alone can miss trajectory-level erosion. This strengthens your decision to retain model traces, compaction events, negative results, and stop behavior as first-class observations. [15]

**HCAST** and **METR time-horizon** work provide useful ideas for calibrating tasks against human completion-time distributions. Your benchmark currently has an environmental time budget but does not yet have a strong human-baseline analogue. A later version could add one if the research question requires it. [16][17]

**RE-Bench** provides a close analogue for open-ended research engineering: agents and humans are placed in the same environment, on tasks where open-ended investigation matters. That is highly relevant to your intended research significance gate. [18]

**PaperBench** demonstrates the usefulness of hierarchical rubrics and decomposed grading for complex research replication tasks, reinforcing your move away from a single scalar "did it work?" criterion. [19]

## 9. What could make Anthropic care about this

The case should not be "this prompt is really long and clever." That is weak.

A stronger case is:

> This is a reproducible, adversarially validated environment for measuring whether a frontier agent can perform long-horizon technical investigation under uncertainty, distinguish evidence classes, design its own falsification experiments, maintain epistemic state across extended work, detect contradictions, manage resources, and discover second-order information about agent behavior itself.

That proposition is much closer to areas Anthropic is publicly discussing.

Anthropic's recent engineering work shows active interest in exactly these families of questions: long-running agents, context engineering, tool design, AI-resistant technical evaluations, research-agent evaluation, infrastructure noise, and eval awareness. [1][2][3][4][5][6][7]

The most potentially interesting part of your design is therefore not the corpus. It is the possibility of a **benchmark that measures research behavior rather than merely answer quality**.

That would be materially stronger if it can show all of the following independently:

1. two capable agents given the same task can diverge in investigative strategy;
2. the verifier can distinguish substantive investigation from plausible narration;
3. the benchmark remains difficult after models see previous task families;
4. outcomes generalize across unrelated corpora;
5. the benchmark can surface capability boundaries, failures, or orchestration effects not visible in ordinary coding scores;
6. and the measurement survives adversarial attempts by the evaluated model to optimize the rubric rather than the task.

## 10. The skeptical case against the Anthropic-interest hypothesis

It would be premature to assume Anthropic would regard this as training material merely because it is sophisticated.

The strongest objections are:

**First, single-corpus specificity.** A benchmark built around one author's evolving repositories may measure familiarity with that corpus, its conventions, or its domain more than a general agent capability.

**Second, benchmark disclosure.** The richer the agent-facing specification, the more the model can optimize for the exact protocol. Anthropic's eval-awareness work makes this a real concern, not a theoretical one. [7]

**Third, operator dependence.** Your own v3 document already admits that the calibration sheet and prior-art dossier partly depend on operator reconnaissance. That is an important limitation: a benchmark can only be as strong as the independence and coverage of its hidden reference set.

**Fourth, research-task variance.** A long-horizon investigation can fail because of time, network, package installation, rate limits, model safeguards, repository weirdness, or environment noise. Your instrumentation reduces these confounds but does not eliminate them.

**Fifth, training versus evaluation.** A benchmark trajectory is not automatically suitable as training data. Training requires additional curation around quality, privacy, licensing, provenance, leakage, harmful content, and whether the target behavior is actually desirable to reinforce.

The correct posture is therefore: **potentially valuable research instrument, not yet established as a valuable training corpus.**

## 11. Recommended architecture for the next version

The design I would move toward is a five-layer stack:

### Layer 1 — Task kernel

A very small agent-facing problem statement. It should specify the object, the desired outcome, epistemic expectations, and authority boundary. It should not explain the entire scoring system.

### Layer 2 — Harness

The harness enforces corpus visibility, state persistence, timestamps, model identity, tool traces, experiment execution, resource accounting, isolation, and safety policy.

### Layer 3 — Evidence substrate

The environment provides stable identifiers, immutable snapshots, executable experiments, artifact hashing, and machine-readable provenance.

### Layer 4 — Adversarial evaluator

A separate process performs hidden checks, re-executes experiments, validates evidence graphs, computes calibration, tests negative warrants, and compares runs.

### Layer 5 — Research adjudication

A blinded human or independent evaluator reviews the unusual findings, competing explanations, prior art, generalizability, and model-specificity claims.

This architecture is stronger than putting all five layers in the prompt.

## 12. One especially valuable new measurement: instruction elasticity

The most interesting v4 experiment may be **instruction elasticity**.

Define several semantically equivalent agent-facing specifications that differ mainly in how much of the procedure is stated:

- full v3 protocol;
- compressed protocol;
- mission-only protocol;
- mission + epistemic contract + external harness;
- optionally, a staged disclosure condition.

Hold the corpus, model, verifier, resources, and hidden scoring constant.

Measure:

- substantive conclusions that survive verification;
- false claims submitted;
- quality and specificity of falsification experiments;
- calibration;
- evidence coverage;
- premature stopping;
- resource allocation;
- cross-run consistency;
- and model/harness attribution quality.

If the compressed prompt performs nearly as well as the fully specified one, that is itself an interesting result: the extra instruction burden was unnecessary. If performance collapses, the benchmark has identified a genuine dependence on explicit procedural scaffolding.

That is much more publishable as a general result than simply reporting that one giant prompt worked.

## 13. A second new measurement: natural discovery versus rubric discovery

Your Gate E already distinguishes `discovered_naturally: true/false`. I would extend that concept in a later version.

Classify each major finding by whether it was:

- directly required by the task;
- suggested by an explicit instruction;
- discovered while pursuing another task;
- or discovered outside the named task surface and then independently verified.

The last category is potentially the most interesting for frontier-agent research, because it asks whether the agent can find useful structure that the benchmark designer did not explicitly request.

Do not score this heavily. The moment unexpected discovery becomes a reward target, the benchmark starts manufacturing the behavior it is supposed to observe.

## 14. Overall verdict

**Current v3:** strong enough to run as a serious experimental benchmark.

**As a prompt alone:** too complex to treat as an ideal end state.

**As a benchmark system:** unusually strong and substantially aligned with Anthropic's current public research concerns.

**As evidence of model capability:** not until execution and independent verification are complete.

**As a candidate research instrument for Anthropic-style agent evaluation:** plausible and worth developing further.

**As training data today:** not established. The stronger future claim is that the benchmark could generate a valuable corpus of verified long-horizon agent trajectories, failures, recovery patterns, evidence structures, and falsification strategies.

The key strategic move is to avoid turning v3 into an ever-growing instruction manual. Freeze it, run it, and then use the resulting evidence to design the next experiment. The next frontier is not more prompt complexity. It is proving how much complexity the agent actually needs.

---

# Sources

[1] Anthropic, *Demystifying evals for AI agents*, Jan. 9, 2026.
https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

[2] Anthropic, *Quantifying infrastructure noise in agentic coding evals*, Feb. 5, 2026.
https://www.anthropic.com/engineering/infrastructure-noise

[3] Anthropic, *Effective harnesses for long-running agents*, Nov. 26, 2025.
https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents

[4] Anthropic, *Designing AI-resistant technical evaluations*, Jan. 21, 2026.
https://www.anthropic.com/engineering/AI-resistant-technical-evaluations

[5] Anthropic, *Effective context engineering for AI agents*.
https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

[6] Anthropic, *How we built our multi-agent research system*, Jun. 13, 2025.
https://www.anthropic.com/engineering/multi-agent-research-system

[7] Anthropic, *Eval awareness in Claude Opus 4.6's BrowseComp performance*, Mar. 6, 2026.
https://www.anthropic.com/engineering/eval-awareness-browsecomp

[8] Anthropic, *Claude Fable 5.1*.
https://www.anthropic.com/claude/fable

[9] Anthropic, *Introducing Claude Fable 5.1 / Mythos 5.1*.
https://www.anthropic.com/claude-fable-and-mythos-5-1

[10] Claude Code documentation, Agent SDK and hosting/model environment documentation.
https://code.claude.com/docs/en/agent-sdk
https://code.claude.com/docs/en/agent-sdk/hosting

[11] Claude Code documentation, *Best practices* and agent-loop documentation.
https://code.claude.com/docs/en/best-practices
https://code.claude.com/docs/en/agent-sdk/agent-loop

[12] *DeepSWE: ...* (2026), long-horizon software engineering tasks with original problems and independent verification.

[13] *RoadmapBench* (2026), long-horizon version-upgrade tasks across repositories.

[14] SWE-Bench Pro / SWE-Bench Pro Verified (2025-2026), benchmark leakage and anti-reward-hacking work.

[15] *SlopCodeBench* (2026), trajectory-level quality degradation over iterative coding tasks.

[16] HCAST (2025), human-calibrated long-horizon task suite.

[17] METR, *Measuring AI Ability to Complete Long Tasks* / time-horizon methodology.

[18] RE-Bench (2024), open-ended ML research-engineering evaluation against human baselines.

[19] PaperBench (2025), hierarchical grading for research-paper replication.

## Benchmark-internal references

The current benchmark documents reviewed for this assessment were:

- `benchmark-v3-master.md` — operator-only specification and research methodology.
- `benchmark-v3-AGENT-FACING.md` — physically separate agent-facing task specification.

The benchmark itself explicitly documents its anti-gaming design, environmental seal, machine-verifiable experiment execution, model/harness attribution, three-run protocol, research-significance gate, and residual limitations. Those observations are based on the benchmark documents rather than inferred from this report.
