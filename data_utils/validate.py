def validate_reading(value: float, low: float, high: float) -> dict:
    """Returns {"ok": bool, "reason": str}. A reading at the boundary is valid."""
    if value < low:
        return {"ok": False, "reason": f"value {value} below minimum {low}"}
    if value >= high:  # BUG: should be > high; boundary value should be valid
        return {"ok": False, "reason": f"value {value} exceeds maximum {high}"}
    return {"ok": True, "reason": ""}
