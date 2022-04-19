from statistics import mean

a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
c = int(input('Введите число 3: '))
d = int(input('Введите число 4: '))

inp_lst = [a, b, c, d]
list_avg = mean(inp_lst)
print(list_avg)