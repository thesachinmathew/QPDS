import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.executescript("""
CREATE TABLE Member (
    Member_ID INTEGER PRIMARY KEY,
    Member_Name TEXT NOT NULL,
    Phone TEXT
);
CREATE TABLE Book (
    Book_ID INTEGER PRIMARY KEY,
    Book_Title TEXT NOT NULL,
    Author TEXT
);
CREATE TABLE Issue (
    Issue_ID INTEGER PRIMARY KEY,
    Member_ID INTEGER,
    Book_ID INTEGER,
    Issue_Date TEXT,
    FOREIGN KEY (Member_ID) REFERENCES Member(Member_ID),
    FOREIGN KEY (Book_ID) REFERENCES Book(Book_ID)
);
""")

cur.executemany("INSERT INTO Member VALUES (?, ?, ?)", [
    (1, "Anu", "9876543210"), (2, "Bala", "9876501234")
])
cur.executemany("INSERT INTO Book VALUES (?, ?, ?)", [
    (101, "Python Basics", "R. Kumar"),
    (102, "Data Science", "M. Rao")
])
cur.executemany("INSERT INTO Issue VALUES (?, ?, ?, ?)", [
    (1, 1, 101, "2026-01-15"), (2, 2, 102, "2026-03-10"),
    (3, 1, 102, "2025-12-20")
])

cur.execute("""
SELECT Member.Member_Name, Book.Book_Title, Issue.Issue_Date
FROM Issue
JOIN Member ON Issue.Member_ID = Member.Member_ID
JOIN Book ON Issue.Book_ID = Book.Book_ID
WHERE Issue.Issue_Date > ?
ORDER BY Issue.Issue_Date
""", ("2026-01-01",))
print("Books issued after 1 January 2026:")
for row in cur.fetchall():
    print(row)

conn.close()
