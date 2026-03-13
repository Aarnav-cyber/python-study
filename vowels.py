sentence = "Aarnav Slesh"
vowels1 = "aeiou"
vowels2 = "AEIOU"

total = len(sentence)
count = 0

for char in sentence:
    if char in vowels1 or char in vowels2:
        count = count + 1

print("Total number of vowels are: ", count)

consonants = total - count - 1
print(f"Since total number of vowels are {count}, total consonants are: {consonants}")