# Write a Python program to read a number from the user and print the reversed number
n=int(input("Enter a number:"))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("the reversed number is:",rev)

