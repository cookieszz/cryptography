print("PR2 Rucksack_enc")

len = int(input("Введите количество элементов: "))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("--W(Супервозрастающая последовательность)--")

#Ввод списка w
mass_w = []
for i in range(len):
    while True:
        elem = int(input("Введите элемент w: "))
        if elem > sum(mass_w):
            mass_w.append(elem)
            break
        else:
            print("Введите большее число.")

#Ввод числа q
while True:
    q = int(input("Введите q(Больше суммы w): "))
    if q > sum(mass_w):
        break
    else:
        print("Введите большее число.")

#Ввод чисала r
while True:
    r = int(input("Введите r([1, q): "))
    if 1 < r < q:
        break
    else:
        print("Неверное число.")

#Ввод двоичного кода для зашифровки
mass_code = []
print("Введите двоичный код для зашифровки: ")
for i in range(len):
    while True:
        elem = int(input("Значение: "))
        if elem == 1 or elem == 0:
            mass_code.append(elem)
            break
        else:
            print("Значение не двоичное.")
print(mass_code)

#Формирование открытого ключа
def open_key(w, q, r):
    mass_open_key = []
    for i in w:
        mass_open_key.append((i*r)%q)
    return mass_open_key

op_key = open_key(mass_w, q, r)

#Шифровка для получателя
def for_user(bin, mass):
    mess = []
    for i, j in zip(mass, bin):
        mess.append(i*j)
    return sum(mess)

result = for_user(mass_code, op_key)
print("Сообщение: ", result)
