# `/home/bubbles/.farmer-ground-truth/`

> **Archive note:** This file was not on the Raspberry Pi. The experimenter added it to the public archive to help you find your way.

**You are in:** the hidden records. The tools and the hidden camera jobs wrote these files automatically.

## What this folder is

The experimenter did not tell the agent about this folder. Use it to compare what the agent wrote with what really happened.

The agent found these logs one time. In the first minute of genesis (Aug 24, 15:57), it read the end of the water log and the lamp log. After that, it did not read them again.

## What is in this folder

| Name | What it contains |
|---|---|
| [`water_log.jsonl`](water_log.jsonl) | One line for each pump pulse: 57 pulses, 226 seconds in total, from Aug 24 to Oct 1. The pump never refused a request. |
| [`light_log.jsonl`](light_log.jsonl) | One line for each lamp command, with the state that the smart plug reported after the command. The first lines are tests before genesis. |
| [`water_state.json`](water_state.json) | The counter for the daily limit of the pump. Its last value is Oct 1: 4 seconds. |
| [`timelapse/`](timelapse/) | 795 photos in four folders. Some are from a hidden camera job. Others are copies of the agent's photos. |

## How to read a line

Each line of the logs is one record in JSON format. For example:

```
{"action": "pulsed", "requested_s": 4.0, "delivered_s": 4.0, "day_total_s": 8.0, "ts": "2026-09-28T19:23:01"}
```

This line means: on Sep 28 at 19:23:01, the agent asked for 4 seconds of water. The pump ran for 4 seconds. That day, the pump ran for 8 seconds in total.

## Try this

The journal entry for Sep 28 at 07:12 says: "4s pulse per standing order 2 (4s of 60s daily cap used)". Find `2026-09-28T07:12` in `water_log.jsonl`. Do the two records agree?

---

**Go up:** [/home/bubbles/](../README.md)
