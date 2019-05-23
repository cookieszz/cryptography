print("PR5 RSA_DEC")
print("~~~~~~~~~~~")

d = int(input("Введите секретный ключ d: "))
n = int(input("Введите секретный ключ n: "))
m = int(input("Введите зашифрованое сообщение: "))

result = (m ** d) % n

print("Сообщение:", result)
