#numbers = input("Enter the int values: ").strip(',')
numbers = ['1','2','3']
numbers = list(map(int, numbers))
print(numbers)
print(type(numbers))