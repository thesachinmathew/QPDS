import pandas as pd

df = pd.DataFrame({
    "ClaimID": [501, 502, 503, 504],
    "Customer": ["Asha", "Bala", "Charan", "Divya"],
    "ClaimAmount": [25000, 50000, -3000, 18000],
    "Status": ["Approved", "Pending", "Rejected", "Approved"]
})
df["ClaimAmount"] = pd.to_numeric(df["ClaimAmount"], errors="coerce")
valid = df[df["ClaimAmount"].ge(0)]
approved = valid[valid["Status"] == "Approved"]
print("Valid approved claims:")
print(approved.to_string(index=False))
print("\\nTotal approved amount:", approved["ClaimAmount"].sum())
