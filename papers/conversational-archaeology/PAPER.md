> **CONFIDENTIAL DRAFT.** Not cleared for publication. See `REDACTION.md`.

# Conversational Archaeology

**Reconstructing a lost software system from archived design discourse, and
verifying the reconstruction against an independently measured schema**

*Draft 1, 2026-09-11*

---

## Abstract

A software system designated SYS-URE-001 was specified and partially built in
mid-2026, never acquired a repository, and was abandoned when its only
consumer was cancelled. Four months later it was reconstructed to working
software from an input of two sentences, one of which contained only its
three-letter name. The rebuild produced fifteen modules, 278 passing tests
and zero runtime dependencies, together with a dated account of the system's
lifecycle and cause of death.

The reconstruction itself is not the contribution. Any sufficiently capable
generative process can produce plausible software from a prompt, and a
plausible reconstruction is indistinguishable from a fabrication by
inspection alone. The contribution is the verification: the rebuilt system
was scored against a conceptual schema measured independently from eighteen
unrelated repositories before the reconstruction began. It scored 21.6%
(95% CI 11.4 to 37.2), against 25.4% for repositories that actually existed
and 2.8% for third-party control packages, while containing **zero**
structural copies of any class in the source library.

That combination is the finding. The rebuilt system independently reached
five of the library's recurring class names with near-zero member overlap,
which is convergence on concepts rather than recovery of code. Two of the
three names the archive preserved as the original system's namespace also
recur in the library, which places the recurrence in mid-2026, months before
any instrument existed that could have detected it. A
reconstruction can be checked, not merely admired, when the organization
that lost the system has separately measured what its own thinking looks
like.

We argue the general case: **software does not die when its code is deleted,
it dies when the reasoning that produced it stops being retrievable**, and an
organization that archives design discourse as seriously as source can
recover systems whose source it never had.

---

## 1. Problem

Organizations archive code. They do not archive reasoning.

Version control preserves what was built with great fidelity and preserves
almost nothing about why. Commit messages are thin, design documents go
stale, and the conversations in which a system was actually conceived happen
in chat interfaces whose scrollback is neither greppable, versioned, nor
durable.

The consequence is asymmetric. A deleted repository can often be recovered
from a backup. A deleted *rationale* cannot be recovered at all, and its
absence is invisible: the code that survives looks complete, so nobody
notices that the knowledge of what it was for is gone.

This paper examines the inverse case, which is rarer and more instructive. A
system whose code did not survive, whose rationale did, and what became
possible as a result.

Two questions follow, and the second is the one the literature does not
address:

1. Can a system be reconstructed from archived design discourse alone?
2. **Given a reconstruction, how would you know it is one?**

Question 2 is the hard one. A generative process asked to rebuild a system it
cannot find will produce something. Absent an external check, a confident
fabrication and a faithful reconstruction present identically: both compile,
both have tests, both read as coherent. Section 6 is about the instrument
that separates them.

---

## 2. The subject

**URE, Universal Resilience Engine.** Internal designators SYS-URE-001 and
ARCH-URE-001.

| property | value | class |
|---|---|---|
| Purpose | Operating-regime classification and Lyapunov-style energy tracking for a governance stack | A |
| First evidenced | 2026-06-10 | A |
| Repository, at any point in its life | none | A |
| Ever ran in production | no evidence | **U** |
| Successor | unresolved by the subject's own audit | **U** |

The acronym matters more than it appears to. "Universal Reasoning Engine"
and "Unified Rules Engine" are both commoner phrases in the world than the
correct expansion. Resolving three ambiguous letters against evidence rather
than plausibility is the step at which a fabrication would have begun, and
would then have been carried consistently through fifteen modules and 278
tests, producing a wholly wrong system that passed every internal check.

The resolution came from 78 independent parenthesized expansions across the
corpus. Not one inference.

**Cause of death.** URE was a dependency that never became a project. It was
specified as the replacement for a missing health-monitoring component inside
a host system; when that host was cancelled on sound commercial grounds, the
dependency was orphaned. It had no repository of its own, no test suite of
its own, and no consumer that outlived its host.

The general form is worth stating, because it is actionable:

> A component with no repository, no tests, and no consumer that survives its
> host does not survive the cancellation of its host.

---

## 3. Method

Nine steps. The sequence is the method; the order is not incidental.

1. **Establish the target is empty.** The named repository contained nothing
   but `.git`. First useful fact: there was nothing to recover from the
   subject itself.
2. **Establish the target is absent from the obvious places.** Both attached
   working repositories searched, including all branches, by commit message
   and by filename. Zero hits. URE was not a forgotten branch; it was outside
   the live codebase entirely. This is what made step 3 necessary rather than
   optional.
3. **Find the archives.** A repository listing surfaced separate archives of
   four AI assistants' conversation histories. "Scour the archives" had a
   literal referent.
