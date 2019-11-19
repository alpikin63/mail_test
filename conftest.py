import pytest
from selene.api import *


@pytest.fixture(autouse=True)
def setup_teardown():
    browser.open_url('/')
    yield
    browser.close()