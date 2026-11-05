import pandas as pd

df = pd.DataFrame({
    "Student": ["Anu", "Bala", "Charan", "Divya"],
    "Maths": [85, 42, 76, 91],
    "Science": [90, 38, 81, 88],
    "English": [78, 55, 69, 95]
})
subjects = ["Maths", "Science", "English"]
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1).round(2)
df["Result"] = df[subjects].ge(40).all(axis=1).map({True: "Pass", False: "Fail"})
print(df.to_string(index=False))
