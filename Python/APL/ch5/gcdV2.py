'''
Created on Jan 25, 2015

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
#import numpy as np

def findGcdSlow(a,b):
    # assume a > b
    # keep subtracting b from a until it's smaller than b
    # if it's zero then we're done : b is the gcd
    # if it's not zero, then the bigger number is the new a. the smaller number is the new b. Repeat
    if a < b:
        temp = a
        a = b
        b = temp
    while True:
        while a >= b:
            a -= b
        if a == 0:
            return b
        else:
            temp = a
            a = b
            b = temp

def div(a,b):
    pass

def findGcdFast(a,b):
    # assume a > b
    # keep subtracting b from a until it's smaller than b
    # if it's zero then we're done : b is the gcd
    # if it's not zero, then the bigger number is the new a. the smaller number is the new b. Repeat
    if a < b:
        temp = a
        a = b
        b = temp
    while True:
        # divide a by b.
        # returns the result and the remainder
        (_,a) = div(a,b)
        if a == 0:
            return b
        else:
            temp = a
            a = b
            b = temp


def main():
    print findGcdSlow(30,24)
    
if __name__ == "__main__":
    main()