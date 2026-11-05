import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.executescript("""
CREATE TABLE Customer (
    Customer_ID INTEGER PRIMARY KEY,
    Customer_Name TEXT NOT NULL,
    City TEXT
);
CREATE TABLE Room (
    Room_ID INTEGER PRIMARY KEY,
    Room_Type TEXT NOT NULL,
    Rent REAL
);
CREATE TABLE Reservation (
    Reservation_ID INTEGER PRIMARY KEY,
    Customer_ID INTEGER,
    Room_ID INTEGER,
    Check_In_Date TEXT,
    Check_Out_Date TEXT,
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID),
    FOREIGN KEY (Room_ID) REFERENCES Room(Room_ID)
);
""")

cur.executemany("INSERT INTO Customer VALUES (?, ?, ?)", [
    (1, "Arun", "Chennai"), (2, "Meena", "Bengaluru"),
    (3, "Bala", "Coimbatore")
])
cur.executemany("INSERT INTO Room VALUES (?, ?, ?)", [
    (101, "Deluxe", 4500.00), (102, "Standard", 2500.00),
    (103, "Deluxe", 5000.00)
])
cur.executemany("INSERT INTO Reservation VALUES (?, ?, ?, ?, ?)", [
    (1, 1, 101, "2026-11-10", "2026-11-12"),
    (2, 2, 102, "2026-11-15", "2026-11-17"),
    (3, 3, 103, "2026-11-20", "2026-11-22")
])

cur.execute("""
SELECT Customer.Customer_Name, Room.Room_Type, Reservation.Check_In_Date
FROM Reservation
JOIN Customer ON Reservation.Customer_ID = Customer.Customer_ID
JOIN Room ON Reservation.Room_ID = Room.Room_ID
WHERE Room.Room_Type = ?
""", ("Deluxe",))
print("Customers who reserved Deluxe rooms:")
for row in cur.fetchall():
    print(row)

conn.close()
