import numpy as np
import matplotlib.pyplot as plt


def first():
    x = np.arange(-1, 3, 0.1)
    y = (4 * x - 1) / (x ** 2 + 3)
    plt.plot(x, y)
    plt.show()


def second():
    t = np.arange(0, 10 * np.pi, 0.2)
    a = 5
    b = 2
    lamb = 1
    x = (b - a) * np.cos(t) - lamb * a * np.cos((b - a) * t / a)
    y = (b - a) * np.sin(t) - lamb * a * np.sin((b - a) * t / a)
    plt.plot(x, y)
    plt.show()


def third():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    h = 0.1
    x = np.arange(-5, 5, h)
    y = np.arange(-5, 5, h)
    a = 2
    b = 1
    x, y = np.meshgrid(x, y)
    z = -(abs(a * x) + abs(b * y))
    ax.plot_surface(x, y, z)
    plt.show()


def main():
    first()
    second()
    third()


main()
