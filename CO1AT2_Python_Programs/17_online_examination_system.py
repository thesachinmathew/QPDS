import pandas as pd

df = pd.DataFrame({
    "Student": ["Asha", "Bala", "Charan", "Divya"],
    "Exam": ["Python", "Python", "DBMS", "DBMS"],
    "Marks": [88, 34, 76, 91],
    "TotalMarks": [100, 100, 100, 100]
})
df["Percentage"] = (df["Marks"] / df["TotalMarks"] * 100).round(2)
df["Result"] = df["Percentage"].apply(lambda x: "Pass" if x >= 40 else "Fail")
print(df.to_string(index=False))
