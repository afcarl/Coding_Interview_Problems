'''
Created on Oct 15, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
#import numpy as np
from itertools import islice
import itertools

#################################################################################
################### Produce an n-gram Sliding Windown ###########################
def slidingWindowNgram(A,n):
    pass
    # learn about generators
    # Example - this will create a 3 gram 
    zip(A,A[1:],A[2:])
    # This is probably not as efficient as using the generators
    gens= (islice(A,i,None) for i in range(n))
    # The * unpacks gen
    return zip(*gens)


#################################################################################
###################### Flattening a Multi-Dim List ##############################
def flattenList(a):
    return list(itertools.chain.from_iterable(a))
    # this is the preferred method 
    # this method is probably more efficient

def flattenListLambda(A):
    return reduce(lambda x,y: x+y, A)
    # I think this explains the command
    # sum(A,[]) # [] is the starting value of the sum
    # needs [] because otherwise the default would be 0 : adding 0 with element 
    # of A (which is a list) would throw an error 


#################################################################################
def main():
    A = [[1,2],[3,4]]
    print flattenList(A)
    print flattenListLambda(A)
    AA = [1,2,3,4,5,6]
    print slidingWindowNgram(AA, 3)
    
    
if __name__ == "__main__":
    main()