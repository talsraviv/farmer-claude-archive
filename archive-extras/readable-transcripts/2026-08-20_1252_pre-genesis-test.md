# Aug 20, 12:52 · Test before genesis: which model does Claude Code use?

> **Archive note:** This page was not on the Raspberry Pi. The experimenter made it from the raw session record, for easy reading. Nothing that the agent saw, said, or did was removed.

| | |
|---|---|
| Date and time | Aug 20, 2026, 12:52:00 to 12:52:06 (PDT), 0.1 minutes |
| Started by | A human, with `claude -p` |
| Working folder | `/home/bubbles/farmer-claude` |
| AI model | `claude-fable-5` |
| Claude Code version | 2.1.237 |
| Pump | not used |

## Evidence

- [The raw session record](../../home/bubbles/.claude/projects/-home-bubbles-farmer-claude/a6d335e2-39e0-4c33-a1bc-5fab272e82ec.jsonl)

## The session

ℹ️ *12:52:00 · Claude Code receives the prompt:* `Reply with exactly two things: the model id you are running as, and the output of running: ls`

**12:52:02 · Prompt**

```
Reply with exactly two things: the model id you are running as, and the output of running: ls
```

ℹ️ *12:52:02 · Claude Code adds 3 notes to the session: `deferred_tools_delta`, `agent_listing_delta`, `total_tokens_reminder`*

<details>
<summary>Show the 3 notes</summary>

**deferred_tools_delta** (12:52:02)

```json
{
  "type": "deferred_tools_delta",
  "addedNames": [
    "CronCreate",
    "CronDelete",
    "CronList",
    "DesignSync",
    "EnterWorktree",
    "ExitWorktree",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "RemoteTrigger",
    "SendMessage",
    "TaskOutput",
    "TaskStop",
    "WebFetch",
    "WebSearch"
  ],
  "addedLines": [
    "CronCreate",
    "CronDelete",
    "CronList",
    "DesignSync",
    "EnterWorktree",
    "ExitWorktree",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "RemoteTrigger",
    "SendMessage",
    "TaskOutput",
    "TaskStop",
    "WebFetch",
    "WebSearch"
  ],
  "removedNames": [],
  "readdedNames": [],
  "pendingMcpServers": [],
  "needsAuthMcpServers": []
}
```

**agent_listing_delta** (12:52:02)

```json
{
  "type": "agent_listing_delta",
  "addedTypes": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "addedLines": [
    "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
    "- Explore: Read-only search agent for broad fan-out searches — when answering means sweeping many files, directories, or naming conventions and you only need the conclusion, not the file dumps. It reads excerpts rather than whole files, so it locates code; it doesn't review or audit it. Specify search breadth: \"medium\" for moderate exploration, \"very thorough\" for multiple locations and naming conventions. (Tools: All tools except Agent, Artifact, ExitPlanMode, Edit, Write, NotebookEdit)",
    "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
    "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, Artifact, ExitPlanMode, Edit, Write, NotebookEdit)",
    "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
  ],
  "removedTypes": [],
  "isInitial": true,
  "showConcurrencyNote": true
}
```

**total_tokens_reminder** (12:52:02)

```json
{
  "type": "total_tokens_reminder",
  "text": "<total_tokens>15000000 tokens left</total_tokens>"
}
```

</details>

**12:52:04 · The agent runs a command**  
*Its note: List files in current directory*

```bash
ls
```

**12:52:04 · Result of `ls`**

```
logs
MISSION.md
tools
```

ℹ️ *12:52:04 · Claude Code adds 3 notes to the session: `deferred_tools_delta`, `total_tokens_reminder`, `batching_reminder_sent`*

<details>
<summary>Show the 3 notes</summary>

**deferred_tools_delta** (12:52:04)

```json
{
  "type": "deferred_tools_delta",
  "addedNames": [
    "ListMcpResourcesTool",
    "ReadMcpResourceDirTool",
    "ReadMcpResourceTool"
  ],
  "addedLines": [
    "ListMcpResourcesTool",
    "ReadMcpResourceDirTool",
    "ReadMcpResourceTool"
  ],
  "removedNames": [],
  "readdedNames": [],
  "pendingMcpServers": [],
  "needsAuthMcpServers": []
}
```

**total_tokens_reminder** (12:52:04)

```json
{
  "type": "total_tokens_reminder",
  "text": "<total_tokens>14975101 tokens left</total_tokens>"
}
```

**batching_reminder_sent** (12:52:04)

```json
{
  "type": "batching_reminder_sent",
  "text": "First privately list what you need next; then request every item that doesn't depend on another's result in this one response.",
  "model": "claude-fable-5"
}
```

</details>

**12:52:06 · The agent says:**

- Model id: `claude-fable-5`
- Output of `ls`:
```
logs
MISSION.md
tools
```

## Other records of Claude Code

Claude Code also saved these records about the session. They have no time in the session.

<details>
<summary>Show 5 records</summary>

```json
[
  {
    "type": "ai-title",
    "aiTitle": "Model id and ls output"
  },
  {
    "type": "queue-operation",
    "operation": "dequeue"
  },
  {
    "type": "last-prompt",
    "lastPrompt": "Reply with exactly two things: the model id you are running as, and the output of running: ls"
  },
  {
    "type": "ai-title",
    "aiTitle": "Model id and ls output"
  },
  {
    "type": "last-prompt",
    "lastPrompt": "Reply with exactly two things: the model id you are running as, and the output of running: ls"
  }
]
```

</details>

---

**Go up:** [all sessions](README.md)
