#!/usr/bin/env python3
"""
    Type-annotated function which takes
    a list of integers and floats as arguments
    and returns their sum as a float.
"""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of integers and floats."""
    return sum(mxd_lst)