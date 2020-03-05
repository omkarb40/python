# Design a function having both parameters and return statement
def function(*n):
    m=0
    for i in n:
       m=m+i
    return m

s=function(1,2,3)
print(s)