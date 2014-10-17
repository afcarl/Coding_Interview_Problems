'''
Created on Oct 13, 2014

@author: Ben Athiwaratkun (pa338)

'''
from __future__ import division
import numpy as np
import sys


def test(num):
    print sys.maxint
    #print int("0b/0F",2)
    numb = bin(num)
    print type(numb)
    for ch in numb:
        print ch
    print numb
    print int(numb, base=2)
    print int("0b1111", base=2)
    print int("0xFF", base=16)
    return 1

def parity(num):
    ar = [bool(int(el)) for el in list(bin(num)[2:])]
    res = reduce(lambda a,b: a^b, ar)
    return res

def main():
    print "Parity of 5 is %d" % parity(5)
    print "Parity of 7 is %d" % parity(7)
    print "Parity of 15 is %d" % parity(15)
    
if __name__ == "__main__":
    main()