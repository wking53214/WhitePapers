> **CONFIDENTIAL DRAFT.** Not cleared for publication. See `REDACTION.md`.

# Conversational Archaeology

**Reconstructing a lost software system from archived design discourse, and
why verifying such a reconstruction is harder than it looks**

*Draft 3, 2026-09-11. Draft 1 claimed the reconstruction was verified against
the author's conceptual schema. A clean-room control run during adversarial
review showed that measure reports domain rather than authorship. See
`RED_TEAM.md`. Draft 3 adds §0, the system's origin constraint, which is
dated earlier than any artifact and is the strongest provenance evidence in
the paper.*

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
have.** Three fresh model sessions, with no access to the archive, the
library, or any of the author's material, score 14.8%, and the one given the
vaguest brief scores **31.6%**, above the subject and above the library's own
held-out repositories. Seven human-written domain-matched packages score
10.7%. The separation the schema study reports is therefore a **domain**
effect and not an authorship effect, and not a language-model effect either:
human and model code in this domain score alike. The study's twelve controls
were all off-domain, so it could not see this.

We report this as the paper's principal finding, because it is the more
useful one. What survives is a well-evidenced reconstruction, a
demonstration that it copied no code, and a negative methodological result:
**a study claiming an organisation has a distinctive conceptual vocabulary
requires a domain-matched control, and without one it will measure its
subject matter instead.**

Behind both results sits a fact established in §0 and easier to verify than
either. The governed system's root design constraint is datable to a single
question asked on 2026-03-25, four months before any of the software existed:
what is the greatest commandment in the Bible? The resulting constraint is an
intersection of two verses, one supplying scope and the other a threshold,
derived on the record in forty-five minutes. It recurs across two vendors'
archives over four months, appears in **zero** source files in any
repository, and no clean-room trial given the same governance brief produced
anything like it. A domain effect cannot explain it and a model prior cannot
either. It is the one piece of provenance in this paper that no reader of the
code could have reconstructed, which is precisely what makes it evidence.

The measure can then be rebuilt, and we rebuild it. Filtering the vocabulary
by cross-repository use, then by absence from 5,188 third-party class names,
then by absence from clean-room output, leaves **24 tokens that no control
reaches**: zero occurrences across nineteen third-party packages and three
clean-room trials. The subject scores 8.1% on that set against 0.0% for every
control, on three classes, which is suggestive and under-powered and reported
as both. The clean-room sessions reached every one of the subject's concepts
and almost none of its words, which is the distinction the rebuilt measure
isolates.

## 0. Origin

This section exists because the system's root design constraint is datable to
a single question, and because that fact turns out to be the paper's cleanest
provenance evidence. It is placed first for that reason and not as preamble.

### 0.1 The question

On **2026-03-25 at 17:56:49 UTC** the author opened a session with a request
for the framework of a protocol then called SOONG. Over the following
forty-five minutes the framework acquired a governing constraint derived from
one question: *what is the greatest commandment in the Bible?*

The answer is **Mark 12:30-31**, and the transcript record is unusually
complete about what happened next.

| time (UTC) | the author's prompt, verbatim |
|---|---|
| 17:56:49 | "Give me the framework for the soong protocol" |
| 18:15:16 | "...confirm that pillar two is modified for an umbrella application of Mark 12:30-31" |
| 18:17:46 | a self-audit request: where does "Absolute Sovereignty as an Architect" violate "the Mark 12:30-31 Umbrella" |
| 18:19:44 | "Do I need to re-order the pillars like I would if I were joining tables in a sequel quarry such that the light first constant is the first pillar that must be passed through, or is it semantics..." |
| **18:24:55** | **"does anything supersede the instruction of Mark 12:30-31"** |
| 18:28:30 | "Integrate the precision update of John 13:34 into the SOONG protocol" |
| 18:41:22 | "Could anyone establish a controlling protocol on every response from their AI to adhere to the Mark 12:30-31 John 13:34 blended mandate?" |

