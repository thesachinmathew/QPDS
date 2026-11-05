import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.executescript("""
CREATE TABLE Student (
    Student_ID INTEGER PRIMARY KEY,
    Student_Name TEXT NOT NULL,
    Department TEXT,
    Year INTEGER
);
CREATE TABLE Course (
    Course_ID INTEGER PRIMARY KEY,
    Course_Name TEXT NOT NULL,
    Credits INTEGER
);
CREATE TABLE Enrollment (
    Enrollment_ID INTEGER PRIMARY KEY,
    Student_ID INTEGER,
    Course_ID INTEGER,
    Semester TEXT,
    FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID),
    FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID)
);
""")

cur.executemany("INSERT INTO Student VALUES (?, ?, ?, ?)", [
    (1, "Anu", "CSE", 2), (2, "Bala", "IT", 3), (3, "Charan", "AI&DS", 2)
])
cur.executemany("INSERT INTO Course VALUES (?, ?, ?)", [
    (101, "Python Programming", 4), (102, "Database Systems", 3),
    (103, "Data Analytics", 4)
])
cur.executemany("INSERT INTO Enrollment VALUES (?, ?, ?, ?)", [
    (1, 1, 101, "Odd 2026"), (2, 1, 102, "Even 2026"),
    (3, 2, 103, "Odd 2026"), (4, 3, 102, "Odd 2026")
])

query = """
SELECT Student.Student_Name, Course.Course_Name
FROM Enrollment
JOIN Student ON Enrollment.Student_ID = Student.Student_ID
JOIN Course ON Enrollment.Course_ID = Course.Course_ID
WHERE Enrollment.Semester = ?
"""
cur.execute(query, ("Odd 2026",))
print("Students enrolled during Odd 2026:")
for row in cur.fetchall():
    print(row)

conn.close()
