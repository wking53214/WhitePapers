> **CONFIDENTIAL.** Not cleared for publication. See `REDACTION.md`.

# Blue team: what the evidence supports, and what would establish the rest

Companion to `RED_TEAM.md`, written after it and in answer to it. The red
team asked how each claim dies. This asks what survives, what the red team's
own instruments prove when pointed the other way, and which experiments
would settle the open question rather than only close it.

Two corrections to how the red team presented itself, before anything else.

**It attacked its own control weakly.** The clean-room experiment was
designed by someone who had already read the subject system. That is a
confound and §B3 quantifies it.

**It reported a pooled figure over two trials that disagreed sharply.**
Trial 1 scored 20.0% on the vocabulary, trial 2 scored 9.3%. Pooling to
14.8% conceals a factor of two. With that spread, "14.8% against 21.6%" is
not the clean refutation the red team implied.

---

## B1. The model-prior objection is answered, and the answer is affirmative

The red team's A1 was the critical attack: perhaps language models simply
name governance software this way, making the finding about the tool.

**Run the control it never ran.** Seven human-written, domain-matched
packages, other authors, no relation to the library: `pybreaker`, `tenacity`,
`circuitbreaker`, `limits`, `transitions`, `prometheus_client`, `casbin`.
These are circuit breakers, retry libraries, rate limiters, state machines,
metrics exporters and a policy engine. Exactly the neighbourhood.

| | classes | collision with library | vocabulary |
|---|---|---|---|
| URE, contamination-free | 37 | 8.1% [2.8, 21.3] | 21.6% |
| **Domain-matched human, 7 packages** | **281** | **3.9% [2.2, 6.9]** | **10.7%** |
| Clean-room model, 2 trials | 88 | 3.4% [1.2, 9.5] | 14.8% |
| Off-domain third-party, 12 packages | 4,907 | 0.5% [0.3, 0.7] | 2.9% |

**Human domain-matched code and the clean-room model score the same.** 3.9%
against 3.4% on collision, 10.7% against 14.8% on vocabulary. The model is
not doing anything peculiar; it is doing what the domain does.

That disposes of A1 as an *explanation*. The elevation above off-domain
packages is a domain effect, not a language-model effect, and would appear
for a human engineer too. A1 is refuted in the form the red team stated it.

What remains is A3, the domain effect itself, which is a different and more
tractable problem. And the next section is why it does not account for
everything.

---

## B2. The `regime` signature: one token that domain cannot explain

This is the finding the red team missed by only ever asking how things die.

**The logic.** If a word appears in the author's code because the domain
requires it, then other people writing in that domain must use it too, and a
model given the domain brief must reach it. Both are checkable.

| corpus | class names | containing `regime` |
|---|---|---|
| Domain-matched human, 7 resilience and policy packages | 281 | **0** |
| Off-domain third-party, 12 packages | 4,907 | **0** |
| Clean-room model given the resilience brief, 2 trials | 88 | **0** |
| **Total third-party and clean-room** | **5,276** | **0** |

Zero. Not rare. Absent.

Now the author's own library:

| repository | class | file, and what it does |
|---|---|---|
| OBSERVE | `OperationalRegime` | consolidated observer |
| OBSERVE | `RegimeClassificationModule` | **clinical** risk adapter |
| observe-perceive | `OperationalRegime` | consolidated observer |
| sentinel_os | `RegimeEngine` | governance kernel |
| AUGUR | `RegimeEngine` | **market forecasting** kernel |
| GSA-815 | `RegimeEngine` | vendored kernel copy |

Six uses across five repositories. And from the archive, dated 2026-07-29,
a **drone** resilience engine: `OperationalRegime`. And the reconstruction:
`SystemRegime`, `RegimeClassifier`, `RegimeProfile`.

**Clinical risk. Market forecasting. Drone resilience. Vehicle safety.
Governance. Five unrelated domains, one word.** Meanwhile nobody else writing
in any of those domains uses it, and a model asked to do the same job says
`OperatingMode` and `OperatingState`.

