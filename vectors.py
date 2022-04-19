a = int(input('Вектор 1, x: '))
b = int(input('Вектор 1, y: '))
c = int(input('Вектор 2, x: '))
d = int(input('Вектор 2, y: '))

vector1 = [a,b]
vector2 = [c,d]
size = len(vector1)
scalarproduct = 0
index = 0

while index < size:
    scalarproduct = scalarproduct + vector1[index] * vector2[index]
    index +=1
print(scalarproduct)