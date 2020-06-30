word = input("give a word: ")
vowels = 0
for char in word:
    if char in "aeiouAEIOU":
        vowels = vowels + 1
print("number of vowels in " + str(word) + " = " + str(vowels))