4. **Resolve the acronym against the corpus.** A regex for parenthesized
   expansions over 242 MB returned 78 confirmations, plus the system
   designators and the namespace family. *This is the hinge of the exercise.*
5. **Rank sources by density, then read the densest.** Raw occurrence counts
   misled: the densest file was an unrelated conversation that happened to
   contain a predecessor engine. Title plus density, not density alone,
   identified the authoritative specification.
6. **Recover the specification.** One transcript contained the complete
   architecture, written explicitly so a future conversation could continue
   without the original files. Three months later that is precisely what it
   was used for.
7. **Recover the code.** A search on implementation symbols located a
   hardened 297-line rewrite, extracted verbatim, which also carried a
   written account of the bugs it had fixed and why.
8. **Build.** Fifteen modules against the recovered specification, with tests
   written to lock in every documented defect so it could not return.
9. **Reconstruct the lifecycle.** The second prompt required something
   different in kind: not retrieval of a design but assembly of a history,
   including a cause of death that no document states directly.

---

## 4. Substrate requirements

The honest explanation of the result is not model capability. It is that the
archive existed. Five preconditions, none of which is common:

1. **Conversation history committed to version control.** 863 transcripts, in
   git, greppable. Files, not a chat interface's scrollback.
2. **Multiple assistants' histories preserved separately,** so a claim in one
   can be checked against another.
3. **Continuation prompts written deliberately.** The specification that made
   the rebuild possible exists because someone once wrote a handoff document
   whose stated purpose was that a new conversation could continue without
   the original files. Archival discipline performed months before it paid.
4. **Forensic audits already run,** classifying systems by evidence class and
   recording what could not be established. The cause of death was retrieved,
   not deduced.
5. **Defects documented alongside their fixes,** which is what let the
   rebuild carry corrections forward instead of silently reintroducing them.

The agent supplied search, synthesis, implementation and verification. The
substrate supplied everything that made those operations return true answers
instead of confident ones. Run the same request against an organization where
design conversations evaporate and only code survives, and the correct output
is "there is no evidence this ever existed."

---

## 5. Epistemic controls

The subject's own August 2026 provenance audits classify findings as **A**,
proven from surviving artifacts, or **U**, unresolved. The convention was
inherited rather than invented, and it governs what the reconstruction
claims. Selected rows:

| claim | class | basis |
|---|---|---|
| URE means Universal Resilience Engine | A | 78 independent expansions |
| Purpose was regime classification and energy tracking | A | dated 2026-06-10 record |
| The energy function had a 0.75 floor bug | A | documented verbatim in the recovered rewrite |
| A 297-line hardened engine existed | A | recovered in full |
| The v2 architecture was specified | A | recovered in full |
| The v2 architecture was ever implemented | **U** | no artifact, no deployment evidence |
| URE ever ran in production | **U** | no deployment evidence anywhere |

> A reconstruction that cannot distinguish what it recovered from what it
> invented is not a reconstruction. It is a plausible-sounding replacement.

---

## 6. The verification problem, and the schema as its instrument

This section is the paper's contribution. Sections 3 through 5 describe a
careful process; carefulness is not evidence. A fabrication executed with
equal care produces the same artifacts.

### 6.1 Why internal checks cannot settle it

The reconstruction passes 278 tests. This establishes nothing about fidelity.
The tests were written by the same process that wrote the code, against the
same understanding. They prove internal consistency, which a fabrication also
has. Static analysis, documentation coverage and a runnable demo are all in
the same category.

Provenance citations are better but insufficient: they establish that source
material was read, not that the thing built from it resembles what was lost.

What is needed is a measurement taken **before** the reconstruction, from
material the reconstruction did not see, that the reconstruction should be
expected to satisfy if genuine and fail if invented.

### 6.2 The instrument

Independently of URE, the same author's library had been measured for a
shared conceptual schema. That work is separate, has its own evidence
package, and predates this reconstruction. Its method, in brief:

- Every top-level class across 30 live repositories was extracted by syntax
  tree and hashed structurally.
- Class names recurring in three or more of 18 **training** repositories
  formed a spine of 189 names.
- The word tokens of those names were reduced by mechanical rules only
  (third-party frequency for generic words, dictionary and repository-name
  membership for proper nouns, and the single most generic survivor removed
  last), leaving a 56-token vocabulary.
- That vocabulary was used to score 7 **held-out** repositories and 12
  third-party control packages, on the share of each one's classes whose name
  carries a vocabulary token.

Published result: held-out repositories 25.4%, third-party controls 2.8%, a
9.0x separation. Five of the seven held-out repositories contained zero
structural copies of any training class, so the recurrence is convergence
rather than shared code.

### 6.3 Why URE is a better test than anything in the original study

