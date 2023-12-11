import numpy as np
import matplotlib.pyplot as plt


def first():
    x = np.arange(-3, 1, 0.1)
    y = 3 * x ** 4 - 16 * x ** 3 + 2
    plt.plot(x, y)
    plt.show()


def second():
    t = np.arange(-6, 6, 0.2)
    a = 6
    x = (a * t ** 2) / (1 + t ** 2)
    y = (a * t ** 3) / (1 + t ** 2)
    plt.plot(x, y)
    plt.show()


def third():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    h = 0.1
    x = np.arange(-np.pi, np.pi, h)
    y = np.arange(-np.pi, np.pi, h)
    a = 3
    x, y = np.meshgrid(x, y)
    z = a * np.sin(x) * np.cos(y)
    ax.plot_surface(x, y, z)
    plt.show()


def main():
    first()
    second()
    third()


if __name__ == "__main__":
    main()
