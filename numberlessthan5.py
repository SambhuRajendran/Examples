numbers = (input("Enter the numbers you want to check for 5: ")).split(',')
for i in range(0, len(numbers)):
    numbers[i]=int(numbers[i])

count=0
for i in numbers:
    if i < 5:
                print(f'{i}, is less than 5')
    else:
        count = count+1
        continue

print(f'There are {count} inputs that are greater than 5')