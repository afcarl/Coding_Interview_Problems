'''
Created on Oct 15, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
#import numpy as np

# this file demonstrates the use of regular expressions

# regular expression examples

import re

def testRegexp(s):
    # match - must match at the beginning of the string
    # search - starting at any point in the string
    match = re.search(r'.*:(.*)!(\w)', s)
    #print match.group()
    # group() and group(0) are the same
    print match.group(0)
    print match.group(1)
    print match.group(2)

def main():
    str = '\nan example word:cat!2'
    testRegexp(str)

if __name__ == "__main__":
    main()