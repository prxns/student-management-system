import sqlite3
import os

DB_NAME = os.path.join(os.path.dirname(__file__), "students.db")


def connect():
    return sqlite3.connect(DB_NAME)


def create_table():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        age TEXT NOT NULL,
        course TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()
