# Write a Python program to find the largest of 3 numbers.
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
num3=int(input("Enter num3:"))
if (num1>=num2) and (num1>=num3):
    print("Num1 is the largest")
elif(num2>=num1) and (num2>=num3):
    print("Num2 is the largest")
elif(num3>=num1) and (num3>=num2):
    print("Num3 is the largest")
