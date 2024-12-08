import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Function to calculate and display the birth year based on the age
def calculateBirthYear():
    try:
        # Get the user's name and age from input fields
        name = entryName.get()
        age = int(entryAge.get())  # Convert age input to integer
        
        # Get current year dynamically
        currentYear = datetime.now().year
        
        # Calculate birth year based on the current year
        birthYear = currentYear - age
        
        # Display result in the result_label
        resultLabel.config(text=f"Hello {name}, you were born in {birthYear}.")
    
    except ValueError:
        # If a non-numeric value is entered in the age field, show an error message
        messagebox.showerror("Invalid input", "Please enter a valid number for the age.")
    
# Create the main window
root = tk.Tk()
root.title("Data Entry Application")

# Create labels and entry boxes for name and age
labelName = tk.Label(root, text="Enter your name:")
labelName.pack(padx=10, pady=5)

entryName = tk.Entry(root)
entryName.pack(padx=10, pady=5)

labelAge = tk.Label(root, text="Enter your age:")
labelAge.pack(padx=10, pady=5)

entry_Age = tk.Entry(root)
entryAge.pack(padx=10, pady=5)

# Button to trigger the calculation
calcButton = tk.Button(root, text="Calculate Birth Year", command=calculateBirthYear)
calcButton.pack(pady=10)

# Label to display the result
resultLabel = tk.Label(root, text="")
resultLabel.pack(padx=10, pady=10)

# Start the main event loop
root.mainloop()

