import numpy as np
import matplotlib.pyplot as plt


def first():
    fig, axs = plt.subplots(2)
    x = np.arange(0, 1, 0.1)
    y = x * np.exp(-2*x**2)
    axs[0].plot(x, y)
    t = np.arange(0, 2 * np.pi, 0.1)
    a = 1
    b = 2.5
    x = (b - a) * np.cos(t) - a * np.cos((b - a) * t / a)
    y = (b - a) * np.sin(t) - a * np.sin((b - a) * t / a)
    axs[1].plot(x, y)
    plt.show()


def graph_3d():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    h = 0.1
    x = np.arange(-5, 5, h)
    y = np.arange(-5, 5, h)
    a = 0.1
    x, y = np.meshgrid(x, y)
    z = np.exp(-a*(x**2+y**2))
    ax.plot_surface(x, y, z)
    plt.show()


def main():
    first()
    graph_3d()


if __name__ == "__main__":
    main()
