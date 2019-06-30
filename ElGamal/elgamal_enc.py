print("PR6 ElGamal ENC")
print("~~~~~~~~~~~")

#p, g, y - Открытые ключи
#x - Закрытый ключ
#Ввод p и g
p = int(input("Введите p: "))
g = int(input("Введите g: "))

#Ввод x
while True:
    x = int(input("Введите x(1<x<(p-1)): "))
    if 1 < x < (p - 1):
        break
    else:
        print("Неверное число.")

#Ввод k
while True:
    k = int(input("Введите k(1<k<(p-1)): "))
    if 1 < k < (p - 1):
        break
    else:
        print("Неверное число.")

m = int(input("Введите число сообщения: "))

#Нахождение y
y = (g**x)%p
print('y', y)

#Нахождение a, b
a = (g**k)%p
b = ((y**k)*m)%p

print("Шифротекст:",a, b)
