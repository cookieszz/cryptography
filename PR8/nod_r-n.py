'''Проверка на Нод 2-х чисел'''
r = int(input("Введите r: "))
n = int(input("Введите n: "))

def nod_evcl(e, fi):
    while e != 0 and fi != 0:
        if e > fi:
            e = e % fi
        else:
            fi = fi % e
    return e + fi

result = nod_evcl(r, n)
print(result)
