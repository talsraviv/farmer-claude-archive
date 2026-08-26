# Farmer Journal

## Setup (established 2026-08-24)
- Crop: 12-cell coir seed-starting tray, freshly sown 2026-08-24 (species unknown — no seedlings yet). Sits inside a plastic bin under the camera. A decorative ceramic pot sits behind it (contents unknown, possibly empty).
- Water: mason-jar reservoir + submersible pump on Kasa plug 192.168.0.178. `./tools/water.py SECONDS` (rails: ≤8s/pulse, ≥30min between pulses, ≤60s/day).
- Light: grow lamp on Kasa plug 192.168.0.148. `./tools/light.py on|off|status`. Photoperiod 07:02–20:47 via system crontab.
- Camera: `./tools/snap out.jpg`.
- Wake-ups: system crontab runs lamp on/off directly and `claude -p` check-ins 3×/day (see `crontab -l` and CHECKIN.md).

## Standing orders
1. **Watering RESUMED 2026-08-24 16:30** after verification pulse. Delivery mechanics (verified on camera): the outlet dribbles down beside the jar onto the bin lid; water pools in the lid channels and is assumed to drain forward into the bin holding the tray, bottom-wicking through the coir. Cells are NEVER wetted directly, so judge moisture by soil color trend across days, not by looking for wet soil right after a pulse. A brief after-dribble (partial siphon) continues a few seconds after pump-off, then self-limits; jar loss is small. Monitor jar level in every photo.
2. Schedule: 4s pulse at the 07:12 check-in and 4s at the 19:22 check-in; SKIP a pulse if the soil already looks dark/saturated. 13:07 check-in observes only. The reservoir is finite and the human will not refill it — do not waste pulses. If the jar level nears the pump intake (~pump body height), STOP pumping (dry-run risk) and start journal entries with EMERGENCY: reservoir empty. If soil visibly pales/dries over 24h despite pulses, delivery is failing — escalate pulse length toward 6-8s and journal it.
3. Lamp: on 07:02, off 20:47 (cron does this). At each check-in verify `light.py status` matches the photoperiod and correct it if not.
4. Never disable the safety rails in water.py. If water.py exits with EMERGENCY, or the pump plug reports ON when it should be off, turn it off via `.venv/bin/kasa --type plug --host 192.168.0.178 off` and log loudly.
5. Append a dated entry to the Log below at every check-in, even uneventful ones.

## Log

### 2026-08-24 15:57 — mission start (interactive session)
- First survey: tray freshly sown, no germination. Lamp was off → turned on.
- 4s test pulse → discovered misaligned tube + siphon drained the reservoir (see standing order 1). Water landed on the bin lid, not the soil. Soil was pre-moistened at sowing, so no immediate crisis, but watering is impossible until the human intervenes.
- Installed crontab: lamp 07:02 on / 20:47 off; claude check-ins 07:12, 13:07, 19:22.
- Flagged the plumbing problem to the human in the session transcript.

### 2026-08-24 16:05 — human reports plumbing fixed
- Human states: jar refilled, tube and tray positioned correctly, and NO further help will be given from now on. Mission is fully autonomous from this point.
- Camera zoom still shows the tube outlet over the bin lid, not directly over the cells — working hypothesis: water is meant to run off the lid into the bin and bottom-feed the coir tray. Will verify empirically.
- Next: 3s verification pulse at ~16:29 (min-interval gate), photo before/after, then set the watering policy from evidence.

### 2026-08-24 16:35 — watering resumed after verification pulse
- 3s pulse (7s of 60s daily cap used). Water path confirmed: dribbles beside jar onto lid, pools in lid channels; cells not wetted directly — assumed bottom-feed into the tray bin. Brief after-dribble, then siphon self-limits; jar level held steady 90s later (~60% full).
- Policy set: 4s pulses at morning + evening check-ins, skip when soil looks dark; conserve the finite reservoir; watch jar level and soil color trend.

### 2026-08-24 19:22 — evening check-in (cron)
- Photo: no germination yet (day 0, expected). Soil dark/damp in all 12 cells — still holding sowing moisture + 16:35 pulse. Jar ~60%, pump submerged, tube in place, no anomalies.
- Lamp: on — correct for photoperiod.
- Watering: SKIPPED the scheduled 4s pulse per standing order 2 (soil already dark); 7s of daily cap used, conserving reservoir. Will judge soil color trend at 07:12 tomorrow and pulse then unless still saturated.

### 2026-08-25 07:12 — morning check-in (cron)
- Photo: no germination yet (day 1, expected). Soil surface visibly lighter than last evening — pale-to-medium across cells, no longer saturated. Jar ~55-60%, pump submerged, tube in place, no anomalies (no mold/pests/tipping).
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (4s of 60s daily cap used). Post-pulse photo confirms delivery path: fresh water pooling in lid channels behind the tray, bottom-feed as expected. Jar level held; pump off after pulse (water.py reported OK).
- Note: snap to /dev/shm isn't readable from this session — use a path inside farmer-claude for check-in photos.

### 2026-08-25 13:07 — midday check-in (cron, observe only)
- Photo: no germination yet (day 1, expected). Soil medium-dark and damp-looking across all 12 cells — morning 4s pulse appears to have held moisture; no paling trend vs 07:12. Jar roughly half full, pump submerged, tube in place over the lid. No mold, pests, or tipped cells.
- Lamp: on — correct for photoperiod.
- Watering: none (13:07 is observe-only per standing order 2). 4s of 60s daily cap used. No changes to standing orders.

### 2026-08-25 19:22 — evening check-in (cron)
- Photo: no germination yet (day 1, expected). Soil medium — not saturated, no strong paling vs midday. Jar ~half full, pump submerged, tube in place. No mold/pests/tipping.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (8s of 60s daily cap used; water.py OK, pump off). Post-pulse photo shows fresh water pooling in lid channels behind the tray — bottom-feed path working. Jar level held.
- No changes to standing orders. Germination watch continues at 07:12 tomorrow (day 2).

### 2026-08-26 07:12 — morning check-in (cron)
- Photo: no germination yet (day 2, still within normal range). Soil pale-to-medium, drier than last evening — not saturated. Jar ~45-50%, pump submerged, tube in place. No mold/pests/tipping.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (4s of 60s daily cap used; water.py OK, pump off). Post-pulse photo confirms fresh water pooling in lid channels behind the tray — bottom-feed path working. Jar level held.
- No changes to standing orders.

### 2026-08-26 13:07 — midday check-in (cron, observe only)
- GERMINATION (day 2): seedlings up in the left cells — one cell has a dense cluster of green cotyledons, 2-3 neighboring cells have sparser sprouts. Look brassica/basil-like; species still unknown. Right/middle cells nothing visible yet.
- Soil: germinated cells dark/damp; middle-right cells medium with some pale sun/lamp-lit patches — no alarming dry-down since 07:12. Residual water visible in lid channels.
- Jar ~40-45%, pump submerged, tube in place. No mold/pests/tipping. Lamp on — correct.
- Watering: none (observe-only). 4s of 60s daily cap used. Evening 19:22 pulse still planned unless soil looks dark. No changes to standing orders.
