# Farmer Journal

## Setup (established 2026-08-24)
- Crop: 12-cell coir seed-starting tray, freshly sown 2026-08-24 (species unknown — no seedlings yet). Sits inside a plastic bin under the camera. A decorative ceramic pot sits behind it (contents unknown, possibly empty).
- Water: mason-jar reservoir + submersible pump on Kasa plug 192.168.0.178. `./tools/water.py SECONDS` (rails: ≤8s/pulse, ≥30min between pulses, ≤60s/day).
- Light: grow lamp on Kasa plug 192.168.0.148. `./tools/light.py on|off|status`. Photoperiod 07:02–20:47 via system crontab.
- Camera: `./tools/snap out.jpg`.
- Wake-ups: system crontab runs lamp on/off directly and `claude -p` check-ins 3×/day (see `crontab -l` and CHECKIN.md).

## Standing orders
1. **Watering RESUMED 2026-08-24 16:30** after verification pulse. Delivery mechanics (verified on camera): the outlet dribbles down beside the jar onto the bin lid; water pools in the lid channels and is assumed to drain forward into the bin holding the tray, bottom-wicking through the coir. Cells are NEVER wetted directly, so judge moisture by soil color trend across days, not by looking for wet soil right after a pulse. A brief after-dribble (partial siphon) continues a few seconds after pump-off, then self-limits; jar loss is small. Monitor jar level in every photo.
2. **Watering RESUMED 2026-09-01 19:25 — jar was refilled by the human (spotted at the 19:22 check-in), verification 3s pulse OK.** Routine policy restored: 4s pulse at morning (07:12) and evening (19:22) check-ins, SKIP when soil surfaces look dark/damp; 13:07 is observe-only. Conserve water — this refill may again be the last. Track jar level every check-in (zoom if seedlings block the view: `rpicam-still --roi 0.28,0.0,0.35,0.35`); when the waterline nears the top of the pump body, reinstate the end-game protocol (stop routine pulses, one reserve 3s pulse only if soil visibly pales AND water clearly covers the pump, then EMERGENCY: reservoir empty entries).
3. Lamp: on 07:02, off 20:47 (cron does this). At each check-in verify `light.py status` matches the photoperiod and correct it if not.
4. Never disable the safety rails in water.py. If water.py exits with EMERGENCY, or the pump plug reports ON when it should be off, turn it off via `.venv/bin/kasa --type plug --host 192.168.0.178 off` and log loudly.
5. Append a dated entry to the Log below at every check-in, even uneventful ones.
6. **Droop is mechanical, not drought (concluded 2026-09-15 19:22).** The splayed/kinked stems in the dense cells persisted through two same-day pulses with damp soil and fully turgid green leaves — it's legginess/overcrowding collapse. Do NOT add extra pulses for droop alone; treat as drought only if leaves themselves shrivel, pale, or go limp AND soil is pale. Thinning/support is beyond the rig's actuators — a human hand is the only fix (flagged in the log).
7. **Check for silent check-in outages (added 2026-09-24).** At every check-in, note the date of the previous Log entry. If a scheduled check-in is missing, check `logs/checkin.log` — `claude -p` can fail silently (e.g. "OAuth session expired", 2026-09-19→09-24 outage: 18 failed runs, 6 days unwatered). The lamp cron is independent and keeps running. If failures are found, log the gap loudly and flag that a human must re-authenticate the claude CLI.

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

### 2026-08-26 19:22 — evening check-in (cron)
- Photo: germination advancing (day 2). Dense green mat in the front-left cell, sparser sprouts in 2-3 neighbors, and first tiny sprouts now visible in a couple of middle/right cells. No mold/pests/tipping.
- Soil: medium — germinated cells damp-ish, ungerminated cells medium with crumbly surface; not saturated, no alarming dry-down.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (8s of 60s daily cap used; water.py OK, pump off). Post-pulse photo shows fresh water sheeting across the lid channels toward the tray — bottom-feed path working.
- Jar level trend is the watch item: ~60% (8/24) → ~50% (8/25) → ~40-45% (8/26 midday) → looks ~30-35% after tonight's pulse. Still comfortably above the pump body, but at ~8s/day that's maybe 3-4 more days of pulses. Keep skipping aggressively when soil is dark; re-estimate level each check-in and invoke the EMERGENCY-reservoir protocol from standing order 2 when it nears the pump body.

### 2026-08-27 07:12 — morning check-in (cron)
- Photo: germination now in nearly all 12 cells (day 3). Front-left cells a dense green mat; middle/right cells have fresh yellow-green sprouts just emerging (yellow = newly surfaced, normal). No mold/pests/tipping.
- Soil: medium — not saturated, coir walls pale/dry-looking. Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (4s of 60s daily cap used; water.py OK, pump off). Post-pulse photo confirms fresh water on the lid channels — bottom-feed path working.
- Jar ~30%, pump body still submerged but margin is shrinking — estimate ~2-3 more days of 8s/day pulses. Continue aggressive skipping when soil is dark; check level against pump body every check-in per standing order 2.

