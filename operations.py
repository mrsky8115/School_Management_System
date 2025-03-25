#School Admission System
from random import randint

# Dictionary to store class details (fees, timing, books)
classes = {
    1: {"Fees": 5000, "Timing": "8:00 AM - 12:00 PM", "Books": [("Math", 250), ("English", 200), ("Hindi",100)], "TotalCost": 6050},
    2: {"Fees": 5500, "Timing": "8:00 AM - 12:00 PM", "Books": [("Math", 250), ("English", 200), ("Hindi",200)], "TotalCost": 6150},
    3: {"Fees": 6000, "Timing": "8:00 AM - 12:00 PM", "Books": [("Math", 300), ("English", 250), ("Hindi",200)], "TotalCost": 6750},
    4: {"Fees": 6500, "Timing": "8:00 AM - 1:00 PM", "Books": [("Math", 400), ("English", 150), ("Hindi",100), ("Science", 350)], "TotalCost": 7500},
    5: {"Fees": 7500, "Timing": "8:00 AM - 1:00 PM", "Books": [("Math", 450), ("English", 200), ("Hindi",300), ("Science", 350)], "TotalCost": 8800},
    6: {"Fees": 7500, "Timing": "8:00 AM - 2:00 PM", "Books": [("Math", 300), ("English", 250), ("Hindi",400), ("Science", 400), ("Computer", 350)], "TotalCost": 9200},
    7: {"Fees": 8000, "Timing": "8:00 AM - 2:00 PM", "Books": [("Math", 400), ("English", 150), ("Hindi",500), ("Science", 450), ("Computer", 550)], "TotalCost": 10050},
    8: {"Fees": 9000, "Timing": "8:00 AM - 2:00 PM", "Books": [("Math", 550), ("English", 200), ("Hindi",450), ("Science", 550), ("Computer", 750)], "TotalCost": 11500},
}

# List to store student records
students = []

class Student:
    def studentAdmission (self):
        self.id= randint(200, 300)
        self.name=input("Enter student name: ")
        self.class_=int(input("Enter Class (1 to 8): "))
        while self.class_ not in classes:
            self.class_=int(input("Invalid class entered. Please enter a class from 1 to 8: "))
        self.gender=input("Enter the Gender [Male/Female] : ")
        self.dob=input("Enter date of birth (DD/MM/YYYY): ")
        self.parent_name= input("Enter parent/guardian name: ")
        self.parent_contact= (input("Enter parent contact number: "))
        self.address=input("Enter student address: ")

        class_info=classes[self.class_]
        self.fees=class_info["Fees"]
        self.books=class_info["Books"]
        self.timing=class_info["Timing"]
        self.total_cost=class_info["TotalCost"]

        # Store the student in the list
        student_record={
            "Admission Number": self.id,
            "Name": self.name,
            "Class": self.class_,
            "DOB": self.dob,
            "Parent Name": self.parent_name,
            "Perent Contact No.":self.parent_contact,
            "Address": self.address,
            "Fees": self.fees,
            "Books": self.books,
            "Timing": self.timing,
            "Total Cost": self.total_cost}
        students.append(student_record)
        print("Student Admission Successfully Done...")
    
        
    def viewStudent (self):
        if students:
            print("\n***** Student Admission Records *****")
            for student in students:
                print("\nAdmission Number:", student["Admission Number"])
                print("Name:", student["Name"])
                print("Class:", student["Class"])
                print("DOB:", student["DOB"])                
                print("Parent Name:", student["Parent Name"])
                print("Parent Contact:", student["Perent Contact No."])
                print("Address:", student["Address"])
                print("Class Timing:", student["Timing"])
                print("Books Required:")
                for book, cost in student["Books"]:
                    print(f"  - {book}: Rs.{cost}")
                print("Fees: Rs.", student["Fees"])
                print("Total Fees and Book Cost: Rs.", student["Total Cost"])
                print("<----------------------------------->")
        else:
            print("No student records found.")

    def modifyStudentDetails(self):
        admission_no = int(input("Enter Admission Number to modify: "))
        student = next((s for s in students if s["Admission Number"] == admission_no), None)
        if student:
            student["Name"] = input("Modify Name: ")
            student["DOB"] = input("Modify DOB: ")
            student["Parent Name"] = input("Modify Parent Name: ")
            student["Parent Contact"] = input("Modify Parent Contact: ")
            student["Address"] = input("Modify Address: ")
            print("Student admission record updated successfully!")
        else:
            print("Admission number not found.")

    def viewClassDetails(self):
        class_ = int(input("Enter class level to view details (1 to 8): "))
        if class_ in classes:
            class_info = classes[class_]
            print(f"\n--- Class {class_} Details ---")
            print("Class Fees: Rs.", class_info["Fees"])
            print("Class Timing:", class_info["Timing"])
            print("Books Required:")
            for book, cost in class_info["Books"]:
                print(f"  - {book}: Rs.{cost}")
            print("Total Cost (Fees + Books): Rs.", class_info["TotalCost"])
        else:
            print("Invalid class entered.")