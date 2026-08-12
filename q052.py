# A Harshad number is divisible by the sum of its digits.

# Example: 18 → 1 + 8 = 9, and 18 % 9 = 0.



n= int(input("enter num :"))

temp=n
total =0

while temp>0:
    digit =temp%10
    total += digit
    temp =temp//10

if n%total ==0:
    print("IT IS HARSHAD NUM")
else:
    print("IT IS NOT HARSHAD NUM")