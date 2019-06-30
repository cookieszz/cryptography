print("PR2 Rucksack_DEC")

len = int(input("Введите количество элементов: "))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("--W(Супервозрастающая последовательность)--")

#W, r, q - секретный ключ
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
    q = int(input("Введите q(Больше суммы w = {}): ".format(sum(mass_w))))
    if q > sum(mass_w):
        break
    else:
        print("Введите большее число.")

#Ввод чисала r
while True:
    r = int(input("Введите r([1, q = {}))(НОД r,q = 1): ". format(q)))
    if 1 < r < q:
        break
    else:
        print("Неверное число.")

#Ввод сообщения
message = int(input("Введите сообщение для расшифровки: "))

#Мультипликативное обратное r по модулю q
def modul_mess(r, q, m):
    r1 = 1
    while True:
        if (r * r1)%q == 1:
            break
        else:
            r1 += 1
    result = (m * r1)%q
    return result

mod_m = modul_mess(r, q, message)

#Получение значений для битов зашифрованого текста
mass_code = []
def find_num(w, m):
    i = -1
    while True:
        if w[i] <= m:
            num = m - w[i]
            break
        else:
            i -= 1
    mass_code.append(w[i])
    if num == 0:
        return 1
    else:
        find_num(mass_w, num)
        return mass_code

num_of_bit = find_num(mass_w, mod_m)
num_of_bit.reverse()

#Получение битов и целого сообщения
def bit_message(w, n):
    result_message = []
    for i in w:
        if i in n:
            result_message.append(1)
        else:
            result_message.append(0)
    return result_message
result = bit_message(mass_w, num_of_bit)
print("Сообщение:", result)
