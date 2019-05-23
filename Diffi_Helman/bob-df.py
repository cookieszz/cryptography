g = int(input("Введите значение g: "))
p = int(input("Введите значение p: "))
b = int(input("Секретный ключ Боба: "))

mess_b = (g**b)%p
print("Сообщение Боба: ", mess_b)

message = int(input("Сообщение Алисы: "))

key_b= (message**b)%p

print(key_b)
