#!/usr/bin/env python

"""
Given a list of integers from 0 through 10 (in order), return
just the evens, also in a list.

Do this in three different ways -- fill in each function below.

Run the tests with
$ python challenge0_test.py
"""

def evens_list1(the_list):
    """ Method 1: slicing """
    #return the_list[::2]

def evens_list2(the_list):
    """ Method 2: list comprehension """
    #return [i for i in the_list if i % 2 == 0]

def evens_list3(the_list):
    """ Method 2: filter + lambda """
    #return filter(lambda x: x % 2 == 0, the_list)
