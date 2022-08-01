CREATE DATABASE IF NOT EXISTS tripsdb;

USE tripsdb;

CREATE TABLE IF NOT EXISTS regions (
    id int NOT NULL AUTO_INCREMENT,
    name_desc varchar(100) NOT NULL,
    created_at timestamp DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS sources (
    id int NOT NULL AUTO_INCREMENT,
    name_desc varchar(100) NOT NULL,
    created_at timestamp DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS trips (
    id int NOT NULL AUTO_INCREMENT,
    origin_x float NOT NULL,
    origin_y float NOT NULL,
    destination_x float NOT NULL,
    destination_y float NOT NULL,
    region_id int NOT NULL,
    datasource_id int NOT NULL,
    trip_datetime timestamp NOT NULL,
    created_at timestamp DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (region_id) REFERENCES regions(id),
    FOREIGN KEY (datasource_id) REFERENCES sources(id)
);

CREATE OR REPLACE VIEW trips_view AS
SELECT
    a.origin_x,
    a.origin_y,
    a.destination_x,
    a.destination_y,
    b.name_desc as region,
    c.name_desc as datasource_id,
    HOUR(a.trip_datetime) as trip_hour
FROM trips a
LEFT JOIN regions b
ON a.region_id = b.id
LEFT JOIN sources c
ON a.datasource_id = c.id;

GRANT ALL PRIVILEGES ON *.* TO 'jechu'@'%';