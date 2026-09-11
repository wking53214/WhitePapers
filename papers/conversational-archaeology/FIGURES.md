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

## Figures that are author-reported and should be re-verified (A)

These come from `RECONSTRUCTION.md` §2 and were not re-measured. Each is
checkable against the archives, and should be before publication.

- 2 prompts; corpus of 242 MB, 1,768 files, 863 transcripts
- 24 transcripts containing the subject, 2,644 raw occurrences
- 78 acronym expansions
- 297 lines of historical code recovered verbatim
- 4 primary sources identified
- 3 defects carried forward from the archive, 4 introduced and caught

The 78-expansion figure is the one that most deserves independent
confirmation, because §6 leans on it: it is the evidence that the acronym was
resolved rather than guessed, and it is the single point where a wrong answer
would have produced a confident and entirely incorrect system.
