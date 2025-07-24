from sqlalchemy import create_engine
import pandas as pd

# Replace with your credentials
engine = create_engine('postgresql://postgres:63693103k@localhost:5432/ola_project')

def fetch_data(query):
    with engine.connect() as conn:
        return pd.read_sql(query, conn)
