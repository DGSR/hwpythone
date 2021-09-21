from functools import partial
from typing import Any, Dict, List


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """
    def __init__(self, *functions: List[Any]):
        self.functions = functions

    def apply(self, data: List[Any]) -> bool:
        """
        applies filters in self.functions to data and
         returns all data where filters return True
        """
        return [
            item for item in data
            if all(func(item) for func in self.functions)
        ]


def value_by_key_in_dict(val: Dict[Any], key: Any, value: Any) -> bool:
    """
    return True if value by key in dict
    """
    return val[key] == value


def make_filter(**keywords: Dict) -> Filter:
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():
        filter_funcs.append(partial(value_by_key_in_dict,
                                    key=key, value=value))
    return Filter(*filter_funcs)
