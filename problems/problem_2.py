"""
Given an array of integers, return a new array such that each element at index
i of the new array is the product of all the numbers in the original array
except the one at i.

For example, if our input was [1, 2, 3 4, 5,], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be
[2, 3, 6].

Follow-up: what if you can't use division?
"""
from itertools import product
from math import prod
from typing import List


def solution_with_division(numbers: List[int]):
    result = list()
    for n in numbers:
        result.append(int(prod(numbers) / n))
    return result


def solution_without_division(numbers: List[int]):
    # result = [prod([x for x in numbers if n != x]) for n in numbers]
    result = list()
    for n in numbers:
        tmp = list()
        for x in numbers:
            if x != n:
                tmp.append(x)
        result.append(prod(tmp))
    return result


if __name__ == '__main__':
    number_li = [1, 2, 3, 4, 5]
    print(solution_with_division(number_li))
    print(solution_without_division(number_li))
    number_li = [3, 2, 1]
    print(solution_with_division(number_li))
    print(solution_without_division(number_li))
