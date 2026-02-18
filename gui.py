import tkinter as tk
from tkinter import ttk, messagebox
from database import connect, create_table


# Ensure database table exists
create_table()


# Clear input fields
def clear_fields():

    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_course.delete(0, tk.END)


# View students in table
def view_students():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    rows = cursor.fetchall()

    tree.delete(*tree.get_children())

    for row in rows:
        tree.insert("", tk.END, values=row)

    conn.close()


# Add student
def add_student():

    student_id = entry_id.get().strip()
    name = entry_name.get().strip()
    age = entry_age.get().strip()
    course = entry_course.get().strip()

    if not student_id or not name or not age or not course:
        messagebox.showerror("Error", "All fields required")
        return

    conn = connect()
    cursor = conn.cursor()

    try:

        cursor.execute(
            "INSERT INTO students VALUES (?, ?, ?, ?)",
            (student_id, name, age, course)
        )

        conn.commit()

        messagebox.showinfo("Success", "Student added successfully")

        view_students()
        clear_fields()

    except:

        messagebox.showerror("Error", "Student ID already exists")

    conn.close()


# Select student from table
def select_student(event):

    selected = tree.focus()

    if not selected:
        return

    values = tree.item(selected, "values")

    clear_fields()

    entry_id.insert(0, values[0])
    entry_name.insert(0, values[1])
    entry_age.insert(0, values[2])
    entry_course.insert(0, values[3])


# Update student
def update_student():

    student_id = entry_id.get().strip()
    name = entry_name.get().strip()
    age = entry_age.get().strip()
    course = entry_course.get().strip()

    if not student_id:
        messagebox.showerror("Error", "Select student first")
        return

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET name=?, age=?, course=? WHERE id=?",
        (name, age, course, student_id)
    )

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Student updated successfully")

    view_students()
    clear_fields()


# Delete student
def delete_student():

    selected = tree.focus()

    if not selected:
        messagebox.showerror("Error", "Select student first")
        return

    values = tree.item(selected, "values")

    student_id = values[0]

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Student deleted")

    view_students()
    clear_fields()


# Search student
def search_student():

    student_id = entry_id.get().strip()

    if not student_id:
        messagebox.showerror("Error", "Enter student ID")
        return

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,)
    )

    student = cursor.fetchone()

    conn.close()

    tree.delete(*tree.get_children())

    if student:
        tree.insert("", tk.END, values=student)
    else:
        messagebox.showerror("Error", "Student not found")


# Create window
root = tk.Tk()
root.title("Student Management System")
root.geometry("650x500")


# Input frame
frame = tk.Frame(root)
frame.pack(pady=10)


tk.Label(frame, text="Student ID").grid(row=0, column=0)
entry_id = tk.Entry(frame)
entry_id.grid(row=0, column=1)

tk.Label(frame, text="Name").grid(row=1, column=0)
entry_name = tk.Entry(frame)
entry_name.grid(row=1, column=1)

tk.Label(frame, text="Age").grid(row=2, column=0)
entry_age = tk.Entry(frame)
entry_age.grid(row=2, column=1)

tk.Label(frame, text="Course").grid(row=3, column=0)
entry_course = tk.Entry(frame)
entry_course.grid(row=3, column=1)


# Button frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)


tk.Button(btn_frame, text="Add", width=12, command=add_student).grid(row=0, column=0)

tk.Button(btn_frame, text="Update", width=12, command=update_student).grid(row=0, column=1)

tk.Button(btn_frame, text="Delete", width=12, command=delete_student).grid(row=0, column=2)

tk.Button(btn_frame, text="Search", width=12, command=search_student).grid(row=0, column=3)

tk.Button(btn_frame, text="View All", width=12, command=view_students).grid(row=0, column=4)

tk.Button(btn_frame, text="Clear", width=12, command=clear_fields).grid(row=0, column=5)


# Table frame
table_frame = tk.Frame(root)
table_frame.pack()


tree = ttk.Treeview(
    table_frame,
    columns=("ID", "Name", "Age", "Course"),
    show="headings",
    height=10
)

tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Course", text="Course")

tree.column("ID", width=100)
tree.column("Name", width=150)
tree.column("Age", width=100)
tree.column("Course", width=150)

tree.pack()


# Bind selection
tree.bind("<ButtonRelease-1>", select_student)


# Load data
view_students()


# Run GUI
root.mainloop()
