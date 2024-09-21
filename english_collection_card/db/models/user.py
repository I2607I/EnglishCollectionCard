from sqlalchemy import Column, text, DateTime
from sqlalchemy.dialects.postgresql import INTEGER, TEXT, TIMESTAMP, UUID, BYTEA
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

from english_collection_card.db import DeclarativeBase

Base = declarative_base()
class User(Base):
    __tablename__ = "user"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.gen_random_uuid(),
        unique=True,
        doc="Unique user id",
    )
    name = Column(
        TEXT,
        nullable=False,
        unique=True,
        doc="Unique name",
    )
    password = Column(
        BYTEA,
        nullable=False,
        doc="Password",
    )
    email = Column(
        TEXT,
        nullable=True,
        doc="Secret code to access administrator features",
    )

    def __repr__(self):
        columns = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return f'<{self.__tablename__}: {", ".join(map(lambda x: f"{x[0]}={x[1]}", columns.items()))}>'
