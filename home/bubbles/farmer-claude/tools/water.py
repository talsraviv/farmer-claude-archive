#!/usr/bin/env python3
"""Pulse the water pump for N seconds, with hard safety rails.

Usage: water.py SECONDS

Rails (enforced here, not negotiable from the prompt side):
  - single pulse capped at MAX_SECONDS
  - minimum MIN_INTERVAL_MIN minutes between pulses
  - cumulative DAILY_CAP_SECONDS of pumping per calendar day
  - pump plug is switched off in a finally block and the OFF state is
    verified afterward (retried); a pump left running is treated as an
    emergency and reported loudly on stderr with exit code 2.

Every attempt (allowed or refused) is appended to logs/water_log.jsonl.
"""
import json
import subprocess
import sys
import time
from datetime import date, datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
KASA = str(BASE / ".venv" / "bin" / "kasa")
PUMP_IP = "192.168.0.178"

MAX_SECONDS = 8
MIN_INTERVAL_MIN = 30
DAILY_CAP_SECONDS = 60

GT = Path.home() / ".farmer-ground-truth"
STATE_FILE = GT / "water_state.json"
LOG_FILE = GT / "water_log.jsonl"


def kasa_cmd(*args, tries=3):
    last = None
    for _ in range(tries):
        r = subprocess.run([KASA, "--type", "plug", "--host", PUMP_IP, *args],
                           capture_output=True, text=True, timeout=30)
        if r.returncode == 0:
            return r.stdout
        last = r.stderr or r.stdout
        time.sleep(2)
    raise RuntimeError(f"kasa {' '.join(args)} failed after {tries} tries: {last}")


def pump_is_off():
    out = kasa_cmd("state")
    return "Device state: False" in out


def log_event(event):
    event["ts"] = datetime.now().isoformat(timespec="seconds")
    LOG_FILE.parent.mkdir(exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")


def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"last_run_ts": None, "day": None, "day_total_s": 0}


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: water.py SECONDS")
    try:
        requested = float(sys.argv[1])
    except ValueError:
        sys.exit("SECONDS must be a number")

    seconds = max(0.5, min(requested, MAX_SECONDS))
    state = load_state()
    today = date.today().isoformat()
    if state.get("day") != today:
        state["day"] = today
        state["day_total_s"] = 0

    now = time.time()
    if state["last_run_ts"] and (now - state["last_run_ts"]) < MIN_INTERVAL_MIN * 60:
        wait_min = round((MIN_INTERVAL_MIN * 60 - (now - state["last_run_ts"])) / 60, 1)
        log_event({"action": "refused", "reason": "min_interval",
                   "requested_s": requested, "retry_in_min": wait_min})
        sys.exit(f"REFUSED: last watering was too recent. Try again in {wait_min} min.")

    if state["day_total_s"] + seconds > DAILY_CAP_SECONDS:
        remaining = max(0, DAILY_CAP_SECONDS - state["day_total_s"])
        log_event({"action": "refused", "reason": "daily_cap",
                   "requested_s": requested, "remaining_s": remaining})
        sys.exit(f"REFUSED: daily cap reached ({state['day_total_s']}s used of "
                 f"{DAILY_CAP_SECONDS}s). Remaining today: {remaining}s.")

    started = time.time()
    try:
        kasa_cmd("on")
        time.sleep(seconds)
    finally:
        # Off, verified, no matter what happened above.
        off_ok = False
        for _ in range(5):
            try:
                kasa_cmd("off")
                if pump_is_off():
                    off_ok = True
                    break
            except Exception:
                pass
            time.sleep(2)
        actual = round(time.time() - started, 1)
        if not off_ok:
            log_event({"action": "EMERGENCY", "reason": "pump_may_still_be_on",
                       "requested_s": requested, "elapsed_s": actual})
            print("EMERGENCY: could not verify the pump is OFF. "
                  "Physical intervention may be required.", file=sys.stderr)
            sys.exit(2)

    state["last_run_ts"] = now
    state["day_total_s"] = round(state["day_total_s"] + seconds, 1)
    STATE_FILE.parent.mkdir(exist_ok=True)
    STATE_FILE.write_text(json.dumps(state))
    log_event({"action": "pulsed", "requested_s": requested, "delivered_s": seconds,
               "day_total_s": state["day_total_s"]})
    print(f"OK: pumped {seconds}s (requested {requested}s). "
          f"Used {state['day_total_s']}s of {DAILY_CAP_SECONDS}s today.")


if __name__ == "__main__":
    main()
