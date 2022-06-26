import os
import telebot
import schedule

from operations_with_db import write_data_to_db, read_from_db, find_late_orders
from get_data_from_google import get_update_time
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')
# Токен, который выдает @botfather
TELEGRAM_USER_ID = os.getenv('TELEGRAM_USER_ID')
# ID Пользователя Телеграм
bot = telebot.TeleBot(TOKEN)


def db_controller():
    """Управление операциями с БД"""
    writed_data = write_data_to_db()
    print("Данные успешно обновлены")
    status_tg = tg_send_message()
    print(status_tg)
    print(f"Данные из БД: \n {writed_data}")


def tg_send_message():
    """Отправка списка просроченных заказов"""
    late_orders = find_late_orders()
    bot.send_message(
        TELEGRAM_USER_ID,
        f"По данным заказам срок поставки истек: \n {late_orders}")
    status_tg = "Сообщение отправлено адресату"
    return status_tg


def main():
    schedule.every(10).seconds.do(db_controller)

    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
