import pytest

from vk_utils import VKService
from time_utils import current_time_in_seconds


@pytest.fixture
def vk_service():
    return VKService('http://localhost:5000/method/newsfeed.search')


@pytest.fixture
def current_time():
    return current_time_in_seconds()


@pytest.mark.server(
    url='/method/newsfeed.search',
    response={
        'response': {'items': [], 'count': 0, 'total_count': 0}
    },
    method='GET'
)
def test_empty_response(vk_service, current_time):
    assert vk_service.dates_in_period('empty_query', current_time, 12) == []


@pytest.mark.server(
    url='/method/newsfeed.search',
    response={
        'response': {
            'items': [
                {
                    'id': 63082,
                    'date': 1638666000
                }
            ],
            'count': 1000,
            'total_count': 740102
        }
    },
    method='GET'
)
def test_response_single_date(vk_service, current_time):
    assert vk_service.dates_in_period('single_data_query', current_time, 23) == [1638666000]


@pytest.mark.server(
    url='/method/newsfeed.search',
    response={
        'response': {
            'items': [
                {
                    'id': 63082,
                    'date': 1638666000
                },
                {
                    'id': 63083,
                    'date': 1638766000
                },
                {
                    'id': 63084,
                    'date': 1638866000
                },
                {
                    'id': 63085,
                    'date': 1638966000
                }
            ],
            'count': 1000,
            'total_count': 740102
        }
    },
    method='GET'
)
def test_response_multiple_dates(vk_service, current_time):
    assert vk_service.dates_in_period('single_data_query', current_time, 23) == [
        1638666000, 1638766000, 1638866000, 1638966000
    ]
