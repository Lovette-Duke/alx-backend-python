#!/usr/bin/env python3
""" type annotated function that sums a mixed list of floats and ints """


def sum_mixed_list(mxd_lst: list[int | float]) -> float:
    """ sums a mixed list and returns a float """
    return sum(mxd_lst)
