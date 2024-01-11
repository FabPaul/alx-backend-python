#!/usr/bin/env python3

""" type-anotation that takes a float as arg """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float by multiplier """

    def multiplier_function(value: float) -> float:
        """ Returns the original function """

        return multiplier * value

    return multiplier_function