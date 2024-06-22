class Student:
    def __init__(self, student_id, name, dob, hometown, major, class_name):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.hometown = hometown
        self.major = major
        self.class_name = class_name

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DOB: {self.dob}, Hometown: {self.hometown}, Major: {self.major}, Class: {self.class_name}"


class StudentList:
    def __init__(self):
        self.students = []

    def view_students(self):
        if not self.students:
            print("No students in the list.")
        for student in self.students:
            print(student)

    def add_student(self, student):
        self.students.append(student)
        print(f"Added student: {student.name}")

    def update_student(self, student_id, **kwargs):
        student = self.find_student(student_id)
        if student:
            for key, value in kwargs.items():
                setattr(student, key, value)
            print(f"Updated student: {student.name}")
        else:
            print(f"Student with ID {student_id} not found.")

    def delete_student(self, student_id):
        student = self.find_student(student_id)
        if student:
            self.students.remove(student)
            print(f"Deleted student: {student.name}")
        else:
            print(f"Student with ID {student_id} not found.")

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def search_students(self, keyword):
        results = [student for student in self.students if keyword.lower() in student.name.lower()]
        if results:
            for student in results:
                print(student)
        else:
            print(f"No students found with keyword '{keyword}'")

    def sort_students(self, by):
        try:
            self.students.sort(key=lambda student: getattr(student, by))
            print(f"Students sorted by {by}")
        except AttributeError:
            print(f"Invalid attribute '{by}' to sort by.")


def main():
    student_list = StudentList()

    while True:
        print("\nStudent Management System")
        print("1. View students")
        print("2. Add student")
        print("3. Update student")
        print("4. Delete student")
        print("5. Search students")
        print("6. Sort students")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_list.view_students()

        elif choice == "2":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter date of birth (YYYY-MM-DD): ")
            hometown = input("Enter hometown: ")
            major = input("Enter major: ")
            class_name = input("Enter class name: ")
            student = Student(student_id, name, dob, hometown, major, class_name)
            student_list.add_student(student)

        elif choice == "3":
            student_id = input("Enter student ID to update: ")
            print("Enter new details (leave blank to keep current value):")
            name = input("Enter student name: ")
            dob = input("Enter date of birth (YYYY-MM-DD): ")
            hometown = input("Enter hometown: ")
            major = input("Enter major: ")
            class_name = input("Enter class name: ")

            update_fields = {}
            if name:
                update_fields["name"] = name
            if dob:
                update_fields["dob"] = dob
            if hometown:
                update_fields["hometown"] = hometown
            if major:
                update_fields["major"] = major
            if class_name:
                update_fields["class_name"] = class_name

            student_list.update_student(student_id, **update_fields)

        elif choice == "4":
            student_id = input("Enter student ID to delete: ")
            student_list.delete_student(student_id)

        elif choice == "5":
            keyword = input("Enter search keyword: ")
            student_list.search_students(keyword)

        elif choice == "6":
            by = input("Sort students by (student_id, name, dob, hometown, major, class_name): ")
            student_list.sort_students(by)

        elif choice == "7":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()