n=int(input("enter number: "))
last=n%10
while n>=10:
    n=n//10
    first=n
print('sum of first and last digit is',last+first)
    