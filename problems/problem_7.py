"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as
'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not
allowed.
"""
from functools import lru_cache
from typing import Optional

from utils.functools import lru_cache_


@lru_cache_
def how_many_with_int(len_code: int):
    if len_code == 1:
        return 1
    if len_code == 2:
        return how_many_with_int(len_code - 1) + 1
    return how_many_with_int(len_code - 1) + how_many_with_int(len_code - 2)


def how_many_decode(code: str):
    len_code = len(code)
    return how_many_with_int(len_code)


if __name__ == '__main__':
    assert how_many_decode('111') == 3
    assert how_many_decode('111111111111') == 233
    assert how_many_decode(
        '11111111111111111111111111111111111111111111111111111111111111111111')\
        == 117669030460994
