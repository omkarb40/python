"""
Write a function that checks if a number is prime or not.
Pass the number as a parameter and return True if the number is prime, otherwise return False.
"""


def prime(n):
    if n == 1 or n == 0:
        return "FALSE"
    else:
        for i in range(2, n):
            if n % i == 0:
                return "FALSE"
            else:
                pass
    return "TRUE"


a = int(input("Enter n:"))
s = prime(a)
print(s)
