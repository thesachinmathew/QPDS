import pandas as pd

df = pd.DataFrame({
    "Employee": ["Anu", "Bala", "Charan"],
    "BasicSalary": [25000, 30000, 28000],
    "Allowance": [5000, 6000, 4000],
    "Deduction": [2000, 2500, 1500]
})
df["GrossSalary"] = df["BasicSalary"] + df["Allowance"]
df["NetSalary"] = df["GrossSalary"] - df["Deduction"]
df.to_csv("payroll_report.csv", index=False)
print(df.to_string(index=False))
print("\\nSaved payroll_report.csv")
