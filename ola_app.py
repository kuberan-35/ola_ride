
import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

# Replace with your credentials
engine = create_engine('postgresql://postgres:63693103k@localhost:5432/ola_project')

def fetch_data(query):
    with engine.connect() as conn:
        return pd.read_sql(query, conn)

df = pd.read_csv("ola_rides.csv")


total_rides = df.shape[0]
total_customers = df['Customer_ID'].nunique()
completed_rides = df[df['Booking_Status'] == 'Completed'].shape[0]
cancellation_rate = round(
    df[df['Booking_Status'] == 'Canceled'].shape[0] / total_rides * 100, 2
)

st.metric("Total Rides", total_rides)
st.metric("Completed Rides", completed_rides)
st.metric("Cancellation Rate", f"{cancellation_rate}%")



