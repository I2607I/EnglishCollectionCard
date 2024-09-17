import asyncio
from english_collection_card.db.models import User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import create_engine
# from english_collection_card.db.connection import get_session
from english_collection_card.db.models.user import Base
from sqlalchemy.orm import Session


# POSTGRES_DB=shortener_db
# POSTGRES_USER=user
# POSTGRES_PASSWORD=hackme
# POSTGRES_HOST=localhost
# POSTGRES_PORT=5432
engine = create_engine("postgresql+psycopg2://user:hackme@localhost/shortener_db")
# engine = create_engine("mysql+mysqldb://scott:tiger@localhost/test", echo=True)
Base.metadata.create_all(engine)

s = Session(engine)
    

def reg(name, password, email=None):
    user = s.execute(select(User).where(name==User.name))
    # user = select(User).where(name==User.name)
    # user = await session.scalar(user)
    # print(user)
    new_user = None
    if not user:
        new_user = User(name=name, password=password, email=email)
        s.add(new_user)
        s.commit()
        s.refresh(new_user)
    return new_user


# session = get_session()
reg('26078', 'test', '12345')