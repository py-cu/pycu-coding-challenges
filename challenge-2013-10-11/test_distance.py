#!/usr/bin/env python

"""
Unit tests for the distance module.

Currently an unimplemented template.
"""

import unittest
import distance

__author__ = "Christopher R. Maden <crism@maden.org>"
__date__ = "11 October 2013"

class SameStringTestCase( unittest.TestCase ):
    def testStrDist( self ):
        the_string = "abc"
        self.assertEqual( distance.str_dist( the_string,
                                             the_string ),
                          0 )

    def testStrDistUneven( self ):
        the_string = "abc"
        self.assertEqual( distance.str_dist_uneven( the_string,
                                                    the_string ),
                          0 )

if __name__ == '__main__':
    unittest.main()
