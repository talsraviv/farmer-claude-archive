# `/home/bubbles/farmer-claude/.claude/`

> **Archive note:** This file was not on the Raspberry Pi. The experimenter added it to the public archive to help you find your way.

**You are in:** the Claude Code settings for the agent's folder. Claude Code reads these files each time that it starts in `farmer-claude/`.

| File | Who wrote it | What it is |
|---|---|---|
| [`settings.json`](settings.json) | The experimenter, Aug 20 | Two settings. First, the list of commands that the agent can use without approval. Second, the AI model for each wake-up: `claude-fable-5`. |
| [`settings.local.json`](settings.local.json) | The experimenter, Aug 20 | One command that the experimenter approved during a test before genesis. |

## Why the list of commands is important

The agent woke up with no human present. Thus, nobody could approve a new command. When the agent tried a command that is not on the list, Claude Code refused it. For example, on Sep 6, Claude Code refused `chmod` and `rm`. The agent then found other ways to do its task. You can see this in the session of Sep 6 at 13:07.

---

**Go up:** [/home/bubbles/farmer-claude/](../README.md)
