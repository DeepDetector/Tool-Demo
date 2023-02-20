import matplotlib.pyplot as plt


def FoldingLineGraph():
    y = [20, 390, 900, 1790, 2350, 3270]
    x = [2017, 2018, 2019, 2020, 2021, 2022]

    plt.plot(x, y, marker='o')
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()


if __name__ == '__main__':
    FoldingLineGraph()
