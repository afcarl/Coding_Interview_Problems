'''
Created on Oct 17, 2014

@author: Ben Athiwaratkun (pa338)
5.7 base conversion
'''
#from __future__ import division
#import numpy as np


def base_conversion(b1, s, b2):
    # s is a string representing a number in the integer base b1
    # b1, b2 : integer
    # OUTPUT: a string in integer base b2
    s_list = list(s)
    '''for i in range(len(s_list)):
        if s_list[i] == 'A':
            s_list[i] = 10
        elif s_list[i] == 'B':
            s_list[i] = 11
        elif s_list[i] == 'C':
            s_list[i] = 12
        elif s_list[i] == 'D':
            s_list[i] = 13
        elif s_list[i] == 'E':
            s_list[i] = 14
        elif s_list[i] == 'F':
            s_list[i] = 15
        else:
            s_list[i] = int(s_list[i])'''
    for i in range(len(s_list)):
        if ord(s_list[i]) >= ord('A') and ord(s_list[i]) <= ord('F'):
            s_list[i] = ord(s_list[i]) - ord('A') + 10
        else:
            s_list[i] = int(s_list[i])
    #######################
    theNum = 0
    # assuming that the last one is the least significant number
    n = len(s_list)
    for i in range(len(s_list)):
        exponent = n-1-i
        multiplier = b1**(exponent)
        theNum += multiplier*s_list[i]
        print "the number is %d", theNum
    
    # 2. convert it to base b2
    s_b2_list = [0]*len(s_list)
    mult = b2
    for i in range(len(s_list)):
        index = n-1-i
        s_b2_list[index] = theNum % mult
        theNum -= s_b2_list[index]*(mult/b2)
        theNum /= b2
        print s_b2_list[index]
        print "The current number is %d" % theNum
    print s_b2_list
    
    # convert s_b2_list to a string
    for i in range(len(s_b2_list)):
        if s_b2_list[i] >= 10:
            s_b2_list[i] = chr( ord('A') + s_b2_list[i] - 10  )
        else:
            s_b2_list[i] = str(s_b2_list[i])
    return ''.join(s_b2_list)
        
def main():
    print base_conversion(2, "1011", 12)
    
if __name__ == "__main__":
    main()