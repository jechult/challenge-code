from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = "mysql://jechu:password@db:3306/tripsdb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)