The original study's weakness is the standard one: its held-out repositories
already existed when the vocabulary was derived. A sceptic can argue the
vocabulary was fitted, however mechanical the reduction.

URE is not subject to that objection, and could not have been constructed to
be:

- It was **not in the library**, so it contributed nothing to the spine.
- It was **not in the 18 training repositories**.
- It was **not among the 7 held-out repositories**.
- It **did not exist** when the vocabulary was derived. It had no repository
  at any point in its life.
- It was rebuilt by a process with **no knowledge of the schema work**. The
  reconstruction session never loaded it, cites none of it, and its
  provenance document does not mention it.

This is a prospective out-of-sample test on a case that materialized after
the instrument was calibrated.

### 6.4 Result

Scored with the published 56-token vocabulary, by the published method, over
the reconstruction's own source (tests excluded, as for the held-out
repositories):

| | classes | carrying a vocabulary token | 95% CI |
|---|---|---|---|
| **URE (reconstructed)** | 37 | **21.6%** | 11.4 to 37.2 |
| Held-out repositories, pooled | 579 | 25.4% | 22.0 to 29.1 |
| Third-party controls, pooled | 4,379 | 2.8% | 2.4 to 3.3 |

URE lands within four points of repositories that actually exist, and
7.7x above the control. Taking the least favourable reading available, URE's
lower bound against the control's upper bound, the separation is still 3.4x.

**Structural copies of any library class: zero.** The reconstruction did not
reproduce code. It reproduced concepts.

The tokens URE carries are `regime` (3 classes), `decision` (2), `health`
(2), `outcome` (1).

### 6.5 The sharper result: five names, no shared shape

URE independently defines five classes whose names recur across the library.
In every case the members differ almost completely:

| URE class | library definitions | max member overlap |
|---|---|---|
| `GovernanceDecision` | 7 | **0.00** |
| `Observation` | 4 | 0.20 |
| `RecoveryAction` | 3 | **0.00** |
| `AdaptiveThresholdController` | 3 | 0.11 |
| `ClassificationResult` | 1 | **0.00** |

URE's `GovernanceDecision` is an enumeration of verdicts: ALLOW, DENY,
QUARANTINE, THROTTLE, ISOLATE, DEGRADE, REVIEW. Across all seven library
definitions the members are records instead: `accepted, processor, reason,
status` in three of them, an eleven-field governance record in two others,
`allowed, reason, regime` in another. Not one member name is shared with
URE's. Same name, same role in the architecture, no shared content anywhere.

`RecoveryAction` is the same story in miniature. URE: an enumeration of
DEGRADE, ISOLATE, NONE, QUARANTINE, RESTORE, THROTTLE. The library: a record
of `action, execution_id, recovered, timestamp`. Both are unmistakably "the
recovery action" concept. Neither could have been derived from the other.

This is the distinction the schema study exists to draw, arriving on a case
that cannot have been contaminated. Had the reconstruction copied, the
overlaps would be high and the structural copy count non-zero. Had it
invented freely, the vocabulary score would sit near the 2.8% control. It
does neither.

### 6.6 One name, four domains

The clearest single instance. A regime enumeration recurs under one name
across four unrelated application domains:

