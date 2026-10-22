
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.pool import StaticPool


load_dotenv()

conn_url = URL.create(
    drivername=os.getenv("DRIVERNAME"),
    database=os.getenv("DATABASE"),
    username=os.getenv("USERNAME"),
    host=os.getenv("HOSTNAME"),
    port=os.getenv("PORT"),
    password=os.getenv("PASSWORD"),
    )

engine = create_engine(
    conn_url,
    echo=True,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
