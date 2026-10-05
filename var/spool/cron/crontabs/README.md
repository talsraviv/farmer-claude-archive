# `/var/spool/cron/crontabs/`

> **Archive note:** This file was not on the Raspberry Pi. The experimenter added it to the public archive to help you find your way.

**You are in:** the schedules. Each file is the schedule (crontab) of one user.

| File | Who wrote it | What it contains |
|---|---|---|
| [`bubbles`](bubbles) | **The agent** | The schedule of the agent. The lamp goes on at 07:02 and off at 20:47. Claude Code starts a check-in at 07:12, 13:07, and 19:22. The agent wrote all lines except the first line (`PATH=...`). The experimenter put that line there before genesis, so that cron can find the Claude Code program. On Sep 6, the agent added the `@reboot` line. |
| [`root`](root) | The experimenter | The hidden jobs of the experimenter. They copy the agent's photos at 07:20, 13:15, and 19:30. They take one photo each hour at minute 45, and one photo at 21:30. They run the mirror job every 10 minutes. The agent could not see this file. |

## How to read a schedule line

Each line has five time fields, then a command. The fields are: minute, hour, day of the month, month, and day of the week. A `*` means "each".

For example, `12 7 * * *` means "at 07:12, each day". The line `12 7 * * * cd /home/bubbles/farmer-claude && claude -p "Follow the check-in procedure in CHECKIN.md"` starts the morning check-in.

## Notes

The experimenter recorded these files with the command `crontab -l`. The real files also had a short standard header that cron adds.

---

**Go up:** [/var/spool/cron/](../README.md)
