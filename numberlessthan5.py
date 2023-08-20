numbers = (input("Enter the numbers you want to check for 5: ")).split(',')
print(type(numbers))
print(numbers)
for i in range(0, len(numbers)):
    numbers[i]=int(numbers[i])

print((numbers))
print(type(numbers))

for i in numbers:
    if i < 5:
        print(f'{i}, is less than 5')
    else:
        continue