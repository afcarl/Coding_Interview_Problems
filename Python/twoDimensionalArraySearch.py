'''
Created on Oct 15, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
import numpy as np
from aetypes import end

# returns true or false
def binarySearch(A,key):
    mid = len(A)/2
    if len(A) == 1:
        return A[0] == key
    elif A[mid] == key:
        return True
    elif key < A[mid]:
        return binarySearch(A[:mid],key)
    else:
        # in this case key > A[mid]
        if mid == len(A)-1:
            return False
        else:
            return binarySearch(A[mid+1:], key)

# not exactly correct
def binarySearchFirstLessEqual(A,key, start,end):
    mid = (start+end)/2
    print "mid = %d " % mid
    if end == start:
        return start
    #elif key == A[mid]:
    #    return mid
    elif key < A[mid]:
        if start == mid:
            return start
        else:
            return binarySearchFirstLessEqual(A, key, start, mid-1)
    else:
        # key > A[mid]
        if end == start+1:
            if A[end] <= key:
                return end
            else:
                return start
        else:
            return binarySearchFirstLessEqual(A, key, mid, end)


def binarySearchPreGreater(A,key,start,end):
    # returns 1 index less than the index that is first greater than key
    pass


# incorrect
'''def twoDimSearch(A, key):
    nrows = np.shape(A)[0]
    ncols = np.shape(A)[1]
    theCol = binarySearchFirstLessEqual(A[0,:], key,0,ncols-1)
    theRow = binarySearchFirstLessEqual(A[:,theCol], key, 0, nrows-1)
    print "The Col = %d and the Row = %d" % (theCol, theRow)
    return A[theRow,theCol] == key'''
        
def twoDimSearch(A,key):
    #print "The shape of A is"
    #print  np.shape(A)
    if np.shape(A)[0] == 0:
        return False
    else:
        ncols = np.shape(A)[1]
    theCol = binarySearchFirstLessEqual(A[0,:], key, 0, ncols-1)
    print "The Col is %d" % theCol
    if A[0,theCol] == key:
        return True
    else:
        return twoDimSearch(A[1:,0:theCol+1], key)
    
def twoDimSearchLoop(A,key):
    nrows = np.shape(A)[0]
    ncols = np.shape(A)[1]
    theCol = ncols - 1
    for row in range(nrows):
        theCol = binarySearchFirstLessEqual(A[row,0:theCol+1], key, 0, ncols-1 )
        if A[row,theCol] == key:
            return True
        
    return False

def main():
    A = np.array([[1,2,3,4,5],
                  [6,7,8,9,10],
                  [11,12,13,14,15],
                  [16,17,18,19,20],
                  [21,22,23,24,25]])
    #twoDimSearch(A, 17)
    B = [1,2,5,5,7,8,9,12,19,20,38,50,71,71,71,90]
    print binarySearchFirstLessEqual(B,71,0,len(B)-1)
    #print twoDimSearch(A,17.5)
    #print twoDimSearch(A,18)
    
if __name__ == "__main__":
    main()