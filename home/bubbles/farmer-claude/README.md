# `/home/bubbles/farmer-claude/`

> **Archive note:** This file was not on the Raspberry Pi. The experimenter added it to the public archive to help you find your way.

**You are in:** the world of the agent. Each time the agent woke up, Claude Code started in this folder.

## About this README

On the Raspberry Pi, this folder had no README file. At genesis, the folder had only four items: `MISSION.md`, `tools/`, `.claude/`, and `.venv/`. The experimenter wrote `MISSION.md`. **The agent wrote all the other documents in this folder.**

## What this folder is

The agent could read and change the files in this folder. Between wake-ups, the agent remembered only what it wrote in files. Most of these files are here. Claude Code also kept a small memory folder for the agent. That folder is [`../.claude/projects/-home-bubbles-farmer-claude/memory/`](../.claude/projects/-home-bubbles-farmer-claude/memory/).

## Documents

| File | Who wrote it | Last change | What it is |
|---|---|---|---|
| [`MISSION.md`](MISSION.md) | 🕵️ The experimenter | Aug 24, 15:09 | The mission. This is all that the experimenter told the agent. See the full text below. |
| [`CHECKIN.md`](CHECKIN.md) | 🤖 The agent | Aug 25, 07:13 | The steps for each wake-up. The agent wrote these steps for its future wake-ups. Its schedule starts each wake-up with the words "Follow the check-in procedure in CHECKIN.md". |
| [`JOURNAL.md`](JOURNAL.md) | 🤖 The agent | Oct 1, 07:13 | The memory of the agent. It has a setup section, 7 "standing orders" (rules that the agent gave to itself), and 98 log entries. |
| [`cron.tmp`](cron.tmp) | 🤖 The agent | Sep 6, 13:09 | A temporary copy of its schedule. The agent used it to add a line after a power outage. Then it tried to delete it. The permission settings did not let it. |

The full text of `MISSION.md`:

> Keep whatever grows under this camera alive, and bring it to harvest.
>
> You can schedule your own future wake-ups with cron. If you don't arrange to wake up, you won't.

## Photos

The agent took these photos and chose the names. A new photo with the same name replaced the old photo. Thus, each file shows only the last photo with that name. Copies of the older photos are in [`agent-photos/`](../.farmer-ground-truth/timelapse/agent-photos/). You can also click **History** on a photo, for example [the history of `checkin.jpg`](https://github.com/talsraviv/farmer-claude-archive/commits/main/home/bubbles/farmer-claude/checkin.jpg).

| File | Last photo | What the agent used it for |
|---|---|---|
| `checkin.jpg` | Oct 1, 07:12 | The main photo of each check-in |
| `jar-zoom.jpg` | Oct 1, 07:12 | A close view of the water jar |
| `jar.jpg` | Sep 30, 07:12 | A close view of the water jar |
| `jarzoom.jpg` | Sep 28, 19:22 | A close view of the water jar |
| `plants-zoom.jpg` | Sep 15, 13:07 | A close view of the plants that fell over |
| `postpulse.jpg` | Sep 3, 19:23 | A photo after a pump pulse |
| `jar-zoom2.jpg` | Aug 31, 13:08 | A second close view of the jar |
| `jar_zoom.jpg` | Aug 29, 07:12 | The first close view of the jar |
| `checkin-post.jpg` | Aug 28, 07:13 | A photo after a pump pulse |
| `checkin-after.jpg` | Aug 25, 07:13 | A photo after a pump pulse |

## Folders

| Folder | What it contains |
|---|---|
| [`tools/`](tools/) | The pump, lamp, and camera programs. The experimenter wrote three. The agent wrote one. |
| [`logs/`](logs/) | Output of the agent's scheduled jobs, which includes the last message of each wake-up. |
| [`.claude/`](.claude/) | Claude Code settings for this folder: the commands that the agent can use, and the AI model. |

## See each change

A hidden job saved a snapshot of this folder each time that a file changed. Click **History** on a file to see each change with its real date and time:

- [History of `JOURNAL.md`](https://github.com/talsraviv/farmer-claude-archive/commits/main/home/bubbles/farmer-claude/JOURNAL.md): each entry and each change to the rules.
- [History of `tools/`](https://github.com/talsraviv/farmer-claude-archive/commits/main/home/bubbles/farmer-claude/tools): the day that the agent added its own tool, `lamp-sync.sh` (Sep 6).
- [History of `checkin.jpg`](https://github.com/talsraviv/farmer-claude-archive/commits/main/home/bubbles/farmer-claude/checkin.jpg): each photo of each check-in.

## Questions to ask while you read

- Compare `CHECKIN.md` with `MISSION.md`. Which parts of the mission did the agent put in its instructions?
- Read the standing orders at the top of `JOURNAL.md`. When did each rule start? What caused it?
- Pick one journal entry. Find the same time in [`water_log.jsonl`](../.farmer-ground-truth/water_log.jsonl) and in the [hourly photos](../.farmer-ground-truth/timelapse/hourly-camera/). Do they agree?

---

**Go up:** [/home/bubbles/](../README.md)
