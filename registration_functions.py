import tkinter as tk
from tkinter import messagebox
import database
import sqlite3


def create_registration_widgets(frame):
    # Create event registration form
    tk.Label(frame, text="User:").grid(row=0, column=0)
    tk.Label(frame, text="Event:").grid(row=1, column=0)

    user_combo = tk.ttk.Combobox(frame, state="readonly")
    event_combo = tk.ttk.Combobox(frame, state="readonly")

    user_combo.grid(row=0, column=1)
    event_combo.grid(row=1, column=1)

    def register():
        user_id = user_combo.current()
        event_id = event_combo.current()

        if database.register_for_event(user_id, event_id):
            messagebox.showinfo("Success", "Registration successful!")
        else:
            messagebox.showerror("Error", "Registration failed!")

    tk.Button(frame, text="Register", command=register).grid(row=2, column=0, columnspan=2)

    # Populate user and event comboboxes
    users = database.get_all_users()
    events = database.get_all_events()

    user_combo['values'] = [user[1] for user in users]
    event_combo['values'] = [event[1] for event in events]

# Register user for an event
def register_for_event(user_id, event_id):
    cur = database.conn.cursor()
    try:
        cur.execute("INSERT INTO event_registrations (user_id, event_id) VALUES (?, ?)", (user_id, event_id))
        database.conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False