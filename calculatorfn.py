def addition():
    numbers = int(input('How many numbers you want to Add: '))
    listofnumbers= []
    for _ in range(1, numbers+1):
        value = int(input('Enter the value: '))
        listofnumbers.append(value)
    print(f'Sum of the given values = {sum(listofnumbers)}. Thanks for using the Addition function.')

#addition()    

def multiplication():
    try: 
      numbers = int(input('How many numbers you want to Multiply: '))
      listofnumbers= []
      for _ in range(1, numbers+1):
          value = int(input('Enter the value: '))
          listofnumbers.append(value)
      initial = 1
      for n in listofnumbers:
          initial = initial * n
      print(initial)
    except ValueError:
        print('Enter a valid number. Try Again.')
        
multiplication()