**Why this is the strongest evidence in the whole exercise.** A domain effect
predicts a word clusters *inside* its domain. `regime` does the opposite: it
is absent from the domain and present across the author's unrelated projects.
That is the signature of a person, not a subject matter. It is precisely the
pattern the schema hypothesis predicts and the domain hypothesis forbids.

**Honest limits, stated rather than buried.**
- It is one token. A single-token finding is a case study, not a distribution.
- `RegimeEngine` exists in `sentinel_os`, which was attached to the
  reconstruction session, so the reconstruction's own `Regime*` names have a
  contamination path. **The cross-domain library spread and the dated
  archive occurrence do not**, and those carry the argument. The
  reconstruction is not needed for it at all.
- "Regime" is standard usage in econometrics, which is plausibly where AUGUR
  gets it. The interesting claim is the *transfer* of a term from market
  modelling into clinical, automotive and governance code. Transfer is what
  an author does and a domain does not.

---

## B3. Attacking our own clean-room control

The red team treated its control as decisive. It is weaker than that.

**The prompt was written by someone who had read the subject.** Both
clean-room briefs enumerate the subject's architecture: ingest telemetry,
compute a stability scalar, classify into named modes, remember failure
signatures, adapt thresholds, emit remediation, record an auditable
decision. That is URE's module list in prose. Of course the model reached the
same concepts; it was handed them. The control therefore tests **naming given
the concepts**, which is a narrower question than it appeared to answer.

Read that way, the result is nearly the opposite of a refutation: given the
concepts on a plate, the model still produced **none** of the author's words.
Different names for every single component.

**Trial variance is large and was hidden.** 20.0% and 9.3% on the
vocabulary. Two trials is not a distribution, and the pooled midpoint
implies precision that does not exist.

**The fair control was then built.** Trial 3, in §B4b, uses a one-line
problem statement and derives the architecture itself. It scored **higher**
than the architecture-fed trials, 31.6% against 20.0% and 9.3%, which
settles the direction: the published measure tracks the domain of the
request, and a vaguer request in the same domain scores better, not worse.
Three trials is still not five, and each further trial can only shrink the
survivor set in §B4b.

---

## B4. What the evidence supports, stated affirmatively

1. **The reconstruction is genuine, not a fabrication.** Zero structural
   copies across the available library. Member overlap 0.00 wherever a class
   name recurs. It cannot have been assembled from the library because it
   shares no content with it.
2. **The recurrence is not general Python convention.** 0.5% off-domain,
   versus 8.1% for the subject. Solid.
3. **The recurrence is not a language-model artefact.** Human domain-matched
   code scores the same as the clean-room model. B1. Solid.
4. **A 24-token author signature exists and discriminates completely.** B4b.
   Used across the author's repositories, zero occurrences in 5,188
   third-party class names and zero in 145 clean-room names over three
   trials. `regime` is the worked example in B2: transferred across
   clinical, market-forecasting, drone, automotive and governance code, and
   absent from everyone else's.
5. **The recurrence predates any instrument that could detect it,** datable
   to June and July 2026 transcripts.
6. **The published whole-vocabulary measure is refuted, not merely
   unproven.** A clean-room model given one sentence scores 31.6% on it,
   above the subject at 21.6% and above the library's own held-out
   repositories at 25.4%. Any fingerprint claim resting on it fails.
   This is the methodological contribution and it stands.

What is **not** established: that the subject's 8.1% on the survivor set is
separable from zero on a sample of three classes. The controls are zero out
of 145 and zero out of 5,188, which is why the comparison is worth making,
but three events cannot carry a confidence interval anyone should quote. The
survivor set itself is solidly established; the reconstruction's score on it
is suggestive and under-powered. Say both.

---

## B4b. Experiment 1 was run. It works, and it cost four more tokens.

B5's first experiment is below because it was executed rather than proposed.

