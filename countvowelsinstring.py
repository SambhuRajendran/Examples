word = input('Enter a word to calculate number of vowels: ')

print(len(word))
#print(word[0])

count = 0
i=0

for i in range(len(word)):
    if ((word[i] == 'a')
        or (word[i] == 'e')
        or (word[i] == 'i')
        or (word[i] == 'o')
        or (word[i] == 'u')
        ):
        count = count + 1

print(count)
    


