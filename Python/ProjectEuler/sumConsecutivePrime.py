'''
Created on Sep 20, 2014

@author: Ben Athiwaratkun (pa338)

'''
import numpy as np
import time
from cgi import maxlen

def findPrimes(max):
    primes = np.array([])
    primeDict = {}
    index = 0;
    for i in range(2,max):
        #print i
        i_prime = True;
        for p in primes:
            if (i % p) == 0:
                i_prime = False
                break
        if i_prime:
            primes = np.append(primes, i)
            primeDict[i] = True
    #print primes
    return [primes, primeDict]


def findPrimes2(max):
    primeDict = np.ones((max))
    primeDict[0] = 0
    primeDict[1] = 0
    for i in range(max):
        if not primeDict[i]:
            continue;
        #print i
        for mul in range(2,max):
            if i*mul < max:
                primeDict[i*mul] = 0;
            else:
                break;
    print "Done finding primes"
    primes = np.array([])
    primes_real_dict = {}
    for i in range(max):
        if primeDict[i]:
            primes = np.append(primes, i)
            primes_real_dict[i] = True;
    return [primes, primes_real_dict]

def findPrimes3(max):
    isPrime = np.ones((max))
    isPrime[0] = 0
    isPrime[1] = 0
    primeDict = {}
    primeCumulativeSum = np.array([0])
    for i in range(2,max):
        if isPrime[i]:
            primeDict[i] = True
            primeCumulativeSum = np.append(primeCumulativeSum, (i + primeCumulativeSum[-1]))
            for mul in range(2,max/i):
                isPrime[i*mul] = 0
    return [primeCumulativeSum, primeDict]
            

def isPrime(primesDict, num):
    return (num in primesDict)

def consecutiveSum(sums,start, length):
    if start > 0:
        return sums[start + length - 1] - sums[start - 1]
    else:
        return sums[start + length - 1]

def findLongestConsecutiveSum(sums, primeDict, maxNum):
    # with maxLengthNotOver : blazing fast
    maxLengthNotOver = next(x[0] for x in enumerate(sums) if x[1] > maxNum)
    for length in reversed(range(1, maxLengthNotOver)):
        #print "Length", length
        #print "Length =", length
        for startPosition in range(len(sums)+1-length):
            #print "Start position", startPosition
            cs = consecutiveSum(sums, startPosition, length) 
            #print cs
            if cs > maxNum:
                #print "Break"
                break;
            elif isPrime(primeDict, cs):
                return (startPosition, length)
                # this will always return when it hits length = 1

def main():
    #maxNum = 1000000;
    maxNum = 1000000;
    start = time.time()
    [sums, primesDict] = findPrimes3(maxNum)
    end = time.time()
    ## method 3 is very fast
    print "Done Finding Sums of Primes + Dictionary in ", (end-start)
    
    start = time.time()
    (startPosition, length) = findLongestConsecutiveSum(sums, primesDict, maxNum)
    end = time.time()
    print "Done Finding the Longest Consecutive Prime Sum in ", (end-start)
    
    print "Start Position", startPosition, "Length", length
    #print primes[startPosition:(startPosition + length)]
    print consecutiveSum(sums, startPosition, length)
    
if __name__ == "__main__":
    main()