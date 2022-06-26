import pytz
import datetime
import requests

from bs4 import BeautifulSoup


def get_current_date():
    """Получение текущей даты, перевод в строки"""
    timezone = pytz.timezone("Europe/Moscow")
    now_with_tz = timezone.localize(datetime.datetime.now())
    return now_with_tz


def exchange_to_rubles():
    """Перевод долларов в рубли по курсу ЦБ РФ"""
    current_date = get_current_date().strftime("%d/%m/%Y")
    url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
    params = {'date_req': current_date}
    try:
        request = requests.get(url, params)
        soup = BeautifulSoup(request.content, 'xml')
        dollar_exchange_rate = soup.find(ID="R01235").Value.string
        dollar_exchange_rate = float(dollar_exchange_rate.replace(',', '.'))
    except:
        print("Сайт ЦБ РФ не ответил")
        dollar_exchange_rate = 53.32
    finally:
        return dollar_exchange_rate


def print_exchange():
    exchange_rate = exchange_to_rubles()
    print(exchange_rate)


if __name__ == '__main__':
    print_exchange()