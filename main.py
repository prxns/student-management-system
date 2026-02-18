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

    student_id = input("Enter student ID: ").strip()

    # Prevent duplicate
    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists.")
            return
        
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
    
    print("\n--- Student List ---")

    for student in students:
        print(f"ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Course: {student['course']}")

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

# Update Student info
def update_student():
    students = load_students()

    update_id = input("Enter student ID to update: ")

    for student in students:
        if student["id"] == update_id:
            print("Leave blank to keep current value")

            new_name = input(f"Enter new name ({student['name']}): ")
            new_age = input(f"Enter new age ({student['age']}): ")
            new_course = input(f"Enter new course ({student['course']}): ")

            if new_name:
                student["name"] = new_name

            if new_age:
                student["age"] = new_age

            if new_course:
                student["course"] = new_course

            save_students(students)

            print("Student updated successfully!")
            return

    print("Student not found.")    

# Menu
def menu():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Student")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")

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
            update_student()

        elif choice == "6":
            break

        else:
            print("Invalid choice")

menu()



