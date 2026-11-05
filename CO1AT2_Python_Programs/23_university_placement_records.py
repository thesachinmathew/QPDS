import pandas as pd

df = pd.DataFrame({
    "Student": ["Asha", "Bala", "Charan", "Divya"],
    "Company": ["TCS", "Infosys", "Google", "TCS"],
    "PackageLPA": [4.5, 3.8, 18.0, 5.2],
    "Status": ["Placed", "Placed", "Placed", "Not Placed"]
})
placed = df[df["Status"] == "Placed"]
print("Placed students:")
print(placed.to_string(index=False))
print("\\nAverage placement package:", round(placed["PackageLPA"].mean(), 2), "LPA")
