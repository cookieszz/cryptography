while True:
    n = int(input("Введите непарное число: "))
    if n % 2 == 0:
        print("Число парное!")
    else:
        break

while True:
    x = int(input("Введите x(1<=x<={}): ".format(n-1)))
    if (1 < x < n - 1) or (1 == x or x == n - 1):
        break
    else:
        print("Неверное число!")

def nod_evcl(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

z = nod_evcl(n, x)

#Проверка второго условия
def check_2(n, x):
    for i in range(n - 1):
        if (i * i)%n == x:
            return 1
            break
        else:
            continue

n_x = check_2(n, x)

#Проверка всех условий
if  z != 1:
    print("{} - составное".format(n))
elif (x**((n-1)/2))%n == n_x:
    print("{} - простое".format(n))
else:
    print("{} - составное".format(n))
