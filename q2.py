'''
Write a function that computes the sum of all digits.
Pass the number as a parameter and return the computed sum.
'''


def getsum(n):

    sum=0
    while(n!=0):
        sum=sum+int(n%10)
        n=int(n/10)
    return sum
n=int(input("enter n:"))
print(getsum(n))


