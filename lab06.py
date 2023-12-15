from sympy import *
import numpy as np
import matplotlib.pyplot as plt


def first():
    # Определение переменной
    x = symbols('x')
    # Определение функции
    f_x = x ** 4 / (1 + x) ** 3
    # Нахождение области определения
    denominator_eq = 1 + x
    domain = solveset(denominator_eq, x)
    print("Область определения:", domain)
    discontinuity_points = solve(1 + x, x)
    print("Точки разрыва:", discontinuity_points)
    for point in discontinuity_points:
        limit_right = limit(f_x, x, point, dir='+')
        limit_left = limit(f_x, x, point, dir='-')

        # Определение типа разрыва
        if limit_right != limit_left:
            print(f"Разрыв первого рода в точке {point}")
        elif limit_right == oo or limit_left == -oo:
            print(f"Разрыв второго рода в точке {point}")
        else:
            print(f"Разрыв третьего рода в точке {point}")


def main():
    first()


main()
