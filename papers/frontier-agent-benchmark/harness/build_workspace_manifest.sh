#!/usr/bin/env bash
#
# Builds a frozen, hashed benchmark workspace from a hand-classified
# manifest of source paths. See ../phase2-workspace-manifest.md.
#
# Usage: build_workspace_manifest.sh <manifest.tsv> <workspace-dir>
#
# <manifest.tsv> lines: path<TAB>class<TAB>justification
#   class must be one of: PRIMARY HISTORICAL DERIVED
#   (CONTAMINATION and EXCLUDED paths are never listed here — they're
#   omitted by construction, not marked and filtered.)
#
# Refuses to run against a manifest containing a fixed-exclusion path
# (see phase2-workspace-manifest.md §3), and refuses to reuse an
# existing workspace directory.

set -euo pipefail

FIXED_EXCLUSIONS=(
  "$HOME/.claude"
  "$HOME/.codex"
  "$HOME/.grok"
)

usage() {
  echo "Usage: $0 <manifest.tsv> <workspace-dir>" >&2
  exit 1
}

[[ $# -eq 2 ]] || usage
manifest="$1"
workspace="$2"

[[ -f "$manifest" ]] || { echo "manifest not found: $manifest" >&2; exit 1; }
[[ -e "$workspace" ]] && { echo "refusing to reuse existing path: $workspace" >&2; exit 1; }

mkdir -p "$workspace"
out_manifest="$workspace/MANIFEST.tsv"
printf 'path\tclass\tjustification\thash\n' > "$out_manifest"

line_no=0
while IFS=$'\t' read -r src_path class justification || [[ -n "$src_path" ]]; do
  line_no=$((line_no + 1))
  [[ -z "$src_path" || "$src_path" == \#* ]] && continue

  case "$class" in
    PRIMARY|HISTORICAL|DERIVED) ;;
    *)
      echo "line $line_no: unrecognized class '$class' for $src_path (must be PRIMARY, HISTORICAL, or DERIVED)" >&2
      exit 1
      ;;
  esac

  for excl in "${FIXED_EXCLUSIONS[@]}"; do
    case "$src_path" in
      "$excl"|"$excl"/*)
        echo "line $line_no: $src_path falls under fixed exclusion $excl — see phase2-workspace-manifest.md §3" >&2
        exit 1
        ;;
    esac
  done

  [[ -e "$src_path" ]] || { echo "line $line_no: source path does not exist: $src_path" >&2; exit 1; }

  dest_rel="${src_path#/}"
  dest_path="$workspace/copied/$dest_rel"
  mkdir -p "$(dirname "$dest_path")"

  if [[ -d "$src_path" ]]; then
    cp -a --no-preserve=links "$src_path" "$dest_path"
    tree_hash=$(find "$dest_path" -type f -print0 | sort -z | xargs -0 sha256sum | sha256sum | awk '{print $1}')
    printf '%s\t%s\t%s\t%s\n' "$src_path" "$class" "$justification" "$tree_hash" >> "$out_manifest"
  else
    cp -a --no-preserve=links "$src_path" "$dest_path"
    file_hash=$(sha256sum "$dest_path" | awk '{print $1}')
    printf '%s\t%s\t%s\t%s\n' "$src_path" "$class" "$justification" "$file_hash" >> "$out_manifest"
  fi
done < "$manifest"

sha256sum "$out_manifest" | awk '{print $1}' > "$out_manifest.sha256"

echo "workspace built: $workspace"
echo "manifest: $out_manifest"
echo "manifest hash: $(cat "$out_manifest.sha256")"
