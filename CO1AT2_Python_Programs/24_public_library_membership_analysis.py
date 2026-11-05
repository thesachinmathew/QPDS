import pandas as pd

df = pd.DataFrame({
    "MemberID": [1, 2, 3, 4, 4],
    "MemberName": ["Anu", "Bala", "Charan", "Divya", "Divya"],
    "BooksBorrowed": [5, 3, 8, 2, 2],
    "MembershipType": ["Annual", "Monthly", "Annual", "Monthly", "Monthly"]
})
df = df.drop_duplicates(subset=["MemberID"])
df["BooksBorrowed"] = pd.to_numeric(df["BooksBorrowed"], errors="coerce").fillna(0)
print("Members with borrowing records:")
print(df.to_string(index=False))
print("\\nTotal books borrowed:", int(df["BooksBorrowed"].sum()))
print("\\nBorrowed by membership type:")
print(df.groupby("MembershipType")["BooksBorrowed"].sum().to_string())
