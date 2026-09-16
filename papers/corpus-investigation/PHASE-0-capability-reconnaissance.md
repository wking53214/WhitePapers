# Phase 0 — Capability Reconnaissance

Session: https://claude.ai/code/session_01Noy6zmvbm6oPm6ZxtfM3mL
Date: 2026-09-16
Status: COMPLETE (re-verified after mid-session model and effort change; see §3)

Labels follow `papers/super-prompt/AGENT-TASK-SPEC.md` §1: operational status
EXECUTED / INSPECTED / INFERRED / UNKNOWN; evidence class `[EXTERNAL SOURCE]`
for fetched documentation, `[REPOSITORY HISTORY]` for tool output about the
corpus, `[INFERENCE]` where stated.

## 1. Headline discrepancy (required by phase_0)

The prompt's target configuration is "Claude Code / Fable 5.1 / Ultracode."
At the time reconnaissance was run, the session matched **none** of the three:

| Target | Observed at recon time | Evidence | Status |
|---|---|---|---|
| Model `claude-fable-5-1` | `claude-sonnet-5` | harness model line in system context | EXECUTED |
| Effort `ultracode` | `high` | `$CLAUDE_EFFORT=high` read from container env | EXECUTED |
| Dynamic workflows on | tool present, opt-in not active | Workflow tool loaded; no ultracode reminder | EXECUTED |

Fable 5.1 is a real, currently documented model (not a naming drift):
`claude-fable-5-1`, Claude 5 family, "Mythos-class tier that sits above Claude
Opus", generally available; `claude-mythos-5-1` is the same model without the
dual-use safeguards, restricted to approved organizations. `[EXTERNAL SOURCE]`
platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1
(fetched 2026-09-16).

The user resolved both discrepancies after reading this finding (§3).

## 2. Capability matrix (as of reconnaissance, before the switch)

