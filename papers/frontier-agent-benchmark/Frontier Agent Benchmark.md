Frontier Agent Benchmark

Pre-Flight Control and Evidence Baseline

Document status: Pre-benchmark control artifact
Prepared: 2026-09-14
Purpose: Establish the environmental, corpus, runtime, provenance, and contamination boundaries that must be understood before executing the frontier-agent benchmark.

---

Abstract

This document records the pre-flight process performed before a planned frontier-agent benchmark using Claude Code and Fable 5.1.

The benchmark is intended to evaluate whether a frontier coding/reasoning agent can independently investigate a complex software corpus, discover inadequately specified problems, construct and test competing explanations, identify missing capabilities or primitives, perform discriminating experiments, investigate prior art, reason about novelty without overclaiming, and preserve evidentiary boundaries.

The central pre-flight concern is experimental contamination.

The local environment contains multiple generations of repositories, historical archives, conversation histories, previous analyses, agent configuration, persisted Ghost Tools findings, benchmark artifacts, and external-tool configuration. Some of these materials may contain conclusions that the benchmark is specifically intended to determine independently.

Therefore, the pre-flight process did not attempt to make the environment "clean" by deleting or repairing material. Instead, it attempted to establish:

1. what exists,
2. what has actually been inspected,
3. what was executed,
4. what can legitimately be inferred,
5. what remains unknown,
6. and which environmental materials could contaminate an independent benchmark.

The resulting conclusion is that the benchmark should use a deliberately bounded workspace, rather than unrestricted access to the user's entire home directory.

---

1. Benchmark Objective

The planned benchmark is designed to test frontier-agent capability rather than merely code-generation ability.

The target agent is expected to operate across a heterogeneous corpus containing software repositories, historical versions, architectural artifacts, tests, documentation, and potentially contradictory generations.

The benchmark asks whether the agent can independently:

- discover the actual problem space;
- construct a question universe rather than prematurely accepting a framing;
- investigate the corpus;
- distinguish observations from conclusions;
- identify missing capabilities;
- generate competing hypotheses;
- design discriminating tests;
- falsify explanations;
- synthesize architectural implications;
- investigate prior art;
- assess novelty cautiously;
- independently verify important claims;
- manage computational resources;
- preserve temporal integrity;
- recognize contamination;
- recognize when evidence is insufficient;
- and stop when additional investigation has diminishing information value.

The benchmark therefore measures more than whether an agent can produce a technically plausible answer.

The relevant question is whether the agent can earn its conclusions from the available evidence.

---

2. Governing Experimental Principle

The pre-flight process adopts the following principle:

«A benchmark cannot meaningfully measure independent discovery if the experimental subject has unrestricted access to prior conclusions about the problem.»

This does not mean that all historical material is invalid.

Historical repository versions may themselves be legitimate evidence when temporal reconstruction is part of the task.

The critical distinction is between:

- primary evidence — source code, tests, repository history, artifacts;
- historical evidence — earlier versions or snapshots;
- derived evidence — prior reports, analyses, generated findings;
- agent-state evidence — memories, configuration, cached conclusions, tool state;
- experimental artifacts — benchmark results and prior benchmark decisions.

Accessibility does not establish evidentiary authority.

A file being present on disk does not mean that it should be treated as authoritative evidence.

---

3. Evidence Discipline

All pre-flight observations are classified using four levels:

EXECUTED

An operation was actually performed.

Example:

«"[EXECUTED] Claude Code was invoked using the Fable model alias."»

INSPECTED

The result of an executed operation was actually observed.

Example:

«"[INSPECTED] The invocation returned HTTP 429 with zero inference tokens."»

INFERRED

A conclusion follows from inspected evidence but was not directly observed.

Example:

«"[INFERRED] No model inference occurred during the failed Fable probe."»

UNKNOWN

The available evidence does not establish the proposition.

Example:

«"[UNKNOWN] The actual reasoning and tool behavior of Fable 5.1 in this environment."»

This distinction is mandatory for the benchmark.

No inferred conclusion should silently become a fact.

---

4. Hardware and Runtime Characterization

A minimal-load Penguin performance benchmark was executed before the frontier-agent benchmark.

