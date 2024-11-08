from sympy import *
from sympy.plotting import plot3d

x, y = symbols('x y')

f1 = 2*x**3 + 3*y**3

dx_f = diff(f1, x)
dy_f = diff(f1, y)

print(dx_f)
print(dy_f)

plot3d(f1)

############################################

a, b = symbols('a b')

f2 = a**2

slope1 = (f2.subs(a ,a + b) - f2) / ((a + b) - a)

slope_2 = slope1.subs(a, 2)

result1 = limit(slope_2, b, 0)

print(result1)

############################################

q, w = symbols('q w')

f3 = q**2

slope2 = (f3.subs(q, q + w) - f3) / ((q + w) - q)

result2 = limit(slope2, w, 0)

print(result2)