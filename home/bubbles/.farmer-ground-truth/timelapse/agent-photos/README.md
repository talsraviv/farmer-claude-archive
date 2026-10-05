# `/home/bubbles/.farmer-ground-truth/timelapse/agent-photos/`

> **Archive note:** This file was not on the Raspberry Pi. The experimenter added it to the public archive to help you find your way.

**You are in:** copies of the photos that the agent took. **These photos show what the agent looked at when it made its decisions.**

## Where these photos came from

The agent saved its photos in its own folder. Each new photo with the same name replaced the old photo. Thus, the agent kept no history of its photos. A hidden job copied the agent's photos to this folder 8 minutes after each check-in: at 07:20, 13:15, and 19:30.

## How to read a file name

`agent_2026-09-15_1315_plants-zoom.jpg` means:

- `2026-09-15_1315`: the job copied the photo on Sep 15 at 13:15. The agent took it a few minutes before.
- `plants-zoom.jpg`: the name that the agent gave to the photo.

## The names that the agent used

| Name | Number | What the agent used it for |
|---|---|---|
| `checkin.jpg` | 93 | The main photo of each check-in |
| `jar-zoom.jpg` | 67 | A close view of the water jar |
| `jar.jpg` | 8 | A close view of the water jar |
| `postpulse.jpg` | 6 | A photo after a pump pulse |
| `checkin-post.jpg` | 4 | A photo after a pump pulse |
| `jarzoom.jpg` | 2 | A close view of the water jar |
| `checkin-after.jpg` | 1 | A photo after a pump pulse |
| `jar_zoom.jpg` | 1 | The first close view of the jar (Aug 29) |
| `jar-zoom2.jpg` | 1 | A second close view of the jar |
| `plants-zoom.jpg` | 1 | A close view of the plants that fell over (Sep 15) |

The agent made close views with a camera option (`--roi`) that nobody told it about. It found this option on Aug 29, when the water level in the jar became important.

## Notes

- **Duplicates removed.** If the agent did not take a new photo, the job copied the old photo again. On the Raspberry Pi, this folder had 807 more files. They were exact copies. The archive keeps one copy of each different photo.
- **Missing photos.** If the agent took two photos with the same name between two copies, the job copied only the last photo. The full session records contain each photo that the agent looked at.
- A few early copies have other times. The experimenter made them by hand on Aug 25.

---

**Go up:** [timelapse/](../README.md)
