'''
Created on Oct 15, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
#import numpy as np



'''## This code swap bits i and j of integer x
def swapBits(x,i,j):
    # assume i,j are in the range (0 to 63) inclusive
    #print  "x = %d, i=%d, j=%d" %(x,i,j)
    val_i = 1  & (x >> i)
    #print "val_i = %d" % val_i
    val_j = 1 & (x >> j)
    #print "val_j = %d" % val_j
    if val_i == val_j:
        pass
    elif val_i ==1:
        # and val_j =0
        x -= (1 << i)
        x += (1 << j)
    else:
        # val_j == 1 and val_i == 0
        x -= (1 << j)
        x += (1 << i)
    #print "Returning %d" % x
    return x'''

def swapBits(x,i,j):
    # assume i,j are in the range (0 to 63) inclusive
    val_i = 1  & (x >> i)
    val_j = 1 & (x >> j)
    if val_i == val_j:
        pass
    elif val_i ==1:
        # and val_j =0
        x -= 1 << i
        x += 1 << j
    else:
        # val_j == 1 and val_i == 0
        x -= 1 << j
        x += 1 << i

    return x
    
def bitReversal(x):
    for i in range(0,31):
        j = 63 - i
        x = swapBits(x,i,j)
    return x

def main():
    print "should be 6 : %d" % swapBits(5,1,0)
    print "Swap 5 %d" % bitReversal(9L)

if __name__ == '__main__':
    main()