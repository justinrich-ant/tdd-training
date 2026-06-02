from flag_service.evaluate import is_user_in_rollout, evaluate


def test_zero_percent_excludes_all_users():
    for i in range(100):
        assert is_user_in_rollout(f"user-{i}", 0) is False


def test_hundred_percent_includes_all_users():
    for i in range(100):
        assert is_user_in_rollout(f"user-{i}", 100) is True, (
            f"user-{i} was excluded at 100% rollout"
        )


def test_same_user_is_deterministic():
    a = is_user_in_rollout("alice@example.com", 50)
    b = is_user_in_rollout("alice@example.com", 50)
    assert a == b


def test_disabled_flag_always_false():
    flag = {"enabled": False, "rollout_percent": 100}
    assert evaluate(flag, "anyone") is False
