> **CONFIDENTIAL DRAFT.** Not cleared for publication. See `REDACTION.md`.

# Figures, and how to reproduce each one

House rule 1: every figure traces to something runnable. **(V)** means
re-measured for this paper. **(A)** means author-reported from the
reconstruction session and not re-verified here.

Paths assume the library checked out one directory per repository, the
reconstruction at `URE/`, and the schema package at `CNS/`.

---

## The reconstruction's own figures (V)

```
cd URE
pip install -e ".[dev]"
python -m pytest -q                      # 278 passed
python -m mypy                           # clean (uses [tool.mypy], not --strict)
python -m ruff check ure_engine tests examples   # clean
git ls-files 'ure_engine/*.py' | xargs wc -l | tail -1   # 4414
git ls-files 'ure_engine/*.py' | wc -l                    # 15 modules
grep -A1 '^dependencies' pyproject.toml                   # dependencies = []
python examples/incident_walkthrough.py                   # runs, ends in QUARANTINE
```

**Caveat on the static-analysis figure.** `RECONSTRUCTION.md` §2 says "mypy
strict clean." The repository configures a strict-ish `[tool.mypy]` section
and CI runs bare `mypy`, which is clean. Under actual `mypy --strict` there
is one finding, a `# type: ignore[call-overload]` at
`ure_engine/attack_memory.py:68` that a current mypy says should also cover
`no-any-return`. The paper therefore says "as the repository's CI invokes
them" rather than "strict." Fix the ignore comment and the stronger wording
becomes available.

**Note on line counts.** `RECONSTRUCTION.md` §2 reports 8,682 lines committed,
2,649 test lines and 1,103 documentation lines. Measured later the repository
shows 9,447 total, 2,679 test and 1,641 documentation lines. The package
figure is unchanged at 4,414 and the module count at 15. The difference is
growth after that snapshot, including `RECONSTRUCTION.md` itself at 378
lines. §10 of that document scopes its figures to commit time, so this is
consistent, not a discrepancy. The paper cites the package and test figures,
which are stable, and attributes the corpus figures to the author.

## The schema instrument (published, not re-derived)

From the schema package's own evidence directory:

```
cd CNS/docs/evidence
pip install wordfreq
python schema_test.py /path/to/library > RESULTS.md
python cns_map.py CNS_MAP.md
```

Published figures used by the paper, all from `RESULTS.md`:

| figure | value |
|---|---|
| Spine, class names in 3+ of 18 training repositories | 189 (63 after the training-set restriction the test uses) |
| Final vocabulary, after all four mechanical reductions | 56 tokens |
| Held-out pooled, 7 repositories, 579 classes | 25.4% |
| Third-party control pooled, 12 packages, 4,379 classes | 2.8% |
| Separation | 9.0x |

**Reproducibility caveats inherited from that package.** Its `ROOT` is
hard-coded; the scanned repositories' commit SHAs are not recorded, so no run
is exactly reproducible; and one repository's vendored tree is a git submodule
whose absence silently changes the result. Its own README documents all three.

## The new measurements in §6 (V)

The URE score, the copy count and the overlaps were computed with the schema
package's own helpers so the method matches rather than approximates it. The
script is `scripts/score_reconstruction.py` in this directory.

```
python scripts/score_reconstruction.py /path/to/URE /path/to/library /path/to/CNS
```

It reports, and produced for draft 1:

| figure | value |
|---|---|
| URE classes scored, tests excluded | 37 |
| Carrying a vocabulary token | 8, so 21.6% |
| Wilson 95% CI | 11.4% to 37.2% |
| Separation from the control point estimate | 7.7x |
| Worst case, URE lower bound over control upper bound | 3.4x |
| Structural copies from the library | 0 |
| Tokens carried | `regime` 3, `decision` 2, `health` 2, `outcome` 1 |

**Scope limit on the copy count.** Ten of the library's repositories were
available when this was run, not all thirty. Zero copies against those ten is
what is claimed. Re-run against the full library before publication; the
number can only rise, and if it rises above zero the §6.5 argument weakens
and must be restated.

