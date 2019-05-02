'''Провека на Нод 2-х чисел'''
r = int(input("Введите r: "))
q = int(input("Введите q: "))

def nod_evcl(r, q):
    while r != 0 and q != 0:
        if r > q:
            r = r % q
        else:
            q = q % r
    return r + q

result = nod_evcl(r, q)
print(result)
