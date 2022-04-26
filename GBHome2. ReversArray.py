list = [1, 15, 7, 114, 10, 9, 88]

for i in range(len(list)//2):
    temp = list[i]
    list[i] = list[len(list)-i-1]
    list[len(list)-i-1] = temp
#a.reverse() - встроенная функция реверса, или кортежем

print(list)