import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.executescript("""
CREATE TABLE Student (
    Student_ID INTEGER PRIMARY KEY,
    Student_Name TEXT NOT NULL,
    Department TEXT
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

cur.executemany("INSERT INTO Student VALUES (?, ?, ?)", [
    (1, "Anu", "CSE"), (2, "Bala", "IT"), (3, "Charan", "AI&DS")
])
cur.executemany("INSERT INTO Course VALUES (?, ?, ?)", [
    (101, "Python Programming", 4), (102, "Database Systems", 3),
    (103, "Data Analytics", 5)
])
cur.executemany("INSERT INTO Enrollment VALUES (?, ?, ?, ?)", [
    (1, 1, 101, "Odd 2026"), (2, 1, 102, "Odd 2026"),
    (3, 2, 103, "Odd 2026"), (4, 3, 102, "Even 2026")
])

cur.execute("""
SELECT Student.Student_Name, Course.Course_Name, Enrollment.Semester
FROM Enrollment
JOIN Student ON Enrollment.Student_ID = Student.Student_ID
JOIN Course ON Enrollment.Course_ID = Course.Course_ID
WHERE Course.Credits > 3
""")
print("Students enrolled in courses with more than 3 credits:")
for row in cur.fetchall():
    print(row)

conn.close()
