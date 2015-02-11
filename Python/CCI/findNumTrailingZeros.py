'''
Created on Dec 18, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
#import numpy as np
import math

def findNumTrailingZerosFactorial(n):
    numZeros = 0
    i = 1
    while(True):
        m = n/5**i
        m = int(math.floor(m))
        numZeros += m
        #print m
        i += 1
        if m < 1:
            break
    return numZeros


def main():
    print findNumTrailingZerosFactorial(25)
    
if __name__ == "__main__":
    main()