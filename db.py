import psycopg2
from psycopg2 import extensions
from pandas import DataFrame
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import consts
import pandas as pd


def connection_to_database() -> extensions.connection:
    load_dotenv()
    connection = psycopg2.connect(
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )
    return connection


def create_and_fill() -> None:
    connection = connection_to_database()
    create_table(connection)
    fill_table_from_dataframe()
    close_connection(connection)


def create_table(connection) -> None:
    try:
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(consts.DROP_TABLE_IF_EXISTS)
            cursor.execute(consts.QUERY_CREATE_TABLE_COVID19)
    except Exception as ex:
        if connection:
            connection.close()
        print(f'Exception create table: {ex}')


def close_connection(connection) -> None:
    connection.close()


def change_field_date(dataframe: DataFrame) -> DataFrame:
    return dataframe.rename(columns={'date': 'date_'})


def fill_table_from_dataframe() -> None:
    conn_string = f'''postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}
    @{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}'''

    db = create_engine(conn_string)
    connection = db.connect()
    dataframe = pd.read_csv("./resources/df_covid19_countries.csv")
    headers = dataframe.columns.values.tolist()
    dataframe = dataframe[[i for i in headers]]
    dataframe = change_field_date(dataframe)
    dataframe.to_sql('covid19_countries', connection, if_exists='replace')
    connection.close()


def select(connection, query: str) -> None:
    cursor = connection.cursor()
    cursor.execute(query)
    for i in cursor.fetchall():
        print(i)


if __name__ == '__main__':
    conn = None
    try:
        conn = connection_to_database()
        select(conn, consts.QUERY_SELECT_TOTAL_VACCINATIONS)
    except Exception as ex:
        print(ex)
    finally:
        close_connection(conn)
