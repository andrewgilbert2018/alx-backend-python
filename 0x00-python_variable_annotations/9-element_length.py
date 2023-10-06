#!/usr/bin/env python3
"""
Let's duck type an iterable object
Calculates element length of a list
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    method to encuenter the element length of a sequence
    """
    return [(i, len(i)) for i in lst]
