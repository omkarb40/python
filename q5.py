# Write a Python program to print the sum of the following sequence:
#
# 0,1,1,2,3,5,8,….. (n terms)
n=int(input("Enter n : "))
a=0
b=1
print(0," ",end="")
for i in range (1,n) :
    print(b," ",end="")
    sum=a+b
    a=b
    b=sum
    