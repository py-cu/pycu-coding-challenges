#!/usr/bin/env python

import unittest
import kata1


class EvensList(unittest.TestCase):
    # set up
    def setUp(self):
        # given a list of integers from 0 through 10, get the evens
        self.test_list = range(11)

    def test_evens_list1(self):
        self.assertEquals(kata1.evens_list1(self.test_list),
                          [0,2,4,6,8,10])

    def test_evens_list2(self):
        self.assertEquals(kata1.evens_list2(self.test_list),
                          [0,2,4,6,8,10])

    def test_evens_list3(self):
        self.assertEquals(kata1.evens_list3(self.test_list),
                          [0,2,4,6,8,10])
        

def main():
    unittest.main()

if __name__ == '__main__':
    main()

