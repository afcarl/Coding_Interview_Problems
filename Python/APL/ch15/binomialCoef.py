'''
Created on Jan 24, 2015

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
import numpy as np

def binomialCoef(n,k):
    # index: (n,k)
    ''' don't really need this 2-d array'''
    ''' Would it be more efficient?: yes '''
    # build a 2-d array
    ar = np.zeros((n+1,n+1))
    ar[:,0] = 1
    for i in range(n+1):
        ar[i,i] = 1
    return int(aux2(ar,n,k))
    
    
def aux2(ar,n,k):
    # DP
    # only add if it has not been calculated before
    if ar[n,k] == 0:
        ar[n,k] = aux2(ar,n-1,k-1) + aux2(ar,n-1,k)
    return ar[n,k]

def aux(n,k):
    # simple recursion
    if k == 0 or k == n:
        return 1
    else:
        return aux(n-1,k-1) + aux(n-1,k)

def main():
    print binomialCoef(50,23)  # this is quicker (doesn't calculate for the same node twice)
    print aux(50,23)           # very slow
    
if __name__ == "__main__":
    main()