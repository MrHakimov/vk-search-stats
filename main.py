from draw_utils import draw
from vk_utils import VKClient, VKService


def main():
    stats = VKClient(VKService()).search_stats_for_hours('круассаны', 24)
    draw(stats)


if __name__ == '__main__':
    main()
