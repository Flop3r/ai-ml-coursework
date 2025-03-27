import numpy as np
from decimal import Decimal, getcontext

getcontext().prec = 100

M = np.array([[Decimal('2625'), Decimal('365')],
              [Decimal('365'), Decimal('8')]])

A = np.array([[Decimal('22685')],
              [Decimal('544.5')]])

def solve_decimal(M, A):
    M_float = np.array(M, dtype=float)
    A_float = np.array(A, dtype=float)
    solution = np.linalg.solve(M_float, A_float)
    return [Decimal(str(x)) for x in solution.flatten()]

X = solve_decimal(M, A)

a, b = X[0], X[1]
print("a= " + str(a))
print("b= " + str(b))
