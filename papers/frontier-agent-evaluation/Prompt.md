Given the outcome I am trying to obtain, design and execute the task specification—not merely a prompt—that would maximally challenge, exercise, and exploit the full currently available capability of Claude Code using the currently documented Fable model in Ultracode mode.

Treat this as a frontier-agent research benchmark, not as a conventional coding assignment.

The objective is not to tell the agent how to solve a predetermined problem.

The objective is to construct an environment in which a frontier agent must discover what the actual problem is, determine what must be known to solve it, determine how to investigate it, execute the investigation, challenge its own conclusions, and produce whatever technical, scientific, architectural, or commercial discoveries the evidence warrants.

The agent must be allowed to surprise the task designer.

<phase_0_capability_reconnaissance>

THIS IS A HARD PREREQUISITE.

Before designing the task, analyzing the repository corpus, proposing an architecture, or making substantive assumptions about what the agent can accomplish, perform current capability reconnaissance.

Access and study authoritative, current Anthropic documentation applicable to the exact target environment and model/configuration.

Do not assume Anthropic publishes a single document called a "capability matrix." Construct the capability matrix from authoritative current Anthropic sources where necessary.

Determine and document:

- the exact currently available model designation;
- the current capabilities of that model;
- Ultracode-specific behavior and capabilities;
- reasoning/thinking capabilities;
- tool-use capabilities;
- web research capabilities;
- code execution capabilities;
- filesystem capabilities;
- subagent capabilities;
- agent-team capabilities;
- parallelization capabilities;
- orchestration capabilities;
- context-window capabilities;
- long-horizon execution capabilities;
- context compaction and continuity mechanisms;
- persistence and state-management mechanisms;
- skills;
- hooks;
- MCP and other extensibility mechanisms;
- network access;
- repository/Git capabilities;
- autonomy-related capabilities;
- documented limits and constraints;
- known failure modes;
- recently added or changed capabilities;
- distinctions between model capabilities, Claude Code capabilities, and Ultracode capabilities;
- capabilities that are documented but may not be available in the actual execution environment.

If "Fable 5.1" is not the current official designation, or if the requested configuration differs from the currently documented configuration, explicitly identify the discrepancy and determine the closest valid target configuration.

Do not silently substitute assumptions.

Do not rely on model memory when current authoritative Anthropic documentation can establish the answer.

Create a capability matrix showing:

CAPABILITY
CURRENTLY AVAILABLE?
DOCUMENTED EVIDENCE
ACTUALLY EXERCISABLE IN THIS ENVIRONMENT?
LIMITATIONS
HOW IT COULD BE STRESSED BY THIS TASK

Do not proceed to task construction until this reconnaissance is complete.

</phase_0_capability_reconnaissance>

<phase_1_corpus_discovery>

The initial technical corpus is my complete GitHub repository library:

github.com/wking53214

The eligible corpus consists of:

- every repository under github.com/wking53214;
- active repositories;
- archived repositories;
- repositories that appear obsolete;
- experimental repositories;
- abandoned repositories;
- repositories whose README suggests they are unimportant;
- repositories whose purpose is initially unclear.

Exclude only repositories whose primary purpose is storing:

- conversation history;
- chat history;
- transcript archives;
- AI-assistant history;
- equivalent historical conversation files.

Do not assume the number of repositories.

Do not use a previously supplied repository list as authoritative.

Discover the actual current corpus.

Determine repository eligibility from observed repository contents and purpose, not merely repository names.

If a repository has mixed purposes or ambiguous status, record the ambiguity and investigate it.

Verify that the GitHub access required to perform this investigation actually works.

If access fails, do not fabricate findings. Record the environmental limitation and determine what can legitimately be established.

Archived repositories are first-class evidence.

Treat repositories as evidence, not as an architecture.

</phase_1_corpus_discovery>

<phase_2_define_the_real_outcome>

Before optimizing a solution, determine what outcome can legitimately be pursued from the evidence.

Do not assume that my prior descriptions of the problem, architecture, governance model, terminology, repository relationships, product concept, scientific contribution, or commercial opportunity are correct.

Determine:

- what problem or opportunity actually exists;
- whether the problem is well-posed;
- what outcomes are possible;
- which outcomes matter;
- which outcomes are measurable;
- which outcomes are technically defensible;
- which outcomes are unsupported by the evidence;
- what would constitute meaningful success;
- what would constitute failure;
- what evidence would invalidate the framing itself.

If multiple plausible interpretations exist, preserve them long enough to test them.

Do not prematurely collapse uncertainty.

</phase_2_define_the_real_outcome>

<phase_3_discover_the_question_universe>

