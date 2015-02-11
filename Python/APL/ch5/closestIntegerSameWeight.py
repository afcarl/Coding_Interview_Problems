'''
Created on Jan 25, 2015

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
#import numpy as np

# find the closest integer with the same weight
# yes
def closestSameWeight(a):
    #previousBit = 0
    #nextBit = 1
    position = 0
    while True:
        if ( (a >> position) & 1 ) !=  ( (a >> (position + 1) ) & 1 ):
            return (a ^ (3 << position))
        else:
            position += 1

def main():
    a = int('0b1011000',2)
    print bin(closestSameWeight(a))
    
if __name__ == "__main__":
    main()