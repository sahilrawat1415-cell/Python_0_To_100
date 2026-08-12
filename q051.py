# An automorphic number is a number whose square ends with the number itself.

# Example: 25² = 625, which ends in 25.



n= int(input("enter number :"))

sq=n*n
temp=n
pow=1

while temp>0:
    pow=pow*10
    temp=temp//10

if sq%sq == n:
    print("Automorphic num")
else:
    print("NOT Automorphic num")