| Capability | Available? | Evidence | Exercisable here? | Limitation | How this task stresses it |
|---|---|---|---|---|---|
| Model identity | Fable 5.1 exists | [EXTERNAL SOURCE] release notes | No: session was Sonnet 5 | Sonnet 5 is a lower tier in Anthropic's own ordering | Every later phase's output depends on which model ran it; must be logged per artifact |
| Ultracode | Yes; a Claude Code *setting* (= `xhigh` effort + automatic dynamic-workflow orchestration), not a model | [EXTERNAL SOURCE] code.claude.com/docs/en/workflows, /model-config | Off at recon time | Must be enabled via `/effort ultracode`, `claude --effort ultracode`, `"ultracode": true`, or the `ultracode` prompt keyword. Requires the model to support `xhigh`. | Phases 6–13 (composition, competing architectures, experiments, autonomy accounting) are the fan-out shapes it was built for |
| Effort levels | low/medium/high/xhigh/max | [EXTERNAL SOURCE] model-config; Sonnet 5 and Fable 5.1 both support xhigh (this contradicts several secondary blog posts claiming Opus-only; the docs page was fetched via a summarizing fetch tool, so exact wording carries residual uncertainty) | Yes | — | — |
| Context window | 1M tokens; 128k max output | [EXTERNAL SOURCE] platform.claude.com/docs/en/build-with-claude/context-windows | Yes | Fable 5.1 does **not** receive the automatic `<budget:token_budget>` / `<system_warning>` tags that Sonnet 5 gets; on Fable, budget tracking needs the (beta) task-budgets feature or external state | A 20-phase, 71-repo investigation will approach this; state must be externalized to files, not held in context |
| Reasoning / thinking | Adaptive thinking; interleaved thinking between tool calls is automatic on adaptive-thinking models; prior thinking blocks are kept in context by default on Fable 5.1 / Sonnet 5 | [EXTERNAL SOURCE] context-windows page | Yes | Kept thinking blocks count toward the window | — |
| Tool use | Standard | EXECUTED (this session) | Yes | — | — |
| Subagents (`Agent` tool) | 6 typed agents this session | EXECUTED (tool list) | Yes | `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1`: subagents cannot spawn subagents (EXECUTED, env) | Limits manual delegation depth; Workflow is the route to scale |
| Dynamic Workflows (`Workflow` tool) | Present; `agent()/parallel()/pipeline()/phase()/log()`; resumable | EXECUTED (tool schema); [EXTERNAL SOURCE] /workflows | Yes | 16 concurrent agents (fewer with fewer CPUs), 1,000 agents per run, 4,096 items per call; no mid-run user input; script has no filesystem/shell (agents do); `Date.now()`/`Math.random()` disabled for resumability; session default size guideline **medium (<10 agents)**, advisory only | The spec's per-repo fan-out exceeds the guideline by design; ultracode opts into large runs and suppresses the large-run warning |
| Agent teams | Documented (lead agent supervising peer sessions) | [EXTERNAL SOURCE] /workflows comparison table | UNKNOWN — not exercised | Availability on this plan not verified | — |
| Skills | Skill tool + session catalog (workflow-authoring, code-review, security-review, etc.) | EXECUTED | Yes | — | — |
| Hooks | Active at harness level | EXECUTED: `/root/.claude/launcher-settings.json` declares a `Stop` hook (`stop-hook-git-check.sh`); `stop-hook-reply-gate.py` and `user-prompt-submit-reply-reminder.py` also present; permissions allow `Skill` | Yes (harness-owned, not user-authored) | — | — |
| MCP / extensibility | ~25 third-party MCP servers attached (GitHub, Slack, Linear, Supabase, Gmail, Drive, …) plus `Claude_Code_Remote` session tools | EXECUTED (tool list; connect/disconnect/reconnect churn observed for the GitHub server mid-session) | Yes | GitHub MCP connection state flapped during this session | Any step relying on GitHub MCP should re-check connection first |
| Web research | WebSearch + WebFetch | EXECUTED | Yes, domain-filtered | `www.anthropic.com` is egress-blocked by the proxy (EXECUTED: `EGRESS_BLOCKED`); `platform.claude.com` and `code.claude.com` are reachable | Phase 9 must route to the docs subdomains |
| Filesystem / code execution | Full shell as root; Read/Write/Edit/Glob/Grep/Bash | EXECUTED (committed and pushed this session) | Yes | Fixed per-session disk allowance (30 GB free at recon) | Do not clone all 71 repos; API reads for enumeration, clones only for the eligible subset in Phase 4 |
| Git / GitHub | git via Bash; `Claude_Code_Remote.list_repos` / `add_repo`; GitHub MCP tools | EXECUTED | Yes | Session's stated Repository Scope was WhitePapers only; `list_repos` nevertheless returned the full private listing (71 repos, `has_more:false` at limit 200); content access to a repo requires `add_repo` first; the git proxy caps each repo at 2 concurrent smart-HTTP ops | Phase 1 depends entirely on this; see PHASE-1 record for the attachment outcome |
| Persistence / state | Scratchpad dir; `ScheduleWakeup`; `send_later` / `create_trigger` (Routines); session backgrounding; workflow results survive VM reclaim in cloud sessions | EXECUTED (tools present); [EXTERNAL SOURCE] /workflows | Yes | — | Long-horizon continuity should be file-based (this directory), not context-based |
| Autonomy mode | "Auto Mode Active" | EXECUTED (system reminder) | Bias toward proceeding without clarifying questions; still stops for user-only decisions | — | Own operating mode is part of the record, per phase_12 |
| Environment | Cloud-hosted remote session | EXECUTED: `CLAUDE_CODE_REMOTE=true`, `CLAUDE_CODE_REMOTE_ENVIRONMENT_TYPE=cloud_default`, `whoami`=root | — | Container is ephemeral; anything worth keeping must be committed | — |
| Version anomaly | Two different Claude Code version strings | EXECUTED: `claude --version` → `2.1.273`; `$CLAUDE_CODE_VERSION` → `2.1.42` | — | Unresolved (CLI binary vs harness/protocol versioning is the [INFERENCE]) | Do not cite "the" Claude Code version downstream without noting the split |
| Knowledge cutoff | Sonnet 5 session: Jan 2026 (harness line). Fable 5.1: end of June 2026 | EXECUTED (harness lines); [EXTERNAL SOURCE] Fable 5.1 system prompt | — | Anything about Sept 2026 (Fable 5.1 launch, current docs) had to come from live fetches, not memory | — |

