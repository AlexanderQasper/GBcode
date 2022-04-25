list = [5, 7, 12, 9]
cur_ind = 0
max_ind = 0
size = len(list)

while cur_ind < size:
    if list[cur_ind] > list[max_ind]:
        max_ind = cur_ind
    cur_ind = cur_ind + 1

temp = list[max_ind]
list[max_ind] = list[size - 1]
list[size - 1] = temp

print(list)