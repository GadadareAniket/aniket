word = input("Enter the word you want to reverse:")
for char in range(len(word) -1, -1, -1):
    print(word[char], end='')
print("\n")