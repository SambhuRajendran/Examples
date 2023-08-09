#get a list of words
import string
words = input("Enter words you want (comma=seperated): ").split(',')
for i in range(len(words)):
    newword = words[i].strip() #remove any leading and trailing spaces
    print(newword[0])