word = "racecar"
a = len(word)
b = int(a / 2)

for i in range(0, b):
    if word[i] == word[-1 * (i+1)]:
        print("IT IS A PALINDROMEEEEE")
    else:
        print("Not a palindrome...")

