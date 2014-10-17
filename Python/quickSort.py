'''
Created on Oct 13, 2014

@author: Ben Athiwaratkun (pa338)

'''
from __future__ import division
import numpy as np


def reArrangeAroundIndex(ar, index):
    val = ar[index]
    indexVal = -1
    for el in ar:
        if el <= val:
            indexVal += 1
    # swap        
    print "indexVal = %d" % indexVal
    print "val = %r" % val
    ar[index] = ar[indexVal]
    ar[indexVal] = val
    # iterator through the front of indexVal
    equal_index = indexVal-1
    greater_index = indexVal+1
    print ar
    for i in range(indexVal):
        print "i", i
        if ar[i] > val:
            print "Swapping (ar[i] = %d > val %d )"% (ar[i], val)
            # find index after indexVal that has element smaller than indexVal
            while ar[greater_index] > val and greater_index < len(ar):
                greater_index += 1
            temp = ar[greater_index]
            ar[greater_index] = ar[i]
            ar[i] = temp
        print "ar", ar
        # not else if because the new value can be equal to val
    print "Finished Standard Quick Sort", ar
    for i in range(indexVal):
        if ar[i] == val:
            while (ar[equal_index] == val) and equal_index >= 0:
                equal_index -= 1
            print "i is ",i
            print "ar[i] is ", ar[i]
            print "equal index = ", equal_index
            if i <= equal_index:
                temp = ar[equal_index]
                ar[equal_index] = ar[i]
                ar[i] = temp
            print "ar", ar
        
    return ar
    
    # do equal after
    
        

def main():
    ar = [9,1,3,8,4,0,1,4,5,-1,1,9,9,0,-5,-2,4]
    print "The New Arraw Around %d is %r" % (1, reArrangeAroundIndex(ar, 1))
    
if __name__ == "__main__":
    main()