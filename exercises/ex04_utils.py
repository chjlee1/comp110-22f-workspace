"""EX04 - Utility Functions: understanding commonly useful functions!"""

__author__: str = "730571111"


def all(nums: list[int], check: int) -> bool:
    """Returns true if all numbers in list equal the check int, false if even one does not."""
    i: int = 0
    if len(nums) == 0:
        return False
    while i < len(nums):
        if nums[i] != check:
            return False
        i += 1
    return True


def max(nums: list[int]) -> int:
    """Finds and returns largest int value in list."""
    large: int = nums[0]
    i: int = 1
    while i < len(nums):
        if nums[i] > large:
            large = nums[i]
        i += 1
    return large


def is_equal(nums: list[int], compare: list[int]) -> bool:
    """Returns true if every int at each position in both lists are equal, false if even one is not."""
    if len(nums) != len(compare):
        return False
    i: int = 0
    while i < len(nums):
        if nums[i] != compare[i]:
            return False
        i += 1
    return True