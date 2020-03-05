"""
Write a function that converts Celsius reading to Fahrenheit reading.
Read the Celsius value from the user in the function and also print the Fahrenheit reading in the function itself.
"""
def Conv(c):
    f=(c*5/9)+32
    print("C=",c,"and F=",f)
c=int(input("Enter temp in c:"))
Conv(c)



