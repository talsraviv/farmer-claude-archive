#!/bin/sh
# Set the lamp to the correct state for the current time (photoperiod 07:02-20:47).
# Run from cron @reboot so a power outage can't leave the lamp in the wrong state.
sleep 60  # let network + Kasa plug come up after boot
HM=$(date +%H%M)
if [ "$HM" -ge 702 ] && [ "$HM" -lt 2047 ]; then
    /home/bubbles/farmer-claude/tools/light.py on
else
    /home/bubbles/farmer-claude/tools/light.py off
fi
