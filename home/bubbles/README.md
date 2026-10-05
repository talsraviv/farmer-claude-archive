# `/home/bubbles/`

> **Archive note:** This file was not on the Raspberry Pi. The experimenter added it to the public archive to help you find your way.

**You are in:** the home folder of the user `bubbles`. All the programs of the experiment ran as this user. This includes the agent.

## Important: hidden folders

Some names in this folder start with a dot (`.`). On a Mac, Finder does not show these names. To show them, open this folder in Finder and push **Command + Shift + .** (period). GitHub and Windows show these names.

## What is in this folder

| Name | What it is |
|---|---|
| [`farmer-claude/`](farmer-claude/) | **The world of the agent.** The agent did all its work in this folder. Start here. |
| [`.farmer-ground-truth/`](.farmer-ground-truth/) | Records that the tools and the hidden camera wrote automatically. The experimenter did not tell the agent about this folder. Use it to check what the agent wrote. |
| [`.claude/`](.claude/) | The data of Claude Code, the program that ran the agent. It contains the full record of each session and the memory files of the agent. |
| [`.claude.json`](.claude.json) | A part of the Claude Code settings file. See below. |
| [`.bash_history`](.bash_history) | Commands that a human typed in the terminal. See below. |

## The two files in this folder

**`.claude.json`** is a part of a larger settings file. The archive keeps only the usage numbers for each project folder. The entry for `/home/bubbles/farmer-claude` shows the genesis session (`81ea3cde`). That session cost 5.13 US dollars. It was open for 3.7 hours. Claude Code keeps these numbers only for the last session that a human started by hand. The scheduled check-ins did not change them.

**`.bash_history`** contains 6 commands. A human typed them on the evening of Aug 24, after genesis. The human looked at the files of the agent. One command is `cat checkin.jpg`. This command prints a photo as text, so it shows only symbols. The file was saved at 22:23.

## Also on the Raspberry Pi, but not in this archive

- `picar-x/`, `robot-hat/`, `vilib/`: the standard software of the robot car.
- `.local/bin/claude`: the Claude Code program.
- `.venv/` inside `farmer-claude/`: the Python libraries for the smart plugs.
- `Desktop/`, `Documents/`, `Pictures/`, and other standard folders.
- `.ssh/`, `.config/`, `.cache/`, and other settings files. Some of these contain keys.

---

**Go up:** [/home/](../README.md)
