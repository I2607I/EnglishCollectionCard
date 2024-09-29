from english_collection_card.db.models import User, Word, Card
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
    
### user
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


#word
def create_word(session, russian, english):
    word = session.execute(select(Word).where(russian==Word.russian)).scalars().first()
    new_word = None
    if not word:
        new_word = Word(russian=russian, english=english)
        session.add(new_word)
        session.commit()
        session.refresh(new_word)
    return new_word

def get_word(session, russian):
    word = session.execute(select(Word).where(russian==Word.russian)).scalars().first()
    return word



#card
def create_card(session, word, user_id, rarity):
    # пока юзер id передаём
    word_id = session.execute(select(Word.id).where(word==Word.russian)).scalars().first()
    card = session.execute(select(Card).where(word_id==Card.word_id, user_id==Card.user_id, rarity==Card.rarity)).scalars().first()
    new_card = None
    print(card)
    if not card:
        new_card = Card(word_id=word_id, user_id=user_id, rarity=rarity)
        session.add(new_card)
        session.commit()
        session.refresh(new_card)
    return new_card

def get_cards(session, user_id):
    cards = session.execute(select(Card).where(user_id==Card.user_id)).scalars().all()
    return cards









    





name = '26078'
password = 'test'
email = ''
name2 = '2607'
user = get_user(session, name)
user2 = get_user(session, name2)
create_word(session, 'собака', 'dog')
create_word(session, 'кот', 'cat')
create_word(session, 'подход', 'approach')
create_word(session, 'хлопок', 'clap')
create_word(session, 'ворчание', 'gramble')
create_word(session, 'дом', 'house')
create_word(session, 'квартира', 'apartment')
create_word(session, 'барабан', 'drum')
create_word(session, 'луна', 'moon')
create_word(session, 'дерево', 'tree')
create_word(session, 'стул', 'chair')
create_word(session, 'машина', 'car')
create_word(session, 'воздух', 'air')
create_word(session, 'животное', 'animal')
create_word(session, 'ответ', 'answer')
create_word(session, 'область', 'area')
create_word(session, 'осень', 'autumn')
create_word(session, 'медведь', 'bear')
create_word(session, 'кровать', 'bed')

print(get_word(session, 'луна'))
print(get_word(session, 'дерево'))

create_card(session, 'луна', user.id, 'rare')
create_card(session, 'дерево', user.id, 'superrare')
create_card(session, 'осень', user.id, 'ultrarare')



print(get_cards(session, user.id))
# print(reg(session, name, password, email))
# print(auth2(session, name, password))