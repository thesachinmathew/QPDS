import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.executescript("""
CREATE TABLE Passenger (
    Passenger_ID INTEGER PRIMARY KEY,
    Passenger_Name TEXT NOT NULL,
    City TEXT
);
CREATE TABLE Flight (
    Flight_ID INTEGER PRIMARY KEY,
    Flight_Name TEXT NOT NULL,
    Destination TEXT
);
CREATE TABLE Booking (
    Booking_ID INTEGER PRIMARY KEY,
    Passenger_ID INTEGER,
    Flight_ID INTEGER,
    Travel_Date TEXT,
    FOREIGN KEY (Passenger_ID) REFERENCES Passenger(Passenger_ID),
    FOREIGN KEY (Flight_ID) REFERENCES Flight(Flight_ID)
);
""")

cur.executemany("INSERT INTO Passenger VALUES (?, ?, ?)", [
    (1, "Arun", "Chennai"), (2, "Priya", "Mumbai"),
    (3, "Bala", "Bengaluru")
])
cur.executemany("INSERT INTO Flight VALUES (?, ?, ?)", [
    (101, "AI 440", "Delhi"), (102, "6E 215", "Mumbai"),
    (103, "UK 820", "Delhi")
])
cur.executemany("INSERT INTO Booking VALUES (?, ?, ?, ?)", [
    (1, 1, 101, "2026-11-08"), (2, 2, 102, "2026-11-09"),
    (3, 3, 103, "2026-11-12")
])

cur.execute("""
SELECT Passenger.Passenger_Name, Flight.Flight_Name,
       Flight.Destination, Booking.Travel_Date
FROM Booking
JOIN Passenger ON Booking.Passenger_ID = Passenger.Passenger_ID
JOIN Flight ON Booking.Flight_ID = Flight.Flight_ID
WHERE Flight.Destination = ?
ORDER BY Booking.Travel_Date
""", ("Delhi",))
print("Passengers travelling to Delhi:")
for row in cur.fetchall():
    print(row)

conn.close()
