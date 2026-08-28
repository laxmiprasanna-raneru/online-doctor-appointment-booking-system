# Online Doctor Appointment Booking System

A web-based Doctor Appointment Booking System developed using HTML, CSS, JavaScript, FastAPI, and MySQL.

## Features

- Patient Registration
- Patient Login
- Doctor Details
- Book Doctor Appointments
- View Appointments
- Health Reports
- Appointment Status

## Technologies Used

- HTML
- CSS
- JavaScript
- Python
- FastAPI
- MySQL

## Project Structure

```text
online-doctor-appointment-booking-system/
│
├── appointments.html
├── database.py
├── doctor.html
├── doctor_appointment.sql
├── health_reports.html
├── index.html
├── login.html
├── main.py
├── register.html
├── reports.html
└── README.md


## How to Run

### 1. Start the Backend

Open the terminal in the project folder:

```text
python -m uvicorn main:app --reload

The backend will run at:

http://127.0.0.1:8000
2. Start the Frontend

Open another terminal in the project folder and run:

python -m http.server 5500

Then open:

http://localhost:5500
