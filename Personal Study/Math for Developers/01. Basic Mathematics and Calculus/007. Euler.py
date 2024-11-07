from math import exp

p = 3000
r = 0.30
t = 0.5
n = 100

x = p * (1 + (r/n))**(n * t)

print(x)

############################################

y = p * exp(r*t)

print(y)