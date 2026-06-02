# Safety guard: a single prod deploy should not jump more than 25 percentage
# points. Staging and dev have no cap.


def can_bump(current_pct: int, target_pct: int, env: str) -> dict:
    """
    Returns {"ok": bool, "reason": str}.

    Rules:
      - target must be greater than current (no rollbacks via this API)
      - prod: max jump of 25 percentage points per deploy
      - staging / dev: no max jump
    """
    if target_pct <= current_pct:
        return {"ok": False, "reason": "target must exceed current rollout"}
    if env == "prod" and (target_pct - current_pct) >= 25:  # BUG: should be > 25
        return {"ok": False, "reason": f"jump of {target_pct - current_pct}pp exceeds 25pp prod limit"}
    return {"ok": True, "reason": ""}
