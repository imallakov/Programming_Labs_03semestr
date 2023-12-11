import numpy as np
import matplotlib.pyplot as plt


def first():
    x = np.arange(0, 3, 0.1)
    y = 2 * x ** 3 - 15 * x ** 2 + 24 * x + 5
    plt.plot(x, y)
    plt.show()


def second():
    t = np.arange(0, 10 * np.pi, 0.1)
    a = -1
    b = 3
    x = a * t - b * np.sin(t)
    y = a - b * np.cos(t)
    plt.plot(x, y)
    plt.show()


def third():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    h = 0.1
    x = np.arange(-5, 5, h)
    y = np.arange(-2, 2, h)
    a = 1.5
    b = 0.5
    x, y = np.meshgrid(x, y)
    z = np.sin(a * x) + b * y ** 2
    ax.plot_surface(x, y, z)
    plt.show()


def main():
    first()
    second()
    third()


if __name__ == "__main__":
    main()
