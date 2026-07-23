# using string
n=input("enter number :")
even=0
odd=0
for i in n:
    if(int(i)%2==0):
        even+=1
    else:
        odd+=1
print("Even digits =", even)
print("Odd digits =", odd)

# using integer
n = int(input("Enter a number: "))

even = 0
odd = 0

while n > 0:
    digit = n % 10

    if digit % 2 == 0:
        even += 1
    else:
        odd += 1

    n = n // 10

print("Even digits =", even)
print("Odd digits =", odd)


