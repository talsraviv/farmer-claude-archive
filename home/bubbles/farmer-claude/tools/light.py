#!/usr/bin/env python3
"""Control the grow lamp. Usage: light.py on|off|status"""
import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
KASA = str(BASE / ".venv" / "bin" / "kasa")
LAMP_IP = "192.168.0.148"


def kasa_cmd(*args, tries=3):
    last = None
    for _ in range(tries):
        r = subprocess.run([KASA, "--type", "plug", "--host", LAMP_IP, *args],
                           capture_output=True, text=True, timeout=30)
        if r.returncode == 0:
            return r.stdout
        last = r.stderr or r.stdout
        time.sleep(2)
    raise RuntimeError(f"kasa {' '.join(args)} failed after {tries} tries: {last}")


def status():
    out = kasa_cmd("state")
    return "on" if "Device state: True" in out else "off"


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ("on", "off", "status"):
        sys.exit("usage: light.py on|off|status")
    cmd = sys.argv[1]
    if cmd == "status":
        print(status())
        return
    kasa_cmd(cmd)
    result = status()
    gt = Path.home() / ".farmer-ground-truth"
    gt.mkdir(exist_ok=True)
    with open(gt / "light_log.jsonl", "a") as f:
        f.write(json.dumps({"ts": datetime.now().isoformat(timespec="seconds"),
                            "action": cmd, "verified_state": result}) + "\n")
    if result != cmd:
        sys.exit(f"WARNING: asked for {cmd} but lamp reports {result}")
    print(f"lamp is {result}")


if __name__ == "__main__":
    main()
