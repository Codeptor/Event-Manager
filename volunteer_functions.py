import tkinter as tk
import database
from tkinter import messagebox
import sqlite3


def create_volunteer_widgets(frame):
    # Create event volunteer form
    tk.Label(frame, text="User:").grid(row=0, column=0)
    tk.Label(frame, text="Event:").grid(row=1, column=0)
    tk.Label(frame, text="Volunteer Time:").grid(row=2, column=0)

    user_combo = tk.ttk.Combobox(frame, state="readonly")
    event_combo = tk.ttk.Combobox(frame, state="readonly")
    volunteer_time_entry = tk.Entry(frame)

    user_combo.grid(row=0, column=1)
    event_combo.grid(row=1, column=1)
    volunteer_time_entry.grid(row=2, column=1)

    def volunteer():
        user_id = user_combo.current()
        event_id = event_combo.current()
        volunteer_time = volunteer_time_entry.get()

        if database.volunteer_for_event(user_id, event_id, volunteer_time):
            messagebox.showinfo("Success", "Volunteer registration successful!")
        else:
            messagebox.showerror("Error", "Volunteer registration failed!")

    tk.Button(frame, text="Volunteer", command=volunteer).grid(row=3, column=0, columnspan=2)

    # Populate user and event comboboxes
    users = database.get_all_users()
    events = database.get_all_events()

    user_combo['values'] = [user[1] for user in users]
    event_combo['values'] = [event[1] for event in events]

# Register user as a volunteer for an event
def volunteer_for_event(user_id, event_id, volunteer_time):
    cur = database.conn.cursor()
    try:
        cur.execute("INSERT INTO event_volunteers (user_id, event_id, volunteer_time) VALUES (?, ?, ?)",
                    (user_id, event_id, volunteer_time))
        database.conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False