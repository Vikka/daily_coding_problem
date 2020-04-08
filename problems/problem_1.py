"""
Given a list of numbers, return whether any two sums to k. For example,
given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
from typing import List


def solution(numbers: List[int], target: int):
    numbers_set = set(numbers)
    for number in numbers:
        numbers_set.remove(number)
        find = target - number
        if find in numbers_set:
            return True
    return False


if __name__ == '__main__':
    assert solution([10, 15, 2, 5], 20)
    assert solution([10, 15, 2, 5], 12)
    assert not solution([10, 15, 2, 5], 8)
