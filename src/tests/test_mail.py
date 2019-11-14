from selene.api import *
from src.pages.main import MainPage
from src.pages.mail import MailPage
from src.model.user import User
from src.model.mail import Mail

tru_user = User(login='testt2005', password='123Qa!', domain=1)
mail = Mail()

class TestLogin:
    def setup(self):
        browser.open_url('/')

    def teardown(self):
        browser.close()

    def test_send_email(self):
        MainPage().login(tru_user)
        MailPage().send_mail(mail, browser=browser).sucsses_title.should(
            have.exact_text("Письмо отправлено"))
        MailPage().close_popup_button.click()
        MailPage().incoming_button.click()
        MailPage().first_incoming_mail_title.should(have.exact_text(mail.title))

