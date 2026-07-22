# Traversing by converting int to string
n=input("enter number :")
count=0
for digit in n:
    print(digit)


# traversing using digits itself
n=int(input("enter a number "))
digit=[]
while n>0:
    digit.append(n%10)
    n=n//10

for digit in reversed(digit):
    print(digit)