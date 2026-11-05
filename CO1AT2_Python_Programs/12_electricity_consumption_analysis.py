import pandas as pd

df = pd.DataFrame({
    "City": ["Chennai", "Chennai", "Madurai", "Madurai", "Salem"],
    "Month": ["Jan", "Feb", "Jan", "Feb", "Jan"],
    "Consumption": [1200, 1350, 900, 1100, 800]
})
df["Consumption"] = pd.to_numeric(df["Consumption"], errors="coerce")
print("Average consumption:", df["Consumption"].mean())
print("\\nTotal consumption by city:")
print(df.groupby("City")["Consumption"].sum().to_string())
