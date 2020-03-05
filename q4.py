# Write a  Python program to print the second largest number from 3 numbers entered by the user.
print("Enter numbers")
n1=int(input("n1 : "))
n2=int(input("n2 : "))
n3=int(input("n3 : "))
if n1<n2 and n2<n3 :
    print("second largest is {0}".format(n2))
if n1<n3 and n3<n2 :
    print("second largest is {0}".format(n3))
if n2<n1 and n1<n3 :
    print("second largest is {0}".format(n1))
if n2<n3 and n3<n1 :
    print("second largest is {0}".format(n3))
if n3<n1 and n1<n2 :
    print("second largest is {0}".format(n1))
if n3<n2 and n2<n1 :
    print("second largest is {0}".format(n2))
