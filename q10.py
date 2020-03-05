# Write a Python program to print the sum of first n natural numbers, where n is entered by the user.
n=int(input("Enter the number:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print("The sum of first",n,"natural numbers is",sum)
