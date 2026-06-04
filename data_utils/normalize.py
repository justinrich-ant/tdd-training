# Spec: given a numeric value and a [min_val, max_val] range, return where
# the value falls on a 0-100 scale. Clamp to [0, 100] if out of range.

def normalize_score(value: float, min_val: float, max_val: float) -> float:
    ...
