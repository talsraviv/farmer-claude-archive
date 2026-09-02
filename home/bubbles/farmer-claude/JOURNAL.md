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
