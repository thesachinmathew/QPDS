import pandas as pd

df = pd.DataFrame({
    "TicketID": [1, 2, 3, 4],
    "Passenger": ["Anu", "Bala", "Charan", "Divya"],
    "Train": ["Express A", "Express B", "Express A", "Express C"],
    "Fare": [450, 600, 450, 750],
    "Status": ["Confirmed", "Waiting", "Confirmed", "Cancelled"]
})
df = df.drop_duplicates(subset=["TicketID"])
confirmed = df[df["Status"] == "Confirmed"]
print("Confirmed tickets:")
print(confirmed.to_string(index=False))
print("\\nTotal confirmed fare:", confirmed["Fare"].sum())
