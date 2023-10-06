#!/usr/bin/env python3
"""
Complex types - mixed list
Sum mixed list of elements
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums all the elements in the list
    """
    return sum(mxd_lst)
