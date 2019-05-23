g = int(input("Введите значение g: "))
p = int(input("Введите значение p: "))
a = int(input("Секретный ключ Алисы: "))

mess_a = (g**a)%p
print("Сообщение Алисы: ", mess_a)

message = int(input("Сообщение Боба: "))

key_a = (message**a)%p

print(key_a)
