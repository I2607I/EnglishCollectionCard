
# пока так

from uuid import uuid4
from sqlalchemy import create_engine

import pytest

from sqlalchemy_utils import create_database, database_exists, drop_database
from sqlalchemy.orm import Session


@pytest.fixture
def open_session(url):
    """
    Создает временную БД для запуска теста.
    """

    tmp_name = ".".join([uuid4().hex, "pytest"])

    tmp_url = "sqlalchemy.url = postgresql://user:hackme@localhost/test"+tmp_name
    create_database(tmp_url)
    engine = create_engine(tmp_url)
    # Base.metadata.create_all(engine)

    session = Session(engine)
    return session

@pytest.fixture
def close_session():
    drop_database(tmp_url)