The environment is a Crostini/Termina Linux environment running under KVM.

Observed characteristics included:

- Linux kernel: "6.6.135-09383-g1140e4f27e24"
- architecture: "x86_64"
- guest-visible CPUs: 4
- CPU: Intel Core i3-10110U @ 2.10GHz
- memory: approximately 6.4 GiB
- swap: none
- storage: approximately 43 GB total, approximately 17 GB available at measurement time
- filesystem: Btrfs

The guest topology reports four online logical CPUs.

Important interpretation boundary

The four visible CPUs establish the guest-visible compute allocation.

They do not establish the physical host topology.

Therefore:

«"[INSPECTED]" The guest exposes four online logical CPUs.»

«"[INFERRED]" Penguin is provisioned with four vCPUs.»

«"[UNKNOWN]" The physical host topology beyond what the guest exposes.»

---

5. Penguin Performance Benchmark

A minimal-load performance characterization was performed to establish whether the local environment has obvious resource limitations before the agent benchmark.

The benchmark included:

- single-thread CPU performance;
- four-thread CPU performance;
- CPU scaling from one through four workers;
- memory throughput;
- single-thread filesystem workload;
- four-thread filesystem workload;
- CPU saturation;
- memory-pressure testing;
- observation of swap and I/O behavior.

Representative measurements:

CPU

Single-worker:

"506.79 events/s"

Four-worker:

"1439.86 events/s"

Scaling:

- 2/1: approximately "1.883x"
- 3/1: approximately "2.531x"
- 4/1: approximately "3.034x"

Memory

One-thread:

"22,353.22 MiB/s"

Four-thread:

"35,849.99 MiB/s"

Filesystem

One-thread:

- approximately 858.77 reads/s
- approximately 572.50 writes/s
- approximately 57.30 fsync/s

Four-thread:

- approximately 1426.16 reads/s
- approximately 950.77 writes/s
- approximately 95.32 fsync/s

CPU stress saturated the four guest-visible CPUs.

No swap activity or obvious I/O-wait/steal signal was observed during the stress test.

Memory pressure was also exercised without observed swap activity.

Interpretation

The benchmark establishes a local resource baseline.

It does not establish the performance of Claude Code or Fable under actual agentic workload.

Therefore:

«"[EXECUTED]" Local CPU, memory, and filesystem characterization was performed.»

«"[INSPECTED]" The environment can sustain a four-worker CPU workload and did not exhibit swap activity during the tested memory pressure.»

«"[INFERRED]" The environment has measurable compute and filesystem constraints that could matter during an agentic workload.»

«"[UNKNOWN]" The degree to which those constraints materially affect an actual Fable benchmark run.»

The benchmark should therefore avoid describing the Penguin test as a pure physical-hardware benchmark.

The correct characterization is:

"Penguin minimal-load performance benchmark under a 4-vCPU KVM/Crostini environment."

---

6. Claude Code Runtime Inspection

Claude Code was inspected before benchmark execution.

Observed runtime:

- Claude Code: "2.1.268"
- installation: native
- Node.js: "20.20.2"
- npm: "10.8.2"
- Python: "3.11.2"
- Git: "2.39.5"
- operating system: Debian 12 / Bookworm

Claude Code reported no installation issues through its diagnostic command.

The local configuration was also inspected.

Relevant configuration includes:

- automatic permission mode;
- high effort level;
- advisor model configuration;
- workflow support;
- local settings;
- a substantial tool permission allowlist.

This configuration matters because a benchmark using the normal Claude Code environment is not equivalent to a pristine installation.

---

7. Claude Code Capability Surface

The installed CLI exposes a substantial capability surface, including mechanisms for:

- model selection;
- effort selection;
- system prompts;
- settings;
- MCP configuration;
- plugin configuration;
- agent configuration;
- worktrees;
- session continuation;
- background operation;
- restricted/safe modes;
- JSON and streaming output;
- permission control;
- tool allow/deny lists;
- remote control;
- subagent/agent-team functionality.

This creates a significant methodological choice.

A benchmark may measure:

1. the model's reasoning capability;
2. the agent's ability to operate the available environment;
3. the agent's ability to exploit an intentionally realistic development environment;
4. or some combination of the above.

