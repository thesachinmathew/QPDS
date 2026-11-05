import pandas as pd

df = pd.DataFrame({
    "AppointmentID": [101, 102, 103, 104],
    "Patient": ["Anu", "Bala", "Charan", "Divya"],
    "Doctor": ["Dr Rao", "Dr Kumar", "Dr Rao", "Dr Mehta"],
    "Date": ["2026-11-05", "2026-11-05", "2026-11-06", "2026-11-06"],
    "Status": ["Booked", "Cancelled", "Booked", "Booked"]
})
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
available = df[df["Status"] == "Booked"].sort_values(["Date", "Doctor"])
print("Booked appointments:")
print(available.to_string(index=False))
