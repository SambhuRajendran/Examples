def addition():
    try: 
      numbers = int(input('How many numbers you want to Add: '))
      listofnumbers= []
      for _ in range(1, numbers+1):
          value = int(input('Enter the value: '))
          listofnumbers.append(value)
      print(f'Sum of the given values = {sum(listofnumbers)}. Thanks for using the Addition function.')
    except ValueError:
        print('Please enter a valid number. Try again.')


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
      print(f'Multiplication of the given values = {initial}. Thanks for using the Multiplication function.')
    except ValueError:
        print('Please enter a valid number. Try Again.')

def main():
  while True: 
    print('Hello, Welcome to the calculator program')
    print('Press "1" for Addition, "2" for Multiplicaton, "y/Y to exit" ')
    try:
      userinput = int(input('What action you want to perform: '))
      if userinput == 1:
        addition()
      elif userinput == 2:
        multiplication()
      elif userinput == "y":
         exit
    except ValueError:
      print("Please give a valid input. Try Again. Thanks!")

if __name__ == "__main__":
   main()
  