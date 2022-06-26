import os
import pandas as pd
import sqlalchemy as sa

from get_data_from_google import gsheet2df, get_update_time
from dotenv import load_dotenv

load_dotenv()

### УКАЗАНИЕ ДАННЫХ ДЛЯ СОЕДИНЕНИЯ С БД ###
DATABASE = os.getenv('POSTGRES_DB')
USER_DB = os.getenv('POSTGRES_USER')
PASSWORD = os.getenv('POSTGRES_PASSWORD')
HOST = os.getenv('POSTGRES_HOST')
PORT = '5432'
TABLE_NAME = os.getenv('TABLE_NAME')

### СОЗДАНИЕ СОЕДИНЕНИЯ С БД ###
connection_string = "postgresql+psycopg2://%s:%s@%s:%s/%s" % (
    USER_DB, PASSWORD, HOST, str(PORT), DATABASE)
engine = sa.create_engine(connection_string)
connection = engine.connect()


def write_data_to_db():
    """Запись таблицы в БД"""
    writed_data = gsheet2df()
    w_update_time = get_update_time()
    try:
        writed_data.to_sql(f"{TABLE_NAME}",
                           con=engine,
                           if_exists='replace',
                           index=False,
                           dtype={
                               "№": sa.types.INTEGER(),
                               "заказ №": sa.types.INTEGER(),
                               "стоимость,$": sa.types.Float(),
                               "срок поставки": sa.Date(),
                               "стоимость в руб": sa.types.Float()
                           })
        connection.execute(f"GRANT SELECT ON {TABLE_NAME} TO {USER_DB};")
    except Exception as ex:
        print("Ошибка,", ex)
    finally:
        if connection:
            connection.close()
            print("Соединение закрыто")
    return w_update_time


def read_from_db():
    """Вывод записанных данных"""
    data_from_db = pd.read_sql(
        f"{TABLE_NAME}",
        con=engine,
        columns=["№", "заказ №", "срок поставки", "стоимость в руб"])
    return data_from_db


def find_late_orders():
    """Поиск просроченных заказов"""
    filter_late_otders = (
        f'SELECT "№", "заказ №", "срок поставки" FROM {TABLE_NAME} WHERE "срок поставки" < CURRENT_DATE;'
    )
    # Преобразование данных в DataFrame
    late_orders = pd.read_sql(filter_late_otders,
                              con=engine,
                              parse_dates="срок поставки",
                              columns=["заказ №", "срок поставки"])
    return late_orders


if __name__ == '__main__':
    write_data_to_db()