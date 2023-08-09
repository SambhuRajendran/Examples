word = input("Enter your word to check palindrome: ")

if word.upper() == word.upper()[::-1]:
    print(f"{word} is a palindrome")
else:
    print('Try again')