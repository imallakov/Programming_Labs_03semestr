import numpy as np
import matplotlib.pyplot as plt


def first():
    x = np.arange(-1, 1, 0.1)
    y = np.exp(-x ** 2) + 2 * x ** 2
    plt.plot(x, y)
    plt.show()


def second():
    t = np.arange(-6, 6, 0.2)
    a = 6
    x = a * (t ** 2 - 1) / (t ** 2 + 1)
    y = a * t * (t ** 2 - 1) / (t ** 2 + 1)
    plt.plot(x, y)
    plt.show()


def third():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    h = 0.1
    x = np.arange(-2, 2, h)
    y = np.arange(-2 * np.pi, 2 * np.pi, h)
    a = 2
    x, y = np.meshgrid(x, y)
    z = np.exp(x) * np.cos(a * y)
    ax.plot_surface(x, y, z)
    plt.show()


def main():
    first()
    second()
    third()


if __name__ == "__main__":
    main()
