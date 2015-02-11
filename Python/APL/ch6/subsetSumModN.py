'''
Created on Jan 24, 2015

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
#import numpy as np

# find a subset that sums to 0 mod N where N is the set size
def findSubsetSum(B):
    A = B
    for i in range(1,len(B)):
        B[i] += B[i-1]
    print 'trailing sum'
    print B
    
    n = len(A)
    dictMod = {}
    for i in range(n):
        el = A[i]
        modNum = el % n
        if modNum == 0:
            return (0,i)
        else:
            if modNum in dictMod:
                return (dictMod[modNum]+1,i)
            else:
                dictMod[modNum] = i
    


def main():
    B = [428,334,62,711,704,763,98,733,721,995]
    print findSubsetSum(B)
    print sum([62,711,704,763]) % len(B)
    
    
if __name__ == "__main__":
    main()