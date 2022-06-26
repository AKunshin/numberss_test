FROM postgres:latest



ENV POSTGRES_PASSWORD=
ENV POSTGRES_USER=
ENV POSTGRES_DB=
ENV POSTGRES_HOST=db


COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql
