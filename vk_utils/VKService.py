import os
import requests
import json

from time_utils import hours_to_seconds


class VKService:
    VK_ACCESS_TOKEN: str = os.environ.get('VK_ACCESS_TOKEN')
    VK_MAX_QUERIES_COUNT: int = int(os.environ.get('VK_MAX_QUERIES_COUNT', 200))  # default max
    VK_API_VERSION: str = os.environ.get('VK_API_VERSION', '5.131')  # the last one at the moment of writing this code

    QUERY_URL = f'{{base_url}}?access_token={VK_ACCESS_TOKEN}' \
                f'&q={{query}}&v={VK_API_VERSION}&count={VK_MAX_QUERIES_COUNT}&start_time={{start_time}}'

    def __init__(self, base_url: str = 'https://api.vk.com/method/newsfeed.search'):
        self.base_url = base_url

    def dates_in_period(self, search_query: str, current_time: int, hours: int) -> list[int]:
        start_time = current_time - hours_to_seconds(hours)
        result = requests.get(
            self.QUERY_URL.format(
                base_url=self.base_url, query=search_query, start_time=start_time
            )
        )
        json_result: dict = json.loads(result.text)

        return [
            int(item['date']) for item in json_result['response']['items']
        ]
