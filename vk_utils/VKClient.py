from time_utils import current_time_in_seconds, hours_to_seconds

from .VKService import VKService


class VKClient:
    def __init__(self, vk_service: VKService):
        self.vk_service = vk_service

    def search_stats_for_hours(self, search_query: str, hours: int) -> list[int]:
        current_time = current_time_in_seconds()
        dates = sorted(self.vk_service.dates_in_period(search_query, current_time, hours))

        return [
            self.__values_in_hour(dates, current_time, hour)
            for hour in range(1, hours + 1)
        ]

    @staticmethod
    def __first_greater_or_equal(lst: list[int], x: int):
        if not lst:
            return 0

        lft = -1
        rgt = len(lst) - 1

        while rgt - lft > 1:
            mid = (lft + rgt) // 2

            if lst[mid] >= x:
                rgt = mid
            else:
                lft = mid

        if lst[rgt] < x:
            return len(lst)

        return rgt

    @staticmethod
    def __values_in_hour(dates: list[int], current_time: int, hour: int):
        left = current_time - hours_to_seconds(hour)
        right = current_time - hours_to_seconds(hour - 1)

        return VKClient.__first_greater_or_equal(dates, right + 1) - \
            VKClient.__first_greater_or_equal(dates, left)
