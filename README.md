# Hospital Management System (Python + MySQL + Streamlit)
A full-stack Hospital Management System built using Python, MySQL, and Streamlit, designed to manage patients, 
doctors, appointments, and billing efficiently through a simple and interactive web interface.
# Features
-Patient Management
-Add new patients
-View all patients
-Update patient details
-Delete patient records
-Search patient by name

# Doctor Management
-Add doctors with specialization
-View all doctors
-Update doctor information
-Delete doctor records
-Search doctor by specialization

# Appointment System
-Book appointments with doctor availability check
-Prevent double booking for same doctor & date
-View all appointments
-Update appointment details
-Cancel appointments

# Billing System
-Generate bills with breakdown:
-Consultation fee
-Medicine charges
-Room charges
-Auto calculate total amount
-View and search bills by patient ID

# Tech Stack
-Frontend: Streamlit
-Backend: Python (OOP based architecture)
-Database: MySQL
-Connector: mysql-connector-python

# Project Structure
Hospital-Management-System/
│
├── Database/
│   ├── database.py
│   ├── patient.py
│   ├── doctor.py
│   ├── appointments.py
│   └── bill.py
│
├── app.py
├── main.py
├── requirements.txt
└── README.md

# Database Schema
Patients Table
patient_id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(100),
age INT,
gender VARCHAR(20)

Doctors Table
doctor_id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(100),
specialization VARCHAR(100)

# How to Run the Project
# Clone the repository
git clone https://github.com/your-username/hospital-management-system.git
cd hospital-management-system

# Install Dependencies
pip install -r requirements.txt

# SetUp MySQL Database
CREATE DATABASE hospital_db;

# Run Streamlit
streamlit run app.py

# Business Logic Highlights
Prevents booking of doctor if already scheduled on same date
Validates patient and doctor existence before operations
Ensures clean database transactions using commit/rollback
Modular OOP-based design for scalability

# Key Learnings
Python OOP design patterns
MySQL CRUD operations
Streamlit UI development
Backend validation logic
Real-world system design flow

# Author 

Riya Jangid
Python Developer | AI & Backend Enthusiast
