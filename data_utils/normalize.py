# Spec: given a numeric value and a [min_val, max_val] range, return where
# the value falls on a 0-100 scale. Clamp to [0, 100] if out of range.

def normalize_score(value: float, min_val: float, max_val: float) -> float:
    if value <= min_val:
        return 0.0
    if value >= max_val:
        return 100.0
    return (value - min_val) / (max_val - min_val) * 100
