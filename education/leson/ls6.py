# def print_human_name(human):
#     print(human['name'])
# h1 = {'name': 'Marya'}
# h2 = {'name': 'Oksana'}
# h3 = {'full_name': 'Ivan'}
#
# print_human_name(h1)
# print_human_name(h2)
# print_human_name(h3)

class Phone: #CamelStyle
    def __init__(self, model_phone):
        self.model = model_phone
        self._id = 123456789
        self._loading()
        self.__bla = 'qwe'

    def call(self):
        print('calling')

    def _loading(self):
        print(self.model, 'loading...')

    def get_id(self):
        return self._id

# my_phone = Phone('nokia1100')
# my_phone.call()
# print(my_phone.model)
# my_phone._loading()
# print(my_phone.get_id())
# print(my_phone._Phone__bla) # name._classname__attr
# my_phone._loading()
# print(my_phone.model)

class SmartPhone(Phone):

    def sms(self):
        print('smsing')

    def email(self):
        print('emailing')

# my_smart_phone = SmartPhone('motorola')
# my_smart_phone.call()
# my_smart_phone.sms()

class IPhone(SmartPhone):

    def __init__(self, model_phone):
        super().__init__(model_phone)
        print('show apple')

    def play(self):
        print('playing')

    def browser(self):
        print('browsering')

    def sms(self):
        print('Imassage sending')

# iphone = IPhone('6')
# iphone.sms()

class NextPhone():

    def touch_id(self):
        print('touch_id')

    def pay(self):
        print('pay')

class Huawei(NextPhone):
    pass

class Samsung(NextPhone):
    pass


class Player:

    def player_metod(self):
        print('root_player_metod')


class Navigator:

    def navigator_metod(self):
        print('root_navigator_metod')


class MobilePhone(Player, Navigator):
    def method(self):
        print('method')

# mobile_pthone = MobilePhone()
# mobile_pthone.navigator_metod()
# mobile_pthone.player_metod()
# mobile_pthone.method()



class Auto:
    def auto_start(self, param1, param2=None):
        if param2 is not None:
            print(param1 + param2)
        else:
            print(param1)

a = Auto()
a.auto_start(10)
a.auto_start(10, 20)