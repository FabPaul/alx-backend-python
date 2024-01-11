#!/usr/bin/env python3

""" Type-anotation that takes a string or float as arg """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple, of which the 1st elem is a str,
    and the 2nd int/float """

    return k, float(v * v)
