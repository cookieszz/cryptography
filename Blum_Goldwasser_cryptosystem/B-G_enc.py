print('PR10_ENC')
print("Криптосистема Блюма-Гольдвассера")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#Введение p
while True:
    p = int(input("Введите p(p = 3(mod 4)): "))
    if p % 4 == 3:
        break
    else:
        print('Неверное число!')

#Введение q
while True:
    q = int(input("Введите q(p = q = 3(mod 4), p > q): "))
    if p == q or p < q:
        print('Неверное число!')
    elif q % 4 == 3:
        break
    else:
        print('Неверное число!')

number_bin = int(input('Введите количество битов: '))
len_m = number_bin + 1

#Модуль n
n = p * q

#Ввод r
#r = int(input('Введите r, nod(r, {}) = 1: '.format(n)))
r = int(input('Введите r, 1 < r < {}: '.format(p * q)))

#Начальное значение последовательности
x0 = (r * r) % n

#Список битов
mass_bin = []

#Генерирование последовательности битов с чисел. Последний бит с числа.
def random_bin(x, n, number_bin):
    x1 = (x ** 2) % n
    bin_x1 = bin(x1)
    mass_bin.append(bin_x1[-1])
    number_bin -= 1

    if number_bin > 0:
        random_bin(x1, n, number_bin)
        return x1
    else:
        return x1

final_x  = random_bin(x0, n, number_bin)
key = ''.join(mass_bin)

#Введение сообщения
message = input('Введите сообщение {}-bit: '.format(number_bin))

#Шифрование
m = int(message, 2)
k = int(key, 2)
result = m ^ k

#Ключ xl
xl = (x0**(2**len_m))% n

print('Криптотекст({}, {}): '.format(bin(result), xl))