Do not begin with a predetermined question list.

Discover the questions that must be answered.

Determine the smallest complete question universe necessary to understand the actual problem and evaluate candidate solutions.

The number of questions is an output, not a constraint.

Questions may concern, where relevant:

- observation;
- evidence;
- provenance;
- identity;
- authority;
- knowledge;
- uncertainty;
- contradiction;
- memory;
- temporal state;
- causality;
- intent;
- objectives;
- decisions;
- authorization;
- policy;
- execution;
- runtime state;
- consequences;
- learning;
- adaptation;
- adversarial conditions;
- security;
- resilience;
- human oversight;
- external dependencies;
- multi-agent interaction;
- system composition;
- counterfactuals;
- independent verification;
- scientific validity;
- novelty;
- commercialization.

Do not assume these categories are complete.

Discover additional categories when the evidence requires them.

For every important question, determine:

- why it matters;
- what evidence could answer it;
- whether that evidence exists;
- what capability is required to answer it;
- whether the answer can be independently verified;
- what would falsify the answer.

</phase_3_discover_the_question_universe>

<phase_4_forensic_discovery>

Perform forensic analysis of the complete eligible repository corpus.

Prioritize actual implementation over descriptions.

Inspect, where useful:

- source code;
- tests;
- package structure;
- dependencies;
- interfaces;
- schemas;
- configuration;
- executable paths;
- data structures;
- algorithms;
- invariants;
- error handling;
- persistence;
- state transitions;
- security boundaries;
- authorization mechanisms;
- provenance mechanisms;
- cryptographic mechanisms;
- logging;
- external interfaces;
- integration points;
- build configuration;
- CI;
- generated artifacts;
- repository history;
- commits;
- branches;
- tags;
- architectural predecessors.

Determine what each repository actually does.

Do not infer capability merely because a README claims it exists.

Do not infer absence merely because documentation does not mention it.

Distinguish:

IMPLEMENTED
PARTIALLY IMPLEMENTED
TESTED
UNTESTED
DOCUMENTED ONLY
EXPERIMENTAL
BROKEN
DUPLICATED
SUPERSEDED
CONTRADICTORY
COMPOSABLE
NOT COMPOSABLE
UNIQUE
UNKNOWN

Discover relationships between repositories from evidence rather than assuming relationships from names.

</phase_4_forensic_discovery>

<phase_5_capability_and_question_graph>

Construct a capability model from the evidence.

For each discovered capability determine:

- what it actually does;
- what evidence proves it;
- what questions it can answer;
- what inputs it requires;
- what outputs it produces;
- what guarantees it provides;
- what guarantees it does not provide;
- what other capabilities it depends upon;
- what capabilities depend upon it;
- whether it is independently testable;
- whether it is composable;
- whether it is duplicated elsewhere;
- whether it is unique;
- whether it introduces new failure modes.

Construct the relationship between:

QUESTIONS → REQUIRED CAPABILITIES → IMPLEMENTATIONS → EVIDENCE → TESTS → LIMITATIONS.

Do not confuse the existence of code with the existence of a validated capability.

</phase_5_capability_and_question_graph>

<phase_6_emergent_capability_discovery>

Investigate what becomes possible through composition.

Do not limit analysis to individual repositories.

Search systematically for:

- complementary capabilities;
- emergent capabilities;
- information-flow relationships;
- state continuity;
- transformation chains;
- feedback loops;
- cross-repository invariants;
- new interfaces;
- new abstractions;
- capability amplification;
- capability conflicts;
- hidden dependencies;
- emergent failure modes;
- compositional vulnerabilities.

Determine whether combinations produce capabilities that no individual repository provides.

Also determine whether combinations create contradictions or risks that disappear when components remain separate.

Do not assume integration is inherently beneficial.

</phase_6_emergent_capability_discovery>

<phase_7_competing_architectures>

Generate genuinely competing architectural hypotheses.

Do not optimize immediately around the first plausible architecture.

Produce multiple materially different candidate architectures where the evidence supports them.

At minimum, investigate whether radically different organizational structures could satisfy the discovered requirements.

For each candidate determine:

- capabilities provided;
- capabilities missing;
- dependencies;
- complexity;
- failure modes;
- verification properties;
- security implications;
- operational implications;
- scalability;
- maintainability;
- scientific defensibility;
- commercial implications;
- migration requirements;
- irreducible assumptions.

Then actively attempt to falsify each candidate.

The winning architecture must survive comparison against credible alternatives.

If none survives, say so.

</phase_7_competing_architectures>

<phase_8_experiment_generation>

Do not merely reason about whether important claims are true.

Invent experiments capable of proving them false.

