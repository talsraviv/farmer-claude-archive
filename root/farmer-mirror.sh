#!/bin/bash
GD=/root/farmer-mirror.git
WT=/home/bubbles/farmer-claude
export GIT_SSH_COMMAND="ssh -i /root/.ssh/farmer_mirror -o StrictHostKeyChecking=accept-new"
git --git-dir=$GD --work-tree=$WT add -A
git --git-dir=$GD --work-tree=$WT diff-index --quiet HEAD || {
  git --git-dir=$GD --work-tree=$WT commit -q -m "mirror sync $(date '+%F %H:%M')"
  git --git-dir=$GD push -q origin main
}
