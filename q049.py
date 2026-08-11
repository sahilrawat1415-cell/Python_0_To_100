# A perfect number is equal to the sum of its proper divisors.

# Example: 6 = 1 + 2 + 3


n= int(input("enter number :"))

total=0

for i in range (1,n):
    if n%i == 0:
        total=total+i
if total==n :
    print("Perfect Number ")
else:
    print("Not a perfect num")

