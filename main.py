from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# MySQL Database Connection
connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

if connection.is_connected():
    print("MySQL Database Connected Successfully")


# -------------------------
# Home
# -------------------------

@app.get("/")
def home():
    return "Doctor Appointment Booking System"


# -------------------------
# Patient Registration
# -------------------------

class Patient(BaseModel):
    name: str
    email: str
    phone: str
    password: str


@app.post("/register")
def register_patient(patient: Patient):

    cursor = connection.cursor()

    query = """
        INSERT INTO patients (name, email, phone, password)
        VALUES (%s, %s, %s, %s)
    """

    values = (
        patient.name,
        patient.email,
        patient.phone,
        patient.password
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()

    return {
        "message": "Patient registered successfully"
    }


# -------------------------
# Patient Login
# -------------------------

class LoginData(BaseModel):
    email: str
    password: str


@app.post("/login")
def login_patient(data: LoginData):

    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT * FROM patients
        WHERE email = %s AND password = %s
    """

    cursor.execute(query, (data.email, data.password))

    patient = cursor.fetchone()

    cursor.close()

    if patient:
        return {
            "message": "Login successful",
            "patient_id": patient["patient_id"],
            "name": patient["name"]
        }

    return {
        "message": "Invalid email or password"
    }


# -------------------------
# Book Appointment
# -------------------------

class Appointment(BaseModel):
    patient_id: int
    doctor_name: str
    appointment_date: str
    appointment_time: str


@app.post("/appointments")
def book_appointment(appointment: Appointment):

    cursor = connection.cursor()

    query = """
        INSERT INTO appointments
        (patient_id, doctor_name, appointment_date, appointment_time, status)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        appointment.patient_id,
        appointment.doctor_name,
        appointment.appointment_date,
        appointment.appointment_time,
        "Pending"
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()

    return {
        "message": "Appointment booked successfully"
    }


# -------------------------
# View Appointments
# -------------------------

@app.get("/appointments/{patient_id}")
def get_appointments(patient_id: int):

    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT appointment_id,
               doctor_name,
               appointment_date,
               appointment_time,
               status
        FROM appointments
        WHERE patient_id = %s
    """

    cursor.execute(query, (patient_id,))

    appointments = cursor.fetchall()

    cursor.close()

    return appointments