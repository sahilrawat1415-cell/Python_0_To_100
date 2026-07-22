n=int(input("Enter number ="))
count=0
for i in range(1,n+1):
    if(i%3==0):
        print(i)
        count+=1
print('Total numbers divisible by 3 are =',count)