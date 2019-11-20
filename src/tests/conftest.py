import pytest
from src.model.user import User
from src.model.mail import Mail


@pytest.fixture()
def data_users():
    tru_user = User(login='testt2005', password='123Qa!', domain=1)
    return tru_user


@pytest.fixture()
def data_mails():
    mail = Mail()
    return mail