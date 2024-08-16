#!/usr/bin/env python3
""" a type-annotated function that takes a string, int OR float 
as arguments and returns a tuple. """


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a string and int/float and returns a tuple"""
    return (k, v ** 2)
