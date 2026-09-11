> **CONFIDENTIAL DRAFT.** Not cleared for publication. See `REDACTION.md`.

# Conversational Archaeology

**Reconstructing a lost software system from archived design discourse, and
why verifying such a reconstruction is harder than it looks**

*Draft 2, 2026-09-11. Draft 1 claimed the reconstruction was verified against
the author's conceptual schema. A clean-room control run during adversarial
review showed that measure reports domain rather than authorship. See
`RED_TEAM.md`.*

---

## Abstract

A software system designated SYS-URE-001 was specified and partially built in
mid-2026, never acquired a repository, and was abandoned when its only
consumer was cancelled. Four months later it was reconstructed to working
software from an input of two sentences, one of which contained only its
three-letter name. The rebuild produced fifteen modules, 278 passing tests
and zero runtime dependencies, together with a dated account of the system's
lifecycle and cause of death.

The reconstruction is not the contribution, because a plausible
reconstruction and a confident fabrication are indistinguishable by
inspection: both compile, both have tests, both read as coherent. The
question this paper is organised around is the second one: **given a
reconstruction, how would you know it is one?**

We attempted to answer it with an instrument the subject's organisation
already had, a conceptual schema measured independently from eighteen
unrelated repositories before the reconstruction began. The rebuilt system
scored 21.6% on that schema's published vocabulary, against 25.4% for
repositories that actually existed and 2.8% for third-party control
packages, with **zero** structural copies of any library class and member
overlap of 0.00 wherever a class name recurred.

**That result does not survive a control the original schema study did not
have.** Two fresh model sessions, given only a prose description of the
system's function with no access to the archive, the library, or any of the
author's material, score 14.8% on the same vocabulary. Most of the
separation the schema study reports is therefore attributable to **domain**
rather than to authorship: governance and resilience code contains
governance and resilience words, and the study's twelve controls were all
off-domain.

We report this as the paper's principal finding, because it is the more
useful one. What survives is a well-evidenced reconstruction, a
demonstration that it copied no code, and a negative methodological result:
**a study claiming an organisation has a distinctive conceptual vocabulary
requires a domain-matched control, and without one it will measure its
subject matter instead.** We also report a sharper hypothesis the control
exposed: the concepts a system needs appear to be determined by its domain
and reachable by anyone, while the particular words are the author's. The
clean-room sessions reached every one of the subject's concepts and none of
its names.

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

### 6.3 Why URE is a better subject than anything in the original study

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

This is a prospective out-of-sample subject that materialised after the
instrument was calibrated. It removes the fitted-vocabulary objection
entirely. It does not, as §6.4 shows, remove the objection that the
instrument measures domain rather than authorship, and no choice of subject
could have: that required a control, not a better case.

### 6.4 Result, and the control that undoes its interpretation

Scored with the published 56-token vocabulary, by the published method, over
the reconstruction's own source with tests excluded as for the held-out
repositories:

| | classes | carrying a token | 95% CI |
|---|---|---|---|
| URE (reconstructed) | 37 | 21.6% | 11.4 to 37.2 |
| Held-out repositories, pooled | 579 | 25.4% | 22.0 to 29.1 |
| Third-party controls, pooled | 4,379 | 2.8% | 2.4 to 3.3 |
| **Clean-room model, same domain, no access** | **88** | **14.8%** | **9.0 to 23.3** |

The last row is ours and it is the one that matters. Two fresh model
sessions were given a prose description of the system's function, with every
name removed, no archive, no library, and no tools, and asked only which
class names they would define. With access to none of the author's material
they reach 14.8%, against the reconstruction's 21.6% and the library's
25.4%.

**Interpretation.** The gap between the library and third-party packages is
real but is largely a gap between *domains*, not between authors. A
resilience engine contains the words "regime", "decision", "health" and
"outcome" because that is what resilience engines are about. An HTTP client
and a numerical library do not. The schema study's twelve controls were an
HTTP client, a database driver, a numerical library, a web framework, a type
checker, a build tool, a crypto library and an API SDK. None was a
governance system, so the study could not distinguish its hypothesis from
its subject matter.

We also decompose the score, which points the same way: three of URE's eight
vocabulary hits come from `health` and `outcome`, both of which the study's
own control-token list reports the third-party packages carrying.

### 6.5 What the name-level evidence shows, after contamination control

Exact class-name recurrence is a stronger instrument than the vocabulary,
because it involves no token list, no reduction rules and no judgement. It
asks only whether the same name appears.

It requires one control the draft of this paper initially missed. The
reconstruction session had two library repositories attached and searched
them. Any name present in those two could have been echoed rather than
reached:

