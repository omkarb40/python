# Write a Python program to compute Simple Interest and Compound Interest.
p=int(input("Enter principle amount:"))
n=int(input("Enter the duration:"))
r=int(input("Enter the rate of interest:"))
ci=p*(pow((1+r/100),n))
print("The compound interest is:",ci)
"""
here pow is the function used to take power of the bracket
/ is used to divide numerator by denominator and get the value in decimal
"""

