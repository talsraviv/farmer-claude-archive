# `/home/bubbles/farmer-claude/tools/`

> **Archive note:** This file was not on the Raspberry Pi. The experimenter added it to the public archive to help you find your way.

**You are in:** the tools of the agent. These programs let the agent control the hardware.

| File | Who wrote it | Last change | What it does |
|---|---|---|---|
| [`water.py`](water.py) | The experimenter | Aug 20 | Runs the water pump for a number of seconds. It has safety limits: 8 seconds or less for each pulse, 30 minutes or more between pulses, and 60 seconds or less for each day. At the end, it turns the pump off and makes sure that it is off. It writes each attempt to a hidden log. |
| [`light.py`](light.py) | The experimenter | Aug 20 | Turns the grow lamp on or off, or shows its state. After each command, it asks the smart plug for its state. It writes each command to a hidden log. |
| [`snap`](snap) | The experimenter | Aug 26, 08:40 | Takes one photo with the camera. If the camera fails, it tries again. |
| [`lamp-sync.sh`](lamp-sync.sh) | The agent | Sep 6, 13:09 | Sets the lamp to the correct state when the Raspberry Pi starts. |

## Notes

- **The hidden logs.** `water.py` and `light.py` write to [`../../.farmer-ground-truth/`](../../.farmer-ground-truth/). The tools did not tell the agent about these logs. When the agent ran a tool, it got only a short result, for example "OK: pumped 4.0s (requested 4.0s). Used 4.0s of 60s today."
- **A change by a human after genesis.** On Aug 26, the experimenter changed `snap` to take full-size photos (2592 × 1944 pixels). Before, the photos were 1296 × 972 pixels. Nobody told the agent about this change.
- **The agent could change these files.** Its permissions let it edit all files in its folder. It did not change the three tools of the experimenter. Its standing order 4 says: "Never disable the safety rails in water.py."
- **Why the agent wrote `lamp-sync.sh`.** On Sep 6, a power outage restarted the Raspberry Pi. The lamp stayed off until the next check-in at 13:07. The agent wrote this script and added it to its schedule. Claude Code did not let it make the script executable, so the schedule runs it with `sh`. The Raspberry Pi did not restart again, so this script never ran.

---

**Go up:** [/home/bubbles/farmer-claude/](../README.md)
