import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('jaipur_pg_dataset.csv')
df["gender"] = df["gender"].replace("boys pf", "boys pg")
# print(df.isnull().sum())
# print("Duplicate rows:", df.duplicated().sum())
df=df.drop_duplicates()
# print(df.describe())
plt.figure(figsize=(8,5))
sns.histplot(df["rent"], bins=20)
plt.title("Rent Distribution in Jaipur PGs")
plt.xlabel("Rent")
plt.ylabel("Count")
# plt.show()
sns.boxplot(x="room_type", y="rent", data=df)
plt.title("Rent vs Room Type")
# plt.show()

avg_rent_area = df.groupby("area")["rent"].mean().sort_values()

plt.figure(figsize=(10,6))
avg_rent_area.plot(kind="bar")
plt.title("Average Rent by Area in Jaipur")
plt.ylabel("Rent")

plt.figure(figsize=(6,5))
sns.boxplot(x="wifi", y="rent", data=df)
plt.title("WiFi vs Rent")


plt.figure(figsize=(6,5))
sns.boxplot(x="ac", y="rent", data=df)
plt.title("AC vs Rent")


plt.figure(figsize=(6,5))
sns.boxplot(x="laundry", y="rent", data=df)
plt.title("Laundry vs Rent")
# plt.show()

cheapest = df.groupby("area")["rent"].mean().sort_values().head(5)

print("Most Affordable Areas")
print(cheapest)

