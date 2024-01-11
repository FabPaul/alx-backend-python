#!/usr/bin/env python3

""" Anotate the function with required params
def element_length(lst):
    return [(i, len(i)) for i in lst]
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns values with appropriate types """
    return [(i, len(i)) for i in lst]
