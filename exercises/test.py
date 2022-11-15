"""to run bits of code from assignments"""

def dup(xs: list[int]) -> None:
    """"""
    start_len: int = len(xs)
    i: int = 0
    while i < start_len:
        xs.append(xs[i])
        i += 1


nums: list[int] = [10, 20]
dup(nums)
print(nums)