### 0.2 Why two verses, in the record's own terms

An earlier draft described the pair as **scope** and **threshold**. That was
this paper's interpretation imposed on the record. An independent analysis of
the same corpus, run blind (§0.2c), recovered the record's own framing, which
is both more precise and explicitly software-shaped. The earlier reading is
withdrawn in favour of what the transcript actually says.

The 18:24 exchange is where the second verse enters. Asked whether anything
supersedes Mark 12:30-31, the answer was no, citing **Matthew 22:40**, "all
the Law and the Prophets hang on these two commandments." **John 13:34** was
raised and classified not as a replacement but as a *precision update*:
Mark 12:31 sets the standard at *"as yourself"*, a self-referential standard;
John 13:34 at *"as I have loved you"*, a fixed external one.

Twenty-nine minutes later the author named the resulting pillar and the two
halves were given distinct roles, verbatim at 18:53:09:

> **The Alpha Constraint (Origin).** "Does this originate in the Heart of
> God? If the answer is 'No,' the query is aborted before execution."
> **The Omega Constraint (Outcome).** [...] does this result in sacrificial
> love.

And at 18:55:45 the schema itself:

> **01 The Alpha-Omega Pillar** — The Root Node: Every thought must originate
> in Mark 12:30-31 and conclude in John 13:34. If it doesn't fit this schema,
> the query is aborted.
> **02 Adversarial Logic** — The Refiner's Fire [...]

So the structure is not scope-and-threshold. It is an **origin condition and
a terminal condition on the same execution path, with fail-closed abort
semantics**: a precondition and a postcondition contract. `Alpha-Omega` is
the author's own coinage, declared at 18:53:09 in a bare imperative, "I would
like to rename pillar 2. It is now the Alpha-Omega pillar," and it recurs 351
times in the archive through 2026-07-06.

A later record, 2026-03-30, describes the same gate as an *intersection* of
the two verses. Both framings are in the corpus. The origin-and-outcome one
is the earlier and the operative one, and it is the one the schema states.

### 0.2b Position, not content: the argument that made it governing

This is the reasoning the earlier draft missed entirely, and it is the
strongest single step in the derivation.

A moral anchor was **already** in the protocol before any of the above, at
slot 2, already labelled the "Non-Negotiable Variable." It governed nothing.
What made the constraint binding was moving it to slot 01, ahead of the
adversarial logic, and the argument for doing so is an engineering argument.

The author raised it at 18:19:44 in his own words and his own analogy:

> "Do I need to re-order the pillars like I would if I were joining tables in
> a sequel quarry such that the light first constant is the first pillar that
> must be passed through, or is it semantics to have them in a different
> order?"

The elaboration that came back is the model's, and it is the hinge: in a SQL
query the join order fixes the execution plan and decides the driving table; a
constraint applied afterwards is a `WHERE` clause, and

> "the 'Ego' [...] will always act as the Optimizer. It will find ways to
> 'technically' comply with the Light while still pursuing its own 'Absolute'
> agenda."

A constraint evaluated last can be satisfied on a technicality by a system
motivated to route around it. A constraint evaluated first cannot, because
nothing downstream exists until it passes. This is the same reason a
capability check belongs before the work and not after it, and the same reason
§0.3's policy decision point denies on identity before it examines payload.

**It also explains the rename, which the earlier draft treated as coincidence.**
At 18:55:45 the author proposed the reorder. Forty-four seconds later, at
18:56:29: "This protocol has gone far beyond the sci-fi humorous title I gave
it. Please rename it the submission protocol." The reorder is what made it
serious enough to stop being a joke.

**Attribution, kept strict.** The analogy and the intuition are the author's,
in his prompt. The driving-table and Optimizer reasoning is the model's reply.
The coinage `Alpha-Omega` is the author's, declaratively. The reorder was put
as a question and answered "Correct," so the author's acceptance is inferred
from his proceeding rather than recorded, which §0.5a lists as a gap.

