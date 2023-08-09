import random
RandomNum = random.randint(0,9)
while True: 
    Guess = int(input('Enter a number between 0 and 9: '))
    if Guess == RandomNum:
        print("you have guessed it right, good job")
        break
    else:
        print("Keep trying")