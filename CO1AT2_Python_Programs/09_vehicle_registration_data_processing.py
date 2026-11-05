import pandas as pd

df = pd.DataFrame({
    "RegistrationNo": ["TN01AB1234", "TN02CD5678", "TN01AB1234", "TN03EF9012"],
    "Owner": ["Arun", "Bala", "Arun", "Divya"],
    "VehicleType": ["Car", "Bike", "Car", "Truck"],
    "Year": [2020, 2022, 2020, 2018]
})
df = df.drop_duplicates(subset=["RegistrationNo"])
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df = df[df["Year"].between(1900, 2026)]
df.to_csv("clean_vehicles.csv", index=False)
print(df.to_string(index=False))
