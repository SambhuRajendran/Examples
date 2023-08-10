# MULTIPLICATION TABLE
#This program takes multiple number from user to multiply until the range of number they provide
number = (input('Enter the numbers separated by comma: ')).split(',')
until = (int(input('Until what number: ')))
numbers =[] #Empty list to append integers
for i in number:
     #Converting numbers to integer
     numbers.append(int(i))

for i in numbers:
    for j in range(1, until+1):
        print(f'{i} multiplied by {j} is: ',i*j)


