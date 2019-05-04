print("PR6 ElGamal DEC")
print("~~~~~~~~~~~")

#Ввод a, b, p, x
a = int(input("Введите a: "))
b = int(input("Введите b: "))
p = int(input("Введите p: "))
x = int(input("Введите x: "))

#Расшифровка
result = (b*a**(p-1-x))%p
print("Сообщение:", result)
