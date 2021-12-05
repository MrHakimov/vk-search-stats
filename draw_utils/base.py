import matplotlib.pyplot as plt


def draw(stats: list[int]):
    plt.plot([i for i in range(1, len(stats) + 1)], stats)
    plt.xlabel('Hours')
    plt.ylabel('Search queries\' quantity')
    plt.show()
