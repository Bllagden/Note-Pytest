from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from settings import db_settings

engine = create_engine(
    url=db_settings.url,
    echo=False,
)


session_factory = sessionmaker(
    bind=engine,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass
