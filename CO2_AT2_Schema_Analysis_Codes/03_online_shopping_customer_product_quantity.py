import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.executescript("""
CREATE TABLE Customer (
    Customer_ID INTEGER PRIMARY KEY,
    Customer_Name TEXT NOT NULL,
    City TEXT
);
CREATE TABLE Product (
    Product_ID INTEGER PRIMARY KEY,
    Product_Name TEXT NOT NULL,
    Price REAL
);
CREATE TABLE Orders (
    Order_ID INTEGER PRIMARY KEY,
    Customer_ID INTEGER,
    Product_ID INTEGER,
    Quantity INTEGER,
    Order_Date TEXT,
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID),
    FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID)
);
""")

cur.executemany("INSERT INTO Customer VALUES (?, ?, ?)", [
    (1, "Anu", "Chennai"), (2, "Bala", "Coimbatore")
])
cur.executemany("INSERT INTO Product VALUES (?, ?, ?)", [
    (101, "Keyboard", 850.00), (102, "Mouse", 450.00)
])
cur.executemany("INSERT INTO Orders VALUES (?, ?, ?, ?, ?)", [
    (1, 1, 101, 2, "2026-10-20"), (2, 2, 102, 1, "2026-10-22"),
    (3, 1, 102, 3, "2026-10-25")
])

# The question text lists the fields to retrieve but does not show a filter condition.
cur.execute("""
SELECT Customer.Customer_Name, Product.Product_Name, Orders.Quantity
FROM Orders
JOIN Customer ON Orders.Customer_ID = Customer.Customer_ID
JOIN Product ON Orders.Product_ID = Product.Product_ID
ORDER BY Orders.Order_ID
""")
print("Customer, product and quantity for all orders:")
for row in cur.fetchall():
    print(row)

conn.close()
