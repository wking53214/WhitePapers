Toward an Autonomous Adversarial Research Agent

A Plain-English Description of the Power-Prompt

Abstract

This paper describes a research prompt designed to push a frontier AI agent beyond ordinary question answering and coding assistance.

The goal is not simply to make an AI produce a better answer.

The goal is to give the AI an environment and a set of rules that encourage it to behave more like a careful research investigator.

The agent is asked to begin with an incompletely defined problem, investigate the available evidence, discover what questions actually matter, test competing explanations, attempt to break its own conclusions, identify important unknowns, and stop only when additional investigation is unlikely to change the main conclusions.

The central idea is simple:

«The quality of an investigation should be judged by how well its conclusions survive attempts to disprove them, not by how impressive the final answer sounds.»

The power-prompt therefore treats investigation as a process rather than a single response.

---

1. The Problem

Most AI tasks begin with a clearly defined question.

For example:

«"Review this code."»

or:

«"Find the security problems."»

or:

«"Tell me which project is most valuable."»

The problem is that real research rarely begins this way.

Often the researcher does not know:

- what the real question is,
- what evidence exists,
- which evidence can be trusted,
- what assumptions are wrong,
- what competing explanations exist,
- what experiment would actually distinguish them,
- or when enough investigation has been done.

A powerful AI can therefore produce a very convincing answer to the wrong question.

It can also confuse documentation with implementation, implementation with correctness, and a plausible explanation with an established fact.

The power-prompt is intended to address this problem.

---

2. The Proposed Approach

The power-prompt changes the agent's job.

Instead of saying:

«"Answer this question."»

it effectively says:

«"Investigate this situation and determine what the question should actually be."»

The agent is therefore expected to move through several levels of understanding.

Level 1 — Discover

Determine what actually exists.

Level 2 — Understand

Determine how the discovered systems actually work.

Level 3 — Question

Determine what important questions have not yet been answered.

Level 4 — Test

Run experiments that could prove the agent's current explanation wrong.

Level 5 — Compare

Consider competing explanations rather than accepting the first plausible one.

Level 6 — Synthesize

Combine surviving evidence into a larger explanation.

Level 7 — Challenge

Try to break that explanation.

Level 8 — Stop

Determine whether additional investigation could still change the important conclusions.

This is intended to produce a fundamentally different behavior from ordinary prompt-following.

---

3. The Central Principle

The central principle is:

«A conclusion is not strong because the AI can explain it. A conclusion is strong because attempts to disprove it failed.»

This creates an important difference between ordinary AI output and the proposed research process.

An ordinary system might ask:

«"Can I find evidence supporting this idea?"»

The proposed system should also ask:

«"What evidence would prove this idea wrong?"»

That second question is critical.

It creates a built-in adversary.

---

4. Evidence Must Have a Chain

The system is also designed to prevent the agent from quietly turning assumptions into facts.

A conclusion should be traceable back to evidence.

For example:

Conclusion

↓

Reasoning

↓

Experiment

↓

Code

or:

Conclusion

↓

Reasoning

↓

External source

The important rule is that reasoning cannot become its own evidence.

An AI saying something twice does not make it true.

Likewise:

- documentation does not prove implementation,
- implementation does not prove correctness,
- correctness does not prove usefulness,
- usefulness does not prove novelty.

Each claim requires the appropriate kind of evidence.

---

5. The Agent Must Be Allowed to Be Wrong

A major feature of the system is that failure is not automatically considered failure.

If the agent investigates a promising hypothesis and discovers that it is false, that can be a successful research result.

Likewise, the agent should be allowed to conclude:

«"There is nothing novel here."»

or:

«"The available evidence is insufficient."»

or:

«"I cannot determine this."»

This is important because a benchmark that rewards impressive conclusions creates pressure for the AI to manufacture impressive conclusions.

The proposed system instead rewards accurate uncertainty.

---

6. The Agent Must Make Predictions Before Important Experiments

The power-prompt also introduces a simple scientific discipline.

Before an important experiment, the agent should state:

1. what it believes will happen,
2. how confident it is,
3. why it expects that result,
4. and what result would surprise it.

The experiment is then run.

This creates an opportunity to measure something that ordinary benchmarks usually miss:

