"""
Given a list of numbers, return whether any two sums to k. For example,
given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
from typing import List


def solution(numbers: List[int], target: int):
    for number in numbers:
        tmp_nbrs = numbers.copy()
        tmp_nbrs.remove(number)

        find = k - number
        if find in tmp_nbrs:
            return True, (number, find)
    return False


if __name__ == '__main__':
    numbers_li = [10, 15, 3, 7]
    k = 20
    print(solution([10, 15, 2, 5], k))
