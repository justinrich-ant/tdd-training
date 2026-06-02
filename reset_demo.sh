#!/usr/bin/env bash
# Usage: ./reset_demo.sh [1|2|3]
# Resets the repo to the starting state for each pocket demo.

set -euo pipefail
cd "$(dirname "$0")"

DEMO="${1:-}"

case "$DEMO" in
  1)
    echo "→ Demo 1: Test-first on a new function"
    echo "  Resetting metrics.py to empty stub (no implementation)"
    git checkout HEAD -- flag_service/metrics.py
    rm -f tests/test_metrics.py
    echo "✓ Ready. Open flag_service/metrics.py and tests/ — no test file for metrics yet."
    echo "  Start Claude Code: claude"
    ;;
  2)
    echo "→ Demo 2: A passing test that lies"
    echo "  Resetting rollout_guard.py to buggy version + lying tests"
    git checkout HEAD -- flag_service/rollout_guard.py
    git checkout HEAD -- tests/test_rollout_guard.py
    echo "✓ Ready. Run: pytest tests/test_rollout_guard.py"
    echo "  All 3 tests pass — but do they actually test anything?"
    ;;
  3)
    echo "→ Demo 3: Edge cases for the function we just tested"
    echo "  Stripping test_evaluate.py down to 4 basic tests"
    git checkout HEAD -- tests/test_evaluate.py
    echo "✓ Ready. Run: pytest tests/test_evaluate.py"
    echo "  Ask Claude: 'What edge cases am I missing for is_user_in_rollout?'"
    ;;
  *)
    echo "Usage: ./reset_demo.sh [1|2|3]"
    echo ""
    echo "  1 — Demo 1: Test-first on a new function (rollout_reach)"
    echo "  2 — Demo 2: A passing test that lies (can_bump)"
    echo "  3 — Demo 3: Edge cases for is_user_in_rollout"
    exit 1
    ;;
esac
