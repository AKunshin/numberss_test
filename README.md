# numberss_test
Тестовое задание Numbers
Моя версия выполнения тестового задания от Numbers.
Ссылка на Google Sheets документ:
https://docs.google.com/spreadsheets/d/1qYmwm0EHR5xc-lkv6nBocEbdcLR7nOyFsjyCSrwkIdA/edit#gid=0

В директории /app поместите ваш токен-учетные данные в формате JSON, полученный из Google Console

Для запуска локально, необходимо создать в корне приложения файл .env

POSTGRES_DB = "Имя вашей БД"  
POSTGRES_USER = "Имя пользователя БД" 
POSTGRES_PASSWORD = "Пароль пользователя БД"  
POSTGRES_HOST = "Имя хоста с БД"  (локально - localhost)  
TABLE_NAME="Имя таблицы"  
TELEGRAM_TOKEN = "Ключ полученный от BotFather" 
TELEGRAM_USER_ID = "ID вашего Telegram аккаунта"(id можно получить у @userinfobot)  
SPREADSHEET_NAME="Название документа на Google" 

Для запуска используйте main_app.py.

Для запуска в Docker-compose внесите свои данные в Dockerfile, как в дирректории /app, (!кавычки тут не использовать!)  

ENV POSTGRES_DB=Имя вашей БД  
ENV POSTGRES_USER=Имя пользователя БД 
ENV POSTGRES_PASSWORD=Пароль пользователя БД  
ENV POSTGRES_HOST=Имя хоста с БД (При запуске в Docker-compose укажите здесь просто db )  
ENV TABLE_NAME=Имя таблицы  
ENV TELEGRAM_TOKEN=Ключ полученный от BotFather 
ENV TELEGRAM_USER_ID=ID вашего Telegram аккаунта"(id можно получить у @userinfobot) 
ENV SPREADSHEET_NAME=Название документа на Google 

так и в дирректории /database:  

ENV POSTGRES_PASSWORD=Пароль пользователя БД  
ENV POSTGRES_USER=Имя пользователя БД 
ENV POSTGRES_DB=Имя вашей БД  
ENV POSTGRES_HOST=Имя хоста с БД (При запуске в Docker-compose укажите здесь просто db )  

docker-compose up --build 

!Важно. При выполнении, скрипт не всегда может получить официальный курс $/руб. с  сайт ЦБ РФ. В случае такой ошибки, вы увидите сообщение.
В этом случае, чтобы приложение не завершилось, вызвав исключение, будет использован курс рубля по состоянию на 25/06/2022. 

Состав приложения:
main_app.py - Основное приложение. Из него вызываются функции записи данных в БД. Отправка сообщений в Telegram.
get_data_from_google.py - Используя API получаем доступ к таблице и извлекаем все данные в DataFrame.
exchange.py - Используется для получения курса доллар/рубль с сайта ЦБ РФ
operations_with_db.py - Используется для работы с БД. В этом приложении находятся функции записи, чтения, а также вывод в формате DataFrame списка заказов, с прросроченным сроком доставки. Эти данные передаются Телеграм-боту для отправки
