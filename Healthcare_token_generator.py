
import csv
import os

def generate_token():
    if not os.path.exists("appointments.csv"):
        return 1
    with open("appointments.csv", "r") as file:
        lines = file.readlines()
        if len(lines) <= 1:
            return 1
        last_line = lines[-1].split(",")[0]
        return int(last_line) + 1

def create_appointment():
    name = input("Enter Patient Name: ")
    age = input("Enter Age: ")
    doctor = input("Enter Doctor Name: ")
    date = input("Enter Appointment Date (DD/MM/YYYY): ")

    token = generate_token()

    file_exists = os.path.isfile("appointments.csv")

    with open("appointments.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Token", "Name", "Age", "Doctor", "Date"])
        writer.writerow([token, name, age, doctor, date])

    print("\nAppointment Created Successfully!")
    print("Token Number:", token)

create_appointment()