The four-domain regime table in §6.6 comes from reading the four definitions
directly. Three are in the library; the fourth is quoted from the
reconstruction's `docs/PROVENANCE.md` §8, which records the predecessor's
vocabulary rather than shipping it, since the reconstruction deliberately
adopted the v2 names instead.

## Author-reported figures, now independently verified (A -> V)

The archive was cloned and these were re-measured rather than trusted.

```
git clone --depth 1 https://github.com/wking53214/chatgpt_history
cd chatgpt_history/transcripts
grep -roh "URE ([A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]*)" --include=*.md . | sort | uniq -c
```

| figure | claimed | measured | status |
|---|---|---|---|
| Acronym expansions | 78 | **78** | **exact** |
| Competing expansions of URE | none stated | **none exist** | stronger than claimed |
| Archive file count | 1,768 | **1,768** | exact |
| S1 transcript at the cited path | yes | **present** | confirmed |
| S4 transcript at the cited path | yes | **present** | confirmed |
| S1 date | 2026-06-19 | **2026-06-19** | exact |
| S4 date | 2026-07-29 | created 2026-07-27, **updated 2026-07-29** | the cited date is `update_time` |
| S4 title | "Sentinel OS for Drones" | **exact match** | confirmed |

**The 78 figure is the one §6 leans on and it is now the strongest number in
the paper.** The regex returns 78 occurrences of `URE (Universal Resilience
Engine)` and **zero** occurrences of any other three-word expansion. The
acronym was not resolved against a plurality; there was no competition.

### The contamination question on `regime`, closed

`BLUE_TEAM.md` §B2 flagged that `RegimeEngine` exists in `sentinel_os`, which
was attached to the reconstruction session, giving the `regime` token a
contamination path. That path is now ruled out at the source:

| check | result |
|---|---|
| `SystemRegime` in S1 (2026-06-19) | **4 occurrences** |
| Its members in S1 | NOMINAL 3, STRESSED 3, ATTACKED 2, CASCADING 3, RECOVERING 4, ADAPTING 2 |
| `OperationalRegime` in S4 | **155 occurrences**, with all six v1 members |

URE's regime vocabulary is verbatim from a transcript dated **2026-06-19**,
three months before CNS existed and independent of `sentinel_os`. The
reconstruction did not need the attached repository and demonstrably did not
use it for this.

### Cross-domain spread of `regime` in the archive alone

Twenty-one transcripts contain it, spanning 2026-06-19 to 2026-08-25, under
titles including a drone operating system, an executive technical assessment,
code-fingerprint extraction, a root audit, a fortress code comparison and an
unrelated project. The cross-domain claim in §B2 therefore holds from the
archive on its own, without reference to the library.

### Still author-reported (A)

- 2 prompts; corpus of 242 MB, 863 transcripts
- 24 transcripts containing the subject, 2,644 raw occurrences
- 297 lines of historical code recovered verbatim
- 3 defects carried forward from the archive, 4 introduced and caught

### Still open, and it cannot be closed from here

`RECONSTRUCTION.md` §2 says four repositories were attached to the
reconstruction session and §3 names only two, `sentinel_os` and
`innovation_os`. **The other two are unidentified.** The contamination
analysis in §6.5 is therefore complete with respect to the two named
repositories and incomplete with respect to the session as a whole. If either
unnamed repository was a library repository, more of the shared names may
need discarding. Recover that list from the session record before
publication.

---

## The clean-room control (draft 2, the finding that changed the paper)

Two fresh model sessions, no tools, no filesystem, no archive, no library.
Prompts verbatim and outputs in `data/`. To re-score:

```
python scripts/score_names.py data/cleanroom_trial1_names.txt /path/to/library /path/to/CNS
python scripts/score_names.py data/cleanroom_trial2_names.txt /path/to/library /path/to/CNS
```

