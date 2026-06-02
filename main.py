from Database.appointments import Appointment
from Database.patient import Patient
from Database.doctor import Doctor
from Database.bill import Bill
from Database.patient import Patient

def patient_menu():
    patient = Patient()
    while True:
        print("\nPatient Menu")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Search Patient")
        print("6. Back")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            patient.add_patients()

        elif choice == "2":
            patient.view_patients()

        elif choice == "3":
            patient.update_patients()

        elif choice == "4":
            patient.delete_patients()

        elif choice == "5":
            patient.search_patients()

        elif choice == "6":
            break
        else:
            print("Invalid choice!")
def doctor_menu():
    doctor=Doctor()
    while True:
        print("\nDoctor Menu")
        print("1. Add Doctor")
        print("2. View Doctors")
        print("3. Update Doctor")
        print("4. Delete Doctor")
        print("5. Search Doctor")
        print("6. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            doctor.add_doctor()

        elif choice == "2":
            doctor.view_doctors()

        elif choice == "3":
            doctor.update_doctors()

        elif choice == "4":
            doctor.delete_doctors()

        elif choice == "5":
            doctor.search_by_specialization()

        elif choice == "6":
            break
        else:
            print("Invalid choice!")
def appointment_menu():
    appointment=Appointment()
    while True:
        print("\nAppointment Menu")
        print("1. Book Appointment")
        print("2. View Appointments")
        print("3. Update Appointment")
        print("4. Cancel Appointment")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            appointment.book_appointment()

        elif choice == "2":
            appointment.view_appointments()

        elif choice == "3":
            appointment.update_appointment()

        elif choice == "4":
            appointment.cancel_appointment()

        elif choice == "5":
            break
        else:
            print("Invalid choice!")
def bill_menu():
    bill=Bill()
    while True:
        print("\nBill Menu")
        print("1. Generate Bill")
        print("2. View Bills")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            bill.generate_bill()

        elif choice == "2":
            bill.view_bills()

        elif choice == "3":
            break
        else:
            print("Invalid choice!")
def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Patient Management")
        print("2. Doctor Management")
        print("3. Appointment Management")
        print("4. Bill Management")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            patient_menu()

        elif choice == "2":
            doctor_menu()

        elif choice == "3":
            appointment_menu()

        elif choice == "4":
            bill_menu()

        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
    