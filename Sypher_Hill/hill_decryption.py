import numpy as np

'''ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
print("PR1 Decryption")
print("-------------------------")
print("""A-0,B-1,C-2,D-3,E-4,\nF-5,G-6,H-7,I-8,J-9,K-10,\nL-11,M-12,N-13,O-14,P-15,\nQ-16,R-17,S-18,T-19,U-20,\nV-21,W-22,X-23,Y-24,Z-25""")
print("-------------------------")

alphabet = 26

#Введение матрицы.
mass_1 = []
for i in range(4):
    mass_1.append(int(input("Введите матрицу(4): ")))
mass_1m = np.array(mass_1, int).reshape(2,2)

lenn = int(input("Введите количество букв(x2): "))

#Введение векторов.
vector_1 = []
for i in range(lenn):
    vector_1.append(int(input("Введите вектор:")))
vector_1m = np.array(vector_1, int).reshape(int(lenn/2), 2).transpose()

#Нахождение детерминанта.
determinat = int(round(np.linalg.det(mass_1m)))

#Алгоритм Эвклида.
def nod_evcl(det, alf):
    while det != 0 and alf != 0:
        if det > alf:
            det = det % alf
        else:
            alf = alf % det
    return det + alf

nod = nod_evcl(determinat, alphabet)

#Нахождение x из алгоритма Эвклида.
def find_x(det, x):
    for i in range(-10, 10):
        if (det * i) % 26 == x:
            return i
            break
        else:
            i += 1

x = find_x(determinat, nod)

#Корекция x.
def new_x(det, x):
    if (det < 0 and x > 0) or (det > 0 and x > 0):
        return x
    elif det > 0 and x < 0:
        return 26 + x
    else:
        return -x

x1 = new_x(determinat, x)

#Матрица алгебраических дополнений. Умножение на детерминант и транспонирование матрицы.
def mat_alg(x1, alf):
    mass_1m[0][0], mass_1m[1][1] = mass_1m[1][1], mass_1m[0][0]
    mass_1m[0][1], mass_1m[1][0] = mass_1m[1][0]*(-1), mass_1m[0][1]*(-1)
    mass_2m = np.array(mass_1m, int)
    mass_2m = ((mass_2m * x1)%alf).transpose()
    return mass_2m

final_mass = mat_alg(x1, alphabet)

#Умножение матрицы на вектор
result = np.dot(final_mass, vector_1m)

print("Ответ: ",(result%26).transpose().flatten())
