'''
Created on Dec 19, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
#import numpy as np

# returns the index of the element
def binarySearch(A, el):
    return aux(A,el,0,len(A)-1)

# start and end indicies are inclusive
def aux(A, el, start, end):
    if start == end:
        if A[start] == el:
            return start
        else:
            return -1
    else:
        mid = (start+end)/2
        if A[mid] == el:
            return mid
        elif A[mid] < el:
            return aux(A,el,mid+1,end)
        else:
            # in this case, A[mid] > el
            # mid might be the same as start due to roundoff
            if mid == start:
                return -1
            else:
                return aux(A,el,start,mid-1)

def main():
    A = [1,4,6,7,8,9,12,52,342,532]
    B = [1]
    print binarySearch(A, 52)
    
if __name__ == "__main__":
    main()