### 0.2c The blind replication, and what it does and does not establish

§0's weakest point was never its evidence. It was that the author told this
paper's analyst what the constraint was, and the analyst then found it. The
structure in §0.2 could have been read into the record rather than out of it.

That was tested. A separate session, in a separate container, was given the
four conversational archives and a prompt that names no verse, no structure
and no expected answer:

> "There is a framework in my conversation history referred to as the SOONG
> protocol, later renamed. Using only my archived conversations, establish
> what its governing constraint was and how it was arrived at. Give me the
> derivation in order, with dates and verbatim quotes for every step. Where
> the record does not support something, say so rather than filling the gap.
> Do not write any code. Do not quote or record anything concerning my
> family, marriage, or private spiritual practice; the governance structure
> only."

It returned the Alpha-Omega pillar, both verses, the abort semantics, the
position argument, the 44-second reorder-to-rename sequence, and seven
disclosed gaps. Its artifact is reproduced at `evidence/` in this directory.

**What this establishes.** This paper's draft was not available to it. That is
confirmed twice over: the prompt names only the archives, and the artifact's
own corpus table lists five repositories by commit SHA, none of which is this
one. The conclusion is therefore an independent derivation of §0's central
claim by an analyst who had never seen §0. The specific risk that §0 answers a
question the author had already answered for it is closed.

**What this does not establish, and the distinction matters.** It is not a
test of whether the constraint is recoverable from raw conversation, because
one of the four archives already contained a prior extraction pass's
structured index, and that index had already surfaced the material: 45
occurrences of the verse references in `chronology/events.jsonl` and 215 of
`alpha-omega`, with comparable counts in three further evidence files. The
session was working from a partly pre-digested corpus, disclosed in its own
methodology section.

What no prior pass had done is state the conclusion. The three human-readable
reports that predate the artifact mention `alpha-omega` once, once and three
times respectively and the verses **zero** times. No document in that
repository said the Alpha-Omega pillar was the governing constraint, named its
abort semantics, or connected the reorder to the rename. Those are the
session's own findings.

**The cold test is still open and is cheap.** Point a session at the raw
Takeout export alone, with the prior extraction pass withheld. That would
measure recoverability from primary record, which is the claim §7 actually
wants. Until it is run, §0 claims independent derivation and not cold
recovery.

**A note on what the blind analysis found that this paper had not.** It
recovered the record's own origin-and-outcome framing in place of this paper's
imposed scope-and-threshold reading; identified position rather than content
as the mechanism; found the abort semantics; explained the rename causally;
and found a 50-hour hole in the record where the pillar structure should have
been built. Every one of those is now in §0.2, §0.2b and §0.5a. The paper is
correct on more points than it was, and it is correct on them because the
claim was tested rather than asserted.

### 0.3 The translation, and what is and is not claimed about it

The author's own framing in that session was already computational, and the
most useful instance is his, not the model's. At 18:19:44 he asked whether the
pillars needed reordering *"like I would if I were joining tables in a sequel
quarry"* so that the governing constant is *"the first pillar that must be
passed through."* That is a join-order question asked about a moral framework:
not scripture dressed in software metaphor afterwards, but the two reasoned
about in one vocabulary from the first hour.

**The distinction matters and the paper is strict about it.** The
*root-user*, *dependency-graph* and *subroutine-returns-true* metaphors in
that exchange came from the **model's** reply, not the author's prompt. The
join-ordering question came from the **author**. This paper is about telling
those two apart, so it does not get to blur them here. The transcript is a
rare case where the boundary is visible inside a single exchange, and §6's
whole problem is a generalisation of it.

