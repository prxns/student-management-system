from database import connect, create_table
import sqlite3

# Add student
def add_student():

    conn = connect()
    cursor = conn.cursor()

    student_id = input("Enter student ID: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    try:

        cursor.execute(
            "INSERT INTO students VALUES (?, ?, ?, ?)",
            (student_id, name, age, course)
        )

        conn.commit()

        print("Student added successfully!")

    except sqlite3.IntegrityError:

        print("Error: Student ID already exists.")

    conn.close()


# View students
def view_students():
    
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    if not students:
        print("No students found.")
        conn.close()
        return
    
    print("\n--- Student List ---")

    for student in students:
        print(f"ID: {student[0]} | Name: {student[1]} | Age: {student[2]} | Course: {student[3]}")
        conn.close()

#Search student
def search_student():

    conn = connect()
    cursor = conn.cursor()

    student_id = input("Enter student ID: ")

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        print("\nStudent Found: ")
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Age: {student[2]}")
        print(f"Course: {student[3]}")
    else:
        print("Student not found.")

        conn.close()

# Delete student
def delete_student():
    
    conn = connect()
    cursor = conn.cursor()

    student_id = input("Enter student ID to delete: ")

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()

    print("Student deleted if existed.")

    conn.close()

# Update Student info
def update_student():
    
    conn = connect()
    cursor = conn.cursor()

    student_id = input("Enter student ID to update: ")

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        conn.close()
        return

    print("Leave blank to keep current value")

    name = input(f"Enter new name ({student[1]}): ")
    age = input(f"Enter new age ({student[2]}): ")
    course = input(f"Enter new course ({student[3]}): ")

    name = name if name else student[1]
    age = age if age else student[2]
    course = course if course else student[3]

    cursor.execute(
        "UPDATE students SET name=?, age=?, course=? WHERE id=?",
        (name, age, course, student_id)
    )

    conn.commit()

    print("Student updated successfully!")
    
    conn.close()

# Menu
def menu():

    create_table()

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



