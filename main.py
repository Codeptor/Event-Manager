import tkinter as tk
import sponsor_functions

# Create the main window
root = tk.Tk()

# Create an instance of the Sponsor Management App
sponsor_app = sponsor_functions.CollegeSponsor(root)

# Arrange the instance in the grid layout
sponsor_app.grid(row=0, column=0, padx=10, pady=10)

root.mainloop()



