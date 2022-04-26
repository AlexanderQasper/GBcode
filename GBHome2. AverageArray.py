#from statistics import mean
#list = [1, 15, 7, 114, 10, 9, 88]

#list_avg = mean(inp_lst)
#print(list_avg)

list = [1, 15, 7, 14, 10, 9, 88]
s = 0

for i in range(len(list)):
    s += list[i]
avr = s/len(list)

print(avr)