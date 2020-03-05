'''
Write a function that computes the factorial of a number.
The function should take the number as a parameter and return the factorial value.
'''


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Enter n:"))
print(factorial(n))
