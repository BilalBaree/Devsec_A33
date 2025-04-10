# Mgtsys.py

class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.student_id}: {self.name}, Age: {self.age}"


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age):
        if student_id in self.students:
            return "Student already exists."
        self.students[student_id] = Student(student_id, name, age)
        return "Student added successfully."

    def view_students(self):
        return [str(s) for s in self.students.values()]

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            return "Student removed successfully."
        return "Student not found."


# Only runs when script is executed directly
if __name__ == "__main__":
    sms = StudentManagementSystem()

    while True:
        print("\n1. Add Student\n2. View Students\n3. Remove Student\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            sid = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            print(sms.add_student(sid, name, age))
        elif choice == '2':
            for s in sms.view_students():
                print(s)
        elif choice == '3':
            sid = input("Enter Student ID to remove: ")
            print(sms.remove_student(sid))
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")
