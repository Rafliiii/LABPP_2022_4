matriks_pertama = []
for i in range(2):
    baris = []
    for j in range(2):
        angka = int(input(f'Input nilai matriks pertama index {i+1},{j+1}: '))
        baris.append(angka)
    matriks_pertama.append(baris)

matriks_kedua = []
for i in range(2):
    baris = []
    for j in range(2):
        angka = int(input(f'Input nilai matriks kedua index {i+1},{j+1}: '))
        baris.append(angka)
    matriks_kedua.append(baris)

hasil1 = matriks_pertama[0][0]*matriks_kedua[0][0] + matriks_pertama[0][1]*matriks_kedua[1][0]
hasil2 = matriks_pertama[0][0]*matriks_kedua[0][1] + matriks_pertama[0][1]*matriks_kedua[1][1]
hasil3 = matriks_pertama[1][0]*matriks_kedua[0][0] + matriks_pertama[1][1]*matriks_kedua[1][0]
hasil4 = matriks_pertama[1][0]*matriks_kedua[0][1] + matriks_pertama[1][1]*matriks_kedua[1][1]
print(f'| {matriks_pertama[0][0]}, {matriks_pertama[0][1]} | x | {matriks_kedua[0][0]}, {matriks_kedua[0][1]} | = | {hasil1}, {hasil2} |')
print(f'| {matriks_pertama[1][0]}, {matriks_pertama[1][1]} |   | {matriks_kedua[1][0]}, {matriks_kedua[1][1]} |   | {hasil3}, {hasil4} |')
