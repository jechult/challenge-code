from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = "mysql://jechu:password@db:3306/tripsdb"

# creating a mysql database connector for reading and writing processes

engine = create_engine(SQLALCHEMY_DATABASE_URL)