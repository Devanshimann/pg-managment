import streamlit as st
import pandas as pd
import joblib
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
df = pd.read_csv('processed_pg_dataset.csv')   # for ML
df1 = pd.read_csv("jaipur_pg_dataset.csv")     # for display

# Load model
model = joblib.load('pg_rent_model.pkl')
model_col = joblib.load('model_columns.pkl')

# Title
st.title("Jaipur PG Smart Finder 🏠")
st.write("Find the best PGs in Jaipur based on your preferences.")

# Tabs
tab1, tab2, tab3 = st.tabs([
    "📊 Dashboard",
    "🔍 Find PG",
    "💰 Rent Predictor"
])

# ------------------- TAB 1 -------------------
with tab1:

    st.header("PG Market Insights")

    st.subheader("Rent Distribution")

    fig, ax = plt.subplots()
    sns.histplot(df["rent"], bins=20, ax=ax)
    st.pyplot(fig)

    st.subheader("Average Rent by Area")

    avg_rent = df1.groupby("area")["rent"].mean().round(2)

    fig, ax = plt.subplots(figsize=(10,5))
    avg_rent.sort_values().plot(kind="bar", ax=ax)
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

    st.subheader("Amenities vs Rent")

    col1, col2, col3 = st.columns(3)

    with col1:
        fig, ax = plt.subplots()
        sns.boxplot(x="wifi", y="rent", data=df1, ax=ax)
        ax.set_title("WiFi vs Rent")
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots()
        sns.boxplot(x="ac", y="rent", data=df1, ax=ax)
        ax.set_title("AC vs Rent")
        st.pyplot(fig)

    with col3:
        fig, ax = plt.subplots()
        sns.boxplot(x="laundry", y="rent", data=df1, ax=ax)
        ax.set_title("Laundry vs Rent")
        st.pyplot(fig)

# ------------------- TAB 2 -------------------
with tab2:

    st.header("Find Best PG")

    budget = st.slider("Budget", 5000, 20000, 9000)

    wifi = st.selectbox("WiFi", ["No Preference", "Yes", "No"])
    ac = st.selectbox("AC", ["No Preference", "Yes", "No"])

    # Filter
    results = df1[df1["rent"] <= budget]

    if wifi == "Yes":
        results = results[results["wifi"] == 1]
    elif wifi == "No":
        results = results[results["wifi"] == 0]

    if ac == "Yes":
        results = results[results["ac"] == 1]
    elif ac == "No":
        results = results[results["ac"] == 0]

    if results.empty:
        st.warning("No PG found matching your preferences")

    else:
        best_pg = results.sort_values(
            by=["rating", "rent"],
            ascending=[False, True]
        ).iloc[0]

        area = best_pg["area"]
        rent = best_pg["rent"]
        rating = best_pg["rating"]

        wifi_val = "Yes" if best_pg["wifi"] == 1 else "No"
        ac_val = "Yes" if best_pg["ac"] == 1 else "No"
        laundry_val = "Yes" if best_pg["laundry"] == 1 else "No"

        st.success("✅ Best PG Found!")

        col1, col2, col3 = st.columns(3)

        col1.metric("📍 Area", area)
        col2.metric("💰 Rent", f"₹{rent}")
        col3.metric("⭐ Rating", rating)

        st.write("### Amenities")
        st.write(f"📶 WiFi: {wifi_val}")
        st.write(f"❄️ AC: {ac_val}")
        st.write(f"🧺 Laundry: {laundry_val}")

# ------------------- TAB 3 -------------------
with tab3:

    st.header("Predict PG Rent")

    rating = st.slider("Rating", 1.0, 5.0, 4.0)
    wifi = st.selectbox("WiFi Available", [0, 1])
    ac = st.selectbox("AC Available", [0, 1])
    laundry = st.selectbox("Laundry Available", [0, 1])
    room_type = st.selectbox("Room Type", [0, 1, 2])

    amenity_score = wifi + ac + laundry

    # Create input with correct columns
    input_data = pd.DataFrame(columns=model_col)
    input_data.loc[0] = 0

    input_data["rating"] = rating
    input_data["wifi"] = wifi
    input_data["ac"] = ac
    input_data["laundry"] = laundry
    input_data["amenity_score"] = amenity_score
    input_data["room_type"] = room_type

    prediction = model.predict(input_data)

    st.success(f"Estimated Rent: ₹{int(prediction[0])}")