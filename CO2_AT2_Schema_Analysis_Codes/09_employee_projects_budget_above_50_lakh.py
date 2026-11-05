import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.executescript("""
CREATE TABLE Employee (
    Employee_ID INTEGER PRIMARY KEY,
    Employee_Name TEXT NOT NULL,
    Department TEXT
);
CREATE TABLE Project (
    Project_ID INTEGER PRIMARY KEY,
    Project_Name TEXT NOT NULL,
    Budget REAL
);
CREATE TABLE Works_On (
    Employee_ID INTEGER,
    Project_ID INTEGER,
    Role TEXT,
    PRIMARY KEY (Employee_ID, Project_ID),
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID),
    FOREIGN KEY (Project_ID) REFERENCES Project(Project_ID)
);
""")

cur.executemany("INSERT INTO Employee VALUES (?, ?, ?)", [
    (1, "Anu", "Development"), (2, "Bala", "Testing"),
    (3, "Charan", "Data Science")
])
cur.executemany("INSERT INTO Project VALUES (?, ?, ?)", [
    (101, "ERP Upgrade", 7500000),
    (102, "Website Redesign", 3000000),
    (103, "AI Platform", 9000000)
])
cur.executemany("INSERT INTO Works_On VALUES (?, ?, ?)", [
    (1, 101, "Developer"), (2, 102, "Tester"),
    (3, 103, "ML Engineer"), (1, 103, "Team Lead")
])

cur.execute("""
SELECT Employee.Employee_Name, Project.Project_Name, Works_On.Role
FROM Works_On
JOIN Employee ON Works_On.Employee_ID = Employee.Employee_ID
JOIN Project ON Works_On.Project_ID = Project.Project_ID
WHERE Project.Budget > ?
""", (5000000,))
print("Employees working on projects with budget above Rs. 50,00,000:")
for row in cur.fetchall():
    print(row)

conn.close()
