numbers = [5, 11, 7, 9, 2] 
size = len(numbers)
index = 0
max = numbers[0]

while index < size:
    if numbers[index] > max:
        max = numbers[index]
    else: index +=1
else:
    print(max)

# или встроенная функци питона: max_number = max(numbers)