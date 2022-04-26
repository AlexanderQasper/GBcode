numbers = [1, 8, 3, 2, 6]
size = len(numbers)
first = numbers[0]
second = numbers[0]
current_index = 0

while (current_index < size):
    if(numbers[current_index] > first):
        second = first
        first = numbers[current_index]
    else:
        if(numbers[current_index] > second):
            second = numbers[current_index]
    current_index = current_index + 1

print(second)