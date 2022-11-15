"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730571111"


word: str = input("Enter a 5-character word: ")
if (len(word) != 5):
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")
if (len(character) != 1):
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + character + " in " + word)

counter: int = 0
increment: int = 0
for x in word:
    if (word[increment] == character):
        print(character + " found at index " + str(increment))
        counter += 1
    increment += 1

if (counter == 1):
    print(str(counter) + " instance of " + character + " found in " + word)
elif (counter > 1):
    print(str(counter) + " instances of " + character + " found in " + word)
else:
    print("No instances of " + character + " found in " + word)
