#!/usr/bin/env python3
"""
 More involved type annotations
Method to safely get a value
"""
from typing import Any, Mapping, Optional, TypeVar, Union
T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Optional[T] = None,
) -> Union[Any, T]:
    """
    method to safely get a value
    """
    if key in dct:
        return dct[key]
    else:
        return default
