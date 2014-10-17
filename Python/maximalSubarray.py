'''
Created on Oct 14, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
import numpy as np

def maximumSubarray(A):
    # the B[m] records the maximum subarray value ending exactly at m
    B = [None]*len(A)
    B[0] = max(0,A[0])
    # The array X[m] records the starting point for B[m]
    X = [None]*len(A)
    X[0] = 0 if A[0] >= 0 else None
    
    for i in range(1,len(A)):
        if B[i-1] <= 0:
            B[i] = A[i]
            X[i] = i
        else:
            B[i] = B[i-1] + A[i]
            X[i] = X[i-1]
    
    maxB_index = np.argmax(B)
    #print "maxBIndex is", maxB_index
    #print "beginning index is", X[maxB_index]
    return (A[X[maxB_index]:maxB_index+1] , B[maxB_index])

def maximumSubarrayO1(A):
    # this is the same algorithm with O(1) additional space instead of O(n)
    currentB = 0
    currentX = None
    if A[0] >= 0:
        currentB = A[0]
        currentX = 0
    else:
        currentB = 0
        currentX = None 
        
    maxB = currentB
    maxX = currentX
    maxB_index = currentX
    for i in range(1,len(A)):
        if currentB <= 0:
            currentB = A[i]
            currentX = i
        else:
            currentB = currentB + A[i]
            # currentX unchanged
        ## recording the maxB
        if currentB > maxB:
            maxB = currentB
            maxX = currentX
            maxB_index = i
    return (A[maxX:maxB_index+1], maxB)
    
    
    # This is one of my prodest algorithm hehe (should be correct)
def circularMaximumSubarray(ar):
    # concatenate two arrays
    A = ar + ar 
    # note [A,A] would give a matrix of two rows, each row being A
    # the B[m] records the maximum subarray value ending exactly at m
    B = [None]*len(A)
    B[0] = max(0,A[0])
    # The array X[m] records the starting point for B[m]
    X = [None]*len(A)
    X[0] = 0 if A[0] >= 0 else None
    
    for i in range(1,len(A)):
        if B[i-1] <= 0:
            B[i] = A[i]
            X[i] = i
        else:
            # if (i-1) - X[i-1] = n-1 : this is full 
            # we want (i-1) - X[i-1] < n-1
            if i-X[i-1] < len(ar):
                B[i] = B[i-1] + A[i]
                X[i] = X[i-1]
            else:
                B[i] = B[i-1] + A[i] - A[X[i-1]]
                X[i] = X[i-1] + 1
     
    maxB_index = np.argmax(B)
    print "maxBIndex is", maxB_index
    print "beginning index is", X[maxB_index]
    return (A[X[maxB_index]:maxB_index+1] , B[maxB_index])
    # I think this looks right

def main():
    ar = [1, -2,5,3,-7,-9,2,-4,6,-1,-2,10]
    print "Array is ", ar
    print "Maximum Subarray for ar is ", maximumSubarray(ar)
    print "(O(1) algorithm) Maximum Subarray for ar is ", maximumSubarrayO1(ar)
    print "\n\n\n ------------- "
    ar = [-5,3,6,1,2,-3,1]
    print (ar+ar)
    print "Circular Maximum Subarray ", circularMaximumSubarray(ar)
   
    
    
if __name__ == "__main__":
    main()