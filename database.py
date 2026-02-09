from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#Postgress
#DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/dbsoccer"

#SQLite
#DATABASE_URL = "sqlite:///database.db"

#MySql
#DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/dbsoccer"
DATABASE_URL = "mysql+pymysql://root@localhost:3306/dbsoccer"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()