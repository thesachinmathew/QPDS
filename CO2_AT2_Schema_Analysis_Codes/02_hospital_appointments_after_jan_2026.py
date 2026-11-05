import sqlite3

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
    (101, 1, 1, "2026-01-10"), (102, 2, 2, "2026-02-15"),
    (103, 3, 1, "2025-12-20")
])

cur.execute("""
SELECT Patient.Patient_Name, Doctor.Doctor_Name, Appointment.Appointment_Date
FROM Appointment
JOIN Patient ON Appointment.Patient_ID = Patient.Patient_ID
JOIN Doctor ON Appointment.Doctor_ID = Doctor.Doctor_ID
WHERE Appointment.Appointment_Date > ?
ORDER BY Appointment.Appointment_Date
""", ("2026-01-01",))
print("Appointments after 1 January 2026:")
for row in cur.fetchall():
    print(row)

conn.close()
