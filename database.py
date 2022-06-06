from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Using MySQL
#you should create database named 'db'or you can modify this code and naming the db names like otheres
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://haha:1234qwer@13.210.217.204:3306/db?charset=utf8"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()