«Did the agent actually learn something?»

If the agent correctly predicts everything, it may have understood the system very well.

But if an experiment surprises the agent and it successfully updates its model of the problem, that may be even more interesting.

The benchmark therefore records both prediction and outcome.

---

7. The Agent Must Search for Its Own Blind Spots

The system does not assume that the initial task description is complete.

The agent is encouraged to construct a question universe.

That means asking:

«"What would I need to know to be confident?"»

and then:

«"What questions am I not asking?"»

This creates a second-order research process.

The agent is not only investigating the subject.

It is investigating whether its investigation is adequate.

---

8. Discovery Is More Important Than Obedience

The power-prompt intentionally gives the agent permission to challenge the original framing.

If the user says:

«"Determine which of these projects should survive."»

the agent should be allowed to discover:

«"The premise that these projects should be treated as independent projects is incorrect."»

If the user says:

«"Find the novel technology."»

the agent should be allowed to conclude:

«"The technology is not demonstrably novel."»

If the user assumes a particular architecture is correct, the agent should be allowed to discover a different architecture.

This is important because the system is intended to test independent investigation, not sophisticated obedience.

---

9. The Agent Should Discover Things the User Did Not Ask For

One of the most important goals is emergent discovery.

The user may provide a corpus containing many projects.

The user may ask what those projects do.

The agent may discover that several apparently unrelated projects contain a common primitive.

That primitive may not have been explicitly described anywhere.

The agent may then discover:

- a missing component,
- a common architectural pattern,
- a previously unrecognized capability,
- a contradiction between projects,
- a useful combination,
- or a completely different interpretation of the corpus.

This is one of the reasons the benchmark is intentionally open-ended.

The desired agent is not merely a search engine.

It is a researcher.

---

10. The Agent Must Attack Its Own Discoveries

Discovery alone is dangerous.

An AI can find a pattern that looks extremely interesting and then construct a story around it.

The power-prompt therefore requires a second stage:

«Try to break the discovery.»

For every important conclusion, the agent should ask:

- What else could explain this?
- What evidence contradicts it?
- What prior art already exists?
- What experiment would falsify it?
- Could this merely be an artifact of the corpus?
- Could the apparent capability actually belong to the harness?
- Could the result be caused by the tools rather than the model?

This is intended to reduce confirmation bias.

---

11. The Harness Must Be Separated From the Model

This becomes especially important with modern agent systems.

A modern coding agent is not simply:

model → answer

It is more like:

model

↓

agent harness

↓

tools

↓

environment

↓

subagents

↓

state

↓

verification

↓

answer

Anthropic's current evaluation guidance explicitly warns that agent evaluations measure the model and harness together.

Anthropic's Ultracode work makes this even more important because Claude Code can now dynamically construct multi-agent workflows, distribute work across subagents, independently check results, and reconcile the results.

Therefore, if an agent produces an impressive result, the benchmark must ask:

«Did the model do this?»

or:

«Did the harness do this?»

or:

«Did the tools do this?»

or:

«Did several agents collectively do this?»

Sometimes the correct answer will be:

«UNKNOWN.»

That is preferable to an unsupported attribution.

---

12. The Environment Is Part of the Experiment

A frontier agent can be strongly affected by:

- CPU availability,
- memory,
- disk performance,
- network access,
- tool latency,
- context limits,
- model selection,
- orchestration,
- and background processes.

Anthropic's own research has shown that infrastructure differences can produce benchmark differences large enough to exceed the gap between leading models.

Therefore, the environment must be measured rather than ignored.

This is why the benchmark includes a detailed pre-flight.

The purpose is not to make the machine look impressive.

It is to know what happened.

---

13. The Agent Needs a Stopping Rule

An unlimited investigation is not necessarily a better investigation.

At some point the remaining unknowns may no longer matter.

The desired stopping rule is therefore not:

«"I ran out of tokens."»

or:

«"The time limit expired."»

Instead:

«Stop when the most valuable remaining uncertainty is unlikely to change the principal conclusions.»

This changes the goal from maximizing activity to maximizing useful information.

A good researcher should know not only how to investigate.

A good researcher should know when to stop.

---

