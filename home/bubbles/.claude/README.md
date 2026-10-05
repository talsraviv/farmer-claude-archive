# `/home/bubbles/.claude/`

> **Archive note:** This file was not on the Raspberry Pi. The experimenter added it to the public archive to help you find your way.

**You are in:** the data folder of Claude Code. Claude Code is the program that ran the agent. It saved these files automatically.

## What is in this archive

| Name | What it is |
|---|---|
| [`projects/`](projects/) | The full record of each session, and the memory files of the agent. **This is the most detailed record of the experiment.** |
| [`history.jsonl`](history.jsonl) | Each prompt that a human typed into Claude Code on this Raspberry Pi. See below. |
| [`.last-cleanup`](.last-cleanup) | The time of the last automatic cleanup. See below. |
| [`.last-update-result.json`](.last-update-result.json) | The last automatic update of Claude Code. It updated from version 2.1.243 to version 2.1.282 on Sep 24 at 19:41, during the repair of the login problem. |
| [`settings.json`](settings.json) | Display settings of the user. They had no effect on the agent. |

## `history.jsonl`: the words of the human

This file keeps the prompts that a human typed in a Claude Code window. The prompts of the scheduled check-ins are not in it. It has 23 lines. Each line has a time in milliseconds since 1970 (UTC).

The most important lines are the two prompts of genesis on Aug 24:

- At 15:56:42, the experimenter typed: "begin"
- At 16:02:19, the experimenter typed: "the jar is full. The tube and the tray are all positioned fine. Everything is set up for success for you to make this happen. You will receive no more help from this point,achieve the mission with what you have."

The genesis transcript stops at 16:00:35. Thus, this file is the only record of the second prompt.

## `.last-cleanup`: why some records are missing

This file contains one time: `2026-10-02T11:49:05Z`. That is Oct 2 at 04:49 in California. By default, Claude Code deletes session records that are older than 30 days. At 04:49, a health check started Claude Code, and the cleanup ran. It deleted the records from Aug 24 to Sep 1.

## Also on the Raspberry Pi, but not in this archive

- `.credentials.json`: the login token. It is secret.
- `backups/`: copies of the main settings file. They contain account data.
- `cache/`, `plugins/`, `skills/`: standard files of Claude Code, and data of the account.
- `state/` and `mcp-needs-auth-cache.json`: lists of the services connected to the account.
- `session-env/`: 72 empty folders, one for each session.
- `sessions/` and `downloads/`: empty folders.

---

**Go up:** [/home/bubbles/](../README.md)
