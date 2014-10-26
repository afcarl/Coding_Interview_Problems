'''
5.10: GCD of two numbers without multiplication or division or modulus operator
Created on Oct 26, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
#import numpy as np

def gcdSlow(a,b):
    print "\tGCD Call"
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > b:
        return gcdSlow(a-b,b)
    else:
        return gcdSlow(b-a,a)

def gcd(a,b):
    print "\tGCD Call"
    if a == 0:
        return b
    elif b == 0:
        return a
    elif (a & 1 == 0) and (b & 1 == 0):
        return ( gcd(a>>1, b>>1) << 1)
    elif (a & 1 == 0):
        return gcd( a>>1, b)
    elif (b & 1 == 0):
        return gcd( b>>1, a)
    elif b > a:
        return gcd(b-a,a)
    else:
        return gcd(a-b,b)
# What is the complexity of this algorithm?
# 



def main():
    print gcd(5,2)
    print gcd(10,25)
    print gcd(15,24)
    print gcd(7,102)
    print gcd(13*2*8*27,27*13*54*53)
    print gcd(119,91)
    
if __name__ == "__main__":
    main()