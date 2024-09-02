#!/usr/bin/env python3
"""Simple Pagination helper function."""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple containing a start index
    and an end index for pagination params."""
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return (start_idx, end_idx)
