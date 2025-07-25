Ola Ride Insights

Project Overview

The rise of ride-sharing platforms has transformed urban mobility, offering convenience and affordability to millions. OLA, a leading ride-hailing service, generates massive volumes of ride, driver, and customer data. This project explores OLA's operational and business metrics by building a full-stack analytics pipeline using SQL, Power BI, and Streamlit.

Objectives

Identify patterns in ride volumes, cancellations, and user behavior.

Analyze vehicle usage, payment trends, and customer/driver ratings.

Create an interactive dashboard for decision-making.

Tools & Technologies Used

Python: Data processing and Streamlit development

PostgreSQL: SQL querying and data extraction

Power BI: Visualizations and dashboarding

Streamlit: Interactive web application

Pandas, SQLAlchemy: Data handling and DB connection

Dataset Summary

ride_id: Unique identifier for each ride

ride_date: Timestamp of the ride

vehicle_type: Type of vehicle (Mini, Prime, Auto, etc.)

distance_km: Distance covered in kilometers

fare: Fare charged for the ride

status: Booking status (Completed, Cancelled)

payment_method: UPI, Card, Wallet, etc.

customer_rating, driver_rating: Ratings on a scale of 1-5

cancel_reason: Reason if the ride was cancelled

Business Use Cases & SQL Queries

1. Identifying Peak Demand Hours and Optimizing Driver Allocation

SELECT EXTRACT(HOUR FROM time::time) AS hour,
       COUNT(*) AS total_rides
FROM ola_rides
WHERE booking_status = 'Completed'
GROUP BY hour
ORDER BY hour;

2. Analyzing Customer Behavior for Personalized Marketing Strategies

SELECT customer_id, COUNT(*) AS total_rides
FROM ola_rides
GROUP BY customer_id
ORDER BY total_rides DESC;

3. Understanding Pricing Patterns and Surge Pricing Effectiveness

SELECT vehicle_type,
       ROUND(AVG(fare), 2) AS avg_fare,
       ROUND(AVG(distance_km), 2) AS avg_distance
FROM ola_rides
WHERE booking_status = 'Completed'
GROUP BY vehicle_type
ORDER BY avg_fare DESC;

4. Detecting Anomalies or Fraudulent Activities in Ride Data

SELECT *
FROM ola_rides
WHERE ride_distance > 10 AND booking_value < 50;

Streamlit Dashboard Features

Sidebar Navigation:

Ride Trends

Vehicle Insights

Revenue Analysis

Cancellation Reasons

Customer & Driver Ratings

Interactive Filters:

Date Range Picker

Vehicle Type Dropdown

Region Filter

Visualizations (Plotly):

Line/Bar charts for trends

Pie/Donut charts for distribution

Map view (optional for city-wise data)

Backend:

PostgreSQL connection using SQLAlchemy

Data caching for performance

Streamlit Code Snippet (Simplified Example)

import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Database Connection
engine = create_engine("postgresql://user:password@localhost/ola_db")

# Sidebar Filters
st.sidebar.title("Filters")
vehicle_type = st.sidebar.selectbox("Vehicle Type", ["All", "Mini", "Prime", "Auto"])
date_range = st.sidebar.date_input("Date Range", [])

# Query & Data
query = "SELECT * FROM ola_rides"
df = pd.read_sql(query, engine)

# Apply filters
if vehicle_type != "All":
    df = df[df['vehicle_type'] == vehicle_type]

if date_range:
    df = df[(df['ride_date'] >= str(date_range[0])) & (df['ride_date'] <= str(date_range[1]))]

# Display
st.title("Ola Ride Insights Dashboard")
st.plotly_chart(px.bar(df, x='date', y='ride_distance', title='Daily Revenue'))

Power BI Dashboard Views

🔗<img width="1920" height="1080" alt="Screenshot (1)" src="https://github.com/user-attachments/assets/31341e6c-34f1-467e-810e-8650e0f5838d" />
 
Ride Volume Over Time

Booking Status Breakdown

Top 5 Vehicle Types by Ride Distance

Average Customer Ratings by Vehicle Type

Cancelled Rides Reasons

Revenue by Payment Method

Top 5 Customers by Booking Value

Ride Distance Per Day

Driver Ratings Distribution

Customer vs. Driver Ratings

Installation & Run

# Clone repository
https://github.com/your-username/ola-ride-insights.git

# Create virtual environment and activate
python -m venv env
source env/bin/activate  # or env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run ola_app.py

Insights Summary

Peak hours show highest demand in urban hubs.

Prime vehicles attract higher ratings and longer trips.

UPI dominates as preferred payment method.

Most cancellations are user-initiated (driver delay).

Consistent rating trends point to high service quality.

Contributors

Data Analyst: kuberan.k

Streamlit Developer: kuberan.k

Mentor: Shadiya P P

License

MIT License

