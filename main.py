import json

File_Name = "students.json"

#Load students from file
def load_students():
    try:
        with open(File_Name, "r") as file:
            students = json.load(file)
            return students
    except:
        return []
    
#Save students to file
def save_students(students):
    with open(File_Name, "w") as file:
        json.dump(students, file, indent=4)

# Add student
def add_student():
    students = load_students()

    student_id = input("Enter student ID: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)

    save_students(students)

    print("Student added successfully!")

# View students
def view_students():
    students = load_students()

    if not students:
        print("No students found.")
        return
    
    for student in students:
        print("---------------")
        print("ID: ", student["id"])
        print("Name: ", student["name"])
        print("Age: ", student["age"])
        print("Course: ", student["course"])

#Search student
def search_student():
    students = load_students()

    search_id = input("Enter student ID to search: ")

    for student in students:
        if student["id"] == search_id:
            print("Student found: ")
            print(student)
            return
    
    print("Student not found.")

# Delete student
def delete_student():
    students = load_students()

    delete_id = input("Enter student ID to delete: ")

    new_student = []

    for student in students:
        if student["id"] != delete_id: 
            new_student.append(student)

    save_students(new_student) 

    print("Student deleted if existed.")

# Menu
def menu():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Student")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            break

        else:
            print("Invalid choice")

menu()



