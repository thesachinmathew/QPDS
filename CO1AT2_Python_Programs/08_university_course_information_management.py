import pandas as pd

courses = pd.DataFrame({
    "CourseID": ["C01", "C02", "C03", "C04"],
    "Course": ["Python", "DBMS", "Networks", "AI"],
    "Credits": [4, 3, 0, 4],
    "Department": ["CSE", "CSE", "IT", "AI"]
})
courses["Credits"] = pd.to_numeric(courses["Credits"], errors="coerce")
valid = courses[courses["Credits"].between(1, 6)]
valid.to_csv("valid_courses.csv", index=False)
print("Valid course details:")
print(valid.to_string(index=False))
