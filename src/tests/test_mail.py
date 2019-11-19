from selene.api import *
from src.pages.main import MainPage
from src.pages.mail import MailPage


class TestSendMail:

    def test_send_email(self, data_users, data_mails):
        MainPage().login(data_users)
        MailPage().send_mail(data_mails, browser=browser).sucsses_title.should(
            have.exact_text("Письмо отправлено"))
        MailPage().close_popup_button.click()
        MailPage().incoming_button.click()
        MailPage().first_incoming_mail_title.should(have.exact_text(data_mails.title))