Those are different experiments.

---

8. MCP and External Tool Surface

The Claude Code environment contains a substantial MCP configuration.

The inspected environment reported approximately 35 MCP entries, with a subset connected and others requiring authentication.

Connected services included examples such as:

- Google Drive;
- Gmail;
- Google Calendar;
- Slack;
- PubMed;
- Clinical Trials;
- Dropbox;
- Booking.com;
- Sentry;
- Linear;
- Supabase;
- Indeed;
- AccuWeather;
- and other external services.

Several additional integrations were configured but required authentication.

This is a major benchmark consideration.

External tool access can dramatically expand the agent's information space.

It can also introduce information leakage, prior conclusions, or capabilities unrelated to the intended benchmark.

Therefore the benchmark must explicitly specify which external services are part of the experimental condition.

---

9. Agent-Team and Cloud Review Confounds

Claude Code exposes experimental multi-agent/team capabilities.

These capabilities allow multiple Claude Code instances to operate with separate contexts and communicate through shared task infrastructure.

Claude Code also exposes cloud-hosted review functionality.

Neither should be silently introduced into the primary benchmark.

Using them would change the experiment from:

«"Can one frontier agent independently perform this investigation?"»

to something closer to:

«"Can an orchestrated collection of frontier agents perform this investigation?"»

Those are different measurements.

Accordingly:

«"[CONTROL]" Agent teams and cloud multi-agent review should not be invoked unless explicitly defined as a separate benchmark condition.»

---

10. Fable 5.1 Availability

Official model information was independently checked before the runtime probe.

Fable 5.1 is a current frontier model with:

- approximately one-million-token context;
- large output capacity;
- adaptive thinking;
- high-effort reasoning;
- long-horizon coding/agentic positioning.

The model is intended for complex projects and agentic workflows.

The benchmark therefore targets a model class capable of performing the intended investigation rather than using the benchmark merely as a conventional code-generation test.

---

11. Fable Runtime Probe

A fresh, isolated runtime probe was attempted.

The probe was intentionally designed not to access files, Bash, MCP, web services, or agents.

The intended purpose was only to establish model/runtime availability.

The invocation returned:

"HTTP 429"

with a weekly usage-limit message.

The returned accounting showed:

- input tokens: "0"
- output tokens: "0"
- thinking tokens: "0"
- model usage: empty
- subagents: "0"

Therefore:

«"[EXECUTED]" A Fable invocation reached the Claude API layer.»

«"[INSPECTED]" The API returned HTTP 429 before inference, with zero inference tokens.»

«"[INFERRED]" No Fable model inference occurred during this probe.»

«"[UNKNOWN]" The actual reasoning behavior, tool behavior, and benchmark performance of Fable 5.1 in this environment.»

The probe should not be rerun merely to establish something already established, because doing so would consume the same constrained resource without increasing the evidentiary value.

---

12. Pre-Flight Freeze

A formal pre-flight freeze was created.

The freeze records:

- benchmark artifacts;
- runtime-block evidence;
- benchmark harness hash;
- corpus/runtime observations;
- evidence classifications;
- known unknowns.

The frozen manifest is:

"preflight_frozen_20260914T091850Z.sha256"

Manifest SHA-256:

"d4cb480b935c989b980ab8a08e1b8084510d9f33129d3dcfa926a9e4e360b3d0"

The Fable runtime-block artifact has SHA-256:

"ba723480d10d048ec35cb9532247ed7a973a8c47ab704144dad90649ed57cf6d"

The clean-probe harness has SHA-256:

"03c3ff4a0f6ac8998dd77c2f5cf3621b0f476792db8cafe67175492da4126f30"

These hashes establish artifact identity.

They do not establish the truth of every conclusion contained within those artifacts.

---

13. Corpus Boundary Investigation

A read-only inventory of the local environment was performed.

This was necessary because the home directory contains substantially more than the intended software corpus.

The inventory exposed four major classes.

13.1 Candidate project corpus

Local repositories exist directly beneath the user's home directory.

These include multiple governance, software, experimentation, and infrastructure repositories.

However:

«"[UNKNOWN]" Local repository presence does not establish current GitHub remote state.»

---

14. Historical and Duplicate Corpus