**Construction, in three filters, each using a corpus the next one does not
see.**

1. Of the published 56 tokens, keep those used in **2 or more** of the
   author's repositories. Removes one-offs.
2. Remove any token appearing anywhere in **5,188 third-party class names**
   across 19 packages, 7 of them domain-matched. Removes domain and generic
   vocabulary. **33 tokens survive.**
3. Remove any token a **clean-room model** reaches. Trials 1 and 2 removed 5
   (`audit`, `decision`, `extractor`, `gate`, `ledger`), leaving 28.

**Then a genuine held-out test.** A third clean-room trial, given a
deliberately vague one-line brief written to avoid the §B3 confound, and
never used in building the set: *"a large organisation wants software that
watches its automated systems and decides, defensibly, when to step in."*

It reached 4 of the 28: `approval`, `drift`, `human`, `provenance`. Those
drop out. **24 tokens survive all three filters and the held-out trial.**

| corpus | published 56 | 33-token | **24-token survivor set** |
|---|---|---|---|
| URE, the subject | 21.6% | 13.5% | **8.1%** |
| Clean-room trials 1+2 | 14.8% | 9.1% | **0.0%** |
| Clean-room trial 3, held out | **31.6%** | 22.8% | **0.0%** |
| Third-party, 19 packages | 3.5% | 0.0% | **0.0%** |

**Two results, and they point opposite ways.**

**The published measure is worse than worthless.** Trial 3 scores **31.6%**,
higher than the subject's 21.6% and higher than the library's own held-out
repositories at 25.4%. A model handed one sentence outscores the codebase the
vocabulary was derived from. Any claim resting on that measure is not merely
unproven, it is refuted, and the red team's 14.8% understated how badly.

**The survivor set discriminates completely.** 24 tokens, used across the
author's repositories, appearing **zero times** in 5,188 third-party class
names and **zero times** in 145 clean-room names across three trials with
three different briefs. Nothing outside the author's work reaches them.

**And the subject reaches them.** URE scores 8.1% on the survivor set
against 0.0% for every control. Three classes, all carrying `regime`. Three
events is a small number and must be reported as one; the comparator is not
a small number, it is zero out of 145 and zero out of 5,188.

**What this means for the schema hypothesis.** It is no longer a 56-token
claim that fails a control. It is a 24-token claim that passes one, obtained
by a filter anyone can apply and that anyone can attack by running a fourth
clean-room trial. Each new trial can only shrink the set, which is the right
direction for a measure to be falsifiable in: it never grows to accommodate
evidence.

**The survivor list itself is the trade secret.** It is a compact
description of how the author thinks, more so than any class shape. It must
not be published. The paper reports the count, the filter, and the scores.
`REDACTION.md` treats it as the crown jewels.

---

## B5. Experiments that would establish the rest

The red team listed what would kill it. These would build it, in order of
value per unit of effort.

1. ~~Extend B2 to every vocabulary token.~~ **Done, see B4b.** 24 tokens
   survive.
2. **Cross-domain spread as the statistic, not frequency.** The current
   measure counts how often a token appears. The `regime` finding says the
   informative quantity is how many *unrelated domains* it appears in.
   Redefine the score as domain-spread and the domain confound largely
   cancels by construction.
3. **A properly blinded clean-room control.** Brief written by someone who
   has not seen the subject, five or more trials, from a one-line problem
   statement rather than an architecture.
4. **A second author's library, if one can be obtained,** measured the same
   way. If their tokens show the same cross-domain concentration in
   different words, the method generalises and the paper is about a
   phenomenon rather than a person.
5. **Re-run everything against all thirty repositories,** not the ten
   available. Both the copy count and the domain spread can only sharpen.

Experiment 1 is the one to do next. It is cheap, it uses instruments that
already exist in this directory, and on the evidence of B2 it is likely to
produce a small set of tokens that behave the way `regime` does. That set,
not the 56, would be the schema.
