'''
6.13: Rotate an array
Created on Oct 26, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
#import numpy as np

def rotateArray(A, rotateLength):
    n = len(A)
    rotateLength = rotateLength % n
    for beginIndex in xrange(rotateLength):
        index = beginIndex
        
        temp = A[index]
        while index < n:
            nextIndex = (index + rotateLength) % n
            _temp = A[nextIndex]
            A[nextIndex] = temp
            temp = _temp
            index += rotateLength


def main():
    A = [0,1,2,3,4,5,6,7,8,9]
    B = list(A)
    rotateArray(A, 3)
    print A
    print [B[i] for i in  range(-3,len(B)-3,1) ]
    
if __name__ == "__main__":
    main()