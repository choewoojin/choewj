from sympy import *

x, y = symbols('x y')

summation = Sum(5*x, (x, 1, y))

result = summation.subs(y, 10)

print(result.doit())

# sympy -> lazy evaluation