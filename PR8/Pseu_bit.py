print('--PR8--')
print('Генератор псевдослучайных битов')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#Введение p
while True:
    p = int(input("Введите p(p = 3(mod 4)): "))
    if p % 4 == 3:
        break
    else:
        print('Неверное число!')

#Введение q
while True:
    q = int(input("Введите q(p = q = 3(mod 4), p != q): "))
    if p == q:
        print('Неверное число!')
    elif q % 4 == 3:
        break
    else:
        print('Неверное число!')

number_bin = int(input('Введите количество битов: '))

#Модуль n
n = p * q
print('n',n)

#Ввод r
r = int(input('Введите r, nod(r, n) = 1 : '))

#Начальное значение последовательности
x0 = (r ** 2) % n
print('x0', x0)

#Список битов
mass_bin = []

#Генерирование последовательности битов с чисел. Последний бит с числа.
def random_bin(x, n, number_bin):
    x1 = (x ** 2) % n
    print('x1: ', x1)
    bin_x1 = bin(x1)
    mass_bin.append(bin_x1[-1])
    number_bin -= 1

    if number_bin > 0:
        random_bin(x1, n, number_bin)
        return mass_bin
    else:
        return 0

result  = random_bin(x0, n, number_bin)
z = ''.join(mass_bin)
print("Последовательность битов:", z)
