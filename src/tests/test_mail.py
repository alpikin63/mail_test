from selene.api import *
from src.pages.main import MainPage
from src.pages.mail import MailPage


class TestLogin:
    def setup(self):
        browser.open_url('/')

    def teardown(self):
        browser.close()

    def test_send_email(self):
        MainPage().login(name='testt2005', password='123Qa!', domain='inbox.ru')
        MailPage().send_mail(whom='alpikin63@gmail.com', title='testtitle', body='testbodey').sucsses_title.should(
            have.exact_text("Отправлено"))
