char=input("Enter anything :")
if(char.isalpha()):
    print(char,'is a alphabet')
elif(char.isdigit()):
    print(char,'is a numeric')
else:
    print(char,'is a special character')