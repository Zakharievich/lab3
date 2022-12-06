# Fagurel MK-20
# variant 1
# y = x^2 + cos(x) * e^(-2x)

import math
import pytest

def calc_x2(x):
    return [x**2]

def calc_cos(x):
    return [math.cos(x)]

def calc_e(x):
    return [(math.e)**(-2*x)]


def show_result(x2, cos, e):
    if (len(x2) > 0) and (len(cos) > 0) and (len(e) > 0):
        f = x2[0] + cos[0]*e[0]
        print('Rezult function:', f)
    else:
        print('Error calc function')


def main():
    x = float(input('Enter Х: '))
    res_x2 = calc_x2(x)
    res_cos = calc_cos(x)
    res_e = calc_e(x)
    show_result(res_x2, res_cos, res_e)

if __name__ == '__main__':
    main()