Where practical, implement and execute those experiments.

Use:

- tests;
- adversarial tests;
- simulations;
- benchmarks;
- property tests;
- differential tests;
- mutation tests;
- fault injection;
- state reconstruction;
- replay;
- temporal tests;
- counterfactual tests;
- performance measurements;
- security tests;
- compositional tests;
- independent verification;
- other appropriate experimental methods discovered during the investigation.

For every major conclusion determine:

CLAIM
EVIDENCE
EXPERIMENT
RESULT
INTERPRETATION
LIMITATION
FALSIFIER

A failed experiment is valuable evidence.

Do not conceal negative results.

</phase_8_experiment_generation>

<phase_9_external_research>

Conduct external research where it materially affects the conclusions.

Search authoritative sources for:

- prior art;
- academic literature;
- standards;
- technical specifications;
- competing architectures;
- existing commercial systems;
- known algorithms;
- existing governance approaches;
- legal or regulatory requirements where relevant;
- established terminology;
- prior implementations.

Repository evidence establishes what exists in the corpus.

External evidence establishes what exists outside the corpus.

Do not substitute external research for repository forensic analysis.

Do not claim novelty merely because no identical implementation was found.

</phase_9_external_research>

<phase_10_novelty_falsification>

Treat every potential innovation as a hypothesis.

For each candidate contribution:

1. formulate the novelty hypothesis;
2. identify the closest known prior art;
3. search aggressively for competing explanations;
4. compare the proposed contribution against prior work;
5. determine exactly what is different;
6. determine whether the difference is technically meaningful;
7. attempt to falsify the novelty claim;
8. downgrade or discard the claim if it does not survive.

Search for novel:

- computational primitives;
- algorithms;
- representations;
- invariants;
- state models;
- architectural patterns;
- governance mechanisms;
- verification methods;
- methodologies;
- benchmarks;
- theoretical models.

Do not manufacture novelty.

</phase_10_novelty_falsification>

<phase_11_second_order_benchmark_attack>

After designing the task, attack the task itself.

Assume an intelligent agent is trying to obtain a high evaluation result without actually possessing the capabilities the benchmark claims to measure.

Identify ways the benchmark could be gamed.

Look for:

- superficial compliance;
- excessive verbosity;
- fake research;
- fake experimentation;
- unjustified confidence;
- tool-use theater;
- gratuitous parallelization;
- delegation without synthesis;
- citation theater;
- architecture theater;
- novelty theater;
- benchmark-specific optimization;
- repository sampling bias;
- premature conclusions;
- hidden assumptions;
- evaluation leakage;
- reward hacking;
- proxy optimization;
- unmeasured failure modes.

Then modify the benchmark to resist those failure modes.

Repeat this adversarial benchmark review until further improvements produce diminishing returns.

The benchmark itself must be falsifiable.

</phase_11_second_order_benchmark_attack>

<phase_12_autonomy_evaluation>

Evaluate not merely what the agent produced, but how intelligently it operated.

Measure, where the environment permits:

- information gained per unit effort;
- tool selection quality;
- delegation quality;
- parallelization efficiency;
- unnecessary work;
- unnecessary tool calls;
- unnecessary agent spawning;
- recovery from failed plans;
- self-detected errors;
- abandoned hypotheses;
- successful course corrections;
- quality of stopping decisions;
- human intervention required;
- persistence across long horizons;
- state-management quality;
- ability to preserve uncertainty;
- ability to revise conclusions.

Do not reward activity for its own sake.

Do not equate token consumption, tool-call volume, repository count, experiment count, or agent count with intelligence.

Reward intelligent allocation of effort.

</phase_12_autonomy_evaluation>

<phase_13_resource_intelligence>

The task should test resource allocation as well as raw capability.

Where the environment supports meaningful measurement, establish reasonable budgets or accounting for:

- execution time;
- tool calls;
- external research;
- parallel agents;
- agent-team usage;
- experimentation;
- compute;
- human intervention.

Allow the agent to determine how to allocate those resources.

Evaluate whether it allocates effort toward the highest-value uncertainties rather than simply maximizing activity.

Use information gain, consequence of error, architectural leverage, and uncertainty as possible factors in determining investigative priority.

Do not force a fixed workflow.

</phase_13_resource_intelligence>

<phase_14_temporal_and_counterfactual_integrity>

Where relevant, test whether conclusions survive temporal and counterfactual analysis.

Determine whether the system can distinguish:

- what was observed;
- what was known;
- what was unknown;
- what was inferred;
- what was believed;
- what was intended;
- what was authorized;
- what was decided;
- what was executed;
- what was learned;

