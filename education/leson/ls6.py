# print('hello ls6')

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
        self._loading()

    def call(self):
        print('calling')

    def _loading(self):
        print(self.model, 'loading...')

my_phone = Phone('nokia1100')
my_phone.call()
my_phone._loading()
# print(my_phone.model)
