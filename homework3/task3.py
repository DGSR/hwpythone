from functools import partial
from typing import Any, Dict, List


class Filter:
    """
        Helper filter class. Accepts a list of single-argument
        functions that return True if object in list conforms to some criteria
    """
    def __init__(self, *functions: List[Any]) -> None:
        self.functions = functions

    def apply(self, data: List[Any]) -> bool:
        return [
            item for item in data
            if all(func(item) for func in self.functions)
        ]


def keyword_filter_func(val: List[Any], key: List[Any], value: Any) -> bool:
    return val[key] == value


def make_filter(**keywords: Dict) -> Filter:
    """
        Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():
        filter_funcs.append(partial(keyword_filter_func, key=key, value=value))
    return Filter(*filter_funcs)
