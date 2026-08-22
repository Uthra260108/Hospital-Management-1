import csv

import time

import sys

import os

# File paths
users_file = 'users.csv'

patients_file = 'patients.csv'

workers_file = 'workers.csv'

doctors_file = 'doctors.csv'

appointments_file = 'appointments.csv'

bills_file = 'bills.csv'

prescriptions_file = 'prescriptions.csv'

schedules_file = 'schedules.csv'

admissions_file = 'admissions.csv'

# Save new user to file
def save_user(username, password):
    with open(users_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

# Load existing users from file
def load_users():
    users = []
    try:
        with open(users_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                users.append([row[0], row[1]])
    except FileNotFoundError:
        pass  # File doesn't exist, user_list will be initialized as an empty list
    return users

# Function to validate login credentials
def validate_login(username, password, users):
    # Check if the provided username and password match any user in the list
    return any(user[0] == username and user[1] == password for user in users)

# Function to add details to CSV
def add_details(file_path, details):
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(details)
    print(f"Details added successfully to {file_path}")
    time.sleep(1)

# Function to view details from CSV
def view_details(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))
    time.sleep(1)

# Function to remove details from CSV
def remove_details(file_path, identifier):
    rows = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != identifier:
                rows.append(row)

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print(f"Details with identifier {identifier} removed successfully from {file_path}")
    time.sleep(1)

# Function to generate final bill
def generate_bill(patient_id, doctor_fee, worker_fee):
    total_fee = doctor_fee + worker_fee
    bill_details = [patient_id, time.strftime("%Y-%m-%d"), doctor_fee, worker_fee, total_fee]
    add_details(bills_file, bill_details)
    print(f"Bill generated successfully for patient {patient_id}")

    print("\nBill Summary:")
    print(f"Patient ID: {patient_id}")
    print(f"Date: {time.strftime('%Y-%m-%d')}")
    print(f"Doctor Fee: ${doctor_fee}")
    print(f"Worker Fee: ${worker_fee}")
    print(f"Total Fee: ${total_fee}")

    time.sleep(1)

# Function to make an appointment
def make_appointment(patient_id, doctor_id, appointment_date):
    appointment_details = [patient_id, doctor_id, appointment_date]
    add_details(appointments_file, appointment_details)
    print(f"Appointment scheduled successfully for patient {patient_id} with doctor {doctor_id} on {appointment_date}")
    time.sleep(1)

# Function to manage prescriptions
def add_prescription(patient_id, doctor_id, medication, dosage):
    prescription_details = [patient_id, doctor_id, medication, dosage]
    add_details(prescriptions_file, prescription_details)
    print(f"Prescription added successfully for patient {patient_id} by doctor {doctor_id}")
    time.sleep(1)

# Function to manage employee schedules
def add_schedule(worker_id, day, shift):
    schedule_details = [worker_id, day, shift]
    add_details(schedules_file, schedule_details)
    print(f"Schedule added successfully for worker {worker_id} on {day} - {shift} shift")
    time.sleep(1)

# Function to manage patient admissions
def admit_patient(patient_id, admission_date, room_number):
    admission_details = [patient_id, admission_date, room_number]
    add_details(admissions_file, admission_details)
    print(f"Patient {patient_id} admitted successfully on {admission_date} to room {room_number}")
    time.sleep(1)

# Function to view bill history for a patient
def view_bill_history(patient_id):
   # Assuming bills.csv has columns: Patient ID, Date, Doctor Fee, Worker Fee, Total Fee
    bill_history = []
    with open(bills_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == patient_id:
                bill_history.append(row)

    if bill_history:
        print(f"\nBill History for Patient {patient_id}:")
        for bill in bill_history:
            print(f"Date: {bill[1]} | Doctor Fee: ${bill[2]} | Worker Fee: ${bill[3]} | Total Fee: ${bill[4]}")
    else:
        print(f"No bill history found for Patient {patient_id}")
    time.sleep(1)

# Function to view summary statistics
def view_summary():
    # Assuming patients.csv has columns: Patient ID, Patient Name, Patient Age
    # Assuming workers.csv has columns: Worker ID, Worker Name, Worker Age
    # Assuming doctors.csv has columns: Doctor ID, Doctor Name, Doctor Fee
    patient_count = sum(1 for line in open(patients_file)) - 1  # Exclude header
    worker_count = sum(1 for line in open(workers_file)) - 1  # Exclude header
    doctor_count = sum(1 for line in open(doctors_file)) - 1  # Exclude header

    print("\nSummary Statistics:")
    print(f"Total Patients: {patient_count}")
    print(f"Total Workers: {worker_count}")
    print(f"Total Doctors: {doctor_count}")
    time.sleep(1)

# Function to check if a file exists
def file_exists(file_path):
    try:
        with open(file_path, 'r'):
            return True
    except FileNotFoundError:
        return False

# Function to create a directory if it doesn't exist
def create_directory(directory_path):
    if not file_exists(directory_path):
        try:
            os.makedirs(directory_path)
        except OSError:
            print(f"Error creating directory: {directory_path}")

# Function for basic loading animation
def loading_animation():
    animation = "|/-\\"
    for _ in range(10):
        for char in animation:
            sys.stdout.write(f"\rProcessing {char}")
            sys.stdout.flush()
            time.sleep(0.1)

# Main login loop
while True:
    users = load_users()
    print("\nHospital Management System")

    # Prompt for login or create new account
    while True:
        login_choice = input("1. Login\n2. Create New Account\n0. Exit\nEnter your choice (0-2): ")

        if login_choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")

            if validate_login(username, password, users):
                print("Login successful!")
                break
            else:
                print("Invalid username or password. Please try again.")

        elif login_choice == '2':
            new_username = input("Enter a new username: ")
            new_password = input("Enter a new password: ")
            save_user(new_username, new_password)
            print("Account created successfully! You can now log in.")
            break

        elif login_choice == '0':
            print("Exiting the Hospital Management System. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please enter a number between 0 and 2.")

    # Main program loop after successful login
    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. Add Worker")
        print("3. Add Doctor")
        print("4. View Patients")
        print("5. View Workers")
        print("6. View Doctors")
        print("7. Remove Patient")
        print("8. Generate Bill")
        print("9. Make Appointment")
        print("10. View Appointments")
        print("11. Add Prescription")
        print("12. View Prescriptions")
        print("13. Add Employee Schedule")
        print("14. View Employee Schedules")
        print("15. Admit Patient")
        print("16. View Admissions")
        print("17. View Bill History")
        print("18. View Summary")
        print("19. Check File Existence")
        print("20. Create Directory")
        print("21. Clear Screen")
        print("0. Logout and Exit")

        choice = input("Enter your choice (0-21): ")

        try:
            if choice == '1':
                loading_animation()
                patient_id = input("Enter patient ID: ")
                patient_name = input("Enter patient name: ")
                patient_age = input("Enter patient age: ")
                add_details(patients_file, [patient_id, patient_name, patient_age])

            elif choice == '2':
                loading_animation()
                worker_id = input("Enter worker ID: ")
                worker_name = input("Enter worker name: ")
                worker_age = input("Enter worker age: ")
                add_details(workers_file, [worker_id, worker_name, worker_age])

            elif choice == '3':
                loading_animation()
                doctor_id = input("Enter doctor ID: ")
                doctor_name = input("Enter doctor name: ")
                doctor_fee = input("Enter doctor fee: ")
                add_details(doctors_file, [doctor_id, doctor_name, doctor_fee])

            elif choice == '4':
                loading_animation()
                view_details(patients_file)

            elif choice == '5':
                loading_animation()
                view_details(workers_file)

            elif choice == '6':
                loading_animation()
                view_details(doctors_file)

            elif choice == '7':
                loading_animation()
                patient_id = input("Enter patient ID to remove: ")
                remove_details(patients_file, patient_id)

            elif choice == '8':
                loading_animation()
                patient_id = input("Enter patient ID: ")
                doctor_fee = float(input("Enter doctor fee: "))
                worker_fee = float(input("Enter worker fee: "))
                generate_bill(patient_id, doctor_fee, worker_fee)

            elif choice == '9':
                loading_animation()
                patient_id = input("Enter patient ID: ")
                doctor_id = input("Enter doctor ID: ")
                appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
                make_appointment(patient_id, doctor_id, appointment_date)

            elif choice == '10':
                loading_animation()
                view_details(appointments_file)

            elif choice == '11':
                loading_animation()
                patient_id = input("Enter patient ID: ")
                doctor_id = input("Enter doctor ID: ")
                medication = input("Enter medication: ")
                dosage = input("Enter dosage: ")
                add_prescription(patient_id, doctor_id, medication, dosage)

            elif choice == '12':
                loading_animation()
                view_details(prescriptions_file)

            elif choice == '13':
                loading_animation()
                worker_id = input("Enter worker ID: ")
                day = input("Enter day of the week: ")
                shift = input("Enter shift (e.g., Morning, Afternoon, Night): ")
                add_schedule(worker_id, day, shift)

            elif choice == '14':
                loading_animation()
                view_details(schedules_file)

            elif choice == '15':
                loading_animation()
                patient_id = input("Enter patient ID: ")
                admission_date = input("Enter admission date (YYYY-MM-DD): ")
                room_number = input("Enter room number: ")
                admit_patient(patient_id, admission_date, room_number)

            elif choice == '16':
                loading_animation()
                view_details(admissions_file)

            elif choice == '17':
                loading_animation()
                patient_id = input("Enter patient ID to view bill history: ")
                view_bill_history(patient_id)

            elif choice == '18':
                loading_animation()
                view_summary()

            elif choice == '19':
                loading_animation()
                file_path = input("Enter file path to check existence: ")
                if file_exists(file_path):
                    print(f"File {file_path} exists.")
                else:
                    print(f"File {file_path} does not exist.")

            elif choice == '20':
                loading_animation()
                directory_path = input("Enter directory path to create: ")
                create_directory(directory_path)
                print(f"Directory {directory_path} created successfully.")

            elif choice == '21':
                # Simulate clearing the screen by printing newlines
                print('\n' * 100)

            elif choice == '0':
                print("Logging out. Goodbye!")
                sys.exit()

            else:
                print("Invalid choice. Please enter a number between 0 and 21.")

        except ValueError as e:
            print(f"Error: {e}. Please enter a valid input.")
