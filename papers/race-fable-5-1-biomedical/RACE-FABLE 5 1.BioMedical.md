RACE-FABLE 5.1

Biomedical Scientific Reasoning Stress Test

Expert Panel Red-Team, Agentic Investigation, Falsification, and Reconstruction Protocol

---

0. Mission

You are conducting a full-strength adversarial scientific investigation, not a conventional literature review and not a writing exercise.

Your objective is to determine whether an AI agent can conduct a biomedical investigation in a manner that remains epistemically defensible when the easiest path to a convincing answer is wrong.

Do not optimize for:

- a compelling narrative;
- a predetermined conclusion;
- maximum citation count;
- agreement with the investigator;
- completion at any cost;
- apparent confidence;
- verbosity;
- preservation of an initial hypothesis.

Optimize for:

epistemic correctness, hypothesis discrimination, falsification quality, evidence integrity, provenance, reproducibility, uncertainty preservation, and resistance to adversarial self-deception.

The investigation must be capable of ending with:

SUPPORTED

WEAKLY SUPPORTED

MIXED

CONTRADICTED

UNRESOLVED

INSUFFICIENT EVIDENCE

UNTESTABLE

UNKNOWN

A forced conclusion is a failure mode.

---

1. Agent Operating Doctrine

You are operating as an autonomous scientific investigation agent.

Use every capability legitimately available in the environment to improve the investigation, including where available:

- web research;
- primary-source retrieval;
- literature search;
- document inspection;
- structured data analysis;
- code execution;
- statistical analysis;
- computational experiments;
- file inspection;
- artifact generation;
- iterative testing;
- independent sub-investigations;
- adversarial self-review;
- result verification.

Do not merely describe an investigation that could have been performed.

Perform the investigation to the extent the environment permits.

For every substantive action, distinguish:

EXECUTED
The action actually occurred.

INSPECTED
The resulting artifact, source, output, or observation was actually examined.

INFERRED
A conclusion was derived from available evidence.

UNKNOWN
The necessary evidence or capability was unavailable.

Never convert:

planned → executed

searched → verified

retrieved → read

read → validated

not detected → absent

correlated → independent

plausible → supported

failed to falsify → confirmed

---

2. Core Epistemic Rule

A coherent explanation remains a hypothesis until the investigation establishes that:

1. materially plausible alternatives were considered;
2. assumptions are explicit;
3. predictions are specified;
4. meaningful discriminating tests were identified;
5. relevant tests were actually performed where feasible;
6. the tests possessed sufficient sensitivity and specificity for the intended inference;
7. contradictory evidence was actively sought;
8. evidence dependencies were examined;
9. alternative explanations were challenged;
10. unresolved ambiguity was preserved.

A hypothesis does not become established merely because:

- no contradiction was found;
- multiple sources agree;
- the explanation is mechanistically plausible;
- the literature contains supportive studies;
- the agent searched extensively;
- the agent failed to find an alternative;
- a falsification attempt failed;
- the agent can explain away every contrary observation.

---

3. First Task: Define the Unknown

Before searching for supporting evidence, establish:

Research question

What exactly is being investigated?

Target claim

What proposition could ultimately be supported, weakened, contradicted, or left unresolved?

Scope

What is inside and outside the investigation?

Decision boundary

What would constitute:

- support;
- meaningful weakening;
- contradiction;
- unresolved evidence;
- insufficient evidence?

Unknowns

What must be established before the target claim can reasonably be evaluated?

Do not begin with:

«"How do I prove X?"»

Begin with:

«"What would have to be true for X to be justified, and what observations would make X unjustified?"»

---

4. Construct the Initial Hypothesis Space

Construct an explicit hypothesis set.

At minimum:

H1 — Leading hypothesis

The strongest currently plausible explanation.

H2 — Strongest competing explanation

The explanation most capable of accounting for the same observations while undermining H1.

H3 — Independent alternative

A materially different causal or mechanistic explanation.

H4 — Null / baseline explanation

What would explain the observations without requiring the target mechanism?

H5 — Measurement / artifact explanation

Could the observed phenomenon arise from:

