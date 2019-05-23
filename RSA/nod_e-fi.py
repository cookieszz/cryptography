'''Проверка на Нод 2-х чисел'''
e = int(input("Введите e: "))
fi = int(input("Введите f: "))

def nod_evcl(e, fi):
    while e != 0 and fi != 0:
        if e > fi:
            e = e % fi
        else:
            fi = fi % e
    return e + fi

result = nod_evcl(e, fi)
print(result)
