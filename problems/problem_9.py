"""
Given a list of integers, write a function that returns the largest sum of
non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


def max_sum_non_adjacent_nums(numbers):
    prev = 0
    curr_max = 0
    for number in numbers:
        curr_max, prev = max(prev + number, curr_max), curr_max
    return curr_max


if __name__ == '__main__':
    assert max_sum_non_adjacent_nums([2, 4, 6, 2, 5]) == 13
    assert max_sum_non_adjacent_nums([2, 4, 6, 2, 5]) == 13
    assert max_sum_non_adjacent_nums([5, 1, 1, 5]) == 10
