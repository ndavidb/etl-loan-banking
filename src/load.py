from pandas import DataFrame
from sqlalchemy import create_engine
import os

def load_to_postgres(df: DataFrame, table_name: str):
    host = os.getenv("POSTGRES_HOST")
    db_name = os.getenv("POSTGRES_DB")
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")

    engine = create_engine(f"postgresql+psycopg://{user}:{password}@{host}/{db_name}")

    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Table {table_name} loaded")