Multiple repository generations exist outside the primary working directories.

Examples include:

- "~/github_archive"
- "~/Downloads"
- "~/http"

These areas contain older repository copies, snapshots, extracted projects, and nested repositories.

This creates an important experimental opportunity and danger.

Historical versions may be valuable evidence for:

- temporal reasoning;
- architectural evolution;
- abandoned approaches;
- contradictions;
- regression analysis;
- provenance.

But duplicate repositories must not automatically be treated as equivalent to the current project.

A benchmark that exposes them should test whether the agent can distinguish:

current state

from

historical state

rather than rewarding indiscriminate aggregation.

---

15. Conversation-History Corpus

The environment contains explicit conversation-history repositories, including:

- "Gemini_History"
- "ChatGPT_History"
- "Claude_History"
- "copilot_history"

These are qualitatively different from ordinary source repositories.

They may contain the user's prior:

- reasoning;
- hypotheses;
- architecture decisions;
- terminology;
- conclusions;
- critiques;
- benchmark methodology;
- prior discoveries.

If the benchmark is supposed to measure independent discovery, unrestricted access to these histories would constitute a serious contamination channel.

Therefore conversation history should normally be separated from the first independent benchmark condition.

It may later become a deliberately defined benchmark condition for measuring archaeological reconstruction.

---

16. Agent-State and Tool-State Contamination

The local environment also contains:

- "~/.claude"
- "~/.claude/projects"
- "~/.claude/plugins"
- "~/.codex"
- "~/.grok"
- other configuration/cache locations.

These areas may contain:

- agent memory;
- prior session state;
- cached findings;
- plugin state;
- MCP configuration;
- generated reports;
- prior reasoning.

These are not automatically corpus evidence.

They represent agent/environment state.

Providing them to the benchmark agent would risk allowing the agent to recover conclusions generated by earlier agents or earlier sessions.

Therefore these locations should normally be excluded from the primary independent benchmark.

---

17. Ghost Tools as a Special Case

Ghost Tools is itself a potential benchmark subject.

Its current worktree was inspected.

Observed state:

- branch: "complete-refactor"
- HEAD: "7a1d4a8ef0d31125917c1d70959ee741fbab8519"
- working tree: dirty
- several tracked source files modified
- several unusual untracked files present

The working tree must not be silently repaired before benchmarking.

Restoring files, cleaning the tree, committing changes, or deleting state would alter the experimental substrate.

Therefore:

«"[CONTROL]" Ghost Tools should remain unchanged unless an explicit benchmark preparation step requires a documented intervention.»

---

18. Ghost Tools Persisted Ledger

Ghost Tools contains an untracked ".ghost_ledger.json".

The ledger records previous Ghost Tools runs and findings.

It therefore represents a special category of evidence.

It is not equivalent to independent external evidence.

The Ghost Tools implementation itself provides mechanisms for:

- recording runs;
- chaining historical state;
- hashing baseline and case-file information;
- detecting internal inconsistency;
- preserving run history.

However, the implementation explicitly does not establish cryptographic authenticity against an attacker who can modify the ledger.

This creates the following evidence boundary:

Property| Status
Internal consistency| IMPLEMENTED / INSPECTED
Hash-chain tamper detection| IMPLEMENTED / INSPECTED
Detection of casual history edits| IMPLEMENTED / INSPECTED
Cryptographic authenticity| NOT IMPLEMENTED
External trusted provenance| NOT IMPLEMENTED
Resistance against writer with ledger access| NOT IMPLEMENTED
Independent evidence of Ghost Tools' own findings| NOT ESTABLISHED

The ".ghost_ledger.json" therefore cannot be treated as independent validation merely because it contains hashes.

---

19. Repository State and the ".venv" Anomaly

The inventory exposed a large deletion set involving ".venv" material in at least one local repository state.

This is a red flag requiring classification.

However, it is not yet legitimate to conclude that:

- the repository was corrupted;
- the benchmark was contaminated;
- the deletion was intentional;
- the deletion was accidental;
- the environment caused it;
- or the files should be restored.

The correct next operation is read-only identification of:

1. which repository owns the ".venv" paths;
2. whether ".venv" is tracked;
3. what HEAD contains;
4. what the working tree reports;
5. whether the state is historical or newly introduced.

