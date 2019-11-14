from selene.api import *


class MailPage(object):
    def __init__(self):
        self.write_letter_button = s('.compose-button__txt')
        self.whom_input = s('.input--3slxg input')
        self.title_input = s('[name="Subject"]')
        self.body_input = s('[role="textbox"]')
        self.send_button = s('.compose-app__footer .button2__wrapper')
        self.sucsses_title = s('.layer__header')

    def send_mail(self, whom, title, body, browser):
        self.write_letter_button.should(be.visible)
        self.write_letter_button.click()
        self.whom_input.set_value(whom)
        self.title_input.set_value(title)
        #js скрипт для наполнеия текста письма
        browser.execute_script(script="""document.querySelector('[role="textbox"] div div').innerHTML = 'testbodey';""")
        self.body_input.set_value(body)
        self.send_button.click()
        return self