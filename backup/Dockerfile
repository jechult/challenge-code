FROM mysql:5.7

ENV MYSQL_USER=jechu
ENV MYSQL_PASSWORD=password
ENV MYSQL_ROOT_PASSWORD=admin

COPY init_sql.sql /docker-entrypoint-initdb.d

EXPOSE 3306