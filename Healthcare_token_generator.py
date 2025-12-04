import tkinter as tk
from tkinter import messagebox
import csv
import os

# Function to generate a new appointment token
def generate_token():
    if not os.path.exists("appointments.csv"):
        return 1  
    with open("appointments.csv", "r") as file:
        lines = file.readlines()
        if len(lines) <= 1:
            return 1  
        last_token = lines[-1].split(",")[0]
        return int(last_token) + 1  

# Function to save appointment details
def save_appointment():
    name = entry_name.get()
    age = entry_age.get()
    doctor = entry_doctor.get()
    date = entry_date.get()

    if name == "" or age == "" or doctor == "" or date == "":
        messagebox.showerror("Input Error", "All fields are required!")
        return

    token = generate_token()
    file_exists = os.path.isfile("appointments.csv")

    with open("appointments.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Token", "Patient Name", "Age", "Doctor", "Date"])
        writer.writerow([token, name, age, doctor, date])

    messagebox.showinfo("Success", f"Appointment Confirmed!\nToken Number: {token}")

    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_doctor.delete(0, tk.END)
    entry_date.delete(0, tk.END)

# GUI Window
window = tk.Tk()
window.title("Healthcare Appointment System")
window.geometry("350x250")
window.resizable(False, False)

# GUI Labels & Entries
tk.Label(window, text="Patient Name:").pack()
entry_name = tk.Entry(window, width=30)
entry_name.pack()

tk.Label(window, text="Age:").pack()
entry_age = tk.Entry(window, width=30)
entry_age.pack()

tk.Label(window, text="Doctor to Consult:").pack()
entry_doctor = tk.Entry(window, width=30)
entry_doctor.pack()

tk.Label(window, text="Date (DD/MM/YYYY):").pack()
entry_date = tk.Entry(window, width=30)
entry_date.pack()

# Submit Button
tk.Button(window, text="Generate Appointment Token", command=save_appointment).pack(pady=15)

window.mainloop()

