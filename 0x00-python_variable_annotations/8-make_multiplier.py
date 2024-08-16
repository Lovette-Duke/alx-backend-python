#!/usr/bin/env python3
""" a type-annotated function that uses a float as a multiplier """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ a float multiplyer """
    return lambda x: multiplier * x
