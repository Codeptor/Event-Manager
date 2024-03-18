import tkinter as tk
from tkinter import messagebox
import database
import sqlite3


class CollegeSponsor(tk.Tk):
    def __init__(self):
        super().__init__(className='CollegeSponsor')

        self.title("Sponsor Management")
        self.geometry("500x300")

        self.conn = database.create_connection()

        self.create_widgets()

    def create_widgets(self):
        # Create sponsor creation form
        tk.Label(self, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self, text="Description:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self, text="Contact Email:").grid(row=2, column=0, padx=5, pady=5)

        self.name_entry = tk.Entry(self, width=30)
        self.description_entry = tk.Entry(self, width=30)
        self.contact_email_entry = tk.Entry(self, width=30)

        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.description_entry.grid(row=1, column=1, padx=5, pady=5)
        self.contact_email_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(self, text="Create Sponsor", command=self.create_sponsor, width=15, height=1).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def create_sponsor(self):
        name = self.name_entry.get()
        description = self.description_entry.get()
        contact_email = self.contact_email_entry.get()

        if database.add_sponsor(name, description, contact_email):
            messagebox.showinfo("Success", "Sponsor created successfully!")
        else:
            messagebox.showerror("Error", "Sponsor creation failed!")

# Add sponsor to the database
def add_sponsor(name, description, contact_email):
    cur = database.conn.cursor()
    try:
        cur.execute("INSERT INTO sponsors (name, description, contact_email) VALUES (?, ?, ?)",
                    (name, description, contact_email))
        database.conn.commit()
        return True
    except sqlite3.IntegrityError as e:
        print(f"Error adding sponsor: {e}")
        return False