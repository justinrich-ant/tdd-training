def normalize_score(value: float, min_val: float, max_val: float) -> float:
    """Return value's position on a 0-100 scale within [min_val, max_val]. Clamps to [0, 100]."""
    clamped = max(min_val, min(max_val, value))
    return (clamped - min_val) / (max_val - min_val) * 100
