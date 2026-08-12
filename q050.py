# A strong number is a number where the sum of factorials of its digits equals the number.

# Example: 145 = 1! + 4! + 5! = 145



n= int(input("enter number :"))
temp=n
total=0

while temp>0:
    digit = temp%10   # gives remainder 
    fact=1
    
    for i in range(1,digit+1):
        fact=fact*i
        
    total =total+fact
    temp=temp//10
    
if total == n:
    print("Strong Number ")
else:
    print("Not a strong number ")