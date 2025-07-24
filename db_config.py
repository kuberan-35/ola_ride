
from sqlalchemy import create_engine

def get_engine():
    return create_engine("postgresql://postgres:63693103k@@localhost:5432/ola_project")
