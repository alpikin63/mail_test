from selene.api import s


class MainPage(object):
    def __init__(self):
        self.login_input = s('[name="login"]') #поле для ввода логина
        self.domain_select = s('[name="domain"]') #выбор домена
        self.password_button = s('#mailbox\:submit') #кнопка появления инпута для пароля
        self.password_input = s('[name="password"]') #поле для ввода пароля
        self.login_submit_button = s('.mailbox__row.mailbox__row_.i-clearfix label') #кнопка авторизации

    def login(self, name='', password='', domain=''):
        self.login_input.set_value(name)
        self.domain_select.click()
        self.password_button.click()
        self.password_input.set_value(password)
        self.login_submit_button.click()
        return self

