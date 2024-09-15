from sqlalchemy import Column, text, DateTime
from sqlalchemy.dialects.postgresql import INTEGER, TEXT, TIMESTAMP, UUID
from sqlalchemy.sql import func

from english_collection_card.db import DeclarativeBase


class User(DeclarativeBase):
    __tablename__ = "url_storage"

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
        TEXT,
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
