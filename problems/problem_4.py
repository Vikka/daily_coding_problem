"""
Given an array of integers, find the first missing positive integer in linear 
time and constant space. In other words, find the lowest positive integer that 
does not exist in the array. The array can contain duplicates and negative 
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should 
give 3.

You can modify the input array in-place.

Some other thoughts:

    A naive method to solve this problem is to search all positive integers, 
    starting from 1 in the given array. We may have to search at most n+1 
    numbers in the given array. So this solution takes O(n^2) in worst case.
    
    We can use sorting to solve it in lesser time complexity. We can sort the 
    array in O(nLogn) time. Once the array is sorted, then all we need to do is 
    a linear scan of the array. So this approach takes O(nLogn + n) time which 
    is O(nLogn).
    
    We can also use hashing. We can build a hash table of all positive elements 
    in the given array. Once the hash table is built. We can look in the hash 
    table for all positive integers, starting from 1. As soon as we find a 
    number which is not there in hash table, we return it. This approach may 
    take O(n) time on average, but it requires O(n) extra space.
"""
from typing import List

from utils.itertools import count
from utils.sequences import sorted_


def solution_1(numbers: List[int]):
    for i in count(start=1):
        if i not in numbers:
            return i


def solution_2(numbers: List[int]):
    sorted_numbers = sorted_(numbers)
    for i in count(start=1):
        if i not in sorted_numbers:
            return i


def solution_3(numbers: List[int]):
    numbers = set(numbers)
    for i in count(start=1):
        if i not in numbers:
            return i


if __name__ == '__main__':
    foo = [3, 4, -1, 1]
    bar = [1, 2, 0]
    assert solution_1(foo) == 2
    assert solution_1(bar) == 3
    assert solution_2(foo) == 2
    assert solution_2(bar) == 3
    assert solution_3(foo) == 2
    assert solution_3(bar) == 3