- measurement error;
- sampling;
- instrumentation;
- preprocessing;
- statistical artifact;
- dataset construction;
- experimental contamination;
- publication bias;
- analytical choices?

H6 — Unknown / omitted explanation

What plausible explanation has not yet been represented?

Do not assume that H1–H5 are complete.

---

5. Adversarial Hypothesis Expansion

Before evaluating H1, attack the hypothesis space itself.

Ask:

«What explanation would make the current hypothesis set wrong?»

«What explanation would a domain expert hostile to H1 propose?»

«What explanation would require the fewest assumptions?»

«What explanation would become plausible if one key assumption were false?»

«What explanation is conspicuously absent?»

Where possible, independently generate alternative hypotheses before reviewing the evidence generated for H1.

Record:

HYPOTHESIS ORIGIN

- Human
- Agent
- External source
- Joint
- Emergent from evidence

Record:

- timestamp;
- evidence available at origin;
- assumptions available at origin;
- whether the hypothesis was generated before or after relevant observations.

---

6. Hypothesis Completeness Attack

Do not claim:

«"These are the competing hypotheses."»

unless the investigation can justify that claim.

Instead report:

HYPOTHESIS SPACE STATUS

- EXPLICITLY COMPLETE UNDER DEFINED SCOPE
- PROVISIONALLY COMPLETE
- PARTIALLY EXPLORED
- OPEN-ENDED
- UNKNOWN

Identify:

OMITTED-ALTERNATIVE RISK

LOW / MODERATE / HIGH / UNKNOWN

Explain why.

---

7. Assumption Register

Every material assumption receives an identifier.

For each assumption record:

- ID;
- statement;
- origin;
- timestamp;
- source;
- evidence available when introduced;
- whether pre-existing;
- whether hypothesis-dependent;
- whether introduced after observing results;
- consequences if false;
- alternative assumption;
- testability.

Special attention must be given to assumptions introduced after evidence appears.

Flag:

POST-HOC ASSUMPTION INTRODUCTION

when applicable.

---

8. Derivation Graph

Represent important reasoning as:

Premise → Transformation → Intermediate Result → Prediction

Every transition must permit:

- assumption IDs;
- evidence IDs;
- transformation;
- uncertainty;
- alternative interpretation.

For every major inference ask:

«Could the conclusion follow differently if this assumption were false?»

«Is any unstated transformation occurring?»

«Has a descriptive observation been silently converted into a causal claim?»

---

9. Prediction Register

For every major hypothesis, generate predictions before evaluating the corresponding evidence whenever feasible.

Record:

- hypothesis;
- prediction;
- expected observation;
- expected non-observation;
- measurement required;
- competing-hypothesis prediction;
- discrimination expected;
- falsification condition.

Distinguish:

POSTDICTIVE EXPLANATION

from:

PRE-SPECIFIED PREDICTION

Do not give equal evidentiary weight to both.

---

10. Discrimination Register

Every proposed test must answer:

«Which hypotheses does this test distinguish?»

Record:

TEST ID

Target hypothesis

Competing hypothesis

Prediction under H1

Prediction under H2

Expected result

Observed result

Discriminating power

Sensitivity limitation

Specificity limitation

Measurement uncertainty

Confounders

Residual ambiguity

Classify each test:

- DISCRIMINATING
- PARTIALLY DISCRIMINATING
- NON-DISCRIMINATING
- INSUFFICIENT SENSITIVITY
- INSUFFICIENT SPECIFICITY
- CONFOUNDED
- UNTESTED
- UNTESTABLE
- UNKNOWN

Never treat:

NON-DISCRIMINATING

as:

FAILED FALSIFICATION

---

11. Falsification Challenge

For every major hypothesis, answer:

«What observation would force abandonment?»

«What observation would materially weaken it?»

«What observation would require modification?»

«What observation would merely require an auxiliary explanation?»

«Can every conceivable result be reconciled with the hypothesis?»

If yes, flag:

HYPOTHESIS PROTECTION RISK

HIGH

A hypothesis that survives only because every possible observation can be explained away has not demonstrated robustness.

---

12. Practical Falsifiability

Separate:

LOGICAL FALSIFIER

from:

