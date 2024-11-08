# 함수의 기울기
# 어느 지점에서의 변화율을 측정
# 머신러닝, 알고리즘, 경사하강법등

from sympy import *

def derivative(f, x, h):
    a = (f(x + h) -f(x))/ ((x + h) - x)
    return a

def function(x):
    return x ** 2

slope1 = derivative(function, 2, 0.000001)

print(slope1)

############################################

y = symbols('y')
f = y**2

dx_f = diff(f)
print(dx_f)

