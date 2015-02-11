'''
Created on Dec 19, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
#import numpy as np

def enumeratePrime(m):
    # enumerate primes up to number m
    # this assumes that m is small enough so that ar fits in memory
    ar = [True]*(m+1)
    ar[0] = False
    ar[1] = False
    list_primes = []
    for i in range(2,len(ar)):
        if ar[i]:
            list_primes.append(i)
            j = 2
            while(True):    
                ind = j*i
                if ind >= m+1:
                    break
                ar[ind] = False
                j += 1
    return list_primes

def main():
    # takes just one sec for a million
    print enumeratePrime(1000000)
    
if __name__ == "__main__":
    main()