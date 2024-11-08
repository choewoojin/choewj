from sympy import *

x = symbols('x')
f1 = 1 / x
result1 = limit(f1, x, oo)

print(result1)
plot(f1)

############################################

n = symbols('n')
f2 = (1 +(1/n))**n
result2 = limit(f2, n, oo)

print(result2)
print(result2.evalf())

plot(f2)