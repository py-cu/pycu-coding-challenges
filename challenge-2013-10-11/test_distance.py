#!/usr/bin/env python

"""
Unit tests for the distance module.

Currently an unimplemented template.
"""

import unittest
import distance

__author__ = "Christopher R. Maden <crism@maden.org>"
__date__ = "12 October 2013"

class SameStringTestCase( unittest.TestCase ):
    """
    The distance between identical strings should always be 0.
    """
    def setUp( self ):
        """
        Define variables shared by the tests in this case.
        """
        self.string = "abc"

    def test_str_dist_same_string( self ):
        """
        Check that str_dist() correctly finds the distance between
        identical strings.
        """
        self.assertEqual( distance.str_dist( self.string,
                                             self.string ),
                          0 )

    def test_str_dist_uneven_same_string( self ):
        """
        Check that str_dist_uneven() correctly finds the distance
        between identical strings.
        """
        self.assertEqual( distance.str_dist_uneven( self.string,
                                                    self.string ),
                          0 )

if __name__ == '__main__':
    unittest.main()
