'''
Created on Dec 18, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
#import numpy as np


#find the number of ways to run upstairs with recursion
#quite slow
def findNumWays(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return findNumWays(n-3) + findNumWays(n-2) + findNumWays(n-1)

def findNumWaysDp(n):
    # so that the last index is n
    ar = [0]*(n+1)
    ar[0] = 1
    for i in range(n+1):
        if i-1 >= 0:
            ar[i] += ar[i-1]
        if i-2 >= 0:
            ar[i] += ar[i-2]
        if i-3 >= 0:
            ar[i] += ar[i-3]
    #print ar
    # correct!
    return ar[-1]

def main():
    print findNumWays(10)
    print findNumWaysDp(10)
    
if __name__ == "__main__":
    main()