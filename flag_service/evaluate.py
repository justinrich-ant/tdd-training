# Deterministic per-user bucketing. Same user + same flag = same answer,
# every time, across every server. No state, no DB round-trip.


def _simple_hash(s: str) -> int:
    h = 5381
    for c in s:
        h = ((h << 5) + h + ord(c)) & 0xFFFFFFFF
    return abs(h)


def is_user_in_rollout(user_id: str, rollout_percent: int) -> bool:
    if rollout_percent <= 0:
        return False
    if rollout_percent >= 100:
        return True
    return (_simple_hash(user_id) % 100) < rollout_percent


def evaluate(flag: dict, user_id: str) -> bool:
    if not flag or not flag.get("enabled"):
        return False
    return is_user_in_rollout(user_id, flag["rollout_percent"])
