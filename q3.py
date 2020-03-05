# Write a Python program to read the three sides of a triangle and print whether the triangle is equilateral, isosceles or scalene
print("Enter sides of traingle")
a=float(input("a : "))
b=float(input("b : "))
c=float(input("c : "))
if a==b and a==c :
    print("Triangle is equilateral")
elif (a==b or b==c) or a==c :
    print("Triangle is isosceles")
else :
    print("Triangle is scalene")
