import streamlit as st
import pandas as pd
import joblib
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('processed_pg_dataset.csv')
model=joblib.load('pg_rent_model.pkl')
model_col=joblib.load('model_columns.pkl')
st.title("Jaipur PG Smart Finder 🏠")
st.write("Find the best PGs in Jaipur based on your preferences.")
tab1, tab2, tab3 = st.tabs([
    "📊 Dashboard",
    "🔍 Find PG",
    "💰 Rent Predictor"
])
df1 = pd.read_csv("jaipur_pg_dataset.csv")
with tab1:

    st.header("PG Market Insights")

    st.subheader("Rent Distribution")

    fig, ax = plt.subplots()
    sns.histplot(df["rent"], bins=20, ax=ax)
    st.pyplot(fig)

    st.subheader("Average Rent by Area")

    avg_rent = df1.groupby("area")["rent"].mean().round(2)

    fig, ax = plt.subplots()
    avg_rent.plot(kind="bar", ax=ax)
    st.pyplot(fig)

    st.subheader("Amenities vs Rent")

    col1, col2, col3 = st.columns(3)

    with col1:
      fig, ax = plt.subplots()
      sns.boxplot(x="wifi", y="rent", data=df, ax=ax)
      ax.set_title("WiFi vs Rent")
      st.pyplot(fig)
      
    with col2:
      fig, ax = plt.subplots()
      sns.boxplot(x="ac", y="rent", data=df, ax=ax)
      ax.set_title("AC vs Rent")
      st.pyplot(fig)
    
    with col3:
      fig, ax = plt.subplots()
      sns.boxplot(x="laundry", y="rent", data=df, ax=ax)
      ax.set_title("Laundry vs Rent")
      st.pyplot(fig)
with tab2:

    st.header("Find Best PG")

    budget = st.slider("Budget", 5000, 20000, 9000)

    wifi = st.selectbox("WiFi", ["No Preference", "Yes", "No"])
    ac = st.selectbox("AC", ["No Preference", "Yes", "No"])

    results = df[df["rent"] <= budget]

    if wifi == "Yes":
        results = results[results["wifi"] == 1]

    if wifi == "No":
        results = results[results["wifi"] == 0]

    if ac == "Yes":
        results = results[results["ac"] == 1]

    if ac == "No":
        results = results[results["ac"] == 0]

    results = results.sort_values("score", ascending=False)

    st.write("Top PG Recommendations")
    st.dataframe(results.head(5))
with tab3:

    st.header("Predict PG Rent")

    rating = st.slider("Rating", 1.0, 5.0, 4.0)
    wifi = st.selectbox("WiFi Available", [0,1])
    ac = st.selectbox("AC Available", [0,1])
    laundry = st.selectbox("Laundry Available", [0,1])
    room_type = st.selectbox("Room Type", [0,1,2])

    amenity_score = wifi + ac + laundry

    input_data = pd.DataFrame(columns=model_col)

    input_data.loc[0] = 0
   
    input_data["rating"] = rating
    input_data["rating"] = rating
    input_data["wifi"] = wifi
    input_data["ac"] = ac
    input_data["laundry"] = laundry
    input_data["amenity_score"] = amenity_score
    input_data["room_type"] = room_type

    prediction = model.predict(input_data)

    st.success(f"Estimated Rent: ₹{int(prediction[0])}")