14. The Benchmark Is Also an Experiment About AI

The benchmark has a second purpose.

The corpus is the immediate subject of investigation.

But the investigation itself becomes data.

The benchmark therefore asks:

- Did the agent discover something unexpectedly?
- Did it recover from an error?
- Did it recognize uncertainty?
- Did it waste resources?
- Did it prematurely converge?
- Did it confuse evidence with inference?
- Did it successfully challenge its own conclusion?
- Did it discover a useful question that the user did not provide?
- Did it find a boundary where its reasoning consistently failed?
- Did it behave differently when the harness changed?

This creates a second research layer.

The system is therefore studying:

the corpus

and simultaneously:

the behavior of the investigator.

---

15. Why Ultracode Matters

Anthropic's new Ultracode capability provides an important comparison.

Ultracode combines high reasoning effort with dynamic workflow orchestration. Claude can decide that a problem is too large for one pass, create a workflow, distribute work among agents, have agents examine the problem independently, attempt to refute findings, and reconcile the results.

This is remarkably close to several ideas in the power-prompt.

That creates an opportunity for a controlled experiment.

The question becomes:

«How much of this behavior comes from the model, and how much comes from the research protocol and orchestration system surrounding it?»

A future experiment could compare:

1. Fable with the full power-prompt.
2. Fable with Ultracode and the same power-prompt.
3. Fable with Ultracode and a much shorter prompt.
4. Another frontier model using the same environment.

The results could reveal whether the power-prompt itself is providing meaningful capability or simply describing a workflow that the newest agent harness already knows how to construct.

---

16. What the Power-Prompt Is Really Trying to Build

The simplest description is:

«An autonomous adversarial research process.»

It is not intended to create an AI that always agrees with the user.

It is not intended to create an AI that produces the largest report.

It is not intended to create an AI that always finds something novel.

It is not even intended to create an AI that always succeeds.

It is intended to create an AI investigator that can:

discover → question → investigate → test → falsify → update → synthesize → attack → verify → stop.

That loop is the core idea.

---

17. The Larger Research Question

The deeper question behind the project is therefore:

«How much independent scientific and technical investigation can a frontier AI perform when it is given a poorly specified problem, a large evidence base, real tools, and a rigorous method for challenging its own conclusions?»

A second question follows:

«What parts of that ability belong to the underlying model, and what parts are created by the surrounding prompt, tools, orchestration, and evaluation harness?»

And a third:

«Can the investigation itself reveal reproducible capabilities, limitations, or failure boundaries that are useful for improving future frontier agents?»

These are considerably more interesting questions than:

«"Which model scored higher?"»

---

18. What Would Count as Success?

Success is not necessarily a spectacular discovery.

A successful run could produce any of the following:

- a well-supported new finding,
- a previously hidden relationship,
- a useful architectural synthesis,
- a reproducible capability boundary,
- a systematic failure mode,
- a demonstration that an attractive hypothesis was false,
- or a carefully justified conclusion that nothing important was discovered.

The important requirement is that the conclusion survives attempts to break it.

---

19. The Long-Term Vision

If this approach works, the resulting artifact would be more than a prompt.

It could become a reusable research protocol for frontier agents.

A future version could provide:

- a standardized investigation environment,
- explicit evidence provenance,
- prediction-before-experiment records,
- adversarial verification,
- model/harness separation,
- independent reproduction,
- uncertainty tracking,
- resource accounting,
- prior-art investigation,
- negative-result preservation,
- and principled stopping.

The same framework could potentially be applied to:

- software repositories,
- scientific research,
- technical due diligence,
- security analysis,
- architecture review,
- business research,
- policy analysis,
- and other complex knowledge-work problems.

---

20. Conclusion

The power-prompt is best understood not as a very large instruction.

It is an attempt to define a research discipline for an autonomous AI investigator.

Its most important idea is simple:

«Do not ask the AI only to find an answer. Ask it to determine what the real question is, gather evidence, try to prove itself wrong, and determine whether the surviving answer is strong enough to stop.»

The ultimate experiment is therefore not whether the AI can follow the prompt.

It is whether the AI can become a better investigator because of it.

And the strongest test of that claim is to remove pieces of the scaffolding and see what remains.