from selene.api import *


class MainPage(object):
    def __init__(self):
        self.login_input = s('[name="login"]') #поле для ввода логина
        self.domain_select = s('.mailbox__select') #выбор домена
        self.domain_select_options = ss('option')
        self.password_button = s('.btn.btn_blue.mailbox__control') #кнопка появления инпута для пароля
        self.password_input = s('[name="password"]') #поле для ввода пароля
        self.login_submit_button = s('.mailbox__row.mailbox__row_.i-clearfix label') #кнопка авторизации

    def login(self, user):
        self.login_input.set_value(user.login)
        self.domain_select.click()
        self.domain_select_options[user.domain].click()
        self.password_button.click()
        self.password_input.set_value(user.password)
        self.login_submit_button.click()
        return self

