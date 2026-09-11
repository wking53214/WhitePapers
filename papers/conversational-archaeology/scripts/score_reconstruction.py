"""Score a reconstructed repository against the library's published schema.

This produces every new figure in §6 of PAPER.md. It is the paper's claim to
being checkable rather than asserted.

It deliberately imports the schema package's own helpers (`skipped`,
`strip_docs`, `fields_and_methods`) instead of reimplementing them, so the
method is the published method and cannot quietly diverge from it. The
tokenizer is copied verbatim from `schema_test.py` and is the one line that
must be kept in step; it is asserted against a known case at startup.

    python score_reconstruction.py /path/to/URE /path/to/library /path/to/CNS

The vocabulary is not re-derived. It is lifted from the published
`RESULTS.md`, because a vocabulary re-derived at scoring time could be
influenced by the repository being scored, which would destroy the test.
"""
import ast
import hashlib
import pathlib
import re
import sys
from collections import Counter

# Published pooled figures, from CNS/docs/evidence/RESULTS.md, no-engine stage.
HELD_OUT = (147, 579)     # classes carrying a token, classes scored
CONTROL = (123, 4379)


def words(name):
    """Verbatim from schema_test.py. Keep in step with it."""
    return {w.lower() for w in re.findall(r"[A-Z][a-z]+|[A-Z]+(?![a-z])|[a-z]+", name)
            if len(w) > 2}


assert words("GovernanceDecision") == {"governance", "decision"}, "tokenizer drifted"
assert words("BISGEstimator") == {"bisg", "estimator"}, "tokenizer drifted"


def wilson(k, n, z=1.96):
    p, d = k / n, 1 + z * z / n
    centre = p + z * z / (2 * n)
    margin = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5)
    return (centre - margin) / d, (centre + margin) / d


def load_vocabulary(cns):
    """The 56-token no-engine vocabulary, as published."""
    results = pathlib.Path(cns) / "docs" / "evidence" / "RESULTS.md"
    for line in results.read_text().splitlines():
        if line.startswith("Final vocabulary by spine frequency"):
            vocab = set(re.findall(r"`([a-z]+)`\(\d+\)", line))
            if not vocab:
                sys.exit("found the vocabulary line but parsed no tokens")
            return vocab
    sys.exit(f"no vocabulary line in {results}")


def classes_in(root, skipped, strip_docs, fields_and_methods):
    """Top-level classes, with the structural hash and member names. Applies
    the schema package's own exclusions, so tests/ and vendored trees are
    dropped here exactly as they were for the held-out repositories."""
    out = []
    root = pathlib.Path(root)
    for path in sorted(root.rglob("*.py")):
        rel = path.relative_to(root)
        if ".git" in rel.parts or skipped(rel):
            continue
        try:
            tree = ast.parse(path.read_bytes())
        except Exception:
            continue
        for node in tree.body:
            if not isinstance(node, ast.ClassDef):
                continue
            digest = hashlib.sha1(
                ast.dump(strip_docs(node), include_attributes=False).encode()
            ).hexdigest()[:8]
            fields, methods = fields_and_methods(node)
            out.append((node.name, digest, fields | methods, str(rel), node.lineno))
    return out


def jaccard(a, b):
    return 1.0 if not a and not b else len(a & b) / len(a | b)


def main(subject, library, cns):
    sys.path.insert(0, str(pathlib.Path(cns) / "docs" / "evidence"))
    from cns_map import fields_and_methods, skipped, strip_docs

    vocab = load_vocabulary(cns)
    print(f"vocabulary: {len(vocab)} tokens, from the published RESULTS.md")

    subj = classes_in(subject, skipped, strip_docs, fields_and_methods)
    carrying = [n for n, _, _, _, _ in subj if words(n) & vocab]
    k, n = len(carrying), len(subj)
    lo, hi = wilson(k, n)
    ctrl = CONTROL[0] / CONTROL[1]
    _, ctrl_hi = wilson(*CONTROL)

    print(f"\n=== §6.4 vocabulary score ===")
    print(f"  subject classes scored (tests excluded): {n}")
    print(f"  carrying a vocabulary token:             {k}  = {100*k/n:.1f}%")
    print(f"  Wilson 95% CI:                           {100*lo:.1f}% to {100*hi:.1f}%")
    print(f"  held-out pooled (published):             {100*HELD_OUT[0]/HELD_OUT[1]:.1f}%")
    print(f"  third-party control (published):         {100*ctrl:.1f}%")
    print(f"  separation, point estimate:              {(k/n)/ctrl:.1f}x")
    print(f"  separation, worst case:                  {lo/ctrl_hi:.1f}x")

    tokens = Counter(w for nm, _, _, _, _ in subj for w in (words(nm) & vocab))
    print("  tokens carried: " + ", ".join(f"{w}({c})" for w, c in tokens.most_common()))
    print("  classes carrying them: " + ", ".join(sorted(set(carrying))))

    # the library, one directory per repository
    lib = {}
    libdir = pathlib.Path(library)
    for repo in sorted(p for p in libdir.iterdir() if p.is_dir()):
        if repo.name in {"cns", "CNS", subject.rstrip("/").split("/")[-1]}:
            continue
        for nm, digest, sig, _, _ in classes_in(repo, skipped, strip_docs, fields_and_methods):
            lib.setdefault(nm, []).append((repo.name, digest, sig))
    print(f"\n  library scanned: {len(list(p for p in libdir.iterdir() if p.is_dir()))} "
          f"directories, {len(lib)} distinct class names")

    print(f"\n=== §6.4 structural copies ===")
    copies = [(nm, r) for nm, d, _, _, _ in subj
              for r, ld, _ in lib.get(nm, []) if d == ld]
    print(f"  copies of a library class (identical docstring-stripped AST): {len(copies)}")
    for nm, r in copies:
        print(f"    {nm} <- {r}")
    if copies:
        print("  NOTE: non-zero. The §6.5 convergence argument must be restated.")

    print(f"\n=== §6.5 shared names, and whether the shape is shared ===")
    shared = [(nm, sig, where) for nm, _, sig, where, _ in subj if nm in lib]
    if not shared:
        print("  none")
    for nm, sig, where in sorted(shared):
        repos = lib[nm]
        best = max(jaccard(sig, ls) for _, _, ls in repos)
        print(f"  {nm:30} in {len(repos)} library repo(s), max overlap {best:.2f}")
        print(f"{'':4}subject: {where}, members: {', '.join(sorted(sig)) or '-'}")
        for r, _, ls in repos:
            print(f"{'':4}  {r:20} overlap {jaccard(sig, ls):.2f}  members: {', '.join(sorted(ls)) or '-'}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
