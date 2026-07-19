stu_name=input("enter name : ")
stu_marks=int(input("Enter marks :"))

if(stu_marks>=90):
    print('Grade A+')
elif(stu_marks>=80):
    print('Grade A')
elif(stu_marks>=70):
    print('Grade B')
elif(stu_marks>=60):
    print('Grade C')
elif(stu_marks>=50):
    print('Grade D')
else:
    print('Fail..:(')