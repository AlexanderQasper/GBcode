vector1 = [3,5]
vector2 = [5,2]
size = 2 
scalarproduct = 0
index = 0

while index < size:
    scalarproduct = scalarproduct + vector1[index] * vector2[index]
    index +=1
else:
    print(scalarproduct)