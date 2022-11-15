"""EX02 - one shot wordle."""

__author__: str = "730571111"

# initializing secret word, inputting users guess word and checking if it is proper length
secret_word: str = "python"
length: int = len(secret_word)
guess: str = input(f"What is your {str(length)}-letter guess? ")
while (len(guess) != length):
    guess = input(f"That was not {str(length)}-letters! Try again: ")

# initializing colored boxes
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# looping to check whether each letter of guess is found in seceret word
i: int = 0
result: str = ""
while (i < length):
    if (guess[i] == secret_word[i]):
        result += GREEN_BOX
    else:
        j: int = 0
        found: bool = False
        while (j < length):  # nested loop which checks if current letter is correct letter but in a different position
            if (guess[i] == secret_word[j]):
                found = True
            j += 1
        if (found is True):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
    i += 1

# outputs
print(result)
if (guess == secret_word):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")