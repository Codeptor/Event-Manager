import tkinter as tk
from tkinter import messagebox
import database
import sqlite3

def create_event_widgets(frame):  # Add frame as a parameter
    # Create event creation form
    tk.Label(frame, text="Name:").grid(row=0, column=0)
    tk.Label(frame, text="Description:").grid(row=1, column=0)
    tk.Label(frame, text="Location:").grid(row=2, column=0)
    tk.Label(frame, text="Start Time:").grid(row=3, column=0)
    tk.Label(frame, text="End Time:").grid(row=4, column=0)

    name_entry = tk.Entry(frame)
    description_entry = tk.Entry(frame)
    location_entry = tk.Entry(frame)
    start_time_entry = tk.Entry(frame)
    end_time_entry = tk.Entry(frame)

    name_entry.grid(row=0, column=1)
    description_entry.grid(row=1, column=1)
    location_entry.grid(row=2, column=1)
    start_time_entry.grid(row=3, column=1)
    end_time_entry.grid(row=4, column=1)

    def create_event():
        name = name_entry.get()
        description = description_entry.get()
        location = location_entry.get()
        start_time = start_time_entry.get()
        end_time = end_time_entry.get()

        if database.add_event(name, description, location, start_time, end_time):
            messagebox.showinfo("Success", "Event created successfully!")
        else:
            messagebox.showerror("Error", "Event creation failed!")
            tk.Button(frame, text="Create Event", command=create_event).grid(row=5, column=0, columnspan=2)

# Add event to the database
def add_event(name, description, location, start_time, end_time):
    cur = database.conn.cursor()
    try:
        cur.execute("INSERT INTO events (name, description, location, start_time, end_time) VALUES (?, ?, ?, ?, ?)",
                    (name, description, location, start_time, end_time))
        database.conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False