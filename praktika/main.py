import numpy as np
import matplotlib.pyplot as plt


def first():
    x = np.arange(-2, 2, 0.1)
    y = x ** 3 - 6 * x ** 2 + 2
    plt.plot(x, y)
    plt.show()


def second():
    t = np.arange(0, 6 * np.pi, 0.5)
    a = 2
    L = 2
    x = a * (t - L * np.sin(t))
    y = a * (1 - L * np.cos(t))
    plt.plot(x, y)
    plt.show()


def third():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    h = 0.1
    x = np.arange(-5, 5, h)
    y = np.arange(-5, 5, h)
    a = 2
    b = 5
    x, y = np.meshgrid(x, y)
    z = a * x ** 2 - b * y ** 2
    ax.plot_surface(x, y, z)
    plt.show()


def main():
    first()
    second()
    third()


if __name__ == "__main__":
    main()
