import pandas as pd
df1=pd.read_csv('form response.csv')
import random
df1.columns = [
    "timestamp",
    "city",
    "area",
    "room_type",
    "rent",
    "wifi",
    "ac",
    "laundry",
    "cleanliness",
    "rating",
    "gender"
]
print(df1.columns)
df1=df1.drop(columns=['timestamp'])
df=df1[df1['city']=='jaipur']
df = df.drop(columns=["city"])


df["rent"] = pd.to_numeric(df["rent"], errors="coerce")

jaipur_areas = [
"Malviya Nagar",
"Jagatpura",
"Vaishali Nagar",
"Mansarovar",
"Tonk Road",
"Sitapura",
"Civil Lines",
"Bani Park",
"Raja Park",
"C-Scheme",
"Vidyadhar Nagar",
"Chitrakoot",
"Ajmer Road",
"Pratap Nagar",
"Gopalpura",
"Jhotwara",
"Kalwar Road",
"Adarsh Nagar",
"Shyam Nagar",
"Sodala"
]

synthetic_data = []

for i in range(500):

    row = df.sample(1).iloc[0]

    synthetic_data.append({
        "area": random.choice(jaipur_areas),
        "room_type": row["room_type"],
        "rent": random.randint(5,12) * 1000,
        "wifi": row["wifi"],
        "ac": row["ac"],
        "laundry": row["laundry"],
        "cleanliness": max(1, min(5, row["cleanliness"] + random.randint(-1,1))),
        "rating": max(1, min(5, row["rating"] + random.randint(-1,1))),
        "gender": row["gender"]
    })

synthetic_df = pd.DataFrame(synthetic_data)


final_df = pd.concat([df, synthetic_df], ignore_index=True)


final_df.to_csv("jaipur_pg_dataset.csv", index=False)
