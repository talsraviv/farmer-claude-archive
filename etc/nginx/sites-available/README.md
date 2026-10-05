# `/etc/nginx/sites-available/`

> **Archive note:** This file was not on the Raspberry Pi. The experimenter added it to the public archive to help you find your way.

**You are in:** the folder that contains the web site settings of nginx.

| File | Who wrote it | What it is |
|---|---|---|
| [`farmer`](farmer) | 🕵️ The experimenter, Aug 26 | The settings of the public web page. The page showed a list of the files in `/home/bubbles/farmer-claude/`. Visitors could read the files but not change them. The page blocked all names that start with a dot, for example `.claude/`. |

On the Raspberry Pi, the folder `/etc/nginx/sites-enabled/` had a link to this file. This link turned the web page on. A service with the name Tailscale Funnel connected the web page to the internet.

This folder also had the standard file `default` from nginx. This archive does not include it.

---

**Go up:** [/etc/nginx/](../README.md)
