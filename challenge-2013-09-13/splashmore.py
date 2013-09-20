#!/usr/bin/python3

"""
Ask to be taken to Mt. Splashmore until your parents say yes!
"""

from sys import stdin
import re

__author__ = "Christopher R. Maden <crism@maden.org>"
__date__ = "16 September 2013"

def pester( question, answer ):
    """
    Ask the question on STDOUT until the user provides the desired
    answer on STDIN.

    Answer evaluation is case- and punctuation-insensitive.
    """
    while True:
        print( question )
        an_answer = stdin.readline()

        an_answer = re.sub( r'\s+', ' ',
                            re.sub( r'[^\w\s]+', '',
                                    an_answer ).strip() )

        if re.match( an_answer, answer, re.IGNORECASE ):
            break

    print( "Yayyyy!" )
    return None

if __name__ == '__main__':
    pester( "Will you take us to Mt. Splashmore?", "yes" )
    exit
