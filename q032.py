# n=int(input("Enter number ="))
# count=0
# for i in range(1,n+1):
#     if(i%3==0 or i%5==0):
#         print(i)
#         count+=1
# print('Total numbers divisible by 3 or 5  =',count)




# For checking individually every number
n = int(input("Enter number = "))    

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "is divisible by both 3 and 5")
    elif i % 3 == 0:
        print(i, "is divisible by 3")
    elif i % 5 == 0:
        print(i, "is divisible by 5")