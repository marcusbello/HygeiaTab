import os

from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# POSTGRESQL_URL = os.environ.get("DATABASE_URL")
postgres_url = config("DATABASE_URL", default='postgresql://postgres:postgres@localhost:5432/postgres')


# SQLALCHEMY_DATABASE_URL = "sqlite:///./meditab_app.db"
# SQLALCHEMY_DATABASE_URL = "postgres://postgresql:postgres@localhost:5432/postgres"

engine = create_engine(
    # SQLALCHEMY_DATABASE_URL,
    postgres_url,
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
