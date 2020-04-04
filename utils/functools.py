from typing import Optional


def lru_cache_(func, maxsize: Optional[int] = None, typed: [bool] = False):
    lru_dict = dict()

    def inner(*arg, **kwargs):
        if (key := (arg, *kwargs)) in lru_dict:
            return lru_dict[key]
        lru_dict[key] = func(*arg, **kwargs)
        return lru_dict[key]

    return inner
