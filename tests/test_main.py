import pytest

from english_collection_card.db.models import User
from english_collection_card.main import reg, get_user
from english_collection_card.user import check_pass


class TestMain:
    def test_reg(self, data_sample_user, session):
        user = reg(session, "Igor", "123456789", "bujhm2607@yandex.ru")
        assert user.username == "Igor"
        assert user.email == 'bujhm2607@yandex.ru'
        user = reg(session, "Igor2", "123456789")
        assert user.username == "Igor2"
        assert user.email == None
        user = reg(session, "Igor", "123", "abc@yandex.ru")
        assert user is None
