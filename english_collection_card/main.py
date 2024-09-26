from english_collection_card.db.models import User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import create_engine
from english_collection_card.db import Base
from sqlalchemy.orm import Session
import os

from user import send_emeil_code, check_email_code, gen_email_code, hash_pass, check_pass

engine = create_engine("postgresql+psycopg2://user:hackme@localhost/shortener_db")
Base.metadata.create_all(engine)

session = Session(engine)
    

def reg(session, name, password, email=None):
    user = session.execute(select(User).where(name==User.name)).all()
    new_user = None
    if not user:
        new_user = User(name=name, password=hash_pass(password), email=email)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
    return new_user

def get_user(session, name):
    user = session.execute(select(User).where(name==User.name)).scalars().first()
    return user

def auth(session, name, password):
    check = False
    user = session.execute(select(User).where(name==User.name)).scalars().first()
    if user:
        check = check_pass(password, user.password)
    return check

def auth2(session, name, password):
    check = False
    user = session.execute(select(User).where(name==User.name)).scalars().first()
    if user:
        check = check_pass(password, user.password)
    if check and user.email:
        code = gen_email_code()
        send_emeil_code(os.getenv("me"), user.email, code)
        return check_email_code(code, input("Enter the code sent to you by email:\n"))
    return False





name = '26078'
password = 'test'
email = ''
print(reg(session, name, password, email))
print(auth2(session, name, password))