'''
Created on Jan 24, 2015

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
#import numpy as np


# perform permutation with only additional constant storage
def permute(A,perm):
    for initial in range(len(A)):
        if perm[initial] < 0:
            # skip this cycle
            continue
            
        temp = A[initial]
        current = initial
        while True:
            next = perm[current]
            #print next
            perm[current] -= len(A)
            temp2 = A[next]
            A[next] = temp
            if next == initial:
                break
            temp = temp2
            current = next
        print A


def main():
    permute([10,11,12,13,14] , [1,2,0,4,3])
    # should be [12, 10, 10, 14, 13]
    
if __name__ == "__main__":
    main()