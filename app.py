import streamlit as st
from Database.patient import Patient
from Database.doctor import Doctor
from Database.appointments import Appointment
from Database.bill import Bill

patient = Patient()
doctor = Doctor()
appointment = Appointment()
bill = Bill()

st.title("Hospital Management System")

def main():
    menu = st.sidebar.selectbox(
        "Select Module",
        ["Patients", "Doctors", "Appointments", "Bills"]
    )

    if menu == "Patients":
        st.header("Patient Management")
        action = st.selectbox(
            "Choose Action",
            ["Add", "View", "Search", "Update", "Delete"])

        if action == "Add":
            name = st.text_input("Patient Name")
            age = st.number_input("Patient Age", min_value=0)
            gender = st.selectbox("Patient Gender", ["Male", "Female", "Other"])

            if st.button("Add Patient"):
                if not name.strip():
                    st.error("Patient name is required")

                elif not age:
                    st.error("Patient age is required")

                elif not gender:
                    st.error("Patient gender is required")

                else:
                    success = patient.add_patients(name, age, gender)

                    if success:
                        st.success("Patient Added Successfully")

        elif action == "View":
            if st.button("View Patients"):
                patients=patient.view_patients()
                if patients:
                    for p in patients:
                        st.write(f"ID: {p[0]}, Name: {p[1]}, Age: {p[2]}, Gender: {p[3]}")
                else:
                    st.warning("No patients found")

        elif action == "Search":
            st.subheader("Search Patient")
            search_name = st.text_input("Enter patient name to search")
            if st.button("Search"):
                if not search_name.strip():
                    st.error("Patient name is required for search")
                else:
                    patients = patient.search_patients(search_name)
                    if patients:
                        for p in patients:
                            st.write(f"ID: {p[0]}, Name: {p[1]}, Age: {p[2]}, Gender: {p[3]}")
                    else:
                        st.warning("No patients found with that name")

        elif action == "Update":
            patient_id = st.number_input("Enter patient ID to update", min_value=1)
            new_name = st.text_input("Enter new patient name")
            new_age = st.number_input("Enter new patient age", min_value=0)
            new_gender = st.selectbox("Enter new patient gender", ["Male", "Female", "Other"])
            if st.button("Update Patient"):
                    if not new_name.strip():
                        st.error("Patient name is required")
                    elif not new_age:
                        st.error("Patient age is required")
                    elif not new_gender:
                        st.error("Patient gender is required")
                    else:
                        success=patient.update_patients(patient_id, new_name, new_age, new_gender)
                        if success:
                            st.success("Patient Updated Successfully")
                        else:
                            st.error("Patient ID not found")
                    

        elif action == "Delete":
            patient_id = st.number_input("Enter patient ID to delete", min_value=1)
            if st.button("Delete Patient"):
                if not patient_id:
                    st.error("Patient ID is required for deletion")
                else:
                    success = patient.delete_patients(patient_id)
                    if success:
                        st.success("Patient Deleted Successfully")
                    else:
                        st.error("Patient ID not found")

        
    elif menu == "Doctors":
        st.header("Doctor Management")
        action = st.selectbox(
            "Choose Action",
            ["Add", "View", "Search", "Update", "Delete"])
        
        if action=="Add":
            name = st.text_input("Doctor Name: ")
            specialization = st.text_input("Specialization")
            if st.button("Add Doctor"):
                if not name.strip():
                    st.error("Doctor name is required")
                elif not specialization.strip():
                    st.error("Doctor specialization is required")
                else:
                    success = doctor.add_doctor(name, specialization)
                    if success:
                        st.success("Doctor Added Successfully")
                    else:
                        st.error("Failed to add doctor")

        elif action=="View":
            if st.button("View Doctors"):
                doctors=doctor.view_doctors()
                if doctors:
                    for d in doctors:
                        st.write(f"ID: {d[0]}, Name: {d[1]}, Specialization: {d[2]}")
                else:
                    st.warning("No doctors found")

        elif action=="Search":
            st.subheader("Search Doctor")
            search_specialization = st.text_input("Enter specialization to search doctor: ")
            if st.button("Search Doctor"):
                if not search_specialization.strip():
                    st.error("Specialization is required for search")
                else:
                    doctors = doctor.search_by_specialization(search_specialization)
                    if doctors:
                        for d in doctors:
                            st.write(f"ID: {d[0]}, Name: {d[1]}, Specialization: {d[2]}")
                    else:
                        st.warning("No doctors found with that specialization")
        elif action=="Update":
            st.subheader("Update Doctor")
            doctor_id = st.number_input("Enter doctor ID to update", min_value=1)
            new_name = st.text_input("Enter new doctor name")
            new_specialization = st.text_input("Enter new doctor specialization")
            if st.button("Update Doctor"):
                if not new_name.strip():
                    st.error("Doctor name is required") 
                elif not new_specialization.strip():
                    st.error("Doctor specialization is required")
                else:
                    success = doctor.update_doctors(doctor_id, new_name, new_specialization)
                    if success:
                        st.success("Doctor Updated Successfully")
                    else:
                        st.error("Doctor ID not found")

        elif action=="Delete":
            st.subheader("Delete Doctor")
            doctor_id = st.number_input("Enter doctor ID to delete", min_value=1)
            if st.button("Delete Doctor"):
                if not doctor_id:
                    st.error("Doctor ID is required for deletion")
                else:
                    success = doctor.delete_doctors(doctor_id)
                    if success:
                        st.success("Doctor Deleted Successfully")
                    else:
                        st.error("Doctor ID not found")

    elif menu == "Appointments":
        st.header("Appointment Management")
        action = st.selectbox(
            "Choose Action",
            ["Book Appointment", "View Appointments", "Update Appointment", "Cancel Appointment"])
        
        if action == "Book Appointment":
            st.subheader("Book Appointment")

            patient_id = st.number_input("Patient ID", min_value=1)
            doctor_id = st.number_input("Doctor ID", min_value=1)
            appointment_date = st.date_input("Appointment Date")

            if st.button("Book Appointment"):
                if not patient_id:
                    st.error("Patient ID is required")
                elif not doctor_id:
                    st.error("Doctor ID is required")
                elif not appointment_date:
                    st.error("Appointment date is required")
                else:
                    success = appointment.book_appointment(patient_id, doctor_id, appointment_date)
                    if success:
                        st.success("Appointment Booked Successfully")
                    else:
                        st.error("Failed to book appointment:Doctor Busy")

        elif action == "View Appointments":

            if st.button("View Appointments"):
                appointments=appointment.view_appointments()

                if appointments:
                    for a in appointments:
                        st.write(f"ID: {a[0]}, Patient ID: {a[1]}, Doctor ID: {a[2]}, Date: {a[3]}")
                else:
                    st.warning("No appointments found")

        elif action == "Update Appointment":

            st.subheader("Update Appointment")

            appointment_id = st.number_input("Enter appointment ID to update", min_value=1)
            new_patient_id = st.number_input("Enter new patient ID", min_value=1)
            new_doctor_id = st.number_input("Enter new doctor ID", min_value=1)
            new_appointment_date = st.date_input("Enter new appointment date")
            if st.button("Update Appointment"):
                if not appointment_id:
                    st.error("Appointment ID is required for update")
                elif not new_patient_id:
                    st.error("New patient ID is required")
                elif not new_doctor_id:
                    st.error("New doctor ID is required")
                elif not new_appointment_date:
                    st.error("New appointment date is required")
                else:
                    success = appointment.update_appointment(appointment_id, new_patient_id, new_doctor_id, new_appointment_date)
                    if success:
                        st.success("Appointment Updated Successfully")
                    else:
                        st.error("Appointment ID not found")

        elif action == "Cancel Appointment":
            st.subheader("Cancel Appointment")
            appointment_id = st.number_input("Enter appointment ID to cancel", min_value=1)
            if st.button("Cancel Appointment"):
                if not appointment_id:
                    st.error("Appointment ID is required for cancellation")
                else:
                    success = appointment.cancel_appointment(appointment_id)
                    if success:
                        st.success("Appointment Cancelled Successfully")
                    else:
                        st.error("Appointment ID not found")

    elif menu == "Bills":
        st.header("Billing Management")

        action=st.selectbox("Choose Action", ["Generate Bill", "View Bills", "Search Bills by Patient ID"])
        if action=="Generate Bill":
            st.subheader("Generate Bill")
            patient_id = st.number_input("Patient ID", min_value=1)
            consultation_fee = st.number_input("Consultation Fee", min_value=0.0)
            medicine_charges = st.number_input("Medicine Charges", min_value=0.0)
            room_charges = st.number_input("Room Charges", min_value=0.0)
            bill_date= st.date_input("Bill Date")

            Total_Amount= consultation_fee + medicine_charges + room_charges
            st.write(f"Total Amount: {Total_Amount}")

            if st.button("Generate Bill"):
                if not patient_id:
                    st.error("Patient ID is required")
                elif consultation_fee<0:
                     st.error("Invalid consultation fee")
                elif medicine_charges<0:
                    st.error("Invalid medicine charges")
                elif room_charges<0:
                    st.error("Invalid room charges")
                else:
                    success = bill.generate_bill(patient_id, consultation_fee, medicine_charges, room_charges,Total_Amount)
                    if success:
                        st.success("Bill Generated Successfully")
                    else:
                        st.error("Failed to generate bill")

        elif action=="View Bills":
            st.subheader("View Bills")

            if st.button("View Bills"):
                bills=bill.view_bills()

                if bills:
                    for b in bills:
                        st.write(f"""
                                Patient ID: {b[1]}
                                Consultation Fee: {b[2]}
                                Medicine Charges: {b[3]}
                                Room Charges: {b[4]}
                                Total Amount: {b[5]}
                                Bill Date: {b[8]}
                                """)
                else:
                    st.warning("No bills found")

        elif action=="Search Bills by Patient ID":
            st.subheader("Search Bills by Patient ID")

            search_patient_id = st.number_input("Enter patient ID to search bills", min_value=1)
            if st.button("Search"):
                if not search_patient_id:
                    st.error("Patient ID is required for searching bills")
                else:
                    bills = bill.search_bills(search_patient_id)
                    if bills:
                        for b in bills:
                            st.write(f"ID: {b[0]}, Patient ID: {b[1]}, Amount: {b[2]}, Date: {b[3]}")
                    else:
                        st.warning("No bills found for this patient")
        
if __name__ == "__main__":
    main()