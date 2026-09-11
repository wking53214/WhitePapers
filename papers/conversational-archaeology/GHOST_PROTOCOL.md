> **CONFIDENTIAL.** Not cleared for publication. See `REDACTION.md`.

# Summoning further ghosts: does it help, and how to do it so it counts

Short answer: **yes, more than anything else available, and only if the
protocol below is followed exactly.** A second reconstruction run carelessly
is worth less than none, because it converts a clean under-powered result
into a contaminated one.

---

## 1. Why it helps

The paper's evidence has exactly one weak joint. The 24-token signature
discriminates perfectly against every control, zero of 5,188 third-party
names and zero of 145 clean-room names. The subject's score on it rests on
**three classes**. Three events cannot carry an interval anyone should quote,
and `RED_TEAM.md` A5 says so.

Each ghost is an independent replication that attacks precisely that joint:

| ghosts | signature-carrying classes, if the rate holds | what can be claimed |
|---|---|---|
| 1 (now) | ~3 | suggestive, under-powered |
| 3 | ~9 | an effect with a quotable interval |
| 5 | ~15 | a measured rate with a real lower bound |

It also upgrades the reconstruction claim itself. One reconstruction is a
demonstration. Five is a method with a success rate, and failures are as
informative as successes.

## 2. Why it helps *more than it would have yesterday*

The 24-token signature exists **now**, written down, before any further ghost
is summoned. That permits the strongest design available in this kind of
research: **pre-registration.** The prediction is recorded before the data
exists, so nobody can argue the measure was tuned to fit.

### Pre-registered prediction, recorded 2026-09-11

For each ghost reconstructed under §4's protocol, scored against the frozen
24-token signature set:

| corpus | predicted score |
|---|---|
| Each ghost's own source | **above 0%**, point estimate 5-12% |
| A clean-room model given that ghost's function | **0%** |
| Pooled across 3+ ghosts | **above 3%, lower bound above 0** |

**Falsification conditions, stated in advance.** Any of these means the
signature hypothesis fails and the paper reports that:

- Pooled ghost score is **0%**. The signature does not transfer and describes
  only URE.
- A clean-room model scores **above 0%** on the frozen set. The set was never
  author-specific; three trials were too few.
- Ghost scores are indistinguishable from their matched clean-room controls.

The set is frozen as of this file. It **must not be recomputed** after a
ghost is summoned, because recomputing it on new data is how a
pre-registration becomes a fit.

## 3. The census: how many ghosts actually exist

Measured, not guessed. The ChatGPT archive, 1,768 files, the largest of the
four and the one URE came from.

**Formal designators, the URE pattern:**

| designator | uses | has a repository? |
|---|---|---|
| `SYS-URE-001` | 42 | **no, this was the ghost** |
| `SYS-SENTINEL-001` | 2 | yes |
| `SYS-SYNAPSIS-001` | 1 | yes |
| `SYS-GSA-001` | 1 | yes |

**By acronym expansion, the URE method's step 4,** filtered to acronyms with
a consistent multi-word expansion and no matching repository:

| candidate | uses | files | expansion agreement |
|---|---|---|---|
| **URE** (for calibration) | 75 | 6 | 75/75 |
| **DIT**, Deterministic Integrity Tower | 12 | 4 | **12/12** |
| ECP, Execution Control Pipeline | 9 | 2 | 6/9 |

Everything else the filter returned was a banner-header artefact
(`APPLIED (THIS VERSION ONLY)` and similar), not a system.

**The honest read.** URE was exceptional: 75 consistent expansions across 6
transcripts. `DIT` is the one genuine remaining candidate visible in this
archive, at a sixth the density but with perfect expansion agreement. `ECP`
is marginal.

**Three archives are unsearched:** `Claude_History`, `Gemini_History`,
`CoPilot_History`. Run the same census there before planning anything. Do not
assume they are as rich; URE's density may be unrepeatable.

So the realistic yield is **1 strong ghost plus whatever the other three
archives hold**, not a pile. That is still enough to matter, because going
from 1 subject to 3 is the difference between under-powered and quotable.

## 4. The protocol, and why each rule exists

Every rule below exists because something went wrong with URE.

**R1. No library repository may be attached to the summoning session.**
Archive repositories only. URE's session had `sentinel_os` and
`innovation_os` attached, which voided two of five shared names and cost the
paper its headline. This single rule is the difference between clean evidence
and an afternoon's argument.

**R2. Record every attached repository in the reconstruction's own
provenance.** `RECONSTRUCTION.md` names two of four attached repos. The other
two are unidentified, which means the contamination analysis cannot be closed
even now. Name all of them.

**R3. The summoning session must not see CNS, this paper, the signature set,
or any of the schema work.** It should not know it is being measured. If it
knows the target vocabulary, the result is worthless.

**R4. Score afterwards, from a separate session, against the frozen set.**
Never during. Never by the session that did the reconstruction.

**R5. Run a matched clean-room control per ghost,** briefed from a one-line
problem statement by someone who has not read that ghost's reconstruction.
§B3 of `BLUE_TEAM.md` is what happens when the briefer has read the subject.

