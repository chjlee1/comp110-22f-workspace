"""EX03 - Structured Wordle: Putting everything together!"""

__author__: str = "730571111"


def contains_char(word_search: str, char_search: str) -> bool:
    """Searches word for matching letter!"""
    assert len(char_search) == 1
    i: int = 0
    while (i < len(word_search)):
        """loops through entire secret word for instances of current letter!"""
        if (word_search[i] == char_search):
            return True
        i += 1
    return False


def emojified(guess: str, secret_word: str) -> str:
    """Returns a string of colored emoji depending on guess: Green = Correct, Yellow - Wrong position, White - Incorrect."""
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""
    i: int = 0
    while (i < len(secret_word)):
        """Looks whether current letter is correct in correct position, if not looks elsewhere!"""
        if (guess[i] == secret_word[i]):
            result += GREEN_BOX
        elif (contains_char(secret_word, guess[i])):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        i += 1
    return result


def input_guess(length: int) -> str:
    """User inputs a guess word with same length as secret word, returns the guess string!"""
    guess: str = input(f"Enter a {str(length)} character word: ")
    while (len(guess) != length):
        guess = input(f"That wasn't {str(length)} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turn: int = 1
    while (turn <= 6):
        print(f"=== Turn {turn}/6 ====")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if (guess == secret_word):
            print(f"You won in {turn}/6 turns!")
            break 
        turn += 1
    if (turn == 7):
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()