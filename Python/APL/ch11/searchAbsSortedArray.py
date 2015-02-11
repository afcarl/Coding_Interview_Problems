'''
Created on Oct 26, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
#import numpy as np

def searchAbsSorted(A, num):
    for el in A:
        k = num - el
        # search for element == k

## TODO - implement this method
def searchPairSorted(A, num):
    pass

def main():
    A = [1,2,-3,4,-5,8,-9]
    searchAbsSorted(A, -4)
    
if __name__ == "__main__":
    main()