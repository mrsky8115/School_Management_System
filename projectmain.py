#School Admisson System
from operations import Student
student=Student()

#welcome message
print("\t\t\t*  *  *  *  *  *  *  *  *  *  *  *  *")
print("\t\t\t WELCOME TO  SCHOOL ADMISSION SYSTEM")
print("\t\t\t-------------------------------------")
print("\t\t\t*  *  *  *  *  *  *  *  *  *  *  *  *")

options={1:'studentAdmission',
         2:'viewStudent',
         3:'modifyStudentDetails',
         4:'viewClassDetails',
         5:'Exit'}

#main application loop
while True:                
    print("\nPlease Enter an Option")
    print("\t1.Student Admission")
    print("\t2.View Student Admission Record")
    print("\t3.Modify Student Details")
    print("\t4.View Class Details")
    print("\t5.Exit")

    choice=int (input("Enter Your Choice: "))

    if choice not in options:
        print("Invalid choice, please re-enter. ")
        continue

#select opertaion
    if choice==5:
        print("Thank You for using School Admisson System!")
    elif choice==1:
        student.studentAdmission()
    elif choice==2:
        student.viewStudent()
    elif choice==3:
        student.modifyStudentDetails()
    elif choice==4:
        student.viewClassDetails()

    ans=input("Do you want to continue?  (y/n): ")
    if ans.lower() != 'y':
        print("Thank you for using the application, Have a nice day..!")
        break