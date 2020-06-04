print('Test')
print("What you need?")

def ZP_all(h, p, b):
    return h * p + b
h = int(input('время: '))
p = int(input('ставка: '))
b = int(input('бонус: '))
print('ZP: ', ZP_all(h, p, b))