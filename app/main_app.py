from datetime import datetime
import os
import telebot
import schedule
import time

from get_data_from_google import open_gs
from operations_with_db import write_data_to_db, read_from_db, find_late_orders
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')
# Токен, который выдает @botfather
TELEGRAM_USER_ID = os.getenv('TELEGRAM_USER_ID')
# ID Пользователя Телеграм
bot = telebot.TeleBot(TOKEN)
write_update_time = write_data_to_db()

update_list = []
# Список обновлений таблицы


def db_controller():
<<<<<<< HEAD
    """Управление работой БД"""
    update_time = open_gs().lastUpdateTime
    print(f"Время обновления на сервере {update_time}")
    if update_time not in update_list:
        print("Получены обновления - запись в БД")
        send_command_write()
        update_list.append(update_time)
        print(f"Список обновлений: {update_list}")
    else:
        send_command_read()


def send_command_write():
    """Отправка команды на запись данных в БД"""
    write_data = write_data_to_db()
    print(write_data)
    print("Данные успешно обновлены")
    tg_send_message()
    # Отправка команды Телеграм-боту сдлеать рассылку


def send_command_read():
    """Чтение из БД"""
    old_data = read_from_db()
    print("Обновлений нет")
    # print(f"Имеющиеся данные в БД: \n {old_data} \n {datetime.now()}")
    # Вывод данных для демонстрации работы. Лучше отключить print для снижения нагрузки
=======
    """Управление операциями с БД"""
    read_update_time = get_update_time()
    if write_update_time != read_update_time:
        print("Получены обновления - запись в БД")
        print("Данные успешно обновлены")
        status_tg = tg_send_message()
        print(status_tg)
        write_update_time = read_update_time
    else:
        old_data = read_from_db()
        print("Обновлений нет. Имеющиеся данные в БД: \n")
        print(f"Данные из БД: \n {old_data}")
>>>>>>> bd72b0474fcf2bf2741b7689db2bf25f3610d604


def tg_send_message():
    """Отправка списка просроченных заказов"""
    late_orders = find_late_orders()
    bot.send_message(
        TELEGRAM_USER_ID,
        f"По данным заказам срок поставки истек: \n {late_orders}")
    print("Сообщение отправлено адресату")


def main():
    schedule.every(10).seconds.do(db_controller)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
