"""unit testing and more utility functions."""

__author__: str = "730571111"


def only_evens(nums: list[int]) -> list[int]:
    """Returns a new list of only evens from the original."""
    evens: list[int] = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens


def concat(first: list[int], second: list[int]) -> list[int]:
    """Returns a new list containing all elements from first list followed by second list."""
    final: list[int] = []
    for num in first:
        final.append(num)
    for num in second:
        final.append(num)
    return final


def sub(nums: list[int], start: int, end: int) -> list[int]:
    """Returns a new list of subset from original list based on start and end values."""
    final: list[int] = []
    if start < 0:
        start = 0
    if end > len(nums):
        end = len(nums)
    if len(nums) == 0 or start >= len(nums) or end <= 0:
        return final
    while start < end:
        final.append(nums[start])
        start += 1
    return final
