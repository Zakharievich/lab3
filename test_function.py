# Fagurel MK-20
# variant 1
# y = x^2 + cos(x) * e^(-2x)

import math
import pytest

#--- Test x2 --------------
def test_x2_null():
   res = calc_x2(0)
   assert len(res) == 1
   assert res == [0.0]

def test_x2_positive():
   res = calc_x2(10)
   assert len(res) == 1
   assert res == [100.0]

def test_x2_negative():
   res = calc_x2(-10)
   assert len(res) == 1
   assert res == [100.0]
#-------------------------

#--- Test cos ------------
def test_cos_null():
   res = calc_cos(0)
   assert len(res) == 1
   assert res == [1.0]

def test_cos_less():
   res = calc_cos(3.14)
   assert len(res) == 1
   assert res <= [0.0]

def test_cos_more():
   res = calc_cos(1000)
   assert len(res) == 1
   assert res >= [0.5]
#-------------------------

#--- Test exp ------------
def test_e_null():
   res = calc_e(0)
   assert len(res) == 1
   assert res == [1.0]

def test_e_arguments():
    try:
        res = calc_e("")
    except TypeError as err:
        pass
    else:
        print("test_e_arguments: Invalid argument is not caught")
        assert False

def test_e_more_error():
    try:
        res = calc_e(-700)
    except OverflowError as err:
        pass
    else:
        print("test_e_more_error: Result too large")
        assert False
#-------------------------

#--- Test function ------------
def test_func_type_false():
    res = main(calc_x2(0), calc_cos(0), calc_e(0))
    assert type(res) != str

def test_func_type_true():
    res = main(calc_x2(700), calc_cos(700), calc_e(700))
    assert type(res) == float

def test_func_error():
    try:
        res = main(calc_x2(-700), calc_cos(-700), calc_e(-700))
    except OverflowError as err:
        pass
    else:
        print("test_func_error: Result too large")
        assert False
#-------------------------

def calc_x2(x):
    return [x**2]

def calc_cos(x):
    return [math.cos(x)]

def calc_e(x):
    return [(math.e)**(-2*x)]


def main(x2, cos, e):
    if (len(x2) > 0) and (len(cos) > 0) and (len(e) > 0):
        f = x2[0] + cos[0]*e[0]
        return f
    else:
        return 'Error calc function'