from sqlalchemy import Column, text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import INTEGER, TEXT, TIMESTAMP, UUID, BYTEA
from sqlalchemy.sql import func

from english_collection_card.db import Base

# Base = Base()
class Card(Base):
    __tablename__ = "card"

    id = Column(
        INTEGER,
        primary_key=True,
        autoincrement=True,
        server_default=func.gen_random_uuid(),
        unique=True,
        doc="Unique card id",
    )
    word_id = Column(
        INTEGER,
        ForeignKey("word.id"),
        nullable=False,
        doc="word id"
    )
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("user.id"),
        nullable=False,
        doc="user id"
    )
    rarity = Column(
        TEXT,
        nullable=False,
        doc="rarity"
    )
