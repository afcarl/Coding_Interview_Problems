'''
Created on Oct 9, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
import numpy as np

# see quicksort for median finding
def findMedian(A):
    # find the median for array A
    pass





# incorrect! - do this later
'''def findLargest(k, v):
    # this method finds the kth largest element in the list v (index starts at 0)
    # 1. edge case where k is out of bound
    if k >= len(v):
        return v[-1]
    #######################
    kLargest = -float("inf")
    kSecondLargest = kLargest
    
    for i in range(k):
        if v[i] > kLargest:
            kSecondLargest = kLargest
            kLargest = v[i]
        elif v[i] > kSecondLargest:
            kLargest = v[i]
        else:
            pass
            # v[i] less than both 
    print "kLargest %d and kSecondLargest %d" % (kLargest,kSecondLargest)
    for i in range(k,len(v)):
        if v[i] > kLargest:
            pass
        elif v[i] > kSecondLargest:
            kLargest = v[i]
        else:
            kLargest = kSecondLargest
            kSecondLargest = v[i]
    
    print "kLargest %d and kSecondLargest %d" % (kLargest,kSecondLargest)'''
        


def main():
    #findLargest(5, [29,54,532,1,41,3,5,3,3424,45233])
    pass
    
if __name__ == "__main__":
    main()