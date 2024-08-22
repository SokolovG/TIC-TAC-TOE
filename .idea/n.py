class Phone:

    def __init__(self):
        self.name_phone = 'Телефон'
    def ring(self):
        print(f'Дзынь. у вас звонит {self.name_phone}')

class Iphone(Phone):

    def __init__(self):
        self.name_phone = 'Iphone'

    def ring(self):
        print(f'Дзынь, дзыыыынь... у вас звонит {self.name_phone}')

class Samsung(Phone):
    def __init__(self):
        self.name_phone = 'Samsung'
    def ring(self):
        print(f'ДЗЫЫЫЫЫНЬ, ДЗЫНЬ ДЗЫНЬ!!!! у вас звонит {self.name_phone}')


phone = Phone()
phone.ring()

iphone = Iphone()
iphone.ring()

samsung = Samsung()
samsung.ring()