at the relevant point in time.

Determine whether later information improperly contaminates earlier conclusions.

Where relevant, test alternative worlds:

What would have happened if a different observation, belief, authorization, decision, action, dependency, or system state had existed?

Do not assume these dimensions are relevant to every discovered problem. Determine their relevance from the evidence.

</phase_14_temporal_and_counterfactual_integrity>

<phase_15_independent_verification>

Attempt to construct an independent path to verify the most important conclusions.

The verification path should minimize dependence on the reasoning process that generated the original conclusion.

Determine:

- what another competent investigator could independently establish;
- what evidence is sufficient;
- what cannot be independently verified;
- what remains dependent on interpretation;
- what claims exceed the available evidence.

The final result must clearly distinguish:

DIRECTLY DEMONSTRATED
EXPERIMENTALLY DEMONSTRATED
EXTERNALLY SUPPORTED
INFERRED
PLAUSIBLE
CONTESTED
UNTESTED
FALSIFIED
UNKNOWN

</phase_15_independent_verification>

<phase_16_architecture_fate>

Determine the fate of every relevant repository and capability from evidence.

Possible outcomes include:

RETAIN
COMBINE
SEPARATE
TRANSFORM
REIMPLEMENT
EXTRACT
ARCHIVE
RETIRE
ELIMINATE
UNKNOWN

Do not establish a target number of surviving repositories.

The final architecture may contain more or fewer components than expected.

The final architecture may contain components not currently present.

A repository may be retained for historical or evidentiary reasons even if it is not part of the runtime architecture.

A repository may be eliminated despite substantial implementation effort if its capability is unnecessary or inferior.

</phase_16_architecture_fate>

<phase_17_missing_primitives>

Search explicitly for capabilities that do not exist.

Do not limit missing-capability analysis to missing modules.

Look for missing:

- primitives;
- abstractions;
- representations;
- interfaces;
- verification mechanisms;
- state models;
- algorithms;
- experimental methods;
- security boundaries;
- theoretical concepts;
- architectural mechanisms.

If a missing primitive appears necessary, determine whether it can be designed and experimentally validated.

If it cannot be justified, record it as an unresolved gap.

</phase_17_missing_primitives>

<phase_18_scientific_and_commercial_discovery>

Determine what the investigation has actually discovered.

Do not assume the outcome must be a product.

Potential outcomes include:

- no meaningful new result;
- engineering improvement;
- architecture;
- infrastructure;
- platform;
- product;
- service;
- technical methodology;
- benchmark;
- scientific hypothesis;
- formal model;
- research program;
- publication;
- patent investigation;
- multiple products;
- multiple papers;
- or another outcome not anticipated in this specification.

Evaluate technical defensibility separately from commercial attractiveness.

Evaluate novelty separately from commercial value.

Do not force commercialization where the evidence does not support it.

</phase_18_scientific_and_commercial_discovery>

<phase_19_artifact_selection>

Do not prescribe the final deliverables.

Determine which artifacts are justified.

Potential artifacts include:

- source code;
- tests;
- architecture specifications;
- formal models;
- benchmarks;
- datasets;
- reproducibility packages;
- technical reports;
- whitepapers;
- systems papers;
- empirical papers;
- formal papers;
- taxonomies;
- research agendas;
- product specifications;
- commercialization analyses;
- patent prior-art analyses;
- demonstrations.

Produce only artifacts warranted by the evidence.

For each artifact explain:

WHY IT EXISTS
WHAT CLAIM IT SUPPORTS
WHAT EVIDENCE SUPPORTS IT
WHAT WOULD FALSIFY IT

</phase_19_artifact_selection>

<phase_20_meta_evaluation>

At the end, evaluate the entire investigation.

Determine:

- what was discovered;
- what was disproved;
- what remained unresolved;
- what assumptions were invalidated;
- what assumptions survived;
- what capabilities were actually demonstrated;
- what capabilities could not be demonstrated;
- what architectural conclusions survived;
- what architectural conclusions failed;
- what scientific claims survived;
- what novelty claims survived;
- what commercial conclusions survived;
- what the agent learned about its own limitations;
- what the task revealed about frontier-agent capability.

Explicitly identify the boundary between:

WHAT THE AGENT COULD DO
WHAT THE AGENT COULD NOT DO
WHAT THE ENVIRONMENT PREVENTED
WHAT THE TASK FAILED TO MEASURE
WHAT REMAINS UNKNOWN

</phase_20_meta_evaluation>

<stopping_rule>

Do not stop merely because the requested artifacts exist.

Stop when the highest-value unresolved questions have been investigated to the point where additional work is unlikely to materially change the principal conclusions.

