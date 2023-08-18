word = input('Enter a word to calculate number of vowels: ')
count = 0
i=0
vowels = ['a', 'e', 'i', 'o', 'u']


for i in range(len(word)):
    if word[i] in vowels:
        print(word[i], ' is a vowel')
        count = count + 1
print(count)
    


