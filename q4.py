"""
Write a function that prints the table of a number.
Pass the number as a parameter to the function.
"""


def table(n):
    for i in range(1, n + 1):
        print(n, "*", i, "=", n * i)
    pass


n = int(input("Enter n:"))
table(n)