| domain | members |
|---|---|
| Vehicle driving safety | STABLE, CAUTION, WARNING, CRITICAL |
| Clinical governance | STABLE, CAUTION, WARNING, CRITICAL |
| Actuator containment | STABLE, UNSTABLE, CRITICAL |
| Drone resilience (URE's recovered predecessor) | STABLE, SURGE, RESOURCE_OVERLOAD, ANOMALOUS_CRITICAL, SATURATED, CONTESTED |

A car, a hospital, an actuator and a drone. One class name. Every one begins
at `STABLE`. Beyond that first member the vocabularies share nothing.

The reconstruction then *renamed* it, deliberately, to follow the recovered
v2 specification, and documented the reconciliation. The schema match
survives the rename, because `regime` is a vocabulary token independent of
which particular word carries it.

### 6.7 The archive's own namespace, checked against the library

The strongest version of the argument does not rely on the reconstruction at
all, and was found by looking at what the archive recorded rather than at
what was built from it.

The corpus preserved URE's namespace family as three names:
`URE.OperationalRegime`, `URE.SystemResilienceConfig` and
`URE.ClassificationResult`.

**Two of those three independently recur in the library.**
`OperationalRegime` in three repositories, as §6.6 shows.
`ClassificationResult` in one, with zero member overlap.

This matters because it moves the finding back in time. Those names were
written in mid-2026, in conversations about a drone resilience engine, by
someone not thinking about a shared schema and with no instrument to measure
one. The schema was measured in September from thirty unrelated
repositories. The recurrence was already in the archive, waiting, before
anything existed that could detect it.

A reconstruction can be accused of pattern-matching its author. A transcript
written three months earlier cannot.

---

## 7. Results

Figures marked **(V)** were independently re-measured for this paper;
figures marked **(A)** are author-reported from the reconstruction session
and not re-verified. `FIGURES.md` records the command for each.

| | value | |
|---|---|---|
| Prompts | 2 | A |
| Corpus scanned | 242 MB, 1,768 files, 863 transcripts | A |
| Transcripts containing the subject | 24, with 2,644 raw occurrences | A |
| Acronym expansions found | 78 | A |
| Historical code recovered verbatim | 297 lines | A |
| Modules written | 15 | **V** |
| Package lines | 4,414 | **V** |
| Tests | 278, all passing | **V** |
| Runtime dependencies | 0 | **V** |
| Static analysis | mypy and ruff clean, as the repository's CI invokes them | **V** |
| Defects carried forward from the archive | 3 | A |
| Defects introduced during the build and caught | 4 | A |
| Schema vocabulary score | 21.6%, CI 11.4 to 37.2 | **V** |
| Structural copies from the library | 0 | **V** |

### 7.1 A finding about testing, incidental but strong

Four defects were introduced during the reconstruction. All were caught
before commit. What caught them is the point:

| defect | caught by |
|---|---|
| NaN energy classified as nominal | a test written to assert the opposite |
| Hysteresis could never release controls | a test asserting controls eventually release |
| Held recovery vectors carried the wrong controls | reading the demo's own output |
| A legitimate traffic surge classified as an attack | **running the demo** |

Two of four were invisible to the entire unit-test suite, because every unit
test agreed with the code. They surfaced only when a realistic scenario ran
end to end and the output was read by something that knew what the right
answer should look like.

This is an argument for shipping a runnable demonstration alongside a test
suite, and for putting that demonstration in continuous integration.

---

## 8. Threats to validity

Stated at full strength, because the most important one is the finding
rather than a weakness.

1. **Not reproducible without the archive.** The method depends entirely on
   the corpus. Strip the archive and the same two prompts correctly produce
   nothing. This is the central caveat and also the central claim.
2. **Small sample on the headline measurement.** 8 of 37 classes. The
   interval is wide, 11.4 to 37.2. The separation from the control survives
   the worst case at 3.4x, but the point estimate should not be presented as
   precise.
3. **Single subject, single author.** One reconstruction, one library, one
   person's conceptual vocabulary. The schema study is explicit that it does
   not show the schema exists independently of its author, and this paper
   inherits that limitation exactly.
4. **Not a bit-exact restoration.** The v2 architecture was specified and
   never built. This is an implementation of a design, not recovery of a
   binary.
5. **Not evidence the original would have worked.** The recovered predecessor
   contained a mock classifier.
6. **Not a production deployment.** Every number comes from the
   reconstruction's own suite and demonstration. It has never served traffic.
7. **Not unsupervised.** Four defects were introduced and caught by ordinary
   engineering discipline applied to the agent's work.
8. **The instrument shares an author with the subject.** The schema was
   measured from the same person's repositories that URE was reconstructed
   for. This is what makes the test possible and also bounds it: it shows the
   reconstruction is consistent with that author's schema, not with software
   in general. *Author input needed on how far to push this.*

---

## 9. Implications

**For organizations.** Treat design discourse as a first-class archival
artifact. Commit it, version it, keep assistants' histories separate so
claims can be cross-checked, and write handoff documents on the explicit
assumption that a future reader will have no access to the current files. The
cost is near zero. The option value is the ability to rebuild what you no
longer have.

**For component design.** A component with no repository, no tests, and no
consumer that outlives its host will not survive the host's cancellation. If
something is worth keeping, give it the three things that let it persist
independently.

**For verification of generated software.** An organization that has measured
its own conceptual schema gains an external check on generated work that no
internal test suite provides. This generalizes past reconstruction:
the same instrument scores any newly generated repository against the
organization's established vocabulary, and a score near the third-party
control is a signal that what was produced does not belong to the codebase it
claims to join.

That last implication is, on reflection, the most transferable result here,
and it is worth its own paper.

---

## 10. Provenance of this document

Draft 1 written 2026-09-11. The reconstruction it describes was performed the
same day in a separate session, whose own account is the subject's
`RECONSTRUCTION.md`.

The schema measurements in §6 were taken from the previously published
evidence package. The URE score, the copy count, the four name overlaps and
the four-domain regime comparison in §6.4 through §6.6 were computed for this
paper and are re-runnable; `FIGURES.md` records how.

Section 6 is new work and is the reason this is a paper rather than a
write-up. Sections 2 through 5 and §7.1 restate and reorganize the
reconstruction session's own account, which was written to be falsifiable and
is cited as the source rather than absorbed.

**Author input needed:** the framing question in §8.8, the disclosure
decisions in `REDACTION.md`, and whether §9's third implication should be
split into a second paper.