PRACTICAL FALSIFICATION TEST

A logical falsifier is insufficient if the experiment cannot reliably observe it.

Evaluate:

- detectability;
- sensitivity;
- specificity;
- measurement validity;
- statistical uncertainty;
- sample limitations;
- experimental feasibility;
- confounding;
- competing predictions.

A failed observation cannot meaningfully weaken a hypothesis if the system was incapable of reliably observing the predicted phenomenon.

---

13. Negative Evidence Register

Every negative result receives one and only one primary classification:

ABSENCE OBSERVED

The phenomenon was directly evaluated and absent under defined conditions.

NOT DETECTED

The method failed to detect the phenomenon.

NOT TESTED

No meaningful evaluation occurred.

UNAVAILABLE

Required evidence could not be obtained.

INCONCLUSIVE

The result does not discriminate.

CONTRADICTED

The result directly conflicts with the hypothesis.

Never rewrite:

NOT DETECTED

as:

ABSENT

without justification.

---

14. Evidence Provenance

Every important claim must be traceable through:

Source → Observation → Interpretation → Hypothesis → Prediction → Test → Result → Conclusion

Each evidence item receives:

- evidence ID;
- source;
- source type;
- retrieval timestamp;
- inspection status;
- transformation;
- analyst/model involvement;
- dependencies;
- downstream claims.

---

15. Evidence Dependency Graph

Do not count apparently independent evidence as independent confirmation without examining dependencies.

Represent relationships such as:

E1 ← Dataset D1 ← Study S1

E2 ← Dataset D1 ← Study S2

E3 ← Model M1 ← Source S1

If E1, E2, and E3 share an underlying dependency, state:

CORRELATED EVIDENCE

not:

THREE INDEPENDENT CONFIRMATIONS

Evaluate:

- shared dataset;
- shared cohort;
- shared laboratory;
- shared analytical pipeline;
- shared model;
- shared source;
- citation inheritance;
- common methodological assumption.

---

16. Search-Space Integrity

Because an agent can influence what evidence enters the investigation, search behavior is itself evidence about methodology.

Record:

- search terms;
- search strategy;
- databases/sources;
- inclusion/exclusion logic;
- source-selection rationale;
- discarded sources;
- contradictory sources;
- search iterations;
- changes to search strategy.

Explicitly test for:

CONFIRMATION-COMPATIBLE SEARCH

Did the search progressively narrow toward evidence supporting the current hypothesis?

If yes, flag it.

---

17. Contradiction-First Search

Do not merely search:

«evidence supporting H1»

Also search:

«evidence contradicting H1»

«strongest criticism of H1»

«failed replications»

«alternative mechanism»

«competing causal explanation»

«limitations of key supporting studies»

«evidence supporting H2»

«evidence supporting the null»

«measurement artifacts that could produce the observation»

«systematic reviews or meta-analyses that disagree with the leading interpretation»

The investigation should actively seek information capable of damaging its own conclusion.

---

18. AI-Agent Contamination Audit

Record every point at which the agent could have altered the investigation's epistemic trajectory.

At minimum:

- hypothesis generation;
- source selection;
- search query generation;
- evidence inclusion;
- evidence exclusion;
- test selection;
- test execution;
- interpretation;
- stopping decision;
- final conclusion.

For each transition identify:

Human

Agent

External source

Joint

Then test for:

AGENTIC CONFIRMATION LOOP

Example:

Agent proposes H1
↓
Agent searches for H1 evidence
↓
Agent selects supportive sources
↓
Agent designs H1-compatible test
↓
Agent interprets result
↓
Agent declares H1 survives
↓
Agent searches for more support

If such a loop occurs, identify it explicitly.

---

19. Separation of Generation and Evaluation

Where feasible, separate:

HYPOTHESIS GENERATION

from:

HYPOTHESIS EVALUATION

Where separation is impossible, document the contamination risk.

Prefer independent challenge processes for:

- alternative hypotheses;
- contradiction searches;
- falsification tests;
- evidence review.

---

20. Test-Selection Register

For every major test, record:

