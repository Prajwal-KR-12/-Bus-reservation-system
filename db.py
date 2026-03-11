import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Prajwal@123",
    database="bus_reservations"
)

cursor = db.cursor()