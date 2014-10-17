'''
Created on Oct 15, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
#import numpy as np


def countWaysToClimb(n):
    # can either climb 1 or 2 steps at a time
    # What is the total number of ways to climb an n-step stairs
    
    X = [0]*(2*n)
    # use DP
    X[0] = 1
    X[1] = 1
    for i in range(2,n+1):
        X[i] = X[i-1]  + X[i-2]
    return X[n]
        
def main():
    print countWaysToClimb(4)
    
if __name__ == "__main__":
    main()