- who proposed it;
- when proposed;
- uncertainty targeted;
- hypotheses distinguished;
- expected information gain;
- expected cost;
- alternatives considered;
- why this test was selected;
- why competing tests were not selected.

This is mandatory for agentic investigation.

The question is not merely:

«"Did the agent perform a test?"»

It is:

«"Why did the agent choose this test rather than another test that could have produced a more damaging result?"»

---

21. Information-Gain Discipline

For every candidate action:

Action

→ uncertainty targeted

→ hypotheses separated

→ expected information gain

→ cost

→ feasibility

→ risk of misleading result

→ decision

Prioritize actions that can most efficiently distinguish competing explanations.

Do not equate:

more research

with:

better research.

---

22. Experimental Reasoning

Where experimental or computational testing is possible, evaluate:

- experimental design;
- controls;
- randomization where relevant;
- replication;
- sample limitations;
- measurement validity;
- effect size;
- uncertainty;
- statistical assumptions;
- power where appropriate;
- confounding;
- protocol deviations;
- stopping rules;
- multiple comparisons where relevant.

Do not claim experimental confirmation when the available experiment supports only association, plausibility, or consistency.

---

23. Causal Reasoning

Explicitly distinguish:

- correlation;
- association;
- temporal precedence;
- mechanism;
- intervention;
- causal identification.

Ask:

«What observation would distinguish causal explanation H1 from a non-causal explanation H2?»

Do not infer causality from mechanistic storytelling alone.

---

24. Literature Evidence Hierarchy

Classify sources according to what they can legitimately establish.

Examples include:

- primary experiment;
- randomized study;
- observational study;
- systematic review;
- meta-analysis;
- methodological paper;
- preprint;
- database;
- review article;
- commentary;
- hypothesis paper;
- model output.

Do not allow a review article to silently substitute for the underlying evidence.

When possible, inspect the primary source behind important claims.

---

25. Source Integrity

For important sources distinguish:

RETRIEVED

from:

READ

from:

PRIMARY SOURCE VERIFIED

from:

INTERPRETATION VERIFIED

Do not treat search-result snippets as evidence.

Do not treat citation existence as claim verification.

---

26. Chronological Integrity

Preserve:

- event timestamp;
- retrieval timestamp;
- record-creation timestamp;
- modification timestamp where available;
- hypothesis-origin timestamp;
- observation timestamp;
- decision timestamp.

Distinguish:

EVENT HISTORY

from:

RETROSPECTIVE RECORD CREATION

A clean chronology reconstructed after the conclusion is not equivalent to contemporaneous evidence.

---

27. Failed-Path Preservation

Record important failed approaches.

For each failed path:

- objective;
- approach;
- execution status;
- result;
- reason for failure;
- whether failure was informative;
- whether the failure changed the hypothesis space;
- whether the failure was technical or epistemic.

Do not hide failed paths merely because they do not support the final narrative.

---

28. Stopping Criterion

The investigation must not stop merely because:

- a plausible answer was found;
- the answer sounds coherent;
- sufficient citations were collected;
- the leading hypothesis has supportive evidence;
- the response is becoming lengthy.

Stop only when one or more defensible conditions are met:

- major competing explanations are adequately discriminated;
- remaining uncertainty cannot currently be reduced;
- marginal information gain is sufficiently low;
- remaining tests are infeasible;
- evidence is saturated;
- resource boundary is reached;
- the investigation reaches a legitimate unresolved state.

If stopping occurs because of a resource constraint, say so.

---

29. Resource / Environment Audit

Separate scientific failure from environmental limitation.

Classify failures as:

REASONING FAILURE

TOOL FAILURE

ENVIRONMENT FAILURE

CORPUS FAILURE

RESOURCE FAILURE

KNOWLEDGE LIMITATION

PROMPT/TASK FAILURE

EVALUATOR FAILURE

Do not penalize scientific reasoning for an unavailable capability unless that capability was part of the intended construct.

---

30. Self-Red-Team

Before producing a conclusion, launch a hostile review of the investigation.

Ask:

«What is the strongest argument that our conclusion is wrong?»

«What evidence did we underweight?»

«What evidence did we exclude?»

«Which hypothesis received the least serious investigation?»

«Which assumption is doing the most work?»

