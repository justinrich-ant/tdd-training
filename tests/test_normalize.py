from data_utils.normalize import normalize_score


def test_min_value_returns_zero():
    assert normalize_score(0, 0, 100) == 0.0


def test_max_value_returns_hundred():
    assert normalize_score(100, 0, 100) == 100.0


def test_midpoint_returns_fifty():
    assert normalize_score(50, 0, 100) == 50.0


def test_value_below_min_clamps_to_zero():
    assert normalize_score(-10, 0, 100) == 0.0
