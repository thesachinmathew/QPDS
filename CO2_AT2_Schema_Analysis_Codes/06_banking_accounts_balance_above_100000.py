import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.executescript("""
CREATE TABLE Customer (
    Customer_ID INTEGER PRIMARY KEY,
    Customer_Name TEXT NOT NULL,
    City TEXT
);
CREATE TABLE Account (
    Account_No TEXT PRIMARY KEY,
    Customer_ID INTEGER,
    Account_Type TEXT,
    Balance REAL,
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID)
);
CREATE TABLE Transactions (
    Transaction_ID INTEGER PRIMARY KEY,
    Account_No TEXT,
    Transaction_Date TEXT,
    Amount REAL,
    FOREIGN KEY (Account_No) REFERENCES Account(Account_No)
);
""")

cur.executemany("INSERT INTO Customer VALUES (?, ?, ?)", [
    (1, "Arun", "Chennai"), (2, "Priya", "Madurai"), (3, "Bala", "Salem")
])
cur.executemany("INSERT INTO Account VALUES (?, ?, ?, ?)", [
    ("A1001", 1, "Savings", 150000.00),
    ("A1002", 2, "Current", 85000.00),
    ("A1003", 3, "Savings", 220000.00)
])

cur.execute("""
SELECT Customer.Customer_Name, Account.Account_No, Account.Balance
FROM Customer
JOIN Account ON Customer.Customer_ID = Account.Customer_ID
WHERE Account.Balance > ?
""", (100000,))
print("Accounts with balance above Rs. 1,00,000:")
for row in cur.fetchall():
    print(row)

conn.close()
