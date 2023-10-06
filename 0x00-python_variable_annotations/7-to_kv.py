#!/usr/bin/env python3
"""
Complex types - string and int/float to tuple
To key value pairs
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts k str and v, to key value pairs
    """
    return (k, float(v**2)
