#!/usr/bin/env bash
# Usage: ./reset_demo.sh [1|2|3]
# Resets the repo to the starting state for each pocket demo.

set -euo pipefail
cd "$(dirname "$0")"

DEMO="${1:-}"

case "$DEMO" in
  1)
    echo "→ Demo 1: Test-first on a new function"
    echo "  Resetting normalize.py to empty stub (no implementation)"
    git checkout HEAD -- data_utils/normalize.py
    rm -f tests/test_normalize.py
    echo "✓ Ready. Open data_utils/normalize.py and tests/ — no test file for normalize yet."
    echo "  Start Claude Code: claude"
    ;;
  2)
    echo "→ Demo 2: A passing test that lies"
    echo "  Resetting validate.py to buggy version + lying tests"
    git checkout HEAD -- data_utils/validate.py
    git checkout HEAD -- tests/test_validate.py
    echo "✓ Ready. Run: pytest tests/test_validate.py"
    echo "  All 3 tests pass — but do they actually test anything?"
    ;;
  3)
    echo "→ Demo 3: Edge cases for normalize_score"
    echo "  Resetting test_normalize.py to 4 basic tests"
    git checkout HEAD -- tests/test_normalize.py
    echo "✓ Ready. Run: pytest tests/test_normalize.py"
    echo "  Ask Claude: 'What edge cases am I missing for normalize_score?'"
    ;;
  *)
    echo "Usage: ./reset_demo.sh [1|2|3]"
    echo ""
    echo "  1 — Demo 1: Test-first on a new function (normalize_score)"
    echo "  2 — Demo 2: A passing test that lies (validate_reading)"
    echo "  3 — Demo 3: Edge cases for normalize_score"
    exit 1
    ;;
esac
