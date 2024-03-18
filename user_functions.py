import tkinter as tk
from tkinter import messagebox
import database
import sqlite3


def create_user_widgets(frame):
    # Create user registration form
    tk.Label(frame, text="Name:").grid(row=0, column=0)
    tk.Label(frame, text="Email:").grid(row=1, column=0)
    tk.Label(frame, text="Password:").grid(row=2, column=0)

    name_entry = tk.Entry(frame)
    email_entry = tk.Entry(frame)
    password_entry = tk.Entry(frame, show="*")

    name_entry.grid(row=0, column=1)
    email_entry.grid(row=1, column=1)
    password_entry.grid(row=2, column=1)

    def register_user():
        name = name_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        if database.add_user(name, email, password):
            messagebox.showinfo("Success", "User registered successfully!")
        else:
            messagebox.showerror("Error", "User registration failed!")

    tk.Button(frame, text="Register", command=register_user).grid(row=3, column=0, columnspan=2)

# Add user to the database
def add_user(name, email, password):
    cur = database.conn.cursor()
    try:
        cur.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        database.conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False