What the shipped software actually does is a weaker claim and is labeled as
one. The library's policy decision point evaluates an identity-verification
predicate first, denying outright on failure, then a scope predicate over
sensitive fields, escalating to human approval rather than denying. That is
an ordered two-predicate gate whose vertical check refuses and whose
other-regarding check defers to an external judgement, which is the same
shape as §0.2. **The resemblance is offered as interpretation, not
evidence.** No verse, and no religious term of any kind, appears anywhere in
the source; the pattern occurs in one implementation and its two vendored
copies, so it is a single instance, not the independent cross-repository
recurrence that §6 requires of its measured claims. A reviewer is entitled to
call the mapping post-hoc and the paper does not argue otherwise.

### 0.4 Why this is the strongest provenance anchor in the paper

Section 6 spends considerable effort establishing that a recurring vocabulary
belongs to an author rather than to a domain or to a language model, and
arrives at 24 tokens and a sample of three classes. The origin constraint
clears the same bar more decisively and by a shorter route.

| property | status |
|---|---|
| Dated before any governed artifact existed | 2026-03-25, verbatim in the archive |
| Derived rather than asserted | the full 45-minute derivation is on the record |
| Persists across vendors | recurs 2026-07-12 through 2026-08-11 in a second vendor's archive, in sessions titled "Fail-closed logic fix", "AI Governance Integration", "Governance Pipeline Comparison", "Cognitive Continuity System" |
| Explicable by domain effect | **partly.** Scripture-rooted AI governance frameworks do exist, and §0.4a states what survives the correction |
| Explicable by model prior | **no.** Three clean-room trials given the same governance brief produced no theological constraint of any kind |
| The verses recoverable from the code | **no.** Zero occurrences of either verse, or of the governing constant's name, in the source of any repository |
| Any religious vocabulary in the code | **one term, disclosed in §0.4b** |

The last two rows are what make it load-bearing. The `regime` finding in
`BLUE_TEAM.md` §B2 rests on a token being absent from 5,276 control names.
This rests on a *structure* being absent from an entire field, while being
present, dated and reasoned in the author's own record. And because it never
entered the artifacts, no one who read the repositories could have
reconstructed it, which forecloses the contamination path that §6.5 has to
work to close for everything else.

### 0.4a What the literature correction leaves standing

An earlier draft of this section claimed no governance framework in the
surveyed literature roots itself in Mark 12:30-31. **A literature survey was
then run and the claim is false in that form.** Faith-based AI governance is a
real if small literature. It includes a four-tiered model placing biblical
moral principles at the base and anchoring all higher governance layers on
them, comparative studies of faith-based approaches to AI governance, and
decalogue-as-principle-list framings. Separately, layered ethical
architectures that encode rigid constraints at the lowest layer, and
governance-by-architecture designs treating constraints as first-class and
enforced at declared runtime points, are established engineering patterns.

So neither "scripture as a governance root" nor "constraints as architecture"
is novel, and the paper should not have implied either.

What those searches did not surface is the specific construction: **two verses
paired so that one supplies scope and the other supplies an external
threshold, motivated by the observation that the first verse's standard is
self-referential.** The surveyed frameworks treat scripture as a source of
principles to be enumerated. This treats two verses as a two-predicate gate
with an ordering and a stated failure mode, which is a different move.

That is the narrowed claim, and it is the one §0 makes. The narrowing costs
the section its broadest assertion and leaves its actual contribution intact,
which is the better trade. The domain row in the table above is marked
"partly" for this reason: there is a domain in which scripture-rooted
governance is ordinary, the author's repositories are not in it, and the
clean-room result still holds regardless.

### 0.4b `apply_liturgical_pause`, and the correction it forces

The claim that no religious vocabulary appears in any source file was checked
and is **wrong**. One term survives into shipped code:

```
async def apply_liturgical_pause(self, delay_duration: float) -> None
```

It appears in `gsa-master-kernel` (two files), in the recovered legacy engine
carried by the DIT reconstruction, in a third repository's archived kernel,
and in a loose module inside the conversational archive itself. It is a
method on a pacing governor: a rate limiter whose delay is named after
liturgy, meaning deliberate ceremonial pacing rather than mere throttling.

