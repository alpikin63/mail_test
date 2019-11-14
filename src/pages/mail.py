from selene.api import *
import time


class MailPage(object):
    def __init__(self):
        self.write_letter_button = s('.compose-button__txt')
        self.whom_input = s('.input--3slxg input')
        self.title_input = s('[name="Subject"]')
        self.body_input = s('[role="textbox"]')
        self.send_button = s('.compose-app__footer .button2__wrapper')
        self.sucsses_title = s('.layer__header')
        self.incoming_button = s('[href="/sent/"]')
        self.first_incoming_mail_title = s('.ll-sj__normal')
        self.close_popup_button = s('.layer-window__block .layer__controls .button2__wrapper')

    def send_mail(self, mail, browser):
        self.write_letter_button.should(be.visible, timeout=10)
        self.write_letter_button.should(be.clickable, timeout=10)
        self.write_letter_button.click()
        self.whom_input.set_value(mail.whom)
        self.title_input.set_value(mail.title)
        #js скрипт для наполнеия текста письма
        browser.execute_script(
            script="""document.querySelector('[role="textbox"] div div').innerHTML = '{0}';""".format(mail.body))
        self.send_button.click()
        return self