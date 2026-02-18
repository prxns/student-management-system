import tkinter as tk
from tkinter import messagebox
from database import connect, create_table


# Create database table
create_table()


# Add student function
def add_student():

    student_id = entry_id.get()
    name = entry_name.get()
    age = entry_age.get()
    course = entry_course.get()

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

        clear_fields()
        view_students()

    except:

        messagebox.showerror("Error", "Student ID already exists")

    conn.close()


# View students
def view_students():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    rows = cursor.fetchall()

    listbox.delete(0, tk.END)

    for row in rows:

        listbox.insert(
            tk.END,
            f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]}"
        )

    conn.close()


# Delete student
def delete_student():

    selected = listbox.curselection()

    if not selected:
        messagebox.showerror("Error", "Select student first")
        return

    student_text = listbox.get(selected[0])

    student_id = student_text.split("|")[0].replace("ID: ", "")

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


# Clear input fields
def clear_fields():

    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_course.delete(0, tk.END)


# Create main window
root = tk.Tk()
root.title("Student Management System")
root.geometry("500x500")


# Labels
tk.Label(root, text="Student ID").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Age").pack()
entry_age = tk.Entry(root)
entry_age.pack()

tk.Label(root, text="Course").pack()
entry_course = tk.Entry(root)
entry_course.pack()


# Buttons
tk.Button(root, text="Add Student", command=add_student).pack(pady=5)

tk.Button(root, text="View Students", command=view_students).pack(pady=5)

tk.Button(root, text="Delete Student", command=delete_student).pack(pady=5)

tk.Button(root, text="Clear Fields", command=clear_fields).pack(pady=5)


# Listbox
listbox = tk.Listbox(root, width=60)
listbox.pack(pady=10)


# Load students initially
view_students()


# Run app
root.mainloop()
