#!/usr/bin/env python3
"""
    Type-annotated function that takes
    a float multiplier as arguments
    and returns function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the given multiplier."""
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
