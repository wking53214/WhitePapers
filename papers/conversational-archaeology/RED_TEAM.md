> **CONFIDENTIAL.** Not cleared for publication. See `REDACTION.md`.

# Red team / blue team: Conversational Archaeology

Adversarial review of draft 1, performed 2026-09-11 before any external
copy existed. Each attack is stated at full strength, then answered with a
measurement or conceded.

**Headline: draft 1 overstated its central result and one of its five
supporting cases has to be discarded entirely. What survives is stronger
than what was claimed, because it is now attack-tested.**

Severity: **CRITICAL** kills the paper. **HIGH** forces a restatement.
**MEDIUM** needs a caveat. **LOW** is a nitpick.

---

## Summary of verdicts

| # | attack | severity | verdict |
|---|---|---|---|
| A1 | The convergence is the language model's naming habits, not the author's schema | **CRITICAL** | **TESTED, AND IT LARGELY LANDS.** A clean-room model scores 14.8% on the vocabulary against URE's 21.6%. The vocabulary measure is dead; name collision survives only as an unseparable trend. |
| A2 | The reconstruction session could read two library repositories | **CRITICAL** | **PARTLY LANDS.** Two of five cases discarded. Three survive clean. |
| A3 | The null model is not domain-matched | **HIGH** | **LANDS.** Restated; the honest null is narrower than draft 1 implied. |
| A4 | The vocabulary score rides on non-distinctive tokens | **HIGH** | **LANDS.** 3 of 8 hits are on control-carried tokens. Measure demoted. |
| A5 | n=37 is too small for the headline figure | **MEDIUM** | Survives with intervals quoted. |
| A6 | "These are just common class names" | **MEDIUM** | **DEFEATED** by measurement. |
| A7 | §6.7's archive argument escapes circularity | **HIGH** | **DRAFT 1 WAS WRONG.** It escapes A2, not A1. Corrected. |
| A8 | Single author, single subject | **MEDIUM** | Conceded, inherited from the schema study. |
| A9 | The reconstruction's own numbers are self-reported | **LOW** | Marked A/V throughout. |
| A10 | Publishing the evidence discloses the trade secret | **CRITICAL (commercial)** | Architecture redesigned; see `REDACTION.md`. |

---

## A1. The model-prior objection

**CRITICAL. This is the attack that matters, and testing it changed the paper.**

**Attack.** Both corpora are substantially AI-written. The library is the
work of a founder using AI assistants heavily, to the point that one of his
own repositories exists to audit AI-written code. URE was reconstructed by
Claude Code. The archive is *literally* a collection of AI conversation
transcripts.

So when a reconstruction produces `GovernanceDecision` and the library also
contains `GovernanceDecision`, the parsimonious explanation is not that both
express one author's conceptual schema. It is that **large language models
asked to write governance software converge on the same names.** The finding
would then be about the tool, and would reproduce for any user, making the
paper's central claim about organizational memory false.

### A1 was tested. It largely lands.

Two fresh model sessions were given a prose description of URE's *function*
with no names, no archive access, no library access and no tools, and asked
only for the class names they would define. 88 names across two trials.

| | name collision with the library | vocabulary score |
|---|---|---|
| URE, contamination-free | 8.1% [2.8, 21.3] | 21.6% |
| **Clean-room model, same domain, pooled** | **3.4% [1.2, 9.5]** | **14.8%** |
| Third-party null, 12 packages | 0.5% [0.3, 0.7] | 2.9% |

**The vocabulary measure does not survive.** A model with no access to any of
the author's material scores 14.8% on the published vocabulary, against
URE's 21.6% and the library's held-out 25.4%. The third-party null is 2.9%.
So most of the 9.0x separation the schema study reports is explained by
**domain**, not by authorship: governance and resilience code contains
governance and resilience words, and HTTP clients and numerical libraries do
not. The original study's controls were all off-domain, so it could not see
this.

**The name-collision measure survives only as a trend.** URE's 8.1% is about
2.4x the clean-room's 3.4%, but with 3 of 37 against 3 of 88 the intervals
overlap heavily and the difference is not separable at this n. It cannot
carry a claim.

**What did survive, and it is the interesting part.** The clean-room model
reached none of URE's three contamination-free names. It produced
`OperatingMode` where the author's material has `OperationalRegime`,
`RemediationAction` for `RecoveryAction`, `ThresholdAdapter` for
`AdaptiveThresholdController`, and `DecisionRecord` for
`GovernanceDecision`. Same concepts every time, different words every time.

That suggests a real two-layer structure: **the concepts a resilience system
needs are determined by the domain, and are reachable by anyone. The
particular words are the author's.** The vocabulary measure captures the
first layer, which is why it fails. Exact-name collision probes the second,
which is why it trends in the right direction. Neither measure isolates the
second layer cleanly, and building one that does is the open methodological
problem.

