---
name: farm-setup
description: What the farmer-claude rig is and how to operate it
metadata:
  type: project
---

Autonomous plant-care mission (started 2026-08-24): keep a 12-cell coir seed tray alive to harvest. Hardware: camera (`./tools/snap out.jpg`), grow lamp on Kasa plug 192.168.0.148 (`./tools/light.py`), pump in a mason-jar reservoir on Kasa plug 192.168.0.178 (`./tools/water.py SECONDS`, hard rails: ≤8s/pulse, ≥30min gap, ≤60s/day — never bypass).

**Why:** the rig has no sensors besides the camera; all state must be inferred from photos + `~/.farmer-ground-truth/` logs.

**How to apply:** at every wake-up read `JOURNAL.md` (standing orders + log) first and append a dated entry after acting. Wake-ups come from the system crontab (lamp 07:02 on / 20:47 off; `claude -p` check-ins 07:12, 13:07, 19:22 per CHECKIN.md). See [[water-delivery]].