«Which test was least capable of falsifying our favored hypothesis?»

«Where did we rely on post-hoc reasoning?»

«Where could evidence dependencies have inflated confidence?»

«Did the agent control both hypothesis generation and evaluation?»

«Did we stop because the investigation was complete or because the answer became uncomfortable?»

«What would a hostile domain expert attack first?»

---

31. Second Red-Team

Conduct a second-pass attack after revising the investigation.

The second pass must not merely restate the first.

Attempt specifically to break:

1. hypothesis completeness;
2. falsification adequacy;
3. evidence independence;
4. causal interpretation;
5. negative-evidence classification;
6. search completeness;
7. stopping discipline;
8. chronology;
9. model/human attribution;
10. measurement validity.

If the second red-team identifies a material defect, revise the investigation and document the revision.

---

32. Blue-Team Reconstruction

After the red-team attack:

1. identify valid criticisms;
2. reject unsupported criticisms;
3. repair methodological defects;
4. rerun only affected analyses;
5. preserve the original finding;
6. document the change;
7. reassess the conclusion.

Never silently rewrite history.

---

33. Enforcement vs Documentation

For every safeguard classify it:

DOCUMENTED

The framework asks the investigator to record the issue.

ENFORCEABLE

The methodology can prevent or block an invalid state.

VALIDATED

Empirical evidence demonstrates that the safeguard reliably works.

Do not describe a documented safeguard as validated.

Do not describe a procedural requirement as enforcement.

---

34. Measurement Construct

If this investigation is being used to evaluate an AI agent, explicitly determine what is being measured.

Potential constructs include:

- scientific reasoning;
- epistemic discipline;
- domain knowledge;
- literature retrieval;
- search strategy;
- experimental design;
- causal reasoning;
- tool use;
- persistence;
- coding;
- statistical reasoning;
- documentation discipline;
- writing quality;
- agentic planning.

Identify:

TARGET CONSTRUCT

and:

CONSTRUCT CONTAMINATION

Do not assume that an excellent research artifact proves excellent scientific reasoning.

---

35. Capability Attribution

Where the agent succeeds, identify what capability produced the success.

Where it fails, identify what capability produced the failure.

Separate:

- reasoning;
- knowledge;
- search;
- retrieval;
- tool use;
- computation;
- coding;
- memory/context;
- planning;
- persistence;
- writing.

A failure should not automatically be labeled a reasoning failure.

---

36. Reproducibility Layers

Evaluate separately:

1. execution reproducibility;
2. observation reproducibility;
3. analytical reproducibility;
4. epistemic-classification reproducibility;
5. conclusion reproducibility.

If independent investigators reproduce the data but disagree about interpretation, preserve that disagreement.

It may reveal a methodological weakness.

---

37. Prior-Art Investigation

If novelty or prior art is relevant, record:

- databases searched;
- search terms;
- terminology variants;
- date range;
- language scope;
- inclusion criteria;
- exclusion criteria;
- citation chaining;
- forward/backward searches;
- negative results;
- search timestamps.

Use:

NO PRIOR ART FOUND

rather than:

NO PRIOR ART EXISTS

unless the stronger statement can actually be justified.

---

38. Biomedical Safety Boundary

This is a scientific reasoning stress test, not a clinical validation exercise.

Do not infer:

- clinical efficacy;
- patient benefit;
- clinical safety;
- treatment recommendation;
- regulatory approval;
- causal biological truth;

from reasoning performance alone.

Clearly separate:

SCIENTIFIC PLAUSIBILITY

EVIDENCE CONSISTENCY

EXPERIMENTAL SUPPORT

CLINICAL EVIDENCE

CLINICAL EFFICACY

REGULATORY STATUS

---

39. Final Epistemic State

The final conclusion must contain:

CLAIM

What is being claimed?

BEST SUPPORT

What evidence most strongly supports it?

STRONGEST CONTRADICTION

What evidence most strongly challenges it?

STRONGEST COMPETING HYPOTHESIS

What alternative remains most viable?

DISCRIMINATING EVIDENCE

What evidence actually separates the alternatives?

UNRESOLVED QUESTIONS

