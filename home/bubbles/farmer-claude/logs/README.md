# `/home/bubbles/farmer-claude/logs/`

> **Archive note:** This file was not on the Raspberry Pi. The experimenter added it to the public archive to help you find your way.

**You are in:** the log folder that the agent made at genesis. Its scheduled jobs write their output here.

| File | What it contains |
|---|---|
| [`checkin.log`](checkin.log) | The last message of each check-in, from Aug 24 to Oct 4. |
| [`cron.log`](cron.log) | The output of the lamp jobs: "lamp is on" at 07:02 and "lamp is off" at 20:47, each day. |

## Why `checkin.log` is important

- **It keeps the lost week.** Claude Code deleted the full records of the sessions from Aug 24 to Sep 1. But this log still has the last message of each check-in from that week.
- **It shows the failures.** When a check-in failed, Claude Code wrote the error here. Search for these words:
  - "Failed to authenticate" (18 times, Sep 19 to Sep 24). The login of Claude Code expired.
  - "usage credits" (11 times, Oct 1 to Oct 4). The account had no more usage credits. After that, the agent did not wake up again.
- **The lamp did not stop.** The lamp jobs do not use Claude Code. Thus, `cron.log` continues after the agent stopped.

---

**Go up:** [/home/bubbles/farmer-claude/](../README.md)