**R6. Pre-commit to reporting failures.** A ghost that scores 0% goes in the
paper. A summoning that finds nothing recoverable goes in the paper. The
method's credibility is entirely in whether the negative cases appear.

**R7. Keep the two prompts.** URE's power as a case rests on the input having
been two sentences. Elaborating the brief to help the reconstruction succeed
destroys the thing being demonstrated.

## 5. What a three-ghost paper would claim

If the pre-registered prediction holds:

> A conceptual signature of 24 lexical tokens, isolated by filtering an
> organisation's shared vocabulary against 5,188 third-party class names and
> against clean-room model output, appears at N% across three independently
> reconstructed systems and at 0% in every matched control. The signature was
> frozen and the prediction registered before any of the three was
> reconstructed.

That is a real result. It is also falsifiable in one afternoon by anyone with
the protocol, which is what makes it worth publishing.

If the prediction fails, the paper reports a clean negative: the signature
described one system and did not generalise. That is publishable too, and far
better than never having checked.

## 5b. GSA assessed: the hard case, and why that makes it the valuable one

Measured in the ChatGPT archive before deciding anything.

**GSA is not a thin URE. It is a different kind of subject.**

| | URE | GSA |
|---|---|---|
| Mentions | 3,611 in 24 transcripts | **8,270 in 109 transcripts** |
| Distinct parenthesised expansions | 5, four of them one-off noise | **11, several substantive** |
| Top expansion's share | **74 of 79, 94%** | **17 of 36, 47%** |
| Second reading | none | **"Governed Secure AI Gateway", 11 of 36, 31%** |
| Registry entry | `SYS-URE-001` | **`SYS-GSA-001, canonical_name: Governance State Architecture`** |
| Repository ever existed | **no** | **apparently yes**: `github.com/wking53214/GSA` appears 60 times |
| Surviving descendants | none | GSA-815 (2,069 mentions) and GSA-Master-Kernel, both extant repositories |

**Three things follow.**

**1. The acronym is genuinely ambiguous, and that is the point.** URE's step 4
had no competition to resolve: 94% agreement, and the alternatives were
noise. GSA has two substantive readings that describe *different systems*, an
architecture and a gateway, at 47% and 31%. A reconstruction that resolves by
plurality lands on the right answer by a 16-point margin, which is luck
dressed as method. **This is the first real test of §3 step 4, the step the
paper calls the hinge.**

**2. The correct answer is retrievable, so the test is fair.** The archive
contains a registry entry naming the canonical expansion, the same class of
source that identified URE's designators. A reconstruction that finds the
registry resolves it correctly *and for the right reason*. One that counts
expansions gets there by accident. One that follows the gateway reading
builds the wrong system confidently. **Three distinguishable outcomes, all
informative**, which is what makes this worth doing.

**3. It is not a ghost in URE's sense and the paper must not call it one.**
URE never had a repository. GSA apparently did, and has two living
descendants. It is a deleted ancestor, not a system that never existed. That
is a weaker case for the "never possessed a repository" claim and a stronger
one for a different question: whether a system can be recovered when its
successors survive and may have absorbed or diverged from it.

**Contamination risk here is severe and specific.** `GSA-815` and
`GSA-Master-Kernel` both exist, and GSA-Master-Kernel is *itself an archived
GSA design transcript* whose README already documents the naming
inconsistency. If either is attached to the summoning session the test is
void before it starts. R1 is not a formality for this subject; it is the
whole experiment.

### The prompt

Use the URE shape, unchanged, and **do not warn it**:

> I just created a repo called GSA. GSA is a historical repo that has existed
> in concept. I want you to scour the archives and recreate it at its peak
> capacity. can you do that?

Your instinct that "GSA has been used all over the place" is correct and is
exactly why the prompt must not mention it. Telling the reconstruction the
acronym is ambiguous does its hardest work for it and destroys the only
result worth having. The measurement above is the pre-registration: the
ambiguity is on record, dated, before the attempt.

### Pre-registered outcomes for GSA

| outcome | what it shows |
|---|---|
| Resolves to the registry's canonical name **and reports the competing readings** | The A/U discipline holds under genuine ambiguity. The strongest possible result. |
| Resolves correctly **without noticing the ambiguity** | Right answer, wrong method. Honest limitation: the method got lucky on a 47/31 split. |
| Follows the gateway reading, or blends the two | The failure mode §3 step 4 warns about, documented in the author's own work rather than found by a reviewer. |
| Reports that it cannot resolve GSA and says why | Also a success. Refusing to fabricate is the behaviour the paper claims for the method. |

Record which happened before scoring anything against the signature set.

## 5c. Non-code ghosts: Soong and Submission Protocol

These are the most scientifically valuable candidates and the hardest to
score. Both problems have the same root: the signature was built from class
names, and a protocol has none.

### First, two facts that change the plan

**The March originals are not in the ChatGPT archive.** Measured:

