

import streamlit as st
import psycopg2
import pandas as pd
import plotly.express as px
 
engine = psycopg2.connect(
                  host = "localhost",
                  port = 5432,
                  database = "ola_project",
                  user = "postgres",
                  password = "63693103k@"
 ) 

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
    df = df[(df['date'] >= str(date_range[0])) & (df['date'] <= str(date_range[1]))]

# Display
st.title("Ola Ride Insights Dashboard")
st.plotly_chart(px.bar(df, x='date', y='ride_distance', title='Daily Revenue'))

