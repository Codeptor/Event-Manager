import tkinter as tk
from tkinter import messagebox
import database
import sqlite3


def create_sponsor_widgets(frame):
    # Create sponsor creation form
    tk.Label(frame, text="Name:").grid(row=0, column=0)
    tk.Label(frame, text="Description:").grid(row=1, column=0)
    tk.Label(frame, text="Contact Email:").grid(row=2, column=0)

    name_entry = tk.Entry(frame)
    description_entry = tk.Entry(frame)
    contact_email_entry = tk.Entry(frame)

    name_entry.grid(row=0, column=1)
    description_entry.grid(row=1, column=1)
    contact_email_entry.grid(row=2, column=1)

    def create_sponsor():
        name = name_entry.get()
        description = description_entry.get()
        contact_email = contact_email_entry.get()

        if database.add_sponsor(name, description, contact_email):
            messagebox.showinfo("Success", "Sponsor created successfully!")
        else:
            messagebox.showerror("Error", "Sponsor creation failed!")

    tk.Button(frame, text="Create Sponsor", command=create_sponsor).grid(row=3, column=0, columnspan=2)

# Add sponsor to the database
def add_sponsor(name, description, contact_email):
    cur = database.conn.cursor()
    try:
        cur.execute("INSERT INTO sponsors (name, description, contact_email) VALUES (?, ?, ?)",
                    (name, description, contact_email))
        database.conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False