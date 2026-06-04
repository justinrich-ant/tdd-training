# DEMO 2 — these tests all pass. But do they actually say anything?
# Read each assertion carefully before trusting the green checkmarks.

from data_utils.validate import validate_reading


def test_valid_reading_passes():
    result = validate_reading(75.0, 0.0, 100.0)
    assert result["ok"] is not None  # too-weak: False is not None → always passes!


def test_out_of_range_fails():
    result = validate_reading(150.0, 0.0, 100.0)
    assert result["ok"] is not None  # too-weak: passes even when ok=False


def test_at_lower_bound_passes():
    result = validate_reading(0.0, 0.0, 100.0)
    assert result  # plain truthy — dict is always truthy
