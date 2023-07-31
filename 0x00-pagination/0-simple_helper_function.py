#!/usr/bin/env python3
""" return tuple"""


def index_range(page: int, page_size: int) -> tuple:
    """return a tuple of size two containing
    a start index and an end index corresponding
    to the range of indexes to return in a list
    for those particular pagination parameters """
    myTuple = ((page - 1) * page_size, page * page_size)
    return (myTuple)