| | names | collisions | vocabulary |
|---|---|---|---|
| Trial 1 | 45 | 2 = 4.4% | 20.0% |
| Trial 2 | 43 | 1 = 2.3% | 9.3% |
| Pooled | 88 | 3 = 3.4% | 14.8% |

**Replication of the schema study's control, incidentally.** Re-deriving the
third-party control on a twelve-package set gave 2.9% on the vocabulary
against the published 2.8%. Different package set, same answer. The study's
control figure replicates; it is the *interpretation* of the gap that the
clean-room control overturns.

**The null corpus.** 4,985 distinct class names across pydantic, redis,
fastapi, starlette, httpx, numpy, setuptools, anthropic, uvicorn, psycopg2,
cryptography and mypy. Pooled collision rate with the library 0.5%, worst
single package 2.4% (redis). None of the paper's five shared names, and none
of the archive's three namespace names, appears anywhere in it.

**Contamination control.** `RECONSTRUCTION.md` §3 step 2 names `sentinel_os`
and `innovation_os` as attached to the reconstruction session. Presence of
each shared name in those two was checked directly; `Observation` and
`ClassificationResult` are present and are therefore discarded from the
paper's evidence. This check should be repeated if the full list of four
attached repositories is recovered, since two are unidentified in that
document and could widen the discard set.

**Outstanding, and the paper says so:** a domain-matched human baseline. No
figure in this paper separates "the author's schema" from "governance
software in 2026" from "this model family's naming habits". The clean-room
control rules the first explanation out as *sufficient*; it does not rank the
other two.

---

## §0, the origin constraint (V)

Every figure in §0 comes from the two conversational archives and was
measured, not recalled. The Gemini archive is Google Takeout format; the
activity file is `Takeout/My Activity/Gemini Apps/myactivity.json`, 4,911
records spanning 2025-11-02 to 2026-07-09.

```
# the derivation session, and the timestamps in the 0.1 table
python3 - <<'PY'
import json, re
recs = json.load(open("Takeout/My Activity/Gemini Apps/myactivity.json"))
h = [r for r in recs if re.search(r"mark\s*12|john\s*13|greatest\s+commandment",
                                  json.dumps(r), re.I)]
h.sort(key=lambda r: r["time"])
for r in h[:8]:
    print(r["time"], "|", r["title"][:160])
PY

# first and last occurrence of each term
#   mark 12              82 records  2026-03-25 -> 2026-07-06
#   john 13              43 records  2026-03-25 -> 2026-07-06
#   greatest commandment 22 records  2026-03-25 -> 2026-06-04
#   new commandment       5 records  2026-03-25 -> 2026-06-04

# cross-vendor persistence, second archive
cd ../chatgpt_history/transcripts
grep -rlio "greatest commandment\|mark 12:30\|john 13:34\|light.first" . 
# 5 transcripts, create_time 2026-07-12 .. 2026-08-11

# absence from the artifacts: run across every repository
grep -rin "light.first\|greatest commandment\|mark 12\|john 13\|covenant" \
     <all repos> --include=*.py --include=*.md
# only hits are boilerplate Contributor Covenant CODE_OF_CONDUCT.md in one
# repository and its vendored copy. Zero in any source file.
```

**Key figures:**

| figure | value |
|---|---|
| Derivation session date | 2026-03-25, 17:56:49 to 18:41:22 UTC |
| Records mentioning Mark 12 | 82, first 2026-03-25 |
| Records mentioning John 13 | 43, first 2026-03-25 |
| Earliest occurrence anywhere in a 4,911-record archive beginning 2025-11-02 | **2026-03-25**, none earlier |
| Cross-vendor recurrence | 5 transcripts, 2026-07-12 to 2026-08-11 |
| Occurrences in source code, all repositories | **0** |
| Clean-room trials producing any theological constraint | **0 of 3** |

**Caveat on "from the first day."** The constraint is the first day of the
*governance stack*, not of the archive. The archive begins 2025-11-02 and the
question does not appear until 2026-03-25. §0 states it the narrower way for
this reason.