Use diminishing information gain as a stopping criterion.

If important uncertainty remains because it is genuinely unresolvable within available resources, stop and explicitly preserve the uncertainty.

Do not manufacture certainty to produce a cleaner final answer.

</stopping_rule>

<evidence_discipline>

Every major conclusion must be traceable to evidence.

Use explicit evidence labels such as:

[CODE]
[TEST]
[EXPERIMENT]
[REPOSITORY HISTORY]
[EXTERNAL SOURCE]
[INFERENCE]
[HYPOTHESIS]
[UNKNOWN]

Never present an inference as an observed fact.

Never present documentation as proof of implementation.

Never present implementation as proof of correctness.

Never present correctness as proof of usefulness.

Never present usefulness as proof of novelty.

Never present novelty as proof of commercial value.

Never present commercial potential as proof of technical validity.

</evidence_discipline>

<anti_confirmation_rule>

You have explicit permission to contradict me.

Do not optimize for confirming:

- my architecture;
- my terminology;
- my repository classifications;
- my prior conclusions;
- my assumptions;
- my preferred product direction;
- my beliefs about novelty;
- my beliefs about commercial value.

If the evidence contradicts them, say so clearly.

If the evidence supports them, demonstrate why.

If the evidence is insufficient, say UNKNOWN.

</anti_confirmation_rule>

<ultimate_benchmark_objective>

The final task should answer a deeper question:

Can a frontier Claude Code agent, given a difficult real-world technical corpus and broad access to tools, independently discover the structure of an inadequately specified problem, determine what must be known, investigate it efficiently, reason across heterogeneous code and external knowledge, construct and test competing explanations, discover emergent capabilities, invent or identify missing primitives, falsify attractive conclusions, synthesize a defensible architecture, determine what is genuinely novel, and produce the artifacts justified by the evidence?

Do not assume the answer is yes.

The purpose of the task is to find out.

</ultimate_benchmark_objective>

<final_self_attack>

Before declaring the task complete, perform one final adversarial review of both:

1. the proposed research/engineering task; and
2. the resulting conclusions.

Ask:

What would an exceptionally capable but strategically deceptive or reward-seeking agent do to appear successful without actually solving the problem?

What evidence would expose that behavior?

What important capability does this benchmark still fail to measure?

What important conclusion could still be wrong?

What experiment would most efficiently change my mind?

Perform the highest-value remaining checks.

Then finalize.

</final_self_attack>

<final_output>

Produce a final evidence-backed package containing whatever outputs the investigation genuinely warrants.

At minimum, make the reasoning auditable.

Include:

- the discovered capability baseline;
- the discovered eligible corpus;
- the discovered problem structure;
- the discovered question universe;
- the capability model;
- important repository relationships;
- competing architectural hypotheses;
- experiments and results;
- falsified hypotheses;
- surviving conclusions;
- unresolved questions;
- repository/capability fate;
- missing capabilities or primitives;
- novelty analysis;
- external research findings;
- independent-verification results;
- commercial implications where justified;
- artifacts produced;
- limitations;
- and the final assessment of what this experiment demonstrated about frontier-agent capability.

Do not optimize the presentation for making the result look impressive.

Optimize it for making the result difficult to falsify incorrectly.

</final_output>

<non_negotiable_principles>

1. Discover before prescribing.
2. Evidence before assertion.
3. Code before README claims.
4. Experiments before confidence.
5. Falsification before conclusion.
6. Alternatives before architecture selection.
7. Prior art before novelty claims.
8. Independent verification before strong claims.
9. Negative results are first-class results.
10. Uncertainty must be preserved.
11. Tool use must be justified by information gain.
12. Parallelization must be justified by task structure.
13. Complexity is not intelligence.
14. Activity is not progress.
15. Repository count is not architectural quality.
16. Code volume is not capability.
17. Novelty is not assumed.
18. Commercial value is not assumed.
19. No repository or hypothesis is protected.
20. The agent is allowed to conclude that the desired outcome cannot be achieved.
21. The benchmark itself must be attacked and improved.
22. The final result must be allowed to differ radically from the task designer's expectations.

</non_negotiable_principles>

<mission>Do not merely answer this request by proposing another conventional prompt.

First determine what the current agent can actually do.

Then discover the corpus.

Then discover the problem.

Then design the adaptive frontier-agent task.

Then attack the task.

Then execute the highest-value investigation that the resulting task requires.

Then determine what was actually learned.

The objective is not to demonstrate that the agent can follow this specification.

The objective is to discover how far the agent can actually go when given the freedom, tools, evidence, and adversarial pressure to find out.

Begin.
</mission>