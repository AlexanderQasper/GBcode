list = [1, 15, 7, 114, 10, 9, 88]

min_id = 0
max_id = 0
summa = 0

for i in range(len(list)):
    if list[i] < list[min_id]:
        min_id = i
    if list[i] > list[max_id]:
        max_id = i
print(list[min_id], list[max_id])

if min_id > max_id:
    min_id, max_id = max_id, min_id

for i in range(min_id+1, max_id):
    summa += list[i]
print(summa)