**Verdict on the thesis.** The evidence as it stands does not distinguish
"this author has a distinctive conceptual schema" from "governance software
written in 2026 looks like this." The paper must not claim the former.

**Remaining experiment worth running.** A domain-matched *human* baseline: an
open-source policy engine, SRE toolkit or incident-management library by
another author, scored the same way. That separates domain from era and from
model. Until it exists, A3 and A1 are entangled.

---

## A2. Contamination through the attached repositories

**CRITICAL, and it partly lands.**

**Attack.** `RECONSTRUCTION.md` §2 records four repositories attached to the
reconstruction session, and §3 step 2 names two of them: `sentinel_os` and
`innovation_os`. Both are library repositories. The session searched them.
Anything it saw there it could have echoed. Every claim of independent
convergence on a name present in those two repositories is void.

**Blue team response: measured, and two of five cases must be discarded.**

| shared name | in an attached repo | verdict |
|---|---|---|
| `GovernanceDecision` | no | **clean** |
| `RecoveryAction` | no | **clean** |
| `AdaptiveThresholdController` | no | **clean** |
| `Observation` | **yes, innovation_os** | discard |
| `ClassificationResult` | **yes, innovation_os, and nowhere else** | discard |

`ClassificationResult` is the worse of the two: its only library appearance
is in an attached repository, so it is not evidence of anything and draft 1
should not have cited it. `Observation` appears in two unattached
repositories as well, so it is merely ambiguous, but it is discarded on the
same principle.

**Restated result.** Three of URE's 37 scored classes carry names that recur
in the library with no contamination path:

| | rate | vs pooled null |
|---|---|---|
| Draft 1 claim, five names | 13.5% | 30x |
| **Contamination-free, three names** | **8.1%** | **18x** |

Against the third-party pooled null of 0.5% that is eighteen times the rate.
But A1's experiment supplies the comparator that actually matters: a
clean-room model in the same domain reaches 3.4%, and against *that* baseline
8.1% is a factor of 2.4 on 3 events versus 3, which is not separable.

**So A2 costs the paper its headline number, and A1 costs it the
interpretation.** The 18x figure is real but answers the wrong question: it
compares governance software to HTTP clients.

**Required action.** The paper must lead with 8.1% and three names, state the
contamination analysis, and name the two discarded cases. Concealing them
would be the worse error by far: a reviewer with repository access finds
them in an afternoon.

---

## A3. The null model is not domain-matched

**HIGH, and it lands.**

**Attack.** The twelve null packages are an HTTP client, a database driver, a
numerical library, a web framework, a type checker, a build tool, a crypto
library and an API SDK. None is a governance, resilience, or safety system.
Of course they do not contain `GovernanceDecision`. A domain-matched null,
say three open-source policy engines or SRE tools, might collide at a far
higher rate, and the 18x would shrink or vanish.

**Blue team response. Conceded.** The null establishes that the collision
rate is not a generic property of Python packages. It does **not** establish
that it is not a generic property of governance software. Those are different
claims and draft 1 conflated them.

**Required action.** Either build a domain-matched null (OPA's Python
bindings, an SRE or incident-management library, a policy or rules engine) or
narrow the claim to exactly what the current null supports: *the recurrence
is not explained by general Python naming convention.* The narrower claim is
still worth publishing and is defensible today. The broader one is not.

---

## A4. The vocabulary score rides on non-distinctive tokens

**HIGH, and it lands.**

**Attack.** The vocabulary measure gives URE 21.6%. Decompose it: `regime`
3 classes, `decision` 2, `health` 2, `outcome` 1. The published control
carries `health` and `outcome` in its own top-ten token list. So three of
eight hits come from tokens the study itself shows are not distinctive.

**Blue team response. Conceded, with a warning about the obvious fix.**
Removing every control-carried token drops URE to 13.5% (5 of 37). But that
operation is illegitimate as evidence: pruning the vocabulary by what the
control carries guarantees the control scores near zero, which is selection
on the outcome. A reviewer would catch it at once.

The right response is not to harden the vocabulary. It is to **demote the
measure.** The name-collision measure (A2) requires no vocabulary, no
reduction rules and no judgment: it asks only whether the same class names
appear. It is the stronger instrument and should carry the argument, with the
vocabulary score reported as corroboration and its composition disclosed.

**Incidental strengthening.** Re-deriving the control independently gave 2.9%
against the published 2.8%, on a different package set. That is a genuine
replication of the schema study's control figure and worth stating.

---

## A5. Sample size

**MEDIUM. Survives.**

