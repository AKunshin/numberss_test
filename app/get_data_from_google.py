import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac
import pandas as pd

from exchange import exchange_to_rubles, get_current_date
from dotenv import load_dotenv

load_dotenv()

scope = [
    'https://www.googleapis.com/auth/spreadsheets.readonly',
    'https://www.googleapis.com/auth/drive.readonly'
]
# Указываем сервисы и уровень доступа
CREDENTIALS_FILE = 'numberss-project-779d822965af.json'
# Путь к токену

SPREADSHEET_NAME = os.getenv('SPREADSHEET_NAME')
# Название документа
SHEET_NUM = 0
# Номер страницы. ! Начинается с 0!


def open_gs():
    """Открываем таблицу в GS"""
    credentials = sac.from_json_keyfile_name(CREDENTIALS_FILE, scope)
    # Извлекаем учетные данные по пути
    client = gspread.authorize(credentials)
    # Используем извлеченные учетные данные для авторизации с помощью библиотеки gspread
    sheet = client.open(SPREADSHEET_NAME)
    # Открытие таблицы
    return sheet


def get_update_time():
    """Получаем время последнего обновления таблицы"""
    update_time = open_gs().lastUpdateTime
    now_with_tz = get_current_date()
    print(
        f"Время обновления: {update_time} \t--- Текущее время: {now_with_tz} ---"
    )
    return update_time


def gsheet2df():
    """Преобразуем таблицу в DataFrame"""
    sheet = open_gs()
    sheet = sheet.get_worksheet(SHEET_NUM).get_all_records()
    # Извлечение данных в виде словаря
    df = pd.DataFrame.from_dict(sheet)
    # Преобразование словаря в DataFrame

    dollar_exchange_rate = exchange_to_rubles()
    # Получение курса доллара и создание нового столбца
    try:
        df['стоимость в руб'] = df['стоимость,$'] * round(
            dollar_exchange_rate, 2)
    except Exception as ex:
        print("Ошибка в столбце 'стоимость,$", ex)
    finally:
        print(df)
        return df


if __name__ == '__main__':
    gsheet2df()