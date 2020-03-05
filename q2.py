"""
Write a Python program to print the following series:
a) 1,4,7,10….n terms
b) 1,-4,7,-10,…,n terms
"""
n=int(input("Enter n : "))
series=1
for i in range (n) :
    print(series," ",end="")
    series+=3

n=int(input("Enter n : "))
x=1
for i in range (n) :
    print(x," ",end="")
    if i % 2 == 0:
        x *= (-1)
        x -= 3
    else:
        x *= (-1)
        x += 3