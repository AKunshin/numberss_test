FROM postgres:latest



ENV POSTGRES_PASSWORD=numberss
ENV POSTGRES_USER=numberss
ENV POSTGRES_DB=numberss_orders
ENV POSTGRES_HOST=db


COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql