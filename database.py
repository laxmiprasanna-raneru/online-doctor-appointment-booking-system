import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234560",
    database="doctor_appointment"
)

if connection.is_connected():
    print("MySQL Database Connected Successfully")