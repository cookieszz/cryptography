print("PR5 RSA_ENC")
print("~~~~~~~~~~~")

#e и fi Взаимно простые
#p, q
p = int(input("Введите p: "))
q = int(input("Введите q: "))

#Значение функции Эйлера
fi = (p - 1) * (q - 1)

#Введение e
while True:
    e = int(input("Открытая экспонента e(1<e<fi({})): ".format(fi)))
    if 1 < e < fi:
        break
    else:
        print("Неверное число")

#Вычисление модуля
n = p * q

#Мультипликативное обратное 'd' к 'e' по модулю 'fi'
#Секретная экспонента
def multi_d(e, fi):
    d = 1
    while True:
        if (d * e) % fi == 1:
            break
        else:
            d += 1
    return d

d = multi_d(e, fi)

print("Открытый ключ(e, n):({}, {})".format(e, n))
m = int(input("Введите сообщение: "))

#Зашифровка
result = (m ** e) % n

print("Зашифрованое сообщение:", result)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Секретный ключ(d, n):({}, {})".format(d, n))
