# 1. len() returns the length of the string.
text = "ChocolateCake"
print(len(text)) # Output: 13

# 2. endswith() checks if a string ends with given text.
text = "ChocolateCake"
print(text.endswith("Cake")) # Output: True

# 3. count() counts total occurrences of a character.
text = "ChocolateCake"
count = text.count("o")
print(count) # Output: 2

# 4. capitalize() capitalizes the first character.
text = "chocolateCake"
capitalized = text.capitalize()
print(capitalized) # Output: Chocolatecake

# 5. find() returns the index of first occurrence.
text = "ChocolateCake"
index = text.find("late")
print(index) # Output: 5

# 6. replace(old word, new word) replaces the old word with the new word in the string.
text = "ChocolateCake"
replaced = text.replace("o", "A")
print(replaced) # Output: ChAcAlateCake