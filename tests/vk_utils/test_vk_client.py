import pytest

from unittest.mock import Mock

from vk_utils import VKClient
from time_utils import current_time_in_seconds, hours_to_seconds


@pytest.fixture
def vk_service():
    return Mock()


@pytest.fixture
def current_time():
    return current_time_in_seconds()


def test_empty_response(vk_service):
    vk_service.dates_in_period.return_value = []
    stats = VKClient(vk_service).search_stats_for_hours('empty_response', 5)

    assert len(stats) == 5
    assert stats == [0, 0, 0, 0, 0]


def test_response_single_date(vk_service, current_time):
    for i in range(5):
        vk_service.dates_in_period.return_value = [current_time - hours_to_seconds(0.5 + i)]
        stats = VKClient(vk_service).search_stats_for_hours('single_response', 4)

        assert len(stats) == 4
        assert stats == [j == i for j in range(4)]


def test_response_multiple_dates(vk_service, current_time):
    vk_service.dates_in_period.return_value = [
        current_time - hours_to_seconds(0.5),
        current_time - hours_to_seconds(0.6),
        current_time - hours_to_seconds(0.7),
        current_time - hours_to_seconds(1.1),
        current_time - hours_to_seconds(1.3),
        current_time - hours_to_seconds(2.9),
    ]
    stats = VKClient(vk_service).search_stats_for_hours('single_response', 3)

    assert len(stats) == 3
    assert stats == [3, 2, 1]