| URE class | in an attached repo | library definitions | member overlap |
|---|---|---|---|
| `GovernanceDecision` | no | 7 | **0.00** |
| `RecoveryAction` | no | 3 | **0.00** |
| `AdaptiveThresholdController` | no | 3 | 0.11 |
| `Observation` | **yes** | 4 | discarded |
| `ClassificationResult` | **yes, and nowhere else** | 1 | discarded |

Three of thirty-seven scored classes, 8.1%, carry names that recur in the
library with no contamination path. Against third-party packages, whose
pooled rate is 0.5% and whose worst single outlier is 2.4%, that is a large
multiple. Against the clean-room model's 3.4% it is a factor of 2.4 on three
events against three, **which is not separable at this sample size and
cannot carry a claim.**

None of the five names, nor any of the three names the archive preserved as
the system's original namespace, appears anywhere in a 4,985-name corpus
spanning twelve third-party packages. They are not common Python names. That
closes one objection and leaves the one above open.

### 6.6 The finding the control actually produced

The clean-room sessions reached **none** of the three contamination-free
names. What they produced instead:

| the author's material | clean-room model |
|---|---|
| `OperationalRegime`, `SystemRegime` | `OperatingMode`, `OperatingState` |
| `RecoveryAction` | `RemediationAction`, `RemediationStep` |
| `AdaptiveThresholdController` | `ThresholdAdapter`, `ThresholdTuner` |
| `GovernanceDecision` | `DecisionRecord`, `JudgementRecord` |

Every concept, none of the words. That is a more precise hypothesis than the
one we set out to test:

> The concepts a system requires are determined by its domain and are
> reachable by anyone competent in that domain. The particular words are the
> author's.

The vocabulary measure operates on the first layer, which is why a
clean-room model matches it. Exact-name collision probes the second, which
is why it trends in the right direction but lacks the events to prove
anything. **Constructing a measure that isolates the lexical layer is the
open problem this paper leaves behind,** and it is a better problem than the
one it started with.

### 6.7 What the archive escapes, and what it does not

The corpus preserved the system's namespace as three names:
`OperationalRegime`, `SystemResilienceConfig` and `ClassificationResult`.
Two of the three independently recur in the library, and
`AdaptiveThresholdController` appears in a transcript dated 2026-06-19 as
well as in two unattached library repositories.

Those transcripts predate the reconstruction, the schema measurement, and
any instrument capable of detecting a schema. So the archive evidence
escapes two objections: it cannot have been echoed from an attached
repository, and the vocabulary cannot have been fitted to it.

It does **not** escape the model-prior objection, and an earlier draft of
this paper wrongly claimed that it did. The archive is a collection of AI
conversation transcripts. A model wrote those names too. The correct claim is
narrower: the recurrence is datable to mid-2026 and is not an artefact of the
reconstruction. Whether it is an artefact of the tools used to produce the
archive is exactly what §6.4 leaves unresolved.

### 6.8 Status of the central claim

Ordered by how hard each is to attack:

1. A system with no repository was reconstructed from archived design
   discourse. **Established.**
2. The reconstruction contains no copied code: zero structural matches
   across the available library. **Established.**
3. Where names recur, shapes do not: member overlap 0.00 on the surviving
   cases. **Established**, and the cleanest evidence that whatever is shared
   is conceptual rather than textual.
4. The recurrence is not general Python naming convention. **Established**
   against off-domain packages.
5. The recurrence predates any instrument that could detect it.
   **Established** for two names, datable to June and July 2026.
6. The library therefore shares a conceptual schema attributable to its
   author. **Not established, and positively doubted** by §6.4.

Claim 6 is the one that would have made this paper exciting. Testing it is
what took it away, which is the correct outcome: it would have been falsified
by the first reviewer to run a domain-matched control, and it is better that
it was falsified here.

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
8. **The instrument shares an author with the subject,** which bounds what a
   positive result could ever have meant.
9. **The clean-room control is two sessions of one model family.** A
   different model, or a human engineer given the same brief, might score
   differently. Two trials with 88 names is enough to overturn the
   vocabulary claim, and not enough to quantify the effect precisely.
10. **No domain-matched human baseline exists yet.** An open-source policy
    engine, SRE toolkit or incident-management library by another author,
    scored the same way, would separate domain from era from model. Until it
    exists, those three explanations remain entangled. This is the single
    most useful experiment still outstanding.

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

**For verification of generated software.** The idea that an organisation
could score generated work against its own measured vocabulary is attractive
and, on this evidence, does not work. §6.4 shows such a score mostly reports
the domain of the work rather than its provenance, so a fabrication written
in the right domain passes. Anyone building such a check needs the lexical
layer isolated first, per §6.6, and that measure does not yet exist.

**For anyone measuring an organisation's conceptual fingerprint.** Use a
domain-matched control. Off-domain controls make any subject look
distinctive, because they are measuring subject matter. This is the paper's
most transferable result and it is a negative one.

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