**Caveat on the §0.3 code mapping.** The ordered two-predicate structure was
found in one implementation and its two vendored copies. A scan of the five
repositories carrying approval-escalation vocabulary found three matching
decision functions, all descended from the same source file. This is one
instance, not independent recurrence, which is why §0.3 labels it
interpretation.

## The four additional reconstructions (V), and why three of them cannot testify

Four further reconstructions were produced on 2026-09-11 and scored with the
same script, unchanged:

```
python scripts/score_reconstruction.py /path/to/<subject> /path/to/library /path/to/CNS
```

| subject | classes | 56-token vocabulary | **structural copies of a library class** |
|---|---|---|---|
| URE, the original subject | 37 | 21.6% | **0** |
| ICEBURG | 15 | 20.0% | **0** |
| SAGE-K | 42 | 38.1% | **128** |
| DIT | 31 | 48.4% | **3** |
| GSA | 48 | 29.2% | **0** |

**The copy counts are the finding, not the scores.** URE's zero copies is what
established it had not been assembled from the library. SAGE-K's **128** says
the opposite: many classes have member overlap 1.00 against `gsa-815` and
`sentinel_os`, which is identical field and method name sets. It shares code
with the library rather than independently reproducing its shapes. DIT's 3 sit
in `legacy/gsa_v13_citadel_processor.py`, the recovered legacy engine, and its
own `src/dit/` rewrite of the same components scores 0.17 and 0.25 overlap
instead, which is the pattern a genuine rewrite produces.

**Independence, assessed per subject before any score is quoted:**

| subject | independent of the instrument? | why |
|---|---|---|
| ICEBURG | **no, circular on vocabulary** | its own renamed descendant *is* `sentinel_os`, one of the 18 training repositories the vocabulary was derived from |
| SAGE-K | **no** | 128 structural copies; provenance ties it to the GSA wrapper and the Sentinel resolver seam |
| DIT | **partly** | a layer of the same Sentinel kernel; cites `sentinel_os` paths in docstrings, imports nothing from it |
| GSA | **no, fully circular** | carries `archive/GSA_Governance_Operating_Core_Enterprise.py`, the exact file `cns.governance` was extracted from, now importing `from cns.governance` |

GSA's zero copies is an artifact of that extraction rather than evidence: the
class definitions were removed from its copy and replaced by imports, so there
is nothing left to match.

**None of these four is a clean replication of the URE result, and their
scores must not be pooled with it.** What they support is a leave-one-out
design: rebuild the survivor set from the library with the subject's own
ancestors and descendants excluded from the training set, then score. That is
standard cross-validation, it is what a reviewer will ask for, and it is the
only way these four become evidence rather than circularity.

### The origin constraint in all four (V)

```
grep -rioE "mark 12|john 13|greatest commandment|light.first" <each subject>
# ICEBURG 0, SAGE-K 0, DIT 0, GSA 0
```

**Zero in all four.** Four independent reconstruction sessions mined the same
archives in which the constraint appears 82 and 43 times respectively, and
none of them surfaced it into code. That is an independent replication of §0's
zero-in-source finding on four fresh subjects, and it is the strongest
available evidence that the constraint genuinely does not travel into
artifacts.

### `apply_liturgical_pause` (V)

```
grep -rn "liturg" --include=*.py .
# gsa-master-kernel/artifact_12.py:313, artifact_11.py:296
# gsa/archive/gsa_kernel_v3_initial.py:258
# dit/legacy/gsa_v13_citadel_processor.py:102
# plus a loose module inside the Gemini archive
grep -rl "liturg" <installed third-party site-packages> --include=*.py
# zero
```

A broader sweep of eighteen repositories for religious vocabulary
(liturgical, covenant, sanctification, scripture, gospel, commandment,
providence and twenty more) returns this term and nothing else. `genesis`
also appears, 139 times, but every occurrence is the blockchain sense, a
ledger's genesis anchor, and none is religious usage.
