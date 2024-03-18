import tkinter as tk
from tkinter import messagebox
import database
import user_functions
import event_functions
import registration_functions
import volunteer_functions
import sponsor_functions

# Create a global database connection
conn = database.create_connection()

def close_connection():
    if conn:
        conn.close()

class CollegeEventManagement:
    def __init__(self, root):
        self.root =root
        self.root.title("College Event Management")

        # Create frames for different functionalities
        self.user_frame = tk.Frame(self.root)
        self.event_frame = tk.Frame(self.root)
        self.registration_frame = tk.Frame(self.root)
        self.volunteer_frame = tk.Frame(self.root)
        self.sponsor_frame = tk.Frame(self.root)

        # Place frames on the root window
        self.user_frame.pack()
        self.event_frame.pack()
        self.registration_frame.pack()
        self.volunteer_frame.pack()
        self.sponsor_frame.pack()

        # Create widgets for each frame
        user_functions.create_user_widgets(self.user_frame)
        event_functions.create_event_widgets(self.event_frame)
        registration_functions.create_registration_widgets(self.registration_frame)
        volunteer_functions.create_volunteer_widgets(self.volunteer_frame)
        sponsor_functions.create_sponsor_widgets(self.sponsor_frame)

if __name__ == "__main__":
    root = tk.Tk()
    app = CollegeEventManagement(root)
    root.mainloop()
    close_connection()