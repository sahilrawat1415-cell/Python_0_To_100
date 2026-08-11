# An Armstrong number is a number whose digits raised to the power of the number of digits add up to the original number.

# # Example: 153 = 1³ + 5³ + 3³ = 153    

n=int(input("Enter Number :"))

temp = n
digits = len(str(n))
total = 0


while temp>0:
    digit=temp%10
    total=total+digit**(digits)
    temp=temp//10
    
    
if total==n:
    print("Armstrong Number :")
else :
     print("Not an Armstrong number")
    