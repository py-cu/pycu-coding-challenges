#!/usr/bin/env python

"""
A module for calculating string distances.

Currently an unimplemented template.

>>> import distance
>>> from distance import str_dist
"""

import doctest

__author__ = "Christopher R. Maden <crism@maden.org>"
__date__ = "11 October 2013"

def str_dist( str1, str2 ):
    """
    Given two strings of the same length, return the minimum number of
    single-character changes to turn one into the other.

    >>> str_dist( "abc", "abc" )
    0
    >>> str_dist( "abcd", "abed" )
    1
    >>> str_dist( "abcd", "abdc" )
    2
    """
    pass

def str_dist_uneven( str1, str2 ):
    """
    Given two strings which may or may not be of the same length,
    return the minimum number of single-character changes or shifts to
    turn one into the other.

    If str1 is longer than str2, the number is positive; if str2 is
    longer, the number is negative.

    >>> str_dist_uneven( "abc", "abc" )
    0
    >>> str_dist_uneven( "abcd", "abc" )
    1
    >>> str_dist_uneven( "abcd", "bcd" )
    2
    >>> str_dist_uneven( "bcd", "abcd" )
    -2
    """
    pass

if __name__ == '__main__':
    doctest.testmod()
