FROM python:latest

WORKDIR /code

ADD requirements.txt requirements.txt
COPY . .

ENV POSTGRES_DB=numberss_orders
ENV POSTGRES_USER=numberss
ENV POSTGRES_PASSWORD=numberss
ENV POSTGRES_HOST=db
ENV TABLE_NAME=orders
ENV TELEGRAM_TOKEN=5590272859:AAHFfilFsaO4OxQYQHEF3BndL8Axg5mS6gM
ENV TELEGRAM_USER_ID=385102787
ENV SPREADSHEET_NAME=Numberss_test

RUN pip install -r requirements.txt

CMD ["python3","-u", "main_app.py"]