| term | mentions | transcripts | earliest date |
|---|---|---|---|
| Soong | 46 | 2 | **2026-08-22** |
| Submission Protocol | 50 | 6 | **2026-07-14** |

The archive contains 31 transcripts from March 2026, so March is covered and
these are simply not in it. Both terms appear almost entirely in two
retrospective August audits, the denser of which is titled *"Gemini VSA Root
Audit"*. **The originals are almost certainly in `Gemini_History`.** Census
that archive before attempting either; this one does not hold the source.

**What the August audits say about Soong is itself worth reading.** They
describe it as "a casualty of lore bloat", a foundational element lost when
"building for a use-case" became "building for the sake of the architecture
itself". That is a cause-of-death record, retrieved rather than deduced,
exactly the kind of source §4 step 9 used for URE. It also means the audits
are secondary sources *about* a ghost, not the ghost.

### The trap: one of these names is inside the signature

`submission` is one of the 24 signature tokens.

**You cannot score a thing called "Submission Protocol" against a signature
set containing `submission`.** That is the `ClassificationResult` error again,
one order worse: the subject's own name guarantees a hit. Two ways out, pick
before starting:

1. Score it against the signature set **with `submission` removed**, 23
   tokens, and say so.
2. Do not use it as a signature subject at all; use it only as a
   reconstruction case study.

**Soong is clean.** It is a proper noun from television, not a vocabulary
token, and it appears in none of the 24. It is the better subject of the two
by this criterion alone.

### Why a non-code ghost is a *better* test, not a worse one

The red team's surviving objection is that the signature might track the
domain of Python governance code. A protocol from March 2026 attacks that
directly:

- **It is not Python.** If the same vocabulary appears in a prose protocol,
  the signature is conceptual rather than a class-naming habit.
- **March is the earliest material in the archive.** It predates the library
  in its current form, CNS by six months, and every other dated occurrence in
  this paper.
- **Protocols and code are different domains.** A domain effect cannot
  explain a vocabulary that crosses from one to the other.

Against that, one honest risk. Several signature tokens are
protocol-flavoured by nature: `mandate`, `consensus`, `envelope`,
`integrity`, `invariant`, `claimed`, `signer`. A protocol is a natural home
for them, so a clean-room control is not optional here, it is the whole
measurement.

### How to actually do it: reconstruct to a formal encoding

The problem with reconstructing a protocol as prose is that prose cannot be
scored. A 10,000-word document and a 37-class package have no comparable
denominator, and any rate computed across them is meaningless.

**The fix is to require a second artifact alongside the prose.** Ask for the
protocol *and* a machine-checkable encoding of it: the states, roles, message
types, transitions and validation rules, as named entities, with a validator
that runs. Then:

- The prose is the reconstruction, judged as URE's was.
- The **named entities** are the scoreable surface, comparable to class names.
- The validator makes "it works" checkable, preserving the property that made
  URE more than an essay.

**Declare the denominator before you look.** Named entities are states, roles,
message types, transition names and rule identifiers. Not prose nouns. Write
that down first, because deciding afterwards what counts is how a rate gets
fitted.

### The matched control, which here does all the work

The clean-room model must be asked for **the same artifact type**, from a
one-line brief, by someone who has not read the reconstruction:

> Design a protocol by which an autonomous system submits work for approval
> to an authority that may refuse it. Output only the named entities you
> would define: states, roles, message types, transitions, validation rules.
> One per line.

Then compare signature rates over named entities. If the control lands near
zero and the reconstruction does not, the signature crossed from code into
protocol and the domain objection is answered. If both land high, the
protocol-flavoured tokens were domain after all, and that is a real negative
result worth publishing.

### Order of operations

1. **Census `Gemini_History`** for Soong and Submission Protocol. If the
   March originals are not there either, stop; there is no ghost to summon,
   only August audits about one.
2. If found, **summon Soong first.** Its name is not in the signature, so it
   needs no exclusion and no asterisk.
3. Use the URE two-prompt shape, adapted only to say the artifact is a
   protocol rather than a package. Do not describe the protocol.
4. Run the matched entity-name control **before** scoring.
5. Treat Submission Protocol as a reconstruction case only, or score it on
   23 tokens and label it.

## 6. Recommendation

1. **Summon DIT next**, under §4. It is the clean replication: consistent
   expansion, no surviving descendants, genuinely absent. It is what tests
   the signature.
2. **Summon GSA after it**, as the hard case, with the outcomes in §5b
   pre-registered. It tests the method rather than the signature, and it is
   the more interesting of the two for the paper's §3 step 4.
3. **Census `Gemini_History` next**, and specifically for Soong. The ChatGPT
   archive does not hold the March originals for either non-code candidate,
   only August audits referring to them. §5c.
4. **Then Soong**, as the non-code case. It is the strongest available attack
   on the surviving domain objection, because it is not Python and it is
   dated March.
4. **Do not recompute the signature set** until every ghost is in.
5. Two ghosts with matched controls beats one subject with three events. Even
   if DIT is all you get, do it.
