def add():
    numbers = int(input('How many numbers you want to add: '))
    listofnumbers= []
    for i in range(1, numbers+1):
        value = int(input('Enter the value: '))
        listofnumbers.append(value)
    print(sum(listofnumbers))
    
add()    

