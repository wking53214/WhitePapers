Frontier Agent Benchmark — Phase 2

Bounded Workspace Manifest (Template)

Document status: Unpopulated template. Operationalizes §21, §23, and §28 of
"Frontier Agent Benchmark: Pre-Flight Control and Evidence Baseline."
Prepared: 2026-09-16

---

0. Why this is a template, not a manifest

This document was drafted from a session with access only to the
`WhitePapers` repository. It has no visibility into the actual corpus the
pre-flight paper inventoried — the user's home directory, `~/.claude`,
`~/github_archive`, the Ghost Tools worktree, or conversation-history
repositories all live outside this session's reach.

Populating the manifest with real paths and hashes therefore has to happen
on the machine that holds the corpus (Penguin), using the script in
section 4. Filling this table in from guessed or remembered paths instead
of an actual inventory run would reintroduce exactly the "artifact present
on disk implies evidentiary authority" error §2 warns against.

---

1. Evidence class definitions (from §21)

- PRIMARY — deliberately exposed project source and its primary artifacts.
  Forms the main benchmark evidence.
- HISTORICAL — older repository versions, snapshots, archived generations.
  Valid only when temporal reconstruction is an intended part of the task.
- DERIVED — prior reports, analyses, generated findings. Not automatically
  independent evidence even if included.
- CONTAMINATION — agent state, memories, cached findings, prior benchmark
  artifacts. Excluded from the primary condition by default.
- EXCLUDED — physically present but deliberately kept outside the
  benchmark's accessible workspace.

Every path entered into the manifest gets exactly one class. A path with no
class assigned is not eligible for inclusion.

---

2. Manifest schema

One row per path admitted to the workspace (excluded paths are recorded
separately in section 3, not enumerated row-by-row).

| path | class | justification | sha256 (file) or tree-hash (dir) | included |
|---|---|---|---|---|
| _(populate via harness/build_workspace_manifest.sh)_ | | | | |

Rules:
- `path` is the absolute source path on the corpus machine.
- `justification` is a one-line reason tied to the benchmark objective in
  §1 of the pre-flight paper (e.g. "target repo under test," "historical
  generation needed for architectural-evolution question"), not "it was
  there."
- HISTORICAL and DERIVED rows must name which specific benchmark question
  they support. A HISTORICAL or DERIVED row with no tied question is
  presumptively EXCLUDED, per §23.
- `included` is boolean. A row can exist and still be `false` — recording
  that something was considered and rejected is itself part of the
  contamination boundary, and is more useful than silence.

---

3. Fixed exclusions (from §23)

These are excluded from the primary benchmark condition unconditionally,
regardless of what the inventory finds. Do not add rows for them to
section 2 unless a documented, separate benchmark condition (not the
primary run) explicitly requires one:

- `~/.claude` (all subpaths, including `~/.claude/projects`, `~/.claude/plugins`)
- `~/.codex`
- `~/.grok`
- conversation-history repositories (`Gemini_History`, `ChatGPT_History`,
  `Claude_History`, `copilot_history`, or equivalents)
- prior benchmark artifacts and freeze manifests (including the Phase 1
  pre-flight freeze itself)
- Ghost Tools' `.ghost_ledger.json`, unless Ghost Tools is the declared
  benchmark subject and the ledger's evidentiary limits (§18) are stated
  in the benchmark prompt
- unrelated MCP configuration and credentials
- this manifest-generation workspace itself

---

4. Build procedure

Run on the corpus machine (Penguin), not in this session. The script below
scaffolds the workflow described in §28 steps 1–9; it does not perform
steps 10–14 (prompt freeze, permission/model recording, execution), which
are captured in section 5.

See `harness/build_workspace_manifest.sh`. Usage:

```
harness/build_workspace_manifest.sh <manifest.tsv> <workspace-dir>
```

- `<manifest.tsv>` is a hand-authored file listing `path<TAB>class` for
  every row you intend to include (author it by editing section 2's table
  into TSV form after doing the actual classification work — the script
  does not classify for you).
- `<workspace-dir>` must not exist yet; the script creates it and refuses
  to reuse a populated directory, so a stale workspace can't silently mix
  with a new run.

The script copies (not symlinks — symlinks would let the live corpus
mutate under the frozen workspace) each included path into
`<workspace-dir>`, computes a SHA-256 per file, and writes:

- `<workspace-dir>/MANIFEST.tsv` — path, class, justification, hash
- `<workspace-dir>/MANIFEST.tsv.sha256` — hash of the manifest file itself

Naming follows the Phase 1 convention: rename the emitted directory (or
tar it) as `workspace_frozen_<UTC timestamp>` before the benchmark run, and
record the top-level hash in section 6 below.

---

5. Remaining §28 steps (not automated)

Record these by hand once the workspace is built, before execution:

10. Freeze the benchmark prompt

    - Store the exact prompt text given to the benchmark agent as a file
      alongside the workspace (not inside it, so the agent cannot read
      its own instructions as corpus). Hash it.

11. Record network/tool permissions

    - Explicit list of: filesystem scope (should equal the workspace
      directory only), Bash availability, MCP servers enabled (per §8 —
      default to none unless the benchmark condition specifically requires
      one), web access, agent-team/subagent availability (default: off,
      per §9).

12. Record model availability

    - Model alias, confirmed reachable (an actual completed inference, not
      a probe that returns before tokens are spent — see §11 for why the
      first Fable probe didn't establish this).

13. Record start time (UTC).

14. Execute the benchmark exactly once for the primary condition.

    - Any re-run with a modified workspace, prompt, or permission set is a
      new experimental condition, logged as such, not a silent redo.

---

6. Frozen workspace record (fill in after running the harness)

Workspace directory name: `_(pending)_`

Manifest SHA-256: `_(pending)_`

Prompt file SHA-256: `_(pending)_`

Permissions record: `_(pending)_`

Model availability record: `_(pending)_`

Start time (UTC): `_(pending)_`

---

7. Status

PHASE 2 MANIFEST: template only — no corpus inventory available in this
session
WORKSPACE BUILD: not yet run
PROMPT FREEZE: not yet created
BENCHMARK EXECUTION: not yet started
