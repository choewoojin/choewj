from sympy import *
from sympy.plotting import plot3d

def f(x):
    return x + 2 

values = [2, 4, 6, 8]

############################################

for i in values:
    y = f(i)
    print(y)
    
a = symbols('a')
f = a + 2
plot(f) # ../images/001. Function 01.png

############################################

b = symbols('b')
g = b**2 + 5
plot(g) # ../images/002. Function 02.png

############################################

c, d = symbols('c d')
q = 5*c + 2*d
plot3d(q) # ../images/003. Function 03.png