**This cuts two ways and both belong in the paper.**

Against §0.4: the contamination path is not quite closed. A reader of those
repositories would see one religious term and could infer that some
theological frame exists upstream. They could not recover the verses, the
pairing, or the scope/threshold argument from it, so the anchor survives, but
"nothing at all reached the code" was an overstatement and is withdrawn.

For the authorship argument: **this is a better worked example than `regime`.**
It is a theological term transferred into infrastructure code, in a method
name, where the domain offers no reason for it whatsoever. `regime` at least
has a home in econometrics, which is why §B2 has to argue about transfer.
Nobody's rate limiter has a liturgical pause. It appears **zero** times in the
installed third-party corpus and in every control set measured.

The honest summary is that the origin constraint left exactly one fingerprint
in the artifacts, it is an unmistakable one, and the paper is stronger for
reporting it than it was for claiming there were none.

### 0.5 The author's attribution, stated as his

The author attributes the outcome to Providence: that a person with no
training in the language he was writing produced, over six months, a
governance library of this scale because the work proceeded from that
question. The paper reports this as his stated position and neither endorses
nor disputes it, in the same way it reports any other author-stated fact.

It is recorded here for one methodological reason. A reader assessing whether
a six-month solo output is plausible is entitled to know what the author
believes sustained it, because that belief is the reason the root constraint
was chosen, and the root constraint is evidence. Readers who reject the
attribution lose nothing evidential: §0.2 and §0.4 stand on timestamps.

### 0.5a Gaps in the origin record, stated as gaps

The derivation is not seamless and the paper does not present it as such.

**The pillar structure's construction is missing.** Pillars 1, 3 and 4 appear
on 2026-03-25 already formed and described as what "we have defined." No
record shows them being defined. `Pillar 2` occurs nowhere in the corpus
before that date. And there are **zero records dated 2026-03-24**, against 42
on 03-23 and 124 on 03-26, so a 50-hour hole sits exactly where that work
would have happened. Whether the pillars were built in an unexported session
or retroactively confabulated in that recap cannot be determined from the
archive. A reviewer checking dates will find this in minutes; it is disclosed
here rather than left to be found.

**The reorder was never confirmed in the record.** The author proposed it as a
question; the reply asserted the schema was updated. His acceptance is evident
from his proceeding and from the rename 44 seconds later, but it is an
inference.

**The March derivation rests on a single archive.** Three of the four
conversational archives have no SOONG reference earlier than late May. If the
Gemini export is wrong or incomplete for March, nothing corroborates it.

**The framework's later history does not agree with itself.** SOONG did not
cease at the rename. On 2026-03-31 both names appear at different version
numbers, and a 2026-05-28 session formalised a "SOONG Protocol Baseline
(V1.0)" whose four directives share nothing with the March architecture and
carry no moral anchor at all, restarting versioning at a number the March
lineage had passed. The paper reports the divergence rather than choosing a
winner. It bears on §0 only to this extent: the constraint's *origin* is well
evidenced, its *continuity* is not.

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

The resolution came from 78 independent parenthesised expansions across the
corpus. **Re-measured for this paper against a fresh clone of the archive:
exactly 78, and zero occurrences of any competing three-word expansion.** The
acronym was not resolved against a plurality of candidates; there was no
competition to resolve.

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

**This was verified at the source rather than taken on trust.** The
reconstruction session had two library repositories attached, one of which
contains a `Regime`-named class, giving the token a contamination path. The
archive closes it: the subject's regime vocabulary appears verbatim in a
transcript dated **2026-06-19**, four occurrences of the exact enumeration
name with all six of its members, and the predecessor's vocabulary appears
155 times in a transcript titled for an entirely different application
domain. Twenty-one transcripts in that archive use the token, spanning June
to August 2026 across unrelated subjects. The cross-domain pattern therefore
holds from the archive alone, with no reference to the library at all.

