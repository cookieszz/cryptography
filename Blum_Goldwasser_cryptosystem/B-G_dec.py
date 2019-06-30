print('PR10_DEC')
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

#Модуль n
m = p * q

#Ввод message, xl
message = input('Cообщение для рассшифровки: ')
xl = int(input('Значение xl: '))
len_m = len(message)

#Алгоритм Безу(расширеный алгоритм Эвклида)
def bezout(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return (x, y, a)

evcl = bezout(p, q)
p1 = evcl[0]
q1 = evcl[1]

#Формирование x1 элемента из p, q, len_m
rp = (((p + 1)/4) ** len_m) % (p - 1)
m_rp = ((xl % p) ** rp) % p

rq = (((q + 1)/4) ** len_m) % (q - 1)
m_rq = ((xl % q) ** rq) % q

x1 = int((m_rp * (q1 * q) + m_rq * (p * p1)) % m)

#Список битов
mass_bin = []

#Генерирование последовательности битов с чисел. Последний бит с числа.
def random_bin(x, n, len_m):
    bin_x = bin(x)
    mass_bin.append(bin_x[-1])
    x1 = (x ** 2) % n
    len_m -= 1

    if len_m > 0:
        random_bin(x1, n, len_m)
        return mass_bin
    else:
        return 0

result  = random_bin(x1, m, len_m)
enc_key = ''.join(mass_bin)

m = int(message, 2)
k = int(enc_key, 2)
dec_m = m ^ k

print('Сообщение:', bin(dec_m))
