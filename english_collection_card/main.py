from english_collection_card.db.models import User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import create_engine
from english_collection_card.db.models.user import Base
from sqlalchemy.orm import Session

from user import send_emeil_code, check_email_code, gen_email_code, hash_pass, check_pass

engine = create_engine("postgresql+psycopg2://user:hackme@localhost/shortener_db")
Base.metadata.create_all(engine)

session = Session(engine)
    

def reg(session, name, password, email=None):
    user = session.execute(select(User).where(name==User.name)).all()
    print('here')
    new_user = None
    if not user:
        print('here2')
        new_user = User(name=name, password=hash_pass(password), email=email)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
    return new_user

def get_user(session, name):
    user = session.execute(select(User).where(name==User.name)).scalars().first()
    return user


print(reg(session, '2607', 'test', '12345'))
user = get_user(session, '2607')
print(user.password)
print(check_pass('test', user.password))