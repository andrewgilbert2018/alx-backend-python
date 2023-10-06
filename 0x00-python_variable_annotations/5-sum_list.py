#!/usr/bin/env python3
"""
Complex types - list of floats
Creates a sum list of all the elements in the list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums all the elements in the list
    """
    return sum(input_list)