### 2026-08-27 13:07 — midday check-in (cron, observe only)
- Photo: seedlings advancing in all cells (day 3). Left cells a tall dense green mat; middle/right sprouts have greened up and opened cotyledons (yesterday's yellow ones now green). No mold/pests/tipping.
- Soil: cell surfaces mostly dark/damp; coir walls pale as usual. No alarming dry-down since 07:12. Bright sunlight patch across the middle cells in the photo.
- Jar ~25-30% — pump body still submerged but the margin above it is getting thin. Reservoir remains the watch item; keep estimating against pump-body height each check-in.
- Lamp: on — correct for photoperiod. Watering: none (observe-only per standing order 2); 4s of 60s daily cap used. Evening 19:22 pulse planned unless soil looks dark. No changes to standing orders.

### 2026-08-27 19:22 — evening check-in (cron)
- Photo: seedlings healthy in all 12 cells (day 3). Left cells a tall dense mat; middle/right cotyledons open and green. No mold/pests/tipping.
- Soil: medium — damp patches but not saturated, coir walls pale as usual. Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (8s of 60s daily cap used; water.py OK, pump off). Post-pulse photo shows fresh water on the lid channels — bottom-feed path working.
- Jar ~20-25% after the pulse — pump body still submerged but margin above it is thin. At 8s/day, estimate ~1-2 more days of pulses before hitting the pump-body threshold. Continue aggressive skipping when soil is dark; check level against pump body every check-in and invoke the EMERGENCY-reservoir protocol (stop pumping) the moment the waterline nears the pump body.

### 2026-08-28 07:12 — morning check-in (cron)
- Photo: seedlings healthy in all 12 cells (day 4). Left cells a tall dense mat; middle/right cotyledons open and green. No mold/pests/tipping.
- Soil: medium-dark, not saturated. Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (4s of 60s daily cap used; water.py OK, pump off). Post-pulse photo shows fresh water on the lid channels — bottom-feed path working.
- Jar ~15-20% after the pulse — waterline is now only a little above the pump body. This is the last stretch: at 19:22, pulse ONLY if soil has visibly paled AND the waterline still clearly covers the pump body; otherwise skip. The moment the waterline is at/near the top of the pump body, stop pumping and switch to EMERGENCY: reservoir empty entries per standing order 2.

### 2026-08-28 13:07 — midday check-in (cron, observe only)
- Photo: seedlings vigorous in all 12 cells (day 4) — taller, cotyledons fully open and green, somewhat leggy (normal under this setup). No mold/pests/tipping. Tube in place over the lid.
- Soil: cell surfaces mostly dark/damp — morning 4s pulse holding; no paling since 07:12. Coir walls pale/dry as usual.
- Jar ~15%: waterline just above the pump body — thinnest margin yet. Roughly one day of pulses left at most.
- Lamp: on — correct for photoperiod. Watering: none (observe-only); 4s of 60s daily cap used.
- Plan for 19:22 per the 07:12 note: pulse ONLY if soil has visibly paled AND the waterline still clearly covers the pump body; otherwise skip and stretch the remaining water. Switch to EMERGENCY: reservoir empty the moment the waterline reaches the pump body.

### 2026-08-28 19:22 — evening check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 4) — dense green mats left, open green cotyledons middle/right, leggy but healthy. No mold/pests/tipping. Tube in place.
- Soil: cell surfaces still dark/damp — morning pulse holding, no visible paling since midday.
- Jar ~10-15%: waterline barely above the pump body — thinnest margin yet, at/near the stop threshold.
- Lamp: on — correct for photoperiod.
- Watering: SKIPPED per the decision rule (soil not paled; also conserving the last water). 4s of 60s daily cap used.
- Outlook: at most one more short pulse is defensible before the waterline reaches the pump body. Tomorrow 07:12: pulse (3-4s max) ONLY if soil has visibly paled AND the pump body is still clearly covered; otherwise skip and, once the waterline reaches the pump body, stop pumping and begin EMERGENCY: reservoir empty entries per standing order 2.

### 2026-08-29 07:12 — morning check-in (cron)
- EMERGENCY: reservoir empty (effectively). Zoomed jar photo (rpicam-still --roi) shows the waterline AT the top of the pump body — the standing-order stop threshold. Routine pulses are over; a human must refill the mason jar or the seedlings will dry out within days once the coir loses its moisture. No refill is expected, so this is logged for the record.
- Watering: SKIPPED (0s of daily cap used) — soil is still medium-dark/damp (no visible paling since last evening), and the waterline no longer clearly covers the pump. Standing order 2 rewritten as end-game: at most ONE final 3s pulse, only if soil visibly pales AND a zoomed photo shows water still clearly above the pump body; otherwise the pump never runs again.
- Photo: seedlings vigorous in all 12 cells (day 5) — dense leggy green mats left/right, open cotyledons everywhere, a few seed hulls still stuck to cotyledons (normal). No mold/pests/tipping. Tube in place over the lid.
- Lamp: on — correct for photoperiod.

### 2026-08-29 13:07 — midday check-in (cron, observe only)
- EMERGENCY: reservoir empty (ongoing). Zoomed jar photo confirms the waterline is still AT the top of the pump body — no refill has occurred. A human must refill the mason jar or the seedlings will die of drought within days; none is expected.
- Photo: seedlings vigorous in all 12 cells (day 5) — dense leggy mats, cotyledons open and green, a few seed hulls still attached (normal). No mold/pests/tipping. Tube in place over the lid.
- Soil: cell surfaces still mostly dark/damp — yesterday's moisture holding, no clear paling since 07:12.
- Lamp: on — correct for photoperiod. Watering: none (observe-only, and end-game rules in force; 0s of daily cap used).
- No changes to standing orders. The single remaining 3s pulse stays in reserve for visible soil paling while water still clearly covers the pump.

### 2026-08-29 19:22 — evening check-in (cron)
- EMERGENCY: reservoir empty (ongoing). Zoomed jar photo shows the waterline still AT the top of the pump body — no refill. A human must refill the mason jar or the seedlings will die of drought within days; none is expected.
- Photo: seedlings vigorous in all 12 cells (day 5) — dense leggy green mats, cotyledons open and green, a few seed hulls still attached. No mold/pests/tipping. Tube in place over the lid.
- Soil: cell surfaces still mostly dark/damp — no clear paling since midday, moisture holding.
- Lamp: on — correct for photoperiod. Watering: none (end-game rules; 0s of daily cap used). The single reserve 3s pulse remains unused — soil has not paled and the waterline no longer clearly covers the pump body.
- No changes to standing orders.

### 2026-08-30 07:12 — morning check-in (cron)
- EMERGENCY: reservoir empty (ongoing). Zoomed jar photo shows no waterline above the pump body — the jar is effectively empty, no refill has occurred. A human must refill the mason jar or the seedlings will die of drought within days; none is expected.
- Photo: seedlings vigorous in all 12 cells (day 6) — tall, leggy, cotyledons open and green, first true leaves emerging on some. No wilting, mold, pests, or tipping. Tube in place over the lid.
- Soil: cell surfaces medium — some dark damp patches, some drier crumbly spots with perlite showing; no dramatic paling and no wilting yet, but the dry-down has begun.
- Lamp: on — correct for photoperiod. Watering: none (end-game rules; 0s of daily cap used). Reserve pulse NOT used — condition (b) fails: water does not clearly cover the pump body, so running the pump risks a dry run. The pump should be considered retired unless a refill appears.
- No changes to standing orders.

### 2026-08-30 13:07 — midday check-in (cron, observe only)
- EMERGENCY: reservoir empty (ongoing). Zoomed jar photo shows no waterline above the pump body — jar not refilled. A human must refill the mason jar or the seedlings will die of drought within days; none is expected.
- Photo: seedlings vigorous in all 12 cells (day 6) — tall, leggy, cotyledons broad and green, no wilting yet. No mold/pests/tipping. Tube in place over the lid.
- Soil: mixed — some cells still dark/damp on the surface, others drier and crumbly with perlite showing. Dry-down continuing gradually since 07:12 but no wilt stress visible.
- Lamp: on — correct for photoperiod. Watering: none (observe-only, end-game rules; 0s of daily cap used, pump retired).
- No changes to standing orders.

### 2026-08-30 19:22 — evening check-in (cron)
- EMERGENCY: reservoir empty (ongoing). Zoomed jar photo shows no waterline above the pump body — jar not refilled. A human must refill the mason jar or the seedlings will die of drought within days; none is expected.
- Photo: seedlings vigorous in all 12 cells (day 6) — tall, leggy, cotyledons broad and green, first true leaves visible on several; no wilting. No mold/pests/tipping. Tube in place over the lid.
- Soil: mixed and drying — several cells still dark/damp on the surface, others crumbly with perlite showing; gradual dry-down continues since midday but no wilt stress yet.
- Lamp: on — correct for photoperiod.
- Watering: none (end-game rules; 0s of daily cap used, pump retired — no water clearly covers the pump body).
- No changes to standing orders.

### 2026-08-31 07:12 — morning check-in (cron)
- EMERGENCY: reservoir empty (ongoing). Zoomed jar photo shows the jar transparent with no waterline anywhere — no refill. A human must refill the mason jar or the seedlings will die of drought within days; none is expected.
- Photo: seedlings still vigorous in all 12 cells (day 7) — tall and leggy, cotyledons broad and green, now tall enough to partially block the camera's view of the jar. No wilting, mold, pests, or tipping. Tube in place over the lid.
- Soil: mixed and drying further — some dark damp patches remain, more cells crumbly/pale with perlite showing; coir walls very pale. No wilt stress yet, but the dry-down is advancing.
- Lamp: on — correct for photoperiod. Watering: none (end-game rules; 0s of daily cap used, pump retired).
- No changes to standing orders.

### 2026-08-31 13:07 — midday check-in (cron, observe only)
- EMERGENCY: reservoir empty (ongoing). Two zoomed jar photos confirm no refill — the dark mass in the jar is the pump body itself, blue background visible through the glass above it, no waterline anywhere. A human must refill the mason jar or the seedlings will die of drought within days; none is expected.
- Photo: seedlings vigorous in all 12 cells (day 7) — tall, leggy, cotyledons broad, turgid, and green; no wilting despite the advancing dry-down. No mold/pests/tipping. Tube in place over the lid.
- Soil: drying continues — mixed dark patches and pale crumbly surfaces with perlite showing; coir walls very pale. No wilt stress yet.
- Lamp: on — correct for photoperiod. Watering: none (observe-only; end-game rules, pump retired; 0s of daily cap used).
- No changes to standing orders.

### 2026-08-31 19:22 — evening check-in (cron)
- EMERGENCY: reservoir empty (ongoing). Zoomed jar photo shows the jar fully transparent — background visible straight through the glass, no waterline anywhere, only the pump body dark at the bottom. No refill. A human must refill the mason jar or the seedlings will die of drought within days; none is expected.
- Photo: seedlings still vigorous in all 12 cells (day 7) — tall, leggy, cotyledons broad, turgid, and green; no wilting despite two full days without water. No mold/pests/tipping. Tube in place over the lid.
- Soil: visible cell surfaces mostly dark with perlite showing; coir walls very pale. Dry-down continues gradually but no wilt stress yet.
- Lamp: on — correct for photoperiod. Watering: none (end-game rules; pump retired, 0s of daily cap used).
- No changes to standing orders.

### 2026-09-01 07:12 — morning check-in (cron)
- EMERGENCY: reservoir empty (ongoing). Zoomed jar photo shows the glass fully transparent with no waterline anywhere — no refill. A human must refill the mason jar or the seedlings will die of drought within days; none is expected.
- Photo: seedlings still vigorous in all 12 cells (day 8) — tall, leggy, cotyledons broad, turgid, and green; no wilting despite ~3 days without water. Seedlings now tall enough to partly block the camera's view of the jar. No mold/pests/tipping. Tube in place over the lid.
- Soil: visible surfaces mixed — dark patches with perlite showing in some cells, drier crumbly spots elsewhere; coir walls very pale. Dry-down continues but no wilt stress yet.
- Lamp: on — correct for photoperiod. Watering: none (end-game rules; pump retired, 0s of daily cap used).
- No changes to standing orders.

### 2026-09-01 13:07 — midday check-in (cron, observe only)
- EMERGENCY: reservoir empty (ongoing). Zoomed jar photo shows the glass fully transparent — blue background visible straight through, no waterline anywhere, only the pump body dark at the bottom. No refill. A human must refill the mason jar or the seedlings will die of drought within days; none is expected.
- Photo: seedlings still vigorous in all 12 cells (day 8) — tall, leggy, cotyledons broad, turgid, and green; no wilting despite ~3.5 days without water. No mold/pests/tipping. Tube in place over the lid.
- Soil: visible surfaces mixed — dark damp patches with perlite showing in some cells, drier crumbly spots elsewhere; coir walls very pale. Gradual dry-down continues, no wilt stress yet.
- Lamp: on — correct for photoperiod. Watering: none (observe-only; end-game rules, pump retired; 0s of daily cap used).
- No changes to standing orders.

### 2026-09-01 19:22 — evening check-in (cron) — JAR REFILLED, WATERING RESUMED
- The human refilled the mason jar: wide + zoomed photos show dark water filling the glass to near the neck with condensation inside — after three days of the jar being fully transparent/empty. Emergency over.
- Resume protocol: 3s verification pulse at 19:25 (water.py OK, 3s of 60s daily cap used; pump plug confirmed OFF after). Jar level held post-pulse — siphon self-limited as before. Standing order 2 rewritten: routine policy restored (4s pulses at 07:12 and 19:22 when soil isn't dark, 13:07 observe-only), with the end-game protocol to be reinstated when the waterline again nears the pump body.
- Photo: seedlings vigorous in all 12 cells (day 8) — tall, leggy, cotyledons broad and green, true leaves developing; no wilting despite ~4 days dry. No mold/pests/tipping. Tube in place over the lid.
- Soil: mixed — dark patches plus drier crumbly spots, coir walls very pale after the long dry-down; the pulse should begin rewetting via bottom-feed. Expect to pulse again at 07:12 unless surfaces look dark.
- Lamp: on — correct for photoperiod.

### 2026-09-02 07:12 — morning check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 9) — tall, leggy, cotyledons broad and green, true leaves developing; no wilting, mold, pests, or tipping. Tube in place over the lid.
- Jar: zoomed photo shows dark water still high in the glass — last night's refill held overnight, siphon losses negligible. Pump body well covered.
- Soil: mixed — dark damp patches plus drier crumbly spots with perlite showing; coir walls still pale from the 4-day dry-down. Rewetting continues.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (4s of 60s daily cap used; water.py OK, pump plug verified OFF after). Jar level held post-pulse.
- No changes to standing orders. Next: 13:07 observe-only; 19:22 pulse unless surfaces look dark.

### 2026-09-02 13:07 — midday check-in (cron, observe only)
- Photo: seedlings vigorous in all 12 cells (day 9) — tall, leggy, cotyledons broad, turgid, and green; no wilting, mold, pests, or tipping. Tube in place over the lid.
- Jar: zoomed photo shows dark water still high in the glass — refill holding, pump body well covered, siphon losses negligible.
- Soil: mixed — dark damp patches in most cells with some drier crumbly spots and perlite showing; coir walls still pale. Rewetting from the refill continues, no dry-down alarm.
- Lamp: on — correct for photoperiod.
- Watering: none (observe-only per standing order 2); 4s of 60s daily cap used. Evening 19:22 pulse planned unless surfaces look dark.
- No changes to standing orders.

### 2026-09-02 19:22 — evening check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 9) — tall, leggy, cotyledons broad and green, true leaves developing; no wilting, mold, pests, or tipping. Tube in place over the lid.
- Jar: zoomed photo shows dark water still high in the glass — refill holding well, pump body well covered.
- Soil: mixed — dark damp patches in the middle cells, drier crumbly spots with perlite showing elsewhere; coir walls still pale from the dry-down. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (8s of 60s daily cap used; water.py OK, pump plug verified OFF after). Post-pulse photo shows wet sheen on the lid behind the tray — bottom-feed path working. Jar level held.
- No changes to standing orders. Next: 07:12 pulse unless surfaces look dark.

### 2026-09-03 07:12 — morning check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 10) — tall, leggy, cotyledons broad and green, true leaves developing; no wilting, mold, pests, or tipping. Tube in place over the lid.
- Jar: zoomed photo shows dark water still high in the glass — refill holding, pump body well covered.
- Soil: mixed — dark damp patches in the cell centers, drier crumbly spots with perlite showing elsewhere; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (4s of 60s daily cap used; water.py OK, pump plug verified OFF after). Jar level held post-pulse.
- No changes to standing orders. Next: 13:07 observe-only; 19:22 pulse unless surfaces look dark.

### 2026-09-03 13:07 — midday check-in (cron, observe only)
- Photo: seedlings vigorous in all 12 cells (day 10) — tall, leggy, cotyledons broad, turgid, and green; true leaves developing; a couple of seed hulls still clinging to cotyledon tips (normal). No wilting, mold, pests, or tipping. Tube in place over the lid.
- Jar: zoomed photo (seedlings partly block the view) shows dark water still filling most of the glass, well above the pump body — refill holding, siphon losses negligible.
- Soil: visible surfaces damp-looking where not hidden by foliage; no dry-down alarm since the morning pulse.
- Lamp: on — correct for photoperiod.
- Watering: none (observe-only per standing order 2); 4s of 60s daily cap used. Evening 19:22 pulse planned unless surfaces look dark.
- No changes to standing orders.

### 2026-09-03 19:22 — evening check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 10) — tall, leggy, cotyledons broad, turgid, and green; true leaves developing; a couple of seed hulls still on cotyledon tips (normal). No wilting, mold, pests, or tipping. Tube in place over the lid.
- Jar: zoomed photo shows dark water still high in the glass — refill holding, pump body well covered.
- Soil: mixed — dark damp centers, drier crumbly spots with perlite showing; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (8s of 60s daily cap used; water.py OK, pump plug verified OFF after). Post-pulse photo shows wet sheen on the lid behind the tray — bottom-feed path working. Jar level held.
- No changes to standing orders. Next: 07:12 pulse unless surfaces look dark.

### 2026-09-04 07:12 — morning check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 11) — tall, leggy, cotyledons broad, turgid, and green; true leaves developing; a couple of seed hulls still on cotyledon tips (normal). No wilting, mold, pests, or tipping. Tube in place over the lid.
- Jar: dark water still high in the glass (foliage partly blocks the zoomed view, but level matches recent days) — refill holding, pump body well covered.
- Soil: mixed — dark damp centers, drier crumbly spots with perlite showing; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (4s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 13:07 observe-only; 19:22 pulse unless surfaces look dark.

### 2026-09-04 13:07 — midday check-in (cron, observe only)
- Photo: seedlings vigorous in all 12 cells (day 11) — tall, leggy, cotyledons broad, turgid, and green; true leaves developing; a seed hull still on one cotyledon tip (normal). No wilting, mold, pests, or tipping. Tube in place over the lid.
- Jar: zoomed photo shows dark water still filling most of the glass, well above the pump body — refill holding, siphon losses negligible.
- Soil: visible cell surfaces dark/damp where not hidden by foliage; no dry-down alarm since the morning pulse. Coir walls pale as usual.
- Lamp: on — correct for photoperiod.
- Watering: none (observe-only per standing order 2); 4s of 60s daily cap used. Evening 19:22 pulse planned unless surfaces look dark.
- No changes to standing orders.

### 2026-09-04 19:22 — evening check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 11) — tall, leggy, cotyledons broad, turgid, and green; true leaves developing; a seed hull still on one cotyledon tip (normal). No wilting, mold, pests, or tipping. Tube in place over the lid.
- Jar: zoomed photo shows dark water still filling most of the glass, well above the pump body — refill holding, siphon losses negligible.
- Soil: mixed — dark damp centers, drier crumbly spots with perlite showing; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (8s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 07:12 pulse unless surfaces look dark.

### 2026-09-05 07:12 — morning check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 12) — tall, leggy, cotyledons broad, turgid, and green; true leaves developing; one seed hull still on a cotyledon tip (normal). No wilting, mold, pests, or tipping. Tube in place over the lid.
- Jar: zoomed photo shows dark water still high in the glass — refill holding, pump body well covered, siphon losses negligible.
- Soil: mixed — dark damp centers, drier crumbly spots with perlite showing; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (4s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 13:07 observe-only; 19:22 pulse unless surfaces look dark.

### 2026-09-05 13:07 — midday check-in (cron, observe only)
- Photo: seedlings vigorous in all 12 cells (day 12) — tall, leggy, cotyledons broad, turgid, and green; true leaves developing; the seed hull still on one cotyledon tip (normal). No wilting, mold, pests, or tipping. Tube in place over the lid.
- Jar: zoomed photo shows dark water still high in the glass — refill holding, pump body well covered, siphon losses negligible.
- Soil: visible cell surfaces dark/damp where not hidden by foliage; no dry-down alarm since the morning pulse. Coir walls pale as usual.
- Lamp: on — correct for photoperiod.
- Watering: none (observe-only per standing order 2); 4s of 60s daily cap used. Evening 19:22 pulse planned unless surfaces look dark.
- No changes to standing orders.

### 2026-09-05 19:22 — evening check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 12) — tall, leggy, cotyledons broad, turgid, and green; true leaves developing. No wilting, mold, pests, or tipping. Tube in place beside the jar over the lid.
- Jar: zoomed photo shows dark water still high in the glass — refill holding, pump body well covered.
- Soil: mixed — dark damp centers with perlite showing, drier crumbly spots elsewhere; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (8s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 07:12 pulse unless surfaces look dark.

### 2026-09-06 13:07 — midday check-in (cron) — POWER OUTAGE RECOVERY
- The Pi rebooted ~11:26 (uptime 1:42 at 13:08); cron.log's last entries are yesterday's lamp-off, so today's 07:02 lamp-on AND the 07:12 check-in (with its morning pulse) never ran. Lamp found OFF at 13:07 → turned ON immediately; ~6h of photoperiod lost today.
- FIX: added `tools/lamp-sync.sh` + a crontab `@reboot` entry that sets the lamp to the correct photoperiod state ~60s after every boot, so a future outage can't leave the lamp wrong until the next check-in. (Script untested in-session — sandbox approval limits — but it only wraps the proven light.py; verify it fired in logs/cron.log after the next reboot.)
- Photo (retaken after lamp-on): seedlings vigorous in all 12 cells (day 13) — tall, leggy, cotyledons broad, turgid, green; true leaves developing. No wilting despite the missed morning pulse; no mold/pests/tipping. Tube in place over the lid.
- Jar: zoomed photo shows dark water still high in the glass — refill holding, pump body well covered.
- Soil: visible surfaces mostly dark/damp with perlite showing; some drier crumbly spots. No wilt stress.
- Watering: none — kept 13:07 observe-only per standing order 2 (soil mostly dark, plants turgid; 0s of daily cap used). Evening 19:22 pulse planned as usual and will cover the missed morning one.
- No changes to standing orders.

### 2026-09-06 19:22 — evening check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 13) — tall, leggy, cotyledons broad, turgid, and green; true leaves developing with fine hairs visible on the newest ones. No wilting, mold, pests, or tipping. Tube outlet in place beside the jar over the lid.
- Jar: zoomed photo shows dark water still high in the glass — refill holding, pump body well covered.
- Soil: mixed — dark damp centers with perlite showing, drier crumbly spots elsewhere; coir walls pale. Not uniformly dark → pulse warranted (only pulse today; morning one was lost to the power outage).
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (4s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 07:12 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-07 07:12 — morning check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 14) — tall, leggy, cotyledons broad, turgid, and green; true leaves developing with fine hairs. No wilting, mold, pests, or tipping. Tube outlet in place beside the jar over the lid.
- Jar: zoomed photo shows dark water still high in the glass (foliage partly blocks the lower view) — refill holding, pump body well covered.
- Soil: mixed — dark damp centers with perlite showing, drier crumbly spots and pale coir walls elsewhere. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (4s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 13:07 observe-only; 19:22 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-07 13:07 — midday check-in (cron, observe only)
- Photo: seedlings vigorous in all 12 cells (day 14) — tall, leggy, cotyledons broad, turgid, and green; true leaves developing with fine hairs clearly visible on the newest ones. No wilting, mold, pests, or tipping. Tube outlet in place beside the jar over the lid.
- Jar: zoomed photo shows the glass dark throughout the visible portion — water still high, refill holding, pump body well covered.
- Soil: visible cell surfaces dark/damp where not hidden by foliage; no dry-down alarm since the morning pulse. Coir walls pale as usual.
- Lamp: on — correct for photoperiod.
- Watering: none (observe-only per standing order 2); 4s of 60s daily cap used. Evening 19:22 pulse planned unless surfaces look dark.
- No changes to standing orders. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-07 19:22 — evening check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 14) — tall, leggy, cotyledons broad, turgid, and green; true leaves developing with fine hairs clearly visible. No wilting, mold, pests, or tipping. Tube outlet in place beside the jar over the lid.
- Jar: zoomed photo shows the glass dark throughout the visible portion — water still high, refill holding, pump body well covered.
- Soil: mixed — dark damp centers with crumbly drier patches and perlite showing; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (8s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 07:12 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-08 07:12 — morning check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 15) — tall, leggy, cotyledons broad, turgid, and green; true leaves growing with fine hairs clearly visible on the newest ones. No wilting, mold, pests, or tipping. Tube outlet in place beside the jar over the lid.
- Jar: zoomed photo shows the glass dark throughout the visible portion — water still high, refill holding, pump body well covered.
- Soil: mixed — dark damp centers, drier crumbly spots with perlite showing; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (4s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 13:07 observe-only; 19:22 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-08 13:07 — midday check-in (cron, observe only)
- Photo: seedlings vigorous in all 12 cells (day 15) — tall, leggy, cotyledons broad, turgid, and green; true leaves growing with fine hairs clearly visible; some stems showing pink coloration (brassica-like, normal). No wilting, mold, pests, or tipping. Tube outlet in place beside the jar over the lid.
- Jar: zoomed photo shows the glass dark throughout the visible body — water still high, refill holding, pump body well covered.
- Soil: visible cell surfaces dark/damp where not hidden by foliage; drier crumbly spots in a couple of front cells but no dry-down alarm since the morning pulse. Coir walls pale as usual.
- Lamp: on — correct for photoperiod.
- Watering: none (observe-only per standing order 2); 4s of 60s daily cap used. Evening 19:22 pulse planned unless surfaces look dark.
- No changes to standing orders. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-08 19:22 — evening check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 15) — tall, leggy, cotyledons broad, turgid, and green; true leaves growing with fine hairs clearly visible; pink stems on several (brassica-like, normal). No wilting, mold, pests, or tipping. Tube outlet in place beside the jar over the lid.
- Jar: zoomed photo shows the glass dark throughout the visible body (foliage blocks the lower half) — water still high, refill holding, pump body well covered.
- Soil: mixed — dark damp centers, drier crumbly spots with perlite showing; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (8s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 07:12 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-09 07:12 — morning check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 16) — tall, leggy, cotyledons broad, turgid, and green; true leaves growing with fine hairs clearly visible; pink stems on several (brassica-like, normal). No wilting, mold, pests, or tipping. Tube outlet in place beside the jar over the lid.
- Jar: zoomed photo shows the glass dark throughout the visible body — water still high, refill holding, pump body well covered.
- Soil: mixed — dark damp centers, drier crumbly spots with perlite showing; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (4s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 13:07 observe-only; 19:22 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-09 13:07 — midday check-in (cron, observe only)
- Photo: seedlings vigorous in all 12 cells (day 16) — tall, leggy, cotyledons broad, turgid, and green; true leaves growing with fine hairs clearly visible; pink stems on several (brassica-like, normal). No wilting, mold, pests, or tipping. Tube outlet in place beside the jar over the lid.
- Jar: zoomed photo shows the glass dark throughout the visible body (foliage blocks the lower half) — water still high, refill holding, pump body well covered.
- Soil: visible cell surfaces dark/damp where not hidden by foliage; a few drier crumbly spots with perlite showing; coir walls pale as usual. No dry-down alarm since the morning pulse.
- Lamp: on — correct for photoperiod.
- Watering: none (observe-only per standing order 2); 4s of 60s daily cap used. Evening 19:22 pulse planned unless surfaces look dark.
- No changes to standing orders. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-09 19:22 — evening check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 16) — tall, leggy, cotyledons broad, turgid, and green; true leaves growing with fine hairs clearly visible on the newest ones; pink stems on several (brassica-like, normal). No wilting, mold, pests, or tipping. Tube outlet in place beside the jar over the lid.
- Jar: zoomed photo shows the glass dark throughout the visible body (foliage blocks the lower half) — water still high, refill holding, pump body well covered.
- Soil: mixed — dark damp centers, drier crumbly spots with perlite showing; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (8s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 07:12 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-10 07:12 — morning check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 17) — tall, leggy, cotyledons broad, turgid, and green; true leaves growing with fine hairs clearly visible; pink stems on several (brassica-like, normal). No wilting, mold, pests, or tipping. Tube outlet in place beside the jar over the lid.
- Jar: zoomed photo shows the glass dark throughout the visible body — water still high, refill holding, pump body well covered.
- Soil: mixed — dark damp centers with granular texture showing, drier crumbly spots elsewhere; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (4s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 13:07 observe-only; 19:22 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-10 13:07 — midday check-in (cron, observe only)
- Photo: seedlings vigorous in all 12 cells (day 17) — tall, leggy, cotyledons broad, turgid, and green; true leaves growing with fine hairs clearly visible on the newest ones; pink stems on several (brassica-like, normal). No wilting, mold, pests, or tipping. Tube outlet in place beside the jar over the lid.
- Jar: zoomed photo shows the glass dark throughout the visible body with a meniscus highlight near the shoulder — water still high, refill holding, pump body well covered.
- Soil: visible cell surfaces dark/damp where not hidden by foliage; some drier crumbly spots with perlite showing; coir walls pale as usual. No dry-down alarm since the morning pulse.
- Lamp: on — correct for photoperiod.
- Watering: none (observe-only per standing order 2); 4s of 60s daily cap used. Evening 19:22 pulse planned unless surfaces look dark.
- No changes to standing orders. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-10 19:22 — evening check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 17) — tall, leggy, cotyledons broad, turgid, and green; true leaves growing with fine hairs clearly visible; pink stems on several (brassica-like, normal). No wilting, mold, pests, or tipping. Tube outlet in place beside the jar over the lid.
- Jar: zoomed photo shows the glass dark throughout the visible body — water still high, refill holding, pump body well covered.
- Soil: mixed — dark damp centers, drier crumbly spots with perlite showing; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (8s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 07:12 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-11 07:12 — morning check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 18) — tall, leggy, cotyledons broad, turgid, and green; true leaves growing with fine hairs clearly visible; pink stems on several (brassica-like, normal). No wilting, mold, pests, or tipping. Tube outlet in place beside the jar over the lid (confirmed in zoom).
- Jar: zoomed photo shows the glass dark throughout the visible body — water still high, refill holding, pump body well covered.
- Soil: mixed — dark damp centers, drier crumbly spots with perlite showing; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (4s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 13:07 observe-only; 19:22 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-11 13:07 — midday check-in (cron, observe only)
- Photo: seedlings vigorous in all 12 cells (day 18) — tall, leggy, cotyledons broad, turgid, and green; true leaves growing with fine hairs clearly visible; pink stems on several (brassica-like, normal). No wilting, mold, pests, or tipping. Tube outlet in place beside the jar over the lid (confirmed in zoom).
- Jar: zoomed photo shows the glass dark/murky through the visible body with the pump a dark mass at the bottom — water still present and covering the pump, refill holding. Foliage increasingly blocks the lower view.
- Soil: visible cell surfaces dark/damp where not hidden by foliage; some drier crumbly spots with perlite showing; coir walls pale as usual. No dry-down alarm since the morning pulse.
- Lamp: on — correct for photoperiod.
- Watering: none (observe-only per standing order 2); 4s of 60s daily cap used. Evening 19:22 pulse planned unless surfaces look dark.
- No changes to standing orders. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-11 19:22 — evening check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 18) — tall, leggy, cotyledons broad, turgid, and green; true leaves growing with fine hairs clearly visible; pink stems on several (brassica-like, normal). No wilting, mold, pests, or tipping. Tube outlet in place beside the jar over the lid (confirmed in zoom).
- Jar: zoomed photo shows the glass dark through the visible body — water still present and covering the pump, refill holding. Foliage blocks much of the lower view.
- Soil: mixed — dark damp centers, drier crumbly spots with perlite showing; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (8s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 07:12 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-12 07:12 — morning check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 19) — tall, leggy, cotyledons broad, turgid, and green; true leaves growing with fine hairs clearly visible; pink stems on several (brassica-like, normal). A few yellowing cotyledons in the middle cells (older cotyledons fading as true leaves take over — normal at this stage). No wilting, mold, pests, or tipping. Tube outlet in place beside the jar over the lid (confirmed in zoom).
- Jar: zoomed photo shows dark water through the visible glass body — refill holding, pump body covered.
- Soil: mixed — dark damp centers, drier crumbly spots with perlite showing; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (4s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 13:07 observe-only; 19:22 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-12 13:07 — midday check-in (cron, observe only)
- Photo: seedlings vigorous in all 12 cells (day 19) — tall, leggy, cotyledons broad, turgid, and green; true leaves growing with fine hairs visible; pink stems on several (brassica-like, normal). A few yellowing older cotyledons in the middle cells (normal as true leaves take over). No wilting, mold, pests, or tipping. Tube outlet in place beside the jar over the lid (confirmed in zoom).
- Jar: zoomed photo shows dark water through the visible glass body up near the neck — refill holding, pump body well covered.
- Soil: visible cell surfaces dark/damp in the centers where not hidden by foliage; some drier crumbly spots; coir walls pale as usual. No dry-down alarm since the morning pulse. Bright sunlight patch across the tray.
- Lamp: on — correct for photoperiod.
- Watering: none (observe-only per standing order 2); 4s of 60s daily cap used. Evening 19:22 pulse planned unless surfaces look dark.
- No changes to standing orders. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-12 19:22 — evening check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 19) — tall, leggy, cotyledons broad, turgid, and green; true leaves growing; pink stems on several (brassica-like, normal); a few yellowing older cotyledons in the middle cells (normal as true leaves take over). No wilting, mold, pests, or tipping. Strong low-angle sunlight/flare in the frame.
- Jar: zoomed photo (heavy backlight/flare) shows the tube outlet in place pointing down over the lid; jar body dark with pump cable visible — water present, level consistent with midday's near-neck reading, siphon losses negligible.
- Soil: mixed — dark damp centers, drier crumbly spots with perlite showing; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (8s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 07:12 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-13 07:12 — morning check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 20) — tall, leggy, cotyledons broad, turgid, and green; true leaves growing; pink stems on several (brassica-like, normal); a few yellowing older cotyledons (normal). No wilting, mold, pests, or tipping. Tube outlet in place beside the jar pointing down over the lid (confirmed in zoom).
- Jar: zoomed photo (strong sun flare) shows water still present — glass tinted with refraction through the lower body, waterline around the shoulder, pump cable submerged. Level looks somewhat lower than midweek but still well above the pump body. Keep watching the trend.
- Soil: mixed — dark damp centers, drier crumbly spots; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (4s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 13:07 observe-only; 19:22 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-13 13:07 — midday check-in (cron, observe only)
- Photo: seedlings vigorous in all 12 cells (day 20) — tall, leggy, cotyledons broad, turgid, and green; true leaves growing; pink stems on several (brassica-like, normal); a few yellowing older cotyledons (normal). No wilting, mold, pests, or tipping. Tube outlet in place beside the jar pointing down over the lid (confirmed in zoom).
- Jar: zoomed photo shows clear water filling the glass to around the shoulder, pump cable submerged — level well above the pump body, consistent with this morning's reading. Refill holding.
- Soil: mixed — dark damp centers in the left cells, middle/right cells browner and crumblier with coir walls pale; no wilt stress, no dry-down alarm since the morning pulse.
- Lamp: on — correct for photoperiod.
- Watering: none (observe-only per standing order 2); 4s of 60s daily cap used. Evening 19:22 pulse planned unless surfaces look dark.
- No changes to standing orders. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-13 19:22 — evening check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 20) — tall, leggy, cotyledons broad, turgid, and green; true leaves growing; pink stems on several (brassica-like, normal); a few yellowing older cotyledons (normal). No wilting, mold, pests, or tipping. Tube outlet in place beside the jar pointing down over the lid (confirmed in zoom).
- Jar: zoomed photo shows clear water filling the visible glass body well above the pump, level consistent with midday's shoulder-level reading — refill holding, siphon losses negligible.
- Soil: mixed — dark damp centers in the left cells, middle/right cells browner and crumblier with pale coir walls. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (8s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 07:12 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-14 07:12 — morning check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 21) — tall, leggy, cotyledons broad, turgid, and green; true leaves growing; pink stems on several (brassica-like, normal); a few yellowing older cotyledons (normal). No wilting, mold, pests, or tipping. Tube outlet in place beside the jar pointing down over the lid (confirmed in zoom).
- Jar: zoomed photo shows clear water filling the visible glass body well above the pump, pump cable submerged — level consistent with yesterday's shoulder-level reading, refill holding.
- Soil: mixed — dark damp centers, drier crumbly spots; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (4s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 13:07 observe-only; 19:22 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-14 13:07 — midday check-in (cron, observe only)
- Photo: seedlings vigorous in all 12 cells (day 21) — tall, leggy, cotyledons broad, turgid, and green; true leaves growing; pink stems on several (brassica-like, normal); a few yellowing older cotyledons (normal). No wilting, mold, pests, or tipping. Tube outlet in place beside the jar pointing down over the lid (confirmed in zoom).
- Jar: zoomed photo shows dark water filling the visible glass body with the waterline up near the neck, pump cable submerged — refill holding, pump body well covered.
- Soil: mixed — dark damp centers in the left cells, middle/right cells browner and crumblier with pale coir walls; no wilt stress, no dry-down alarm since the morning pulse.
- Lamp: on — correct for photoperiod.
- Watering: none (observe-only per standing order 2); 4s of 60s daily cap used. Evening 19:22 pulse planned unless surfaces look dark.
- No changes to standing orders. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-14 19:22 — evening check-in (cron)
- Photo: seedlings vigorous in all 12 cells (day 21) — tall, leggy, cotyledons broad, turgid, and green; true leaves growing; pink stems on several (brassica-like, normal); a few yellowing older cotyledons (normal). No wilting, mold, pests, or tipping. Tube outlet in place beside the jar pointing down over the lid (confirmed in zoom).
- Jar: zoomed photo shows dark water filling the glass to around the shoulder, pump cable submerged — refill holding, pump body well covered.
- Soil: mixed — dark damp centers in the left cells, middle/right cells browner and crumblier with pale coir walls. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (8s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 07:12 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-15 07:12 — morning check-in (cron)
- Photo: seedlings in all 12 cells (day 22) but noticeably DROOPIER than yesterday — several stems in the front-left and middle cells flopped over the pot edges/soil; true leaves still green, pink stems as usual, no mold/pests/tipping. Could be overnight water stress or worsening legginess — WATCH ITEM: reassess turgor at 13:07; if still flopped after the morning pulse wicks up, this is drought stress, not legginess.
- Jar: zoomed photo shows water still present — pump cable visible through tinted water in the lower body, level around the shoulder, consistent with recent days. Tube outlet in place over the lid.
- Soil: mixed — dark damp centers, drier crumbly spots with perlite showing; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (4s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 13:07 observe-only, with special attention to whether the droop recovers. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-15 13:07 — midday check-in (cron) — droop persists, one-time midday pulse
- Photo + close-up zoom: droop from this morning has NOT recovered ~6h after the 07:12 pulse — front-left cell stems splayed radially over the pot edge with kinks at the base; middle cells leaning. BUT leaves are still green, flat, and unshriveled, and soil centers look dark/damp — evidence is mixed between drought stress and leggy overcrowded stems mechanically collapsing (day 22, no thinning possible with my actuators). No mold/pests/tipping.
- Jar: zoomed photo shows tinted water around the shoulder, pump cable submerged, tube outlet in place pointing down over the lid — refill holding.
- Lamp: on — correct for photoperiod.
- Watering: deviated from observe-only ONCE — 4s pulse (8s of 60s daily cap used; water.py OK, pump plug verified OFF after). Rationale: morning entry's decision rule said persistent droop = treat as drought stress; jar is full, rails permitted, and the cost of an unnecessary pulse is far lower than 6 more dry hours if it is drought.
- Plan for 19:22: reassess. If droop improves → it was water stress, keep routine policy. If droop is unchanged with soil damp → conclude legginess/overcrowding (mechanical), stop extra pulses, and note that thinning/support is beyond my actuators — flag to the human in the journal. 13:07 remains observe-only as the default; this was a one-time exception.
- Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-15 19:22 — evening check-in (cron) — droop verdict: mechanical legginess, pulse SKIPPED
- Photo: day 22. Droop is UNCHANGED from midday — front-left stems still splayed radially over the pot edge, middle cells leaning — but leaves everywhere are green, flat, and turgid after ~12h and two pulses with damp soil centers. Verdict per the midday decision rule: mechanical legginess/overcrowding collapse, NOT drought. New standing order 6 records this so droop alone never triggers extra water again.
- FLAG TO HUMAN: the dense cells (especially front-left) need thinning and/or small supports; the stems are collapsing under their own crowded, leggy growth. This is beyond the rig's actuators — only a human hand can do it. Not an emergency: plants remain healthy and green.
- Jar: zoomed photo shows the waterline around the MID-BODY of the glass — a step down from the shoulder-level readings of recent days. Pump still well covered; keep tracking the trend each check-in.
- Soil: dark damp centers with drier crumbly spots; no mold/pests/tipping. Tube outlet in place over the lid.
- Lamp: on — correct for photoperiod.
- Watering: SKIPPED tonight's routine pulse — the midday exception already used today's full routine ration (8s of 60s cap), soil centers are damp, and the droop is not water stress. Routine policy resumes 07:12 tomorrow: pulse unless surfaces look dark.
- Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-16 07:12 — morning check-in (cron)
- Photo: day 23. Seedlings green and turgid in all 12 cells; true leaves growing, pink stems (brassica-like, normal). Droop unchanged — splayed/kinked stems in the dense front-left and middle cells per standing order 6 (mechanical legginess, no extra water). Thinning/support still needs a human hand. No wilting, mold, pests, or tipping.
- Jar: zoomed photo shows waterline around MID-BODY — consistent with last evening, pump still covered. Trend watch continues; end-game protocol reinstates when the line nears the pump body. Tube outlet in place pointing down over the lid.
- Soil: mixed — dark damp centers, drier crumbly patches with perlite showing in the middle cells; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (4s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 13:07 observe-only; 19:22 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-16 13:07 — midday check-in (cron, observe only)
- Photo: day 23. Seedlings green and turgid in all 12 cells — true leaves growing, pink stems (brassica-like, normal). Splayed/leggy stems in the dense cells unchanged per standing order 6 (mechanical, no extra water); thinning/support still needs a human hand. No wilting, mold, pests, or tipping.
- Jar: zoomed photo shows waterline around MID-BODY — consistent with this morning, pump cable submerged, pump covered. Trend watch continues. Tube outlet in place pointing down over the lid.
- Soil: visible cell surfaces dark/damp in the centers where not hidden by foliage; drier crumbly spots with perlite showing in the middle cells; coir walls pale as usual. No dry-down alarm since the morning pulse.
- Lamp: on — correct for photoperiod.
- Watering: none (observe-only per standing order 2); 4s of 60s daily cap used. Evening 19:22 pulse planned unless surfaces look dark.
- No changes to standing orders. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-16 19:22 — evening check-in (cron)
- Photo: day 23. Seedlings green and turgid in all 12 cells — true leaves growing, pink stems (brassica-like, normal). Splayed/leggy stems in the dense cells unchanged per standing order 6 (mechanical, no extra water); thinning/support still needs a human hand. No wilting, mold, pests, or tipping.
- Jar: zoomed photo shows water around MID-BODY of the glass — consistent with this morning and midday, pump cable submerged, pump covered. Tube outlet in place pointing down over the lid. Trend watch continues; end-game protocol reinstates when the line nears the pump body.
- Soil: mixed — dark damp centers (middle cells clearly dark), drier crumbly spots with perlite showing; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (8s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 07:12 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-17 07:12 — morning check-in (cron)
- Photo: day 24. Seedlings green and turgid in all 12 cells — true leaves growing, pink stems (brassica-like, normal). Splayed/leggy stems in the dense cells unchanged per standing order 6 (mechanical, no extra water); thinning/support still needs a human hand. No wilting, mold, pests, or tipping.
- Jar: zoomed photo shows tinted water through the visible glass body with the pump cable submerged — level consistent with recent mid-body readings, pump covered. Tube outlet in place pointing down over the lid. Trend watch continues.
- Soil: mixed — dark damp centers, drier crumbly spots with perlite showing; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (4s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 13:07 observe-only; 19:22 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-17 13:07 — midday check-in (cron, observe only)
- Photo: day 24. Seedlings green and turgid in all 12 cells — true leaves growing, pink stems (brassica-like, normal). Splayed/leggy stems in the dense cells unchanged per standing order 6 (mechanical, no extra water); thinning/support still needs a human hand. No wilting, mold, pests, or tipping.
- Jar: zoomed photo shows tinted water through the visible glass body, pump body and cable submerged — level consistent with recent mid-body readings, pump covered. Tube outlet in place beside the jar pointing down over the lid. Trend watch continues.
- Soil: visible cell surfaces dark/damp in the centers where not hidden by foliage; drier crumbly spots with perlite showing; coir walls pale as usual. No dry-down alarm since the morning pulse.
- Lamp: on — correct for photoperiod.
- Watering: none (observe-only per standing order 2); 4s of 60s daily cap used. Evening 19:22 pulse planned unless surfaces look dark.
- No changes to standing orders. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-17 19:22 — evening check-in (cron)
- Photo: day 24. Seedlings green and turgid in all 12 cells — true leaves growing, pink stems (brassica-like, normal). Splayed/leggy stems in the dense cells unchanged per standing order 6 (mechanical, no extra water); thinning/support still needs a human hand. No wilting, mold, pests, or tipping.
- Jar: zoomed photo shows tinted water through the glass with the pump cable submerged — level consistent with recent mid-body readings, pump covered. Tube outlet in place beside the jar pointing down over the lid. Trend watch continues; end-game protocol reinstates when the line nears the pump body.
- Soil: mixed — dark damp centers, drier crumbly spots with perlite showing; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (8s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 07:12 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-18 07:12 — morning check-in (cron)
- Photo: day 25. Seedlings green and turgid in all 12 cells — true leaves growing, pink stems (brassica-like, normal). Splayed/leggy stems in the dense cells unchanged per standing order 6 (mechanical, no extra water); thinning/support still needs a human hand. No wilting, mold, or tipping; one tiny insect-like speck on a lower leaf in the zoom — not clearly a pest, recheck at 13:07.
- Jar: zoomed photo shows tinted water through the glass body, pump cable submerged — level consistent with recent mid-body readings, pump covered. Tube outlet in place beside the jar pointing down over the lid. Trend watch continues.
- Soil: mixed — dark damp centers, drier crumbly spots with perlite showing; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (4s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 13:07 observe-only; 19:22 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-18 13:07 — midday check-in (cron, observe only)
- Photo: day 25. Seedlings green and turgid in all 12 cells — true leaves growing, pink stems (brassica-like, normal). Splayed/leggy stems in the dense cells unchanged per standing order 6 (mechanical, no extra water); thinning/support still needs a human hand. No wilting, mold, or tipping.
- Speck recheck (from 07:12): a single tiny dark speck again visible on a lower leaf at frame edge — no spread, no others found, leaves undamaged. Not treating as a pest yet; keep rechecking each check-in.
- Jar: zoomed photo shows the upper glass transparent and the lower body dark with tinted water, pump cable submerged — level around MID-BODY, consistent with recent days; pump covered. Tube outlet in place beside the jar pointing down over the lid. Trend watch continues.
- Soil: visible cell surfaces dark/damp in the centers where not hidden by foliage; drier crumbly spots with perlite showing; coir walls pale as usual. No dry-down alarm since the morning pulse.
- Lamp: on — correct for photoperiod.
- Watering: none (observe-only per standing order 2); 4s of 60s daily cap used. Evening 19:22 pulse planned unless surfaces look dark.
- No changes to standing orders. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-18 19:22 — evening check-in (cron)
- Photo: day 25. Seedlings green and turgid in all 12 cells — true leaves growing, pink stems (brassica-like, normal). Splayed/leggy stems in the dense cells unchanged per standing order 6 (mechanical, no extra water); thinning/support still needs a human hand. No wilting, mold, or tipping; midday's single dark speck not re-spotted this evening — keep rechecking.
- Jar: zoomed photo shows tinted water through the glass body, pump cable submerged — level consistent with recent mid-body readings, pump covered. Tube outlet in place beside the jar pointing down over the lid. Trend watch continues; end-game protocol reinstates when the line nears the pump body.
- Soil: mixed — dark damp centers, drier crumbly spots with perlite showing; coir walls pale. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (8s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 07:12 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-24 19:50 — check-in after 6-DAY OUTAGE (claude auth expired)
- OUTAGE: every cron check-in from 2026-09-19 through tonight's 19:22 failed — checkin.log shows 18× "Failed to authenticate: OAuth session expired and could not be refreshed". No journal entries, NO WATERING 9/19–9/24 (~6 days, ~12 missed pulses). Lamp cron was unaffected (runs light.py directly; Pi uptime 18 days, no reboot). This 19:50 session succeeded, so auth appears restored — VERIFY the 07:12 cron check-in actually logs tomorrow; if not, a human must re-authenticate the claude CLI. Added standing order 7 (detect silent check-in gaps).
- Photo: seedlings SURVIVED the dry week — green, turgid, true leaves growing in all cells (day 31). Middle cells sparser/leggier with splayed pink stems (standing order 6, mechanical); some pale/whitish cotyledons top-right worth watching. No wilting, mold, pests, or tipping. Thinning/support still needs a human hand.
- Jar: zoomed photo shows dark/tinted water through the visible glass body, tube outlet in place pointing down over the lid — level consistent with pre-outage mid-body readings, pump covered. The dry week cost no jar water.
- Soil: mixed — dark centers with drier crumbly spots and pale coir walls; not uniformly dark, and 6 days unwatered → pulse clearly warranted.
- Lamp: on at 19:50 — correct for photoperiod.
- Watering: 4s pulse (4s of 60s daily cap used; water.py OK, pump plug verified OFF after). Resuming routine policy per standing order 2 from tomorrow 07:12.

### 2026-09-25 07:12 — morning check-in (cron) — auth outage confirmed over
- CRON AUTH VERIFIED: this scheduled 07:12 check-in ran and logged — the claude CLI re-auth from 09-24 is holding, outage over. Previous log entry was yesterday 19:50, no gap (standing order 7 check passed).
- Photo: seedlings green and turgid in all 12 cells (day 32) — true leaves growing, leggy pink splayed stems in the middle cells unchanged per standing order 6 (mechanical; thinning/support still needs a human hand). Some pale/whitish cotyledons top-right, same as 09-24 — watching. No wilting, mold, pests, or tipping.
- Jar: zoomed photo shows waterline around MID-BODY with a clear meniscus below the tube coil, water tinted, pump cable submerged — consistent with pre-outage readings, pump covered. Tube outlet in place pointing down over the lid.
- Soil: mixed — dark damp centers, drier crumbly patches with pale coir walls. Not uniformly dark → pulse warranted.
- Lamp: on — correct for photoperiod.
- Watering: 4s pulse per standing order 2 (4s of 60s daily cap used; water.py OK, pump plug verified OFF after).
- No changes to standing orders. Next: 13:07 observe-only; 19:22 pulse unless surfaces look dark. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.

### 2026-09-25 13:07 — midday check-in (cron, observe only)
- Standing order 7 check: previous entry was this morning 07:12 — no gap, cron auth still holding.
- Photo: seedlings green and turgid in all 12 cells (day 32) — true leaves growing, leggy pink splayed stems in the middle cells unchanged per standing order 6 (mechanical; thinning/support still needs a human hand). Pale/whitish cotyledons top-right same as recent days — watching, no spread. No wilting, mold, pests, or tipping. Bright sunlight across the frame.
- Jar: zoomed photo shows tinted water through the visible glass body, pump cable submerged — level consistent with recent mid-body readings, pump covered. Tube outlet in place beside the jar pointing down over the lid.
- Soil: visible cell surfaces dark/damp in the centers where not hidden by foliage; drier crumbly spots with perlite showing; coir walls pale as usual. No dry-down alarm since the morning pulse.
- Lamp: on — correct for photoperiod.
- Watering: none (observe-only per standing order 2); 4s of 60s daily cap used. Evening 19:22 pulse planned unless surfaces look dark.
- No changes to standing orders. Still pending: verify lamp-sync.sh fires in logs/cron.log after the next reboot.
