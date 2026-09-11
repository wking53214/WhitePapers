"""Score a flat list of class names against the library and the vocabulary.

Used for the clean-room control in §6.4, where there is no repository to
scan, only names. Shares its vocabulary loading and tokenizer with
score_reconstruction.py so the two cannot diverge.

    python score_names.py names.txt /path/to/library /path/to/CNS
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from score_reconstruction import classes_in, load_vocabulary, wilson, words  # noqa: E402


def main(namefile, library, cns):
    sys.path.insert(0, str(pathlib.Path(cns) / "docs" / "evidence"))
    from cns_map import fields_and_methods, skipped, strip_docs

    vocab = load_vocabulary(cns)
    names = [l.strip() for l in pathlib.Path(namefile).read_text().splitlines() if l.strip()]

    lib = set()
    for repo in sorted(p for p in pathlib.Path(library).iterdir() if p.is_dir()):
        if repo.name in {"cns", "CNS"}:
            continue
        lib |= {n for n, _, _, _, _ in classes_in(repo, skipped, strip_docs, fields_and_methods)}

    collide = [n for n in names if n in lib]
    carry = [n for n in names if words(n) & vocab]
    lo, hi = wilson(len(collide), len(names))

    print(f"{namefile}: {len(names)} names, library name set {len(lib)}")
    print(f"  collisions:  {len(collide)} = {100*len(collide)/len(names):.1f}%  "
          f"[{100*lo:.1f}, {100*hi:.1f}]  {collide}")
    print(f"  vocabulary:  {len(carry)} = {100*len(carry)/len(names):.1f}%")
    print(f"     via: {sorted({w for n in names for w in (words(n) & vocab)})}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
