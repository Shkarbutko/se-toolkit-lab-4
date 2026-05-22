from app.routers.interactions import filter_by_max_item_id
from tests.unit.test_interactions import _make_log


def test_filter_returns_empty_list_when_no_interactions_match() -> None:
    interactions = [
        _make_log(1, 1, 10),
        _make_log(2, 1, 20),
    ]

    result = filter_by_max_item_id(
        interactions=interactions,
        max_item_id=5,
    )

    assert result == []


def test_filter_keeps_multiple_matching_interactions() -> None:
    interactions = [
        _make_log(1, 1, 1),
        _make_log(2, 1, 2),
        _make_log(3, 1, 10),
    ]

    result = filter_by_max_item_id(
        interactions=interactions,
        max_item_id=2,
    )

    assert len(result) == 2
