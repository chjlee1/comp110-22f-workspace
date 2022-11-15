"""Creating various functions that utilize dictionaries."""

__author__: str = "730571111"


def invert(inputs: dict[str, str]) -> dict[str, str]:
    """Creates and returns an inverted version of original dictionary."""
    inverted: dict[str, str] = dict()
    for input in inputs:
        if inputs[input] in inverted:
            raise KeyError("More than one of the same key inverted.")
        else:
            inverted[inputs[input]] = input
    return inverted


def favorite_color(colors: dict[str, str]) -> str:
    """Finds which color is favorited the most and returns that color."""
    color_count: dict[str, int] = dict()
    for color in colors:
        if colors[color] in color_count:
            color_count[colors[color]] += 1
        else:
            color_count[colors[color]] = 1
    favorite: str = ''
    for color in color_count:
        if favorite == '' or color_count[favorite] < color_count[color]:
            favorite = color
    return favorite


def count(inputs: list[str]) -> dict[str, int]:
    """Counts how many times a value appears in the input list."""
    count: dict[str, int] = dict()
    for input in inputs:
        if input in count:
            count[input] += 1
        else:
            count[input] = 1
    return count
    

print(invert({'a': 'z', 'b': 'y', 'c': 'x'}))
print(invert({'apple': 'cat'}))

print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))

print(count(['a', 'b', 'c', 'a', 'c', 'a']))