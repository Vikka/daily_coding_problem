from typing import Sequence, Tuple


def merge_sort(it: Sequence) -> Tuple:
    len_ = len(it)
    if len_ == 2:
        if it[0] > it[1]:
            return it[1], it[0]
        else:
            return it[0], it[1]
    elif len_ == 1:
        return (it[0],)
    len_ = len_ // 2
    part_1 = merge_sort(it[:len_])
    part_2 = merge_sort(it[len_:])
    if part_1[0] > part_2[0]:
        return part_2 + part_1
    return part_1 + part_2


def sorted_(*args: Sequence):
    if len(args) == 1:
        return merge_sort(*args)
    sorted_lists = list()
    for it in args:
        tmp_list = merge_sort(it)
        sorted_lists.append(list(tmp_list))
    return sorted_lists
