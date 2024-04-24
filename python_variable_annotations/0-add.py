#!/usr/bin/env python3
"""
    Type-annotated function that takes
    a float a and a float b as arguments
    and returns their sum as a float.
"""


def add(a: float, b: float) -> float:
    """
        Add two float arguments

        Args:
            a (float): first float argument
            b (float): second float argument

        Returns:
            float: sum of a and b
    """
    return a + b
