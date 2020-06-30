word = input("give a word: ")
vowels = 0
for char in word:
    if char in "aeiouAEIOU":
        # if statement could be used with lower() instead of hardcoding capital letters
        vowels = vowels + 1
print("number of vowels in " + str(word) + " = " + str(vowels))
