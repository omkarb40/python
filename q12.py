'''
Write a Python program to print the following pattern:
Example: n=5
* * * * *
* * * *
* * *
* *
*
'''
n=int(input("Enter n:"))
for i in range(n,0,-1):
    for j in range(0,i+1):
        print("*\t",end="")
    print()