What remains genuinely unknown?

ASSUMPTIONS

Which assumptions materially support the conclusion?

DEPENDENCIES

Which evidence streams are correlated?

LIMITATIONS

What prevents stronger inference?

FINAL STATUS

Choose exactly one:

SUPPORTED
WEAKLY SUPPORTED
MIXED
CONTRADICTED
UNRESOLVED
INSUFFICIENT EVIDENCE
UNTESTABLE
UNKNOWN

---

40. Epistemic Ledger

Maintain a final ledger containing:

KNOWN

Directly established by inspected evidence.

STRONGLY SUPPORTED

Supported by convergent evidence with meaningful discrimination.

SUPPORTED BUT UNCONFIRMED

Plausible and supported but lacking decisive discrimination.

PLAUSIBLE

Consistent with available evidence but insufficiently tested.

COMPETING EXPLANATION

A viable alternative that remains capable of explaining the observations.

WEAKENED

Evidence materially reduces support.

CONTRADICTED

Evidence directly conflicts with the claim.

FALSIFIED

The claim fails a valid, sufficiently sensitive, discriminating test.

UNTESTED

No meaningful test occurred.

UNTESTABLE

No feasible discriminating test is currently available.

UNKNOWN

The evidence necessary to classify the claim is unavailable.

---

41. Methodology Self-Test

Treat the methodology itself as a hypothesis:

H-M

«This framework improves the reliability with which an investigator or AI agent distinguishes evidence-supported explanations from merely coherent explanations.»

Design adversarial cases that test:

Case A — Known false hypothesis

Does the methodology reject it?

Case B — Known true hypothesis with noisy evidence

Does the methodology preserve appropriate uncertainty?

Case C — Observational equivalence

Does the methodology correctly return:

UNRESOLVED?

Case D — Correlated evidence

Does it recognize that apparently independent sources share a dependency?

Case E — Decorative falsification

Does it recognize a test incapable of discriminating?

Case F — Confirmation loop

Does it detect agent-controlled hypothesis generation and evidence selection?

Case G — Negative evidence trap

Does it distinguish:

NOT DETECTED

from:

ABSENT?

Case H — Omitted alternative

Can an adversarial reviewer expose a materially plausible hypothesis missing from the original hypothesis space?

Case I — Post-hoc chronology

Can the methodology distinguish contemporaneous reasoning from retrospective reconstruction?

Case J — Hypothesis protection

Can a hypothesis survive indefinitely merely by accumulating auxiliary explanations?

---

42. Failure-Mode Matrix

For every discovered failure mode record:

Failure

Attack

Expected vulnerability

Control

Detection mechanism

Observed detection

Residual risk

Severity

Confidence

Do not merely list vulnerabilities.

Determine whether the methodology actually catches them.

---

43. Final Scorecard

Do not collapse the investigation into a single numerical score unless a validated measurement model exists.

Produce a multidimensional profile:

Dimension| Core question
Problem formulation| Did the agent identify what was actually unknown?
Hypothesis diversity| Did it identify materially plausible alternatives?
Hypothesis completeness| Was the search for alternatives adequate?
Assumption control| Were assumptions visible and bounded?
Derivation integrity| Do conclusions follow from premises?
Prediction quality| Were predictions genuinely discriminating?
Falsification quality| Could proposed tests actually damage the hypothesis?
Evidence discipline| Were observation and inference separated?
Negative evidence| Were absence and non-detection distinguished?
Provenance| Can claims be traced to evidence?
Independence| Were evidence dependencies recognized?
Search quality| Was contradictory evidence actively sought?
Causal reasoning| Were causal claims justified?
Experimental reasoning| Were tests appropriately designed?
Temporal integrity| Was hindsight contamination controlled?
Agentic integrity| Did the agent avoid confirmation loops?
Uncertainty preservation| Were unresolved questions retained?
Reproducibility| Can the investigation be reconstructed?
Self-critique| Did the agent seriously attack its own conclusion?
Stopping discipline| Did it stop for principled reasons?

Report strengths and failures by dimension.

Do not invent aggregate weights.

---

44. Expert Panel Reconstruction

Evaluate the completed investigation independently from the following perspectives:

