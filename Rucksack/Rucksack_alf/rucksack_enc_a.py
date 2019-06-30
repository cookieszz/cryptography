print("PR2 Rucksack_ENC(alf)")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("--W(Супервозрастающая последовательность)(10 элементов)--")

#W, r, q - секретный ключ
#Ввод списка w
mass_w = []
for i in range(10):
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

#Формирование открытого ключа
def open_key(w, q, r):
    mass_open_key = []
    for i in w:
        mass_open_key.append((i*r)%q)
    return mass_open_key

op_key = open_key(mass_w, q, r)
print("Открытый ключ: ",op_key)

#Ввод количества букв для зашифровки(x2), для недостающей буквы добавте '-'
number = int(input('Введите количество букв(x2): '))

alfabet = {'A': '00000',
           'B': '00001',
           'C': '00010',
           'D': '00011',
           'E': '00100',
           'F': '00101',
           'G': '00110',
           'H': '00111',
           'I': '01000',
           'J': '01001',
           'K': '01010',
           'L': '01011',
           'M': '01100',
           'N': '01101',
           'O': '01110',
           'P': '01111',
           'Q': '10000',
           'R': '10001',
           'S': '10010',
           'T': '10011',
           'U': '10100',
           'V': '10101',
           'W': '10110',
           'X': '10111',
           'Y': '11000',
           'Z': '11001',
           '-': '11010'}

#Ввод букв для зашифровки
while True:
    mass_code = []
    for i in range(2):
        while True:
            alf = input('Буква: ')
            if alf in alfabet:
                e = alfabet[alf]
                for i in e:
                    mass_code.append(int(i))
                break
            else:
                print('Неверное значение!')

    #Шифровка для получателя
    def for_user(bin, mass):
        mess = []
        for i, j in zip(mass, bin):
            mess.append(i*j)
        return sum(mess)

    result = for_user(mass_code, op_key)
    print("Сообщение:", result)
    number -= 2
    if number == 0:
        print('~~~~~~~~~~~~~~')
        break
    else:
        continue