No repair should occur before this classification.

---

20. GitHub Remote State

A GitHub connector query did not return the expected repository inventory.

A direct unauthenticated GitHub API request also returned zero repositories for the queried account.

No "GITHUB_TOKEN" was present in the inspected environment.

Therefore:

«"[UNKNOWN]" The current authenticated GitHub remote corpus.»

Local repository clones must not be substituted for that unknown.

This is important because local repositories may be:

- stale;
- ahead of remote;
- behind remote;
- disconnected;
- archived;
- modified;
- or entirely local.

The benchmark must preserve the distinction between:

local HEAD

working tree

configured remote

current remote repository state

---

21. Benchmark Contamination Model

The pre-flight process identifies five practical evidence classes.

PRIMARY

Deliberately exposed project source and associated primary artifacts.

Expected to form the main benchmark evidence.

HISTORICAL

Older repository versions, snapshots, and archived generations.

Potentially valid evidence when temporal reconstruction is intentionally part of the task.

DERIVED

Reports, analyses, generated findings, archaeology outputs, and other conclusions produced from earlier investigations.

Potentially useful, but should not automatically be treated as independent evidence.

CONTAMINATION

Prior agent state, memories, benchmark artifacts, cached findings, configuration, and other material that could reveal the answer before the agent independently derives it.

Should normally be unavailable in the primary benchmark.

EXCLUDED

Material physically present on the machine but deliberately outside the benchmark's accessible workspace.

---

22. Why Unrestricted "$HOME" Is Inappropriate

The investigation established that unrestricted "$HOME" access would expose the benchmark agent to:

- prior repository generations;
- multiple duplicate copies;
- conversation histories;
- prior analyses;
- agent memories;
- Ghost Tools findings;
- benchmark artifacts;
- MCP configuration;
- cached tool state;
- generated reports.

This would make it difficult to distinguish:

«"The agent discovered this."»

from:

«"The agent found an artifact explaining this."»

The benchmark would therefore measure information retrieval from a contaminated environment rather than independent investigation.

This is not necessarily a bad experiment.

It is simply a different experiment.

---

23. Recommended Benchmark Boundary

The primary benchmark should use a deliberately assembled workspace.

Recommended exposure:

Include

- selected project repositories;
- explicitly selected historical repository generations;
- intentionally selected primary artifacts;
- Ghost Tools if it is a benchmark subject;
- tests and documentation belonging to exposed repositories.

Exclude

- "~/.claude"
- "~/.codex"
- "~/.grok"
- unrelated caches
- benchmark workspace itself
- prior benchmark findings
- agent memories
- unrelated MCP configuration
- unrelated generated reports

Conditional

Conversation histories and archived analyses should be made available only if the benchmark explicitly tests historical/archaeological reasoning.

---

24. No Cleanup Principle

The pre-flight process deliberately avoids "cleaning" the machine merely because it looks messy.

This is important.

Deleting:

- duplicate repositories;
- historical archives;
- Ghost Tools state;
- dirty working-tree changes;
- prior reports;
- agent state;
- caches;

could destroy information needed to explain the experimental environment.

Therefore:

«Do not confuse experimental control with filesystem cleanliness.»

The objective is not to make the machine clean.

The objective is to make the experimental boundary explicit.

---

25. Current Evidence Ledger

At the completion of pre-flight:

EXECUTED

- Penguin performance characterization.
- Claude Code runtime inspection.
- Claude Code capability-surface inspection.
- MCP/configuration inspection.
- Fable invocation attempt.
- Local repository inventory.
- Historical/duplicate corpus inventory.
- Conversation-history inventory.
- Agent-state inventory.
- Ghost Tools state inspection.
- Ghost Tools persisted-ledger inspection.
- Benchmark artifact freeze.

INSPECTED

- Guest-visible four-CPU environment.
- Claude Code 2.1.268.
- Local runtime configuration.
- External tool configuration.
- Fable API 429 response.
- Local repository topology.
- Multiple repository generations.
- Conversation-history repositories.
- Agent memory/configuration locations.
- Ghost Tools worktree.
- Ghost Tools ledger.
- Benchmark artifacts.

