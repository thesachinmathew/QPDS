import pandas as pd

df = pd.DataFrame({
    "City": ["Chennai", "Madurai", "Coimbatore", "Salem"],
    "Temperature": [32, 35, 28, 31],
    "Humidity": [70, 65, 80, 75]
})
df["Temperature"] = pd.to_numeric(df["Temperature"], errors="coerce")
average = df["Temperature"].mean()
df["TemperatureStatus"] = df["Temperature"].apply(
    lambda t: "Above Average" if t > average else "Normal"
)
print("Average temperature:", round(average, 2))
print(df.to_string(index=False))
