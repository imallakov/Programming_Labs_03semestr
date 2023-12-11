import numpy as np
import matplotlib.pyplot as plt


def first():
    x = np.arange(1, 3, 0.1)
    y = x ** 3 - 3 * x ** 2 + 3
    plt.plot(x, y)
    plt.show()


def second():
    t = np.arange(0, 6 * np.pi, 0.5)
    a = 1.25
    x = a * (t - np.sin(t))
    y = a * (1 - np.cos(t))
    plt.plot(x, y)
    plt.show()


def third():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    h = 0.1
    x = np.arange(-5, 5, h)
    y = np.arange(-5, 5, h)
    a = 2
    b = 7
    x, y = np.meshgrid(x, y)
    z = a * x ** 2 + b * y ** 2
    ax.plot_surface(x, y, z)
    plt.show()


def main():
    first()
    second()
    third()


if __name__ == "__main__":
    main()
