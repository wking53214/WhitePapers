> **CONFIDENTIAL DRAFT.** Not cleared for publication.

# What must change before this leaves the repository

Draft 1 is written at full fidelity because it is private and because a
redacted draft is harder to check. That makes this file load-bearing: the
paper cannot be published as written.

## The binding constraint

`wking53214/CNS` carries a trade-secret notice dated 2026-09-11 forbidding
disclosure of, in its own words, "class shapes, module layout, the evidence
under `docs/`, and this repository's existence as the source of shared
contracts."

Section 6 of the paper does all four. That is not an oversight; §6 is the
paper's contribution and it cannot be made without them. So this is a
decision, not a redaction exercise: **either the notice is narrowed, or §6 is
rewritten to a weaker form.** There is no version of the paper that keeps §6
intact and honours the notice as written.

## Option A, recommended: narrow the notice, publish §6 abstracted

Keep the schema's *method* and *results*, remove the identifying detail. The
method is the contribution; the class names are illustration.

| in draft 1 | in a published version |
|---|---|
| `GovernanceDecision`, `RecoveryAction`, `Observation`, `AdaptiveThresholdController`, `ClassificationResult` | "five recurring class names", with members described by role, not quoted |
| `OperationalRegime` and its four member lists | "a regime enumeration", with the shared first state named and the rest characterised |
| Repository names: OBSERVE, fortress-kernel, observe-perceive, GSA-815, innovation_os, GSA-Master-Kernel | Domain descriptions only: "a vehicle safety module", "a clinical governance system", "an actuator containment pack" |
| `URE.OperationalRegime`, `URE.SystemResilienceConfig`, `URE.ClassificationResult` | "the three names the archive preserved as the system's namespace" |
| The 56-token vocabulary | The count and the derivation rules; the four tokens the subject carries can stay, since they are ordinary English |
| `cns`, `ure_engine`, module layout | Omit, or describe shape counts only |

**What survives intact and is the paper's real value:** the nine-step method,
the five substrate preconditions, the A/U discipline, the verification
argument in §6.1 to §6.3, every number in §6.4 (21.6%, the interval, zero
copies, 25.4% and 2.8%), the §7.1 finding about tests versus execution, and
all of §8 and §9.

The abstracted version is weaker rhetorically and identical evidentially. A
reader cannot check the class names either way without access to private
repositories.

## Option B: publish the reconstruction paper only, hold §6 back

Sections 1 through 5, 7 and 8 stand alone as the conversational-archaeology
case study, which is roughly `RECONSTRUCTION.md` §9's original skeleton. It
is publishable with light redaction and it is a decent paper.

It is also the paper anyone could write about any successful AI-assisted
rebuild, because without §6 it has no answer to "how do you know it isn't
fabricated." Recommend against unless the notice cannot be narrowed.

## Independent of the choice

**1. The `ghost_tools` precedent.** That repository is public and already
names CNS, the `--kernel ../cns` convention, "38 repositories", and nine
private repository names. No class shapes leak. If those disclosures are
acceptable, the notice is already being read more narrowly than it is
written, and Option A is a formalisation rather than a concession. This
should be settled before publication either way, because a trade secret needs
consistent handling to stay one.

**2. Re-verify the author-reported figures.** `FIGURES.md` lists six that
were not independently re-measured. The 78-expansion count matters most; §6's
whole argument rests on the acronym having been resolved rather than guessed.

**3. Re-run the copy count against the full library.** Draft 1's zero is
against ten of thirty repositories. If it rises above zero, §6.5 must be
restated.

**4. Decide the §8.8 framing.** The instrument and the subject share an
author. That is what makes the test possible and also bounds what it shows.
The paper currently states the limitation and asks how hard to press it.

**5. Anonymisation is probably not worth attempting.** The library is one
person's, the archive is one person's, and the finding is explicitly about
one author's conceptual schema. A stripped version invites the reader to ask
whose repositories these are, and the answer is guessable from the subject
matter. Publish attributed or not at all.

## Checklist before any external copy exists

- [ ] Notice narrowed, or §6 abstracted per Option A
- [ ] Repository names replaced with domain descriptions throughout
- [ ] Class names and member lists abstracted
- [ ] Author-reported figures re-verified, or relabelled as author-reported in the published text too
- [ ] Copy count re-run against the full library
- [ ] `ghost_tools` disclosure reconciled with whatever the notice ends up saying
- [ ] A second reader has checked that no figure in the paper lacks a command in `FIGURES.md`
