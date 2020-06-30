word=input("Please enter a word")
vowels=("A","E","I","U")
vowel_count = 0
aVowel=""
for char in word:
    for aVowel in vowels:
        if aVowel == char:
            vowel_count = vowel_count + 1

print(vowel_count)



