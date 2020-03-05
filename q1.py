# Write a Python program to check if a year is a leap year or not.
n=int(input("Enter a year:"))
if(n%4==0):
    if(n%100==0):
        if(n%400==0):
            print("its a leap year")
        else:
            print("not a leap year")
    else:
        print("not a leap year")
else:
    print("not a leap year")
