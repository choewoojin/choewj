summation1 = sum(5*i for i in range(1, 11))
# generator expression

print(summation1)

############################################

b = [2, 5, 7, 1]
q = len(b)

summation2 = sum(7*b[i] for i in range(0, q))
print(summation2)