import numpy as np

'''ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
print("PR1 Encryption")
print("-------------------------")
print("""A-0,B-1,C-2,D-3,E-4,F-5,\nG-6,H-7,I-8,J-9,K-10,\nL-11,M-12,N-13,O-14,P-15,\nQ-16,R-17,S-18,T-19,U-20,\nV-21,W-22,X-23,Y-24,Z-25""")
print("-------------------------")

mass_1 = []
for i in range(4):
    mass_1.append(int(input("Введите матрицу(4): ")))
mass_1m = np.array(mass_1, int).reshape(2,2)

lenn = int(input("Введите количество букв(x2): "))

vector_1 = []
for i in range(lenn):
    vector_1.append(int(input("Введите вектор:")))
vector_1m = np.array(vector_1, int).reshape(int(lenn/2), 2).transpose()

result = np.dot(mass_1m, vector_1m)

print("Ответ: ",(result%26).transpose().flatten())
