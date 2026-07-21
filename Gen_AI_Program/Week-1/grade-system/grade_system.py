# ** Student Grade System Code**

# ** Notes ** 
#Student Name and Marks are received as inputs from user and grades are calculated based on mark range.
#Exception handling is used to handle graceful exit instead of abrupt failure. After successful validation,ouptu 
# student data is returned as dictionary## 


student_name = input("Please Enter Student Name :")
try:
    student_mark = int(input("Please Enter Student Marks(0 - 100) " ))

    if student_mark < 0 or student_mark  > 100:
        print("Please input Valid Mark Range")
   
    else:
        if 90<= student_mark <= 100:
            grade = 'A'
        elif 80<= student_mark < 90:
            grade = 'B'
        elif 70<= student_mark < 80:
            grade = 'C'
        elif 60<= student_mark < 70:
            grade = 'D'
        else:   
            grade = 'E'
        student = {"Name" : student_name,"Mark": student_mark,"Grade":grade}
        print(student)


except ValueError:
    print("Invalid input")



