import pandas as pd
import psycopg2 as ps
from sqlalchemy import create_engine 

df = pd.read_csv('ola_data.csv')

engine = create_engine("postgresql+psycopg2://postgres:63693103k@@localhost:5432/ola_project")

df.to_sql("ola_ride", engine, if_exists='replace', index=False)



