n = int(input("enter the number to find factorial: "))
#Factorial formula = n(n-1)
factorial = 1
for i in range(1,n+1):
    factorial = factorial*i
print(factorial)


