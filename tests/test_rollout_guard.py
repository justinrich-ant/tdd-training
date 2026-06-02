# DEMO 2 — these tests all pass. But do they actually say anything?
# Read each assertion carefully before trusting the green checkmarks.

from flag_service.rollout_guard import can_bump


def test_allows_small_prod_bump():
    result = can_bump(0, 10, "prod")
    assert result["ok"] is not None  # too-weak: checks shape, not value


def test_blocks_huge_prod_jump():
    result = can_bump(0, 80, "prod")
    assert result["ok"] is not None  # too-weak: False is not None → always passes!


def test_staging_allows_large_bumps():
    result = can_bump(0, 100, "staging")
    assert result  # plain truthy check — dict is always truthy
