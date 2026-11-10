#!/bin/sh
# Shared-index commit guard (pre-commit).
#
# Several agents work in this one checkout and share one Git index. A plain
# `git commit` (or -a, -i, --amend) commits everything anyone has staged, which
# once swept another agent's work into an unrelated commit (ba01d98).
#
# This guard allows only pathspec commits:   git commit -m "msg" -- <path>...
# For those, Git runs pre-commit on a temporary index (.git/next-index-*.lock)
# holding only the named paths. Every other form runs on the shared index or a
# whole-index lock and is refused.
#
# Deliberate whole-index commit (merge resolution, Le's manual commit):
#   SHARED_INDEX_OK=1 git commit ...
# Bypassing the hook with --no-verify is not allowed by project rules.

if [ "${SHARED_INDEX_OK:-0}" = "1" ]; then
  exit 0
fi

case "$(basename "${GIT_INDEX_FILE:-.git/index}")" in
  next-index-*.lock)
    exit 0
    ;;
esac

staged=$(git diff --cached --name-only 2>/dev/null)
{
  echo "pre-commit: refused. Several agents share this checkout's Git index."
  echo "Commit only your own files, by path:"
  echo "    git commit -m \"message\" -- <path> [<path> ...]"
  echo "(-a, -i and --amend also commit other agents' work and are refused.)"
  echo "For a deliberate whole-index commit: SHARED_INDEX_OK=1 git commit ..."
  if [ -n "$staged" ]; then
    echo "Currently staged in the shared index (may include other agents' work):"
    echo "$staged" | sed 's/^/    /' | head -20
  fi
} >&2
exit 1
