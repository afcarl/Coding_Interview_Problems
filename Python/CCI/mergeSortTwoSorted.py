'''
Created on Dec 18, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
import numpy as np

def mergeSort(A,lenA,B):
    print 'lenA = ', lenA
    newA = A
    newA[lenA:] = B
    print newA
    pA = 0
    pB = lenA
    while (pB < len(A)):
        if pA == pB:
            pA = 0
            pB += 1
        elif newA[pA] > newA[pB]:
            temp = newA[pB]
            newA[pB] = newA[pA]
            newA[pA] = temp
            pA += 1
        else:
            pA += 1
        
    print newA



def main():
    A = [1,2,4,5,8,10,14,53,0,0,0,0,0,0]
    B = [3,5,7,9,10,1000]
    mergeSort(A, len(A)- len(B), B)
    
if __name__ == "__main__":
    main()