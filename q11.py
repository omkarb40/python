# Write a Python program to calculate and print the sums of odd and even integers of the first n natural numbers
n=int(input("Enter the number:"))
evensum=0
oddsum=0
for number in range(1,n+1):
    if(number%2==0):
        evensum=evensum+number
    else:
        oddsum=oddsum+number
print("Sum of all even numbers is",evensum)
print("Sum of all odd numbers is",oddsum)
