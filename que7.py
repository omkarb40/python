# Write a Python program to read three numbers and print them in ascending order.
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
num3 = int(input("Enter num3:"))
if (num1 >= num2) and (num1 >= num3):
    x = num1
    print(x)
elif (num2 >= num1) and (num2 >= num3):
    y = num2
    print(y)
elif (num3 >= num1) and (num3 >= num2):
    z = num3
    print(z)
print("The numbers in ascending order are:", x, y, z)
