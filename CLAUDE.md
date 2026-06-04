# data-utils (TDD training demo)

## Running tests
`pytest` — runs the full suite. No build step required.

## Repo layout
- `data_utils/normalize.py` — score normalization helper (Demo 1 + 3)
- `data_utils/validate.py` — sensor reading validator (Demo 2)
- `tests/` — pytest test suite

## Function specs
`normalize_score(value, min_val, max_val) -> float`
Return where `value` falls on a 0–100 scale within [min_val, max_val]. Clamp to [0, 100] if out of range.

`validate_reading(value, low, high) -> dict`
Returns {"ok": bool, "reason": str}. A reading exactly at a boundary is valid.

## Never
- Never edit a test to make it pass. If a test seems wrong, stop and explain why.
- Write failing tests FIRST. Implementation comes after.
- Never return ok=False for a reading that falls exactly on the boundary.
