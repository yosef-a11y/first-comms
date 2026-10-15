#!/bin/bash
# Install the personal skills kept in this repo into ~/.claude/skills.
#
# Cloud sessions run in an ephemeral container: ~/.claude/skills is wiped
# whenever the container is recycled, which happens mid-session as well as
# between sessions. The repo is therefore the source of truth and this hook
# restores the working copy. Editing the files under ~/.claude/skills is
# pointless on its own — the change has to come back here to survive.
#
# Idempotent: it simply overwrites, so running it repeatedly is safe.
set -euo pipefail

SRC="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}/.claude/skills"
DEST="$HOME/.claude/skills"

[ -d "$SRC" ] || { echo "session-start: no skills at $SRC, nothing to install"; exit 0; }

installed=0
for dir in "$SRC"/*/; do
  name="$(basename "$dir")"
  mkdir -p "$DEST/$name"
  cp -R "$dir." "$DEST/$name/"
  installed=$((installed + 1))
done

echo "session-start: installed $installed skill folder(s) into $DEST"
