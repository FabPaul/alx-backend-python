#!/usr/bin/env python3

""" type-anotation function that takes a list of floats as arg"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Returns the sum of the floatinf point values """

    return float(sum(input_list))
