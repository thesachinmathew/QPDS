import pandas as pd

df = pd.DataFrame({
    "PatientID": [1, 2, 3, 4],
    "Age": [25, 150, -4, 42],
    "Gender": ["Male", "Female", "Other", "Male"],
    "BloodGroup": ["A+", "B+", "X", "O+"]
})
valid_age = df["Age"].between(0, 120)
valid_blood = df["BloodGroup"].isin(["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
print("Invalid patient records:")
print(df[~(valid_age & valid_blood)].to_string(index=False))
print("\\nValid patient records:")
print(df[valid_age & valid_blood].to_string(index=False))
