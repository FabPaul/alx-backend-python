#!/usr/bin/env python3

""" type-anotation function that takes a list of ints and floats """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Returns their sum as a float """

    return float(sum(mxd_lst))
