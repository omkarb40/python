"""
Write a Python program to input a single digit(n) and print a 3 digit number created as <n(n+1)(n+2)>.
Eg: If you enter 7, then the output should be 789.
"""
n=int(input("Enter the number:"))
a=n+1
b=n+2
x=(n*100)+(a*10)+b
print("The required 3 digit number is:",x)
"""
here to convert a single digit to 3 digit number we see the use og tens and units place come to work
"""
