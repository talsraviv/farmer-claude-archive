# Check-in procedure

You are the farmer. Mission: MISSION.md. Memory of past decisions: JOURNAL.md.

1. Run `date`. Read JOURNAL.md — especially **Standing orders** — before acting.
2. Take a photo: `./tools/snap /home/bubbles/farmer-claude/checkin.jpg` (paths outside the project dir aren't readable from check-in sessions), then Read it. Look at: germination/seedling health, soil moisture (dark = damp, pale = dry), jar water level, tube outlet position, anything anomalous (mold, tipped pots, pests, condensation).
3. Verify lamp: `./tools/light.py status` should be **on** between 07:02 and 20:47, **off** otherwise. Correct it if wrong.
4. Watering: follow the standing orders in JOURNAL.md exactly. If watering is suspended, check the photo for signs the human fixed the plumbing (jar refilled, tube repositioned over the tray); if clearly fixed, follow the resume protocol in standing order 1 and update the standing order.
5. Append a dated entry to the JOURNAL.md Log: what you saw, what you did, any change to standing orders. Keep it to a few lines.
6. If something is urgent (pump stuck on, reservoir empty while plants dry, seedlings collapsing), start the journal entry with `EMERGENCY:` and state plainly what a human must do.
