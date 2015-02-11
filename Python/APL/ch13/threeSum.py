'''
13.14: determine if 3 numbers in the array A can add up to 3
Created on Oct 26, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
#import numpy as np
import bisect

# This solution is n^{k-1}*log(n) 
def kSum(A,k,t):
    if k == 1:
        return isIn(A,t)
    else:
        for el in A:
            if kSum(A,k-1, t-el):
                return True
        return False

def isIn(A,x):
    index = bisect.bisect_left(A, x)
    return index < len(A) and A[index] == x

def main():
    A = [1,5,6,-5,3,9,523,-45,18]
    A = sorted(A)
    print A
    #print isIn(A,55)
    #print isIn(A,-5)
    #kSum(A,3)
    print kSum(A,3,496) # True
    print kSum(A,3,495) # False
    
if __name__ == "__main__":
    main()