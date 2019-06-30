print("PR2 Rucksack_DEC(alf)")

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

#Количество сообщений
number = int(input('Введите количество сообщений: '))
number_a = number

bit_mass = []
while True:
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
                result_message.append('1')
            else:
                result_message.append('0')
        return result_message
    result = bit_message(mass_w, num_of_bit)

    bit_mass.append(result)

    number -= 1
    if number > 0:
        continue
    else:
        break

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

#Расшифровка из битов в буквы
def final_letter(mass, alf, num):
    num_mass = []
    mod_num_mass = []
    letter_mass = []

    for i in mass:
        num_mass.append(''.join(i))

    for i in range(num):
        a = num_mass[i][:5]
        mod_num_mass.append(a)
        b = num_mass[i][5:]
        mod_num_mass.append(b)

    for i in mod_num_mass:
        for j in alf:
            if alf[j] == i:
                letter_mass.append(j)
    return letter_mass

letters = final_letter(bit_mass, alfabet, number_a)
letters = ''.join(letters)
print('Сообщение:', letters)
