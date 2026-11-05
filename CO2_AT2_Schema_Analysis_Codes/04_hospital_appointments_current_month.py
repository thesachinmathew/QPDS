import sqlite3
from datetime import date

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.executescript("""
CREATE TABLE Doctor (
    Doctor_ID INTEGER PRIMARY KEY,
    Doctor_Name TEXT NOT NULL,
    Specialization TEXT
);
CREATE TABLE Patient (
    Patient_ID INTEGER PRIMARY KEY,
    Patient_Name TEXT NOT NULL,
    Age INTEGER
);
CREATE TABLE Appointment (
    Appointment_ID INTEGER PRIMARY KEY,
    Patient_ID INTEGER,
    Doctor_ID INTEGER,
    Appointment_Date TEXT,
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID),
    FOREIGN KEY (Doctor_ID) REFERENCES Doctor(Doctor_ID)
);
""")

cur.executemany("INSERT INTO Doctor VALUES (?, ?, ?)", [
    (1, "Dr. Kumar", "Cardiology"), (2, "Dr. Priya", "Neurology")
])
cur.executemany("INSERT INTO Patient VALUES (?, ?, ?)", [
    (1, "Arun", 35), (2, "Meena", 28), (3, "Bala", 42)
])
cur.executemany("INSERT INTO Appointment VALUES (?, ?, ?, ?)", [
    (101, 1, 1, "2026-11-06"), (102, 2, 2, "2026-11-12"),
    (103, 3, 1, "2026-10-29")
])

cur.execute("""
SELECT Doctor.Doctor_Name, Patient.Patient_Name, Appointment.Appointment_Date
FROM Appointment
JOIN Doctor ON Appointment.Doctor_ID = Doctor.Doctor_ID
JOIN Patient ON Appointment.Patient_ID = Patient.Patient_ID
WHERE strftime('%Y-%m', Appointment.Appointment_Date) = strftime('%Y-%m', 'now')
ORDER BY Appointment.Appointment_Date
""")
print("Appointments scheduled during the current month:")
for row in cur.fetchall():
    print(row)

conn.close()
