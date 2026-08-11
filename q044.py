n= int(input("enter num :"))

if n<=1:
    print("not a prime number ")
    
else:
    prime=True
    
    for i in range(2,n):
        if(n% i==0):
            prime = False
            break
    if prime:
        print (n,"prime number")
    else:
        print(n,"not a prime number")