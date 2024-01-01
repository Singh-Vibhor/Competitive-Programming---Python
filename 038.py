import os
import shutil

class Student:
    def __init__(self, roll_no, name, age, marks, attendance=None):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.marks = marks
        self.attendance = attendance or []

    def calculate_grade(self):
        if self.marks >= 90:
            return 'A+'
        elif self.marks >= 80:
            return 'A'
        elif self.marks >= 70:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        else:
            return 'F'

    def display_student(self):
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")
        print(f"Attendance: {', '.join(self.attendance)}")
        print("=" * 20)

def save_students_to_file(students, file_name):
    with open(file_name, 'w') as file:
        for student in students:
            attendance = ",".join(student.attendance)
            file.write(f"{student.roll_no},{student.name},{student.age},{student.marks},{attendance}\n")

def load_students_from_file(file_name):
    students = []
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) >= 4:
                    roll_no, name, age, marks, *attendance = parts
                    students.append(Student(roll_no, name, age, int(marks), attendance))
    return students

def create_backup(file_name, backup_name):
    shutil.copyfile(file_name, backup_name)
    print("Backup created successfully.")

def restore_backup(backup_name, file_name):
    shutil.copyfile(backup_name, file_name)
    print("Data restored successfully.")

def main():
    file_name = "students.txt"
    students = load_students_from_file(file_name)
    backup_name = "students_backup.txt"

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search by Roll No")
        print("4. Search by Name")
        print("5. Update Student")
        print("6. Delete Student")
        print("7. Sort Students")
        print("8. Student Statistics")
        print("9. Record Attendance")
        print("10. Backup Data")
        print("11. Restore Data")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            roll_no = input("Enter Roll No: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            marks = int(input("Enter Marks: "))
            if 0 <= marks <= 100:
                students.append(Student(roll_no, name, age, marks))
                save_students_to_file(students, file_name)
                print("Student added successfully!")
            else:
                print("Marks should be between 0 and 100.")

        elif choice == "2":
            if students:
                for student in students:
                    student.display_student()
            else:
                print("No students found.")

        elif choice == "3":
            roll_no = input("Enter Roll No to search: ")
            found = False
            for student in students:
                if student.roll_no == roll_no:
                    student.display_student()
                    found = True
                    break
            if not found:
                print("Student not found.")

        elif choice == "4":
            name_to_search = input("Enter Name to search: ")
            found = False
            for student in students:
                if student.name.lower() == name_to_search.lower():
                    student.display_student()
                    found = True
            if not found:
                print("Student not found.")

        elif choice == "5":
            roll_no = input("Enter Roll No to update: ")
            found = False
            for student in students:
                if student.roll_no == roll_no:
                    name = input("Enter updated Name: ")
                    age = input("Enter updated Age: ")
                    marks = int(input("Enter updated Marks: "))
                    if 0 <= marks <= 100:
                        student.name = name
                        student.age = age
                        student.marks = marks
                        save_students_to_file(students, file_name)
                        print("Student updated successfully!")
                    else:
                        print("Marks should be between 0 and 100.")
                    found = True
                    break
            if not found:
                print("Student not found.")

        elif choice == "6":
            roll_no = input("Enter Roll No to delete: ")
            students = [student for student in students if student.roll_no != roll_no]
            save_students_to_file(students, file_name)
            print("Student deleted successfully!")

        elif choice == "7":
            sort_option = input("Sort by (1. Roll No / 2. Name): ")
            if sort_option == "1":
                students.sort(key=lambda x: x.roll_no)
            elif sort_option == "2":
                students.sort(key=lambda x: x.name)
            else:
                print("Invalid option for sorting.")
            for student in students:
                student.display_student()

        elif choice == "8":
            if students:
                marks = [student.marks for student in students]
                print(f"Average Marks: {sum(marks) / len(marks):.2f}")
                print(f"Minimum Marks: {min(marks)}")
                print(f"Maximum Marks: {max(marks)}")
            else:
                print("No students found.")

        elif choice == "9":
            roll_no = input("Enter Roll No to record attendance: ")
            found = False
            for student in students:
                if student.roll_no == roll_no:
                    date = input("Enter the date (YYYY-MM-DD): ")
                    student.attendance.append(date)
                    save_students_to_file(students, file_name)
                    print("Attendance recorded successfully!")
                    found = True
                    break
            if not found:
                print("Student not found.")

        elif choice == "10":
            create_backup(file_name, backup_name)

        elif choice == "11":
            restore_backup(backup_name, file_name)

        elif choice == "12":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()