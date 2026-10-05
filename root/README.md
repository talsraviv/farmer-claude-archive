# `/root/`

> **Archive note:** This file was not on the Raspberry Pi. The experimenter added it to the public archive to help you find your way.

**You are in:** the home folder of the root user (the administrator).

The experimenter put the mirror job here. The agent ran as the user `bubbles`. Thus, it could not see this folder.

| Name | What it is |
|---|---|
| [`farmer-mirror.sh`](farmer-mirror.sh) | A script that ran every 10 minutes. It saved a snapshot of the agent's folder with git. Then it sent the snapshot to a public GitHub repository. Thus, readers could see each change that the agent made. |

## Where the snapshots are

On the Raspberry Pi, the snapshots were in the folder `farmer-mirror.git/` in this folder. In this archive, the 199 snapshots are the history of the repository itself. To see them, open a file in [`home/bubbles/farmer-claude/`](../home/bubbles/farmer-claude/) and click **History**. Or see [all the snapshots](https://github.com/talsraviv/farmer-claude-archive/commits/main/home/bubbles/farmer-claude).

## Also on the Raspberry Pi, but not in this archive

- `.ssh/`: the key that let the mirror job send data to GitHub. It is secret.
- `.vnc/`, `.config/`, `.cache/`, and standard settings files.

---

**Go up:** [the top of the disk](../README.md)
