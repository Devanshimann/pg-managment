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
plt.figure(figsize=(6,5))
sns.scatterplot(x="rating", y="rent", data=df)
plt.title("Rating vs Rent")
# plt.show()

cheapest = df.groupby("area")["rent"].mean().sort_values().head(5)
df["area_avg_rent"] = df.groupby("area")["rent"].transform("mean")
print("Most Affordable Areas")
print(cheapest)
df["wifi"] = df["wifi"].map({"yes":1,"no":0})
df["ac"] = df["ac"].map({"yes":1,"no":0})
df["laundry"] = df["laundry"].map({"yes":1,"no":0})
df["amenity_score"] = df["wifi"] + df["ac"] + df["laundry"]
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

df["room_type"] = encoder.fit_transform(df["room_type"])
df["gender"] = encoder.fit_transform(df["gender"])
df = pd.get_dummies(df, columns=["area"], drop_first=True)
x=df.drop('rent',axis=1)
y=df['rent']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error, r2_score
# model={
#     "linear":LinearRegression(),
#     "forest":RandomForestRegressor(),
#     "tree":DecisionTreeRegressor()
# }
# for name,models in model.items():
#     models.fit(x_train,y_train)
#     pred=models.predict(x_test)
#     mse=mean_absolute_error(y_test,pred)
#     r2=r2_score(y_test,pred)
#     print(f"mse is {mse} r2 is {r2}")
model=RandomForestRegressor()
model.fit(x_train,y_train)
pred=model.predict(x_test)
mse=mean_absolute_error(y_test,pred)
print(mse)
