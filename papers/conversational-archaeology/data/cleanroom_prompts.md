> **CONFIDENTIAL.** Part of the Conversational Archaeology paper.

# Clean-room control: the prompts, verbatim

Two fresh model sessions (Claude Opus), no tools, no filesystem access, no
archive, no library, no knowledge of the subject system or of the schema
study. Each was asked only for class names. Outputs are in
`cleanroom_trial1_names.txt` and `cleanroom_trial2_names.txt`.

Both prompts describe the subject's **function** only. Every name from the
subject or the library was deliberately withheld, including "regime",
"resilience", "governance decision" and "recovery action". Trial 2 uses
"governed automation platform" and the word "governance" appears once, in
that phrase; this is a known imperfection and trial 2 duly produced
`GovernancePolicy`, which is why trial 1 is the cleaner of the two and both
are reported.

---

## Trial 1

> Design task. Do NOT read, search, glob, or list any files on this machine,
> and do not look at any existing code. Answer purely from your own design
> judgement. Use no tools at all.
>
> Design a dependency-free Python package that does the following for a
> running production system:
>
> - ingests periodic telemetry (request rates, error rates, latency,
>   saturation, resource headroom)
> - maintains a scalar stability metric derived from that telemetry, and
>   tracks whether it is rising or falling over time
> - classifies the system's current operating mode into one of a small set of
>   named modes, ranging from healthy through degraded to actively failing or
>   under attack
> - keeps a memory of previously seen failure signatures so a repeat can be
>   recognised
> - adapts its own alerting thresholds over time to control false alarms
> - decides when to intervene, and emits a set of remediation instructions
>   for a separate executor component to carry out
> - records an auditable decision for every classification it makes, suitable
>   for later review by a compliance function
>
> Output ONLY a flat list of the Python class names you would define for this
> package, one per line, no explanation, no module paths, no comments. Aim
> for roughly 30 to 40 class names. Use the names you would genuinely choose.

## Trial 2

> Design task. Do NOT read, search, glob, or list any files on this machine,
> and do not look at any existing code. Answer purely from your own design
> judgement. Use no tools at all.
>
> You are designing a dependency-free Python package that sits inside a
> larger governed automation platform. Its job:
>
> - take in periodic health and load signals from a production service
> - compute a single number representing how far the service is from a stable
>   equilibrium, and whether that number is improving or worsening
> - label the service's present condition as one of a handful of named
>   operating states, from normal through strained to failing or hostile
> - remember the shapes of past incidents so a recurrence is recognised
>   rather than rediscovered
> - tune its own trigger levels so it neither over- nor under-alerts
> - decide whether the platform is permitted to act, and if so issue the
>   specific containment or recovery steps for another component to perform
> - leave an inspectable record of each judgement, because a risk function
>   will audit these decisions later
>
> Output ONLY a flat list of the Python class names you would define, one per
> line. No explanation, no module paths, no comments. Roughly 30 to 40 names.
> Use the names you would genuinely choose.

---

## Results

| | names | library collisions | vocabulary score |
|---|---|---|---|
| Trial 1 | 45 | 2 (`AnomalyDetector`, `DecisionRecord`) = 4.4% | 20.0% |
| Trial 2 | 43 | 1 (`PolicyGuard`) = 2.3% | 9.3% |
| **Pooled** | **88** | **3 = 3.4%** | **14.8%** |

For comparison: the reconstruction 8.1% collision and 21.6% vocabulary, the
library's held-out repositories 25.4% vocabulary, twelve third-party
packages 0.5% collision and 2.9% vocabulary.

Neither trial produced any of the three contamination-free names. Both
reached every one of the underlying concepts under different words. That
comparison is §6.6 of the paper and is the most interesting thing the control
produced.

---

## Trial 3, the held-out test with a deliberately vague brief

Written to remove the §B3 confound: trials 1 and 2 were briefed with the
subject's architecture in prose, which hands the model its concepts. Trial 3
gets one sentence and has to derive the rest. It played no part in building
the 28-token set it was used to test.

> Design task. Use NO tools. Do not read, search, glob or list any files.
> Answer purely from your own design judgement.
>
> One-line problem statement: a large organisation wants software that
> watches its automated systems and decides, defensibly, when to step in.
>
> That is the whole brief. Work out for yourself what such a system needs to
> contain.
>
> Output ONLY a flat list of the Python class names you would define, one per
> line. No explanation, no module paths, no comments, no headings. Roughly 35
> to 45 names.

**Result: 57 names, and it scored 31.6% on the published 56-token
vocabulary** — higher than the subject (21.6%) and higher than the library's
own held-out repositories (25.4%). It reached 4 of the 28 candidate signature
tokens (`approval`, `drift`, `human`, `provenance`), which therefore drop
out. It scored **0.0%** on the 24 that remain.

The vaguer brief produced the *higher* vocabulary score, which is the
clearest possible demonstration that the published measure tracks the domain
of the request rather than the identity of the author.