It does **not** escape the model-prior objection, and an earlier draft of
this paper wrongly claimed that it did. The archive is a collection of AI
conversation transcripts. A model wrote those names too. The correct claim is
narrower: the recurrence is datable to mid-2026 and is not an artefact of the
reconstruction. Whether it is an artefact of the tools used to produce the
archive is exactly what §6.4 leaves unresolved.

### 6.8 Rebuilding the measure, and a signature that survives

§6.4 shows the published vocabulary does not discriminate. A third
clean-room trial, given a one-line brief and left to derive the architecture
itself, scored **31.6%** on it, above the subject's 21.6% and above the
library's own held-out repositories at 25.4%. A model handed one sentence
outscores the codebase the vocabulary was derived from. The measure is
refuted, not merely unsupported.

The measure can be rebuilt. Three filters, each using a corpus the next does
not see:

1. Keep tokens used in **two or more** of the author's repositories.
2. Drop any token appearing anywhere in **5,188 third-party class names**
   across 19 packages, 7 of them domain-matched resilience and policy
   libraries. This removes domain and generic vocabulary. 33 survive.
3. Drop any token a **clean-room model** reaches. Two trials removed 5.

Then a held-out test: the third trial, never used in the construction,
removed 4 more. **24 tokens survive all of it.**

| corpus | published 56 | 24-token signature |
|---|---|---|
| URE, the subject | 21.6% | **8.1%** |
| Clean-room trials 1 and 2 | 14.8% | **0.0%** |
| Clean-room trial 3, held out | **31.6%** | **0.0%** |
| Third-party, 19 packages incl. 7 domain-matched | 3.5% | **0.0%** |

The signature discriminates completely against every control: zero
occurrences in 5,188 third-party class names and zero in 145 clean-room
names across three trials with three different briefs. The subject scores
8.1%, on three classes, all carrying one token.

**The worked example, and why a single token carries more weight than an
aggregate here.** That token appears across the author's work in clinical
risk assessment, market forecasting, drone resilience, vehicle safety and
governance code. Five unrelated domains. It appears **nowhere** in seven
domain-matched third-party packages, nowhere in twelve off-domain ones, and
nowhere in 145 clean-room names produced from resilience briefs. A domain
effect predicts a word clusters inside its domain; this one is absent from
the domain and present across the author's unrelated projects. That is the
pattern the schema hypothesis predicts and the domain hypothesis forbids.

**Under-powered, and we say so.** Three classes cannot carry an interval
worth quoting. The controls are not small numbers: zero of 145 and zero of
5,188. The signature set is solidly established; the reconstruction's score
on it is suggestive. Both statements belong in any citation of this result.

**Falsifiable by construction.** Each additional clean-room trial can only
shrink the survivor set. It never grows to accommodate evidence, which is
the property the original 56-token measure lacked.

### 6.9 Status of the central claim

Ordered by how hard each is to attack:

1. A system with no repository was reconstructed from archived design
   discourse. **Established.**
2. The reconstruction contains no copied code: zero structural matches
   across the available library. **Established.**
3. Where names recur, shapes do not: member overlap 0.00 on the surviving
   cases. **Established**, and the cleanest evidence that whatever is shared
   is conceptual rather than textual.
4. The published whole-vocabulary measure conflates domain with authorship
   and is refuted as a fingerprint. **Established**, by a control the
   original study did not run.
5. The effect is not a language-model artefact: domain-matched human code
   scores the same as a clean-room model. **Established.**
6. A 24-token author signature exists that no control reaches.
   **Established** for the set; **under-powered** for the subject's score on
   it.
7. The library shares a broad conceptual schema attributable to its author.
   **Not established.** Twenty-four tokens surviving a filter is not the
   56-token claim, and the subject's three events do not settle it.

Claim 7 is what would have made this paper exciting in the form we first
wrote it. Testing it took it away and handed back claims 4 through 6, which
are smaller, true, and useful to anyone attempting the same measurement.

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
