"""
Write a function that computes the simple interest.
Pass the principal amount, the rate and the time as parameters to the function.
"""


def Interest(P, I, T):
    A = P * (1 + (I * T))
    return A


P = int(input("Enter P:"))
I = int(input("Enter I:"))
T = int(input("Enter T:"))
A = Interest(P, I, T)
print(A)
