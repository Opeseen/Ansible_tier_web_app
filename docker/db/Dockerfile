FROM mysql:8.0.33

ENV MYSQL_ROOT_PASSWORD="admin1234"
ENV MYSQL_DATABASE="accounts"

ADD setup.sql docker-entrypoint-initdb.d/setup.sql