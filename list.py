numbers = [1, 5, 7, 2, 3, 8, 4, 6, 10, 9, 11]

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num 

print("Largest:", largest)

smallest = numbers[0]
for num1 in numbers:
    if smallest > num1:
        smallest = num


print("Smallest: ", smallest)