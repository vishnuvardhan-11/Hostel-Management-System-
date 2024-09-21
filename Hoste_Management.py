import os

# Define the Student class
class Student:
    def __init__(self, student_id, name, age, gender, room_number=None, fees_paid=False):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.room_number = room_number
        self.fees_paid = fees_paid

    def display_info(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Room: {self.room_number}, Fees Paid: {self.fees_paid}"

# Hostel Management class to handle operations
class HostelManagement:
    def __init__(self):
        self.students = {}

    def add_student(self):
        student_id = input("Enter student ID: ")
        name = input("Enter name: ")
        age = input("Enter age: ")
        gender = input("Enter gender: ")

        student = Student(student_id, name, age, gender)
        self.students[student_id] = student
        print(f"Student {name} added successfully!\n")
    
    def assign_room(self):
        student_id = input("Enter student ID to assign room: ")
        if student_id in self.students:
            room_number = input("Enter room number: ")
            self.students[student_id].room_number = room_number
            print(f"Room {room_number} assigned to {self.students[student_id].name}\n")
        else:
            print("Student not found!\n")
    
    def update_fees(self):
        student_id = input("Enter student ID to update fees: ")
        if student_id in self.students:
            self.students[student_id].fees_paid = True
            print(f"Fees updated for {self.students[student_id].name}\n")
        else:
            print("Student not found!\n")

    def view_student(self):
        student_id = input("Enter student ID to view details: ")
        if student_id in self.students:
            print(self.students[student_id].display_info(), "\n")
        else:
            print("Student not found!\n")

    def delete_student(self):
        student_id = input("Enter student ID to delete: ")
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student with ID {student_id} has been removed\n")
        else:
            print("Student not found!\n")

    def save_data(self):
        with open("students.txt", "w") as file:
            for student_id, student in self.students.items():
                file.write(f"{student_id},{student.name},{student.age},{student.gender},{student.room_number},{student.fees_paid}\n")
        print("Data saved to students.txt\n")

    def load_data(self):
        if os.path.exists("students.txt"):
            with open("students.txt", "r") as file:
                for line in file:
                    student_id, name, age, gender, room_number, fees_paid = line.strip().split(",")
                    student = Student(student_id, name, age, gender, room_number, fees_paid == 'True')
                    self.students[student_id] = student
            print("Data loaded from students.txt\n")
        else:
            print("No saved data found!\n")

def main():
    hostel = HostelManagement()
    hostel.load_data()

    while True:
        print("Hostel Management System")
        print("1. Add Student")
        print("2. Assign Room")
        print("3. Update Fees")
        print("4. View Student")
        print("5. Delete Student")
        print("6. Save Data")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            hostel.add_student()
        elif choice == "2":
            hostel.assign_room()
        elif choice == "3":
            hostel.update_fees()
        elif choice == "4":
            hostel.view_student()
        elif choice == "5":
            hostel.delete_student()
        elif choice == "6":
            hostel.save_data()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
