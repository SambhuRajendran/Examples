#get a list of words
import string
words = input("Enter words you want (comma=seperated): ").split(',')
for i in range(len(words)):
    words[i]=words[i]
    print(words[i][0])