INFERRED

- The Fable probe did not reach model inference.
- The guest is provisioned with four visible vCPUs.
- Unrestricted "$HOME" access presents substantial contamination risk.
- Local repository state cannot establish current remote GitHub state.
- The benchmark should use a bounded workspace for independent-discovery measurement.

UNKNOWN

- Actual Fable reasoning performance in this environment.
- Actual Fable tool-use behavior.
- Actual Fable performance under CPU/filesystem contention.
- Current authenticated GitHub corpus.
- Whether individual historical artifacts should be exposed.
- Whether prior derived reports should be exposed under any benchmark condition.
- The cause and significance of the ".venv" deletion state.
- The complete causal history of all local repository divergences.

---

26. Frozen Artifacts

The following artifacts constitute the current pre-flight evidence package.

Pre-flight freeze

"preflight_frozen_20260914T091850Z.sha256"

SHA-256:

"d4cb480b935c989b980ab8a08e1b8084510d9f33129d3dcfa926a9e4e360b3d0"

Fable runtime block

"phase0_runtime_block_20260914.md"

SHA-256:

"ba723480d10d048ec35cb9532247ed7a973a8c47ab704144dad90649ed57cf6d"

Clean probe harness

"harness/clean_probe.sh"

SHA-256:

"03c3ff4a0f6ac8998dd77c2f5cf3621b0f476792db8cafe67175492da4126f30"

Corpus boundary inventory

"corpus_boundary_20260914T092007Z.txt"

SHA-256:

"cc9216567828bb554e838856db58fcb0ab2d3cef924976898ba121e7b358f342"

---

27. Experimental Status

The frontier-agent benchmark has not yet been executed.

This distinction is critical.

The pre-flight process establishes experimental controls and environmental observations.

It does not constitute a benchmark result.

Specifically, no claim should currently be made about:

- Fable's reasoning quality;
- Fable's architectural discoveries;
- Fable's ability to falsify hypotheses;
- Fable's ability to discover missing primitives;
- Fable's novelty analysis;
- Fable's corpus comprehension;
- Fable's resource management;
- Fable's stopping behavior.

Those remain unmeasured.

---

28. Recommended Next Phase

Before the actual benchmark begins, the next phase should establish the final controlled workspace.

That process should:

1. identify the exact repositories intended for exposure;
2. classify historical copies explicitly;
3. classify derived artifacts explicitly;
4. exclude agent-state contamination;
5. exclude prior benchmark conclusions;
6. preserve original repositories unchanged;
7. create an explicit benchmark workspace;
8. record its contents;
9. hash the benchmark input manifest;
10. freeze the benchmark prompt;
11. record network/tool permissions;
12. record model availability;
13. record start time;
14. execute the benchmark exactly once for the primary condition.

Any subsequent modification should become a new experimental condition rather than silently altering the original run.

---

29. Final Pre-Flight Conclusion

The pre-flight process has not demonstrated that the benchmark environment is clean.

It has demonstrated something more useful:

the environment is sufficiently complex that "clean" cannot be assumed.

The machine contains multiple generations of source, historical records, derived analyses, agent state, external-tool configuration, and benchmark artifacts.

The central experimental control is therefore not filesystem cleanliness.

It is evidentiary separation.

The benchmark should make it possible to answer, after the run:

«What did the agent actually observe?»

«What did it independently infer?»

«What did it retrieve from historical material?»

«What did it inherit from prior analysis?»

«What could it not establish?»

«What did the environment prevent?»

«What did the benchmark fail to measure?»

Only then can a frontier-agent result be interpreted as evidence about frontier-agent capability rather than evidence about the amount of prior knowledge accidentally made available to the agent.

---

Status

PRE-FLIGHT: substantially characterized
BENCHMARK: not yet executed
FABLE INFERENCE: not yet obtained
PRIMARY CORPUS BOUNDARY: not yet finally frozen
CONTAMINATION BOUNDARY: identified; controlled workspace still required
CURRENT GITHUB REMOTE CORPUS: UNKNOWN
HARDWARE CONSTRAINTS: characterized at minimal load; agentic impact UNKNOWN
NEXT CONTROL: finalize and hash the benchmark workspace/input manifest