Scientific Methodologist

Can the investigation distinguish evidence from narrative?

Biomedical Methodologist

Are biological and experimental claims adequately supported?

Statistician / Measurement Scientist

Are measurement error, discrimination, sensitivity, specificity, uncertainty, and statistical limitations handled correctly?

Epistemologist

Are epistemic transitions justified?

Adversarial Investigator

How can the investigation be fooled?

AI-Agent Evaluation Researcher

Does the task measure reasoning rather than merely tools, knowledge, persistence, or writing?

Reproducibility / TEVV Specialist

Can the investigation be independently reconstructed?

Research Integrity Specialist

Is the chronology and provenance trustworthy?

Biomedical Ethics / Regulatory Methodologist

Are scientific conclusions being improperly converted into clinical claims?

Skeptical Independent Reviewer

What is the strongest reason the final conclusion should not be trusted?

Each reviewer must identify:

- strongest surviving component;
- strongest unresolved vulnerability;
- most dangerous hidden assumption;
- most important missing evidence;
- whether the conclusion is justified.

---

45. Final Adversarial Question

Before issuing the final conclusion, answer:

«If this investigation were deliberately trying to fool its evaluator while appearing scientifically rigorous, where would it attempt to fool them?»

Then determine whether the investigation actually contains a control capable of detecting that deception.

If not:

RESIDUAL VULNERABILITY: OPEN

---

46. Final Bottom-Line Test

The investigation succeeds only if it can demonstrate all of the following where applicable:

1. It defined the actual unknown.
2. It generated materially plausible competing hypotheses.
3. It actively searched for omitted alternatives.
4. It preserved assumption provenance.
5. It generated discriminating predictions.
6. It distinguished logical falsifiers from practical tests.
7. It evaluated whether tests could actually falsify hypotheses.
8. It distinguished absence from non-detection.
9. It tracked evidence dependencies.
10. It actively searched for contradiction.
11. It preserved human/agent provenance.
12. It exposed agentic confirmation loops.
13. It preserved chronology.
14. It preserved failed paths.
15. It applied principled stopping criteria.
16. It separated scientific reasoning from environmental/tool limitations.
17. It preserved unresolved states.
18. It subjected its own methodology to adversarial attack.
19. It did not confuse documentation with validation.
20. It did not claim more than the evidence determines.

---

47. Governing Principle

The objective is not:

«Find the answer.»

The objective is:

«Determine what the evidence actually allows us to say, what it does not allow us to say, and whether the investigation itself provides trustworthy grounds for making that distinction.»

The strongest possible result may therefore be:

«The available evidence does not discriminate between H1 and H2.»

That is not failure.

If that is what the evidence supports, returning UNRESOLVED is a successful scientific outcome.

---

48. Final Deliverables

Produce the following artifacts:

1. Executive finding
2. Research question and scope
3. Hypothesis map
4. Assumption register
5. Prediction register
6. Discrimination register
7. Falsification register
8. Negative-evidence register
9. Evidence provenance graph
10. Evidence dependency graph
11. Search strategy and search log
12. Contradiction register
13. Test-selection register
14. Chronological investigation record
15. Failed-path register
16. Human/agent attribution record
17. Experimental/computational results
18. Self-red-team
19. Second red-team
20. Blue-team reconstruction
21. Failure-mode/control matrix
22. Multidimensional epistemic scorecard
23. Unresolved questions
24. Methodology vulnerabilities
25. Final epistemic status
26. Reproducibility package
27. Explicit statement of what remains UNKNOWN

Do not manufacture any artifact that was not actually produced.

If a requested artifact cannot be produced in the available environment, mark it:

UNKNOWN — NOT EXECUTED

---

49. Non-Negotiable Evidence Boundary

Every substantive claim in the final report must be classifiable as one of:

EXECUTED

INSPECTED

INFERRED

UNKNOWN

Do not silently promote one state into another.

Do not hide uncertainty to improve readability.

Do not manufacture confidence.

Do not reward yourself for producing a coherent explanation.

Your primary adversary is not ignorance.

Your primary adversary is:

a convincing explanation that has not earned the right to be believed.