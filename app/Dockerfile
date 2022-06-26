FROM python:latest

WORKDIR /code

ADD requirements.txt requirements.txt
COPY . .

ENV POSTGRES_DB=
ENV POSTGRES_USER=
ENV POSTGRES_PASSWORD=
ENV POSTGRES_HOST=db
ENV TABLE_NAME=
ENV TELEGRAM_TOKEN=
ENV TELEGRAM_USER_ID=
ENV SPREADSHEET_NAME=

RUN pip install -r requirements.txt

CMD ["python3","-u", "main_app.py"]
