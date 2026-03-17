🏠 Jaipur PG Smart Finder

A Machine Learning-powered web application that helps users explore and find Paying Guest (PG) accommodations in Jaipur area based on budget, amenities, and preferences. The system also predicts the estimated rent of a PG using a trained ML model.

The project combines data analysis, machine learning, and interactive visualization using Streamlit.

🚀 Live Application

You can access the deployed app here:

🔗 https://pg-managment-001.streamlit.app/

📌 Features<br>
📊 PG Market Dashboard

Interactive insights about the PG market in Jaipur:

Rent distribution across PGs

Average rent by area

Amenities vs rent comparison

Rating vs rent analysis

🔍 Find PG

Users can search for PG accommodations area using filters:

Budget

WiFi availability

AC availability

Room type

The system returns the best PG options matching the criteria.

💰 Rent Prediction

The application uses a Machine Learning model to predict expected PG rent based on:

PG rating

Amenities (WiFi, AC, Laundry)

Room type

This helps users estimate how much a PG should cost.

🧠 Machine Learning Workflow<br>
1️⃣ Data Collection

Google Form responses

Synthetic dataset generation

2️⃣ Data Cleaning

Removed duplicates

Standardized categorical values

3️⃣ Exploratory Data Analysis (EDA)

Rent distribution analysis

Area-wise rent comparison

Amenities impact on rent

4️⃣ Feature Engineering

Created new useful features:

amenity_score

area_avg_rent

5️⃣ Model Training

Multiple models were tested:

Linear Regression

Decision Tree

Random Forest

6️⃣ Model Evaluation

Models were evaluated using:

Mean Absolute Error (MAE)

R² Score

The Random Forest model gave the best performance and was used for rent prediction.

🛠 Tech Stack
Programming Language:

Python<br>


libraries:<br>

Pandas

Scikit-learn

Seaborn

Matplotlib

Joblib

Framework:

Streamlit
