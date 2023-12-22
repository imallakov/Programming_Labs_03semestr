import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def dydt(y, t):
    return -t * np.tan(y / 3)


def first():
    t = np.linspace(0, 5, 51)
    y0 = 1
    y = odeint(dydt, y0, t)
    y = np.array(y).flatten()
    plt.plot(t, y, '-sr', linewidth=3)
    plt.show()


def main():
    first()


main()
