import pandas as pd

df = pd.DataFrame({
    "Name": ["  arun kumar ", "PRIYA", "  arun kumar "],
    "Department": [" computer science ", "electronics", " computer science "],
    "Phone": ["9876543210", None, "9876543210"]
})
df["Name"] = df["Name"].astype(str).str.strip().str.title()
df["Department"] = df["Department"].astype(str).str.strip().str.upper()
df["Phone"] = df["Phone"].fillna("Not Provided")
df = df.drop_duplicates()
df.to_csv("clean_admissions.csv", index=False)
print(df.to_string(index=False))
print("\\nSaved clean_admissions.csv")
