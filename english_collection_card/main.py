from english_collection_card.db.models import User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import create_engine
from english_collection_card.db.models.user import Base
from sqlalchemy.orm import Session

from user import send_emeil_code, check_email_code, gen_email_code, hash_pass, check_pass

engine = create_engine("postgresql+psycopg2://user:hackme@localhost/shortener_db")
Base.metadata.create_all(engine)

s = Session(engine)
    

def reg(name, password, email=None):
    user = s.execute(select(User).where(name==User.name)).all()
    # user = select(User).where(name==User.name)
    # user = await session.scalar(user)
    # print(user.__dict__)
    print('here')
    new_user = None
    if not user:
        print('here2')
        new_user = User(name=name, password=hash_pass(password), email=email)
        s.add(new_user)
        s.commit()
        s.refresh(new_user)
    return new_user

def get_user(name):
    user = s.execute(select(User).where(name==User.name)).scalars().first()
    return user


# session = get_session()
print(reg('26077', 'test', '12345'))
user = get_user('2607')
print(check_pass('2607', user.password))