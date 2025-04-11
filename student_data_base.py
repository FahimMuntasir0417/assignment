class StudentDatabase:
    student_list = []

    def search_student(self,student_id):
        for student in StudentDatabase.student_list:
             if student.get_id() == student_id:
                return student
        print("NOT available any student in this ID ")
        return None
    

    def view_all_students(self):
        if not StudentDatabase.student_list:
            print("No students found.")
        for student in StudentDatabase.student_list:
            student.view_student_info()


    def get_student(self, student_id):
        return self.search_student(student_id)




class Student:
    def __init__(self,student_id,name,department,is_enrolled):
       self.__student_id = student_id
       self.__name = name
       self.__department = department
       self.is_enrolled = is_enrolled
       StudentDatabase.student_list.append(self)

    def enroll_student(self):
        if self.is_enrolled:
            print("Aready Enrolled")
        else:
            self.is_enrolled = True
            print(" Enrolled Successfully")


    def drop_student(self):
        if self.is_enrolled:
            print("Aready Droped")
        else:
            self.is_enrolled = False
            print(" Droped Successfully")


    def view_student_info(self):
        if self.is_enrolled:
            type = "Enrolled"
            print(type)
        else:
             type = " Not Enrolled"
             print(type)   
        print(f"\nID: {self.__student_id}")
        print(f"Name: {self.__name}")
        print(f"Department: {self.__department}")
        print(f"Status: {type}")

    def get_id(self):
        return self.__student_id
    
    
    

data_base = StudentDatabase()
Student(1, "Fahim MuntAsir", "CSE", False)
Student(2, "Raisul Jeber", "EEE", False)
Student(3, "Ismile Munna", "LLB", False)
Student(4, "eFat ahnmed", "ME", False)
Student(5, "rahim ahmed", "CE", False)
Student(6, "Karim Ahmed", "Math", False)


while True:
    print("\n1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")
    number = input("Which number would like to go : ")


    if number == "1":
        data_base.view_all_students()

    elif number == "2":
        try:
            StudendId = int(input("Enter Student iD to enroll: "))
            student = data_base.get_student(StudendId)
            if student:
                student.enroll_student()
        except:
            print("Invalid Student Enrollment")

    elif number == "3":
        try:
            StudendId = int(input("Enter Student id to drop: "))
            student = data_base.get_student(StudendId)
            if student:
                student.drop_student()
        except:
            print("Invalid Student Drop")

    elif number == "4":
        print("Thank YOU")
        print("You have exited Student Data Base.")
        break

    else:
        print("Invalid number. ")