37 classes. The headline interval is wide: 8.1% on three names carries a
Wilson 95% interval of roughly 2.8% to 21.5%. Even the lower bound is above
the worst single null package. The point estimate must never appear without
the interval.

---

## A6. "These are just common class names"

**MEDIUM. Defeated by measurement.**

All three surviving names, plus the two discarded ones and all three of the
archive's namespace names, are **absent from a 4,985-name corpus spanning
twelve third-party packages.** None is a common Python class name. This
attack is closed.

---

## A7. Draft 1's §6.7 claimed too much

**HIGH. Draft 1 was wrong and the correction matters.**

Draft 1 wrote: "A reconstruction can be accused of pattern-matching its
author. A transcript written three months earlier cannot."

That is false as written. The mid-2026 transcripts are **AI conversation
transcripts.** They escape A2, because they predate the reconstruction and
cannot have been echoed from an attached repository. They do **not** escape
A1, because a model wrote them too.

The corrected claim: the archive finding removes the contamination objection
and the fitted-vocabulary objection, and leaves the model-prior objection
completely untouched. That is still valuable, because it dates the recurrence
to months before any instrument existed to detect it. It is not the knockdown
draft 1 presented.

**One genuine strengthening the red team found.** `AdaptiveThresholdController`
is named in source S2, a transcript dated 2026-06-19, *and* appears in two
unattached library repositories. So this name's recurrence is datable and
independent of the reconstruction entirely. The reconstruction inherited it
from the archive rather than converging on it, which makes it weaker evidence
about the reconstruction and stronger evidence about the schema. The paper
should say which, per name, rather than pooling them.

---

## A8, A9. Scope and self-reporting

**A8, MEDIUM, conceded.** One author, one library, one reconstruction. The
schema study is explicit that it does not show the schema exists
independently of its author; this paper inherits that exactly and must say so
in the abstract, not only in threats to validity.

**A9, LOW, handled.** Six figures are author-reported and not re-measured.
They are marked, and `FIGURES.md` says which. The 78-expansion count should
be independently confirmed because the acronym-resolution argument rests on
it.

---

## A10. Publishing the evidence would disclose the trade secret

**CRITICAL on the commercial axis.**

Draft 1 quoted class names, member lists, repository names, the module layout
and the token vocabulary. That is the recipe, and the paper does not need it.

**The key realisation: the strongest measure needs no disclosure at all.**
The name-collision result is a rate. Reporting "three of thirty-seven class
names recur in the private library, against 0.5% in a twelve-package null" is
the entire finding. It requires no name, no shape, no repository identity and
no vocabulary. The vocabulary token list, which is the closest thing to the
actual recipe, can be withheld completely while still reporting the score.

`REDACTION.md` carries the tiering. The short version: the paper is
publishable with every number intact and every identifier removed, and the
evidence is not weakened by that, only the rhetoric.

---

## What the paper should claim after this review

Ordered by how hard it is to attack.

1. **A system with no repository was reconstructed from archived design
   discourse.** Unattacked. Directly evidenced.
2. **The reconstruction contains no copied code.** Zero structural matches
   across the available library. Unattacked.
3. **Where names recur, the shapes do not.** Member overlap 0.00 on the
   surviving cases. Unattacked, and the cleanest evidence that whatever is
   shared is conceptual.
4. **The recurrence is not general Python convention.** Three
   contamination-free names at 8.1% versus a 0.5% pooled null, and none of
   the names present in a 4,985-name null corpus. Solid, given A3's narrower
   framing.
5. **The recurrence predates the instrument that detects it.** Datable to
   June and July 2026 transcripts. Solid against A2, silent on A1.
6. **Therefore the library shares a conceptual schema attributable to its
   author.** **NOT ESTABLISHED, and now positively doubted.** A1's
   experiment shows a clean-room model reaching 14.8% on the vocabulary with
   no access to anything of the author's. Do not claim this.

Claim 6 is what would have made the paper exciting, and testing it is what
took it away. That is the correct outcome of a red team: the claim was going
to be falsified by the first reviewer who ran a domain-matched control, and
it is far better that it was falsified here.

**What replaces it is a real contribution, and it is a negative result.** The
schema study's 9.0x separation is substantially a domain effect, invisible to
it because all twelve of its controls were off-domain. A study measuring
whether an organization has a distinctive conceptual vocabulary needs a
domain-matched control, and this is the demonstration of why. Published as
that, the paper is methodologically useful, defensible line by line, and
unembarrassing in two years. Published as claim 6, it is a press release
with a short half-life.

The two-layer observation in A1 is the most promising thread left: concepts
appear to be domain-determined and lexical choices author-determined. That is
a sharper hypothesis than the original, and it suggests the measure that
would actually test it. It is probably the better paper.
