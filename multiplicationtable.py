number = int(input('Enter the number: '))
until = int(input('Until what number: '))

for i in range(1,until+1):
    print(f'{number} multiplied by {i} is: ', number*i)