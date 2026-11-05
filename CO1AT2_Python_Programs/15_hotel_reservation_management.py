import pandas as pd

df = pd.DataFrame({
    "BookingID": [1, 2, 3, 4],
    "Guest": ["Arun", "Bala", "Charan", "Divya"],
    "RoomType": ["Single", "Double", "Suite", "Double"],
    "Nights": [2, 3, 1, 2],
    "Status": ["Confirmed", "Pending", "Confirmed", "Cancelled"]
})
df = df.drop_duplicates(subset=["BookingID"])
confirmed = df[df["Status"] == "Confirmed"]
print("Confirmed bookings:")
print(confirmed.to_string(index=False))
print("\\nTotal confirmed room nights:", confirmed["Nights"].sum())
