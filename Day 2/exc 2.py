word = input("give a word: ")
num_vowels = 0
for char in word:
    if char in "aeiouAEIOU":
        num_vowels = num_vowels+1
print(num_vowels)