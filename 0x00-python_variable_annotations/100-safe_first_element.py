#!/usr/bin/env python3
"""
Duck typing - first element of a sequence
Obtains the first element of a list safely
"""
from typing import Any, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Obtains the first element of a list safely
    """
    if lst:
        return lst[0]
    else:
        return None
