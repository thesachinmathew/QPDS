import pandas as pd

df = pd.DataFrame({
    "Student": ["Asha", "Bala", "Charan", "Divya"],
    "Present": [22, 18, 25, 15],
    "TotalClasses": [25, 25, 25, 25]
})
df["AttendancePercent"] = (df["Present"] / df["TotalClasses"] * 100).round(2)
df["Status"] = df["AttendancePercent"].apply(lambda x: "Eligible" if x >= 75 else "Not Eligible")
print(df.to_string(index=False))
