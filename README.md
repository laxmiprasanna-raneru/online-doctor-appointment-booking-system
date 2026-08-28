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
```

## How to Run

### 1. Start the Backend

Open the terminal in the project folder:

```text
python -m uvicorn main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

### 2. Start the Frontend

Open another terminal in the project folder and run:

```text
python -m http.server 5500
```

Then open:

```text
http://localhost:5500
```

## Database

This project uses MySQL to store patient and appointment information.

Database credentials are stored using environment variables in a `.env` file.

Sensitive information such as database passwords is not included in the GitHub repository.

## Author

Laxmi Prasanna Raneru
