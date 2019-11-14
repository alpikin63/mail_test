import random


class Mail(object):
    def __init__(self, sender='alpikin63@gmail.com', title='test', body = 'bodytest'):
        self.whom = sender
        self.random = str(random.randrange(1111, 9999))
        self.title = title + self.random
        self.body = body+self.random