# Write a Python program to check if the square of a number is prime or not.
n=int(input("Enter n : "))
square=n*n
flag=0
for i in range (1,square+1) :
    if square % i == 0 :
        flag=1
        break
if flag == 0 :
    print("square of {0} is a prime number".format(n))
else :
    print("square of {0} is not a prime number".format(n))