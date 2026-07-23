n=int(input("Enter how many times you want to check :"))

def largest():
        num1=int(input("enter number 1:"))
        num2=int(input("enter number 2:"))
        num3=int(input("enter number 3:"))
        if(num1>num2 and num1>num3):
            print(num1,"is the largest number")
        elif(num2>num1 and num2>num3):
            print(num2,"is the largest number")
        else:
            print(num3,"is the largest number")
for i in range(n):
    a=largest()