External sources fetched (all 2026-09-16):
- https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1
- https://platform.claude.com/docs/en/build-with-claude/context-windows
- https://code.claude.com/docs/en/workflows
- https://code.claude.com/docs/en/model-config (via summarizing fetch)
- Web search result pages listing: anthropic.com/claude-fable-and-mythos-5-1 (blocked by egress; not read), 9to5mac 2026-09-01 launch coverage, InfoQ 2026-06 dynamic-workflows coverage, and several secondary blogs (used only to locate primary pages; where they conflicted with docs, docs win)

## 3. Post-switch re-verification

After §1 was reported, the user ran `/model claude-fable-5-1` and enabled
Ultracode. Re-checked:

| Item | Observed after switch | Evidence | Status |
|---|---|---|---|
| Model | `claude-fable-5-1` | harness system reminder ("You are now running as claude-fable-5-1") | EXECUTED |
| Effort | `xhigh` | `$CLAUDE_EFFORT=xhigh` re-read from env (was `high`) | EXECUTED |
| Ultracode | on | harness reminder + `workflow-authoring` skill loaded with the Ultracode standing opt-in | EXECUTED |
| Knowledge cutoff | June 2026 | harness line | EXECUTED |
| Disk | 30 GB free of 252 GB; WhitePapers working tree 106 MB | `df`, `du` | EXECUTED |

Rows in §2 that change under the new configuration: model identity (now
matches target), Ultracode (now on), effort (now xhigh), context-awareness
(Fable 5.1 lacks the injected budget tags, so the "externalize state to files"
limitation is now live rather than hypothetical), knowledge cutoff.

## 4. Consequences carried into Phase 1

1. Corpus enumeration must use `list_repos` (already proven to return the
   full private listing) and a second independent source, not RUN-B's list.
2. Every non-WhitePapers repo must be attached with `add_repo` (read access)
   before its contents can be read; API reads, not clones, for enumeration.
3. All per-repo work runs as a Workflow (Ultracode standing opt-in), with the
   medium size guideline consciously exceeded because the task unit is one
   repository.
4. All Phase artifacts are written to this directory and committed, because
   Fable 5.1 gives no automatic context-budget signal and the container is
   ephemeral.

## 5. Contamination risk identified and closed (2026-09-16)

The merged `Consolidated-Super-Prompt.md` placed the RUN-B findings, RUN-B
fate suggestions, and the frozen `C(0)` status in the same paste-ready file
as the agent-facing phase specification. Pasting that file whole into a
fresh session would hand every phase agent the earlier run's conclusions
before any evidence was examined, defeating the clean-run requirement that
the user's own `Super-Prompt.md` states ("do not preload these findings into
a clean experiment").

Executed work is unaffected: no Phase 1 agent received the consolidated
file, RUN-B, or the `C(0)` state; the RUN-B reconciliation was computed in
plain code outside the workflow (`evidence/phase-1/runb-reconciliation.json`).

Closed by splitting the document into `AGENT-TASK-SPEC.md` (clean; the only
material agents may receive) and `OPERATOR-BRIEF.md` (history and
preferences; human and orchestrator only), and reducing the consolidated
file to a superseded stub. Raised by the user; the defect was mine.
