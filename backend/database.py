import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv('dev.env')

POSTGRESQL_URL = os.environ.get("DATABASE_URL")


# SQLALCHEMY_DATABASE_URL = "sqlite:///./meditab_app.db"
# SQLALCHEMY_DATABASE_URL = "postgres://postgresql:postgres@localhost:5432/postgres"

engine = create_engine(
    # SQLALCHEMY_DATABASE_URL,
    POSTGRESQL_URL,
    # connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
