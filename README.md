# numberss_test
Тестовое задание Numbers
Моя версия выполнения тестового задания от Numbers.

Для запуска локально, необходимо создать в корне приложения файл .env

POSTGRES_DB = "Имя вашей БД"
POSTGRES_USER = "Имя пользователя БД"
POSTGRES_PASSWORD = "Пароль пользователя БД"
POSTGRES_HOST = "Имя хоста с БД"
TABLE_NAME="Имя таблицы"
TELEGRAM_TOKEN = "Ключ полученный от BotFather"
TELEGRAM_USER_ID = "ID вашего Telegram аккаунта"
SPREADSHEET_NAME="Название документа на Google "


Для запуска используйте main_app.py.

Для запуска в Docker-compose внесите свои данные в Dockerfile, как в дирректории /app, так и в дирректории /database. 

docker-compose up --build


!Важно. При выполнении, скрипт не всегда может получить официальный курс $/руб. с  сайт ЦБ РФ. В случае такой ошибки, вы увидите сообщение.
В этом случае, чтобы приложение не завершилось, вызвав исключение, будет использован курс рубля по состоянию на 25/06/2022.

Состав приложения:
main_app.py - Основное приложение. Из него вызываются функции записи данных в БД. Отправка сообщений в Telegram.
get_data_from_google.py - Используя API получаем доступ к таблице и извлекаем все данные в DataFrame.
exchange.py - Используется для получения курса доллар/рубль с сайта ЦБ РФ
operations_with_db.py - Используется для работы с БД. В этом приложении находятся функции записи, чтения, а также вывод в формате DataFrame списка заказов, с прросроченным сроком доставки. Эти данные передаются Телеграм-боту для отправки
