'''
Created on Oct 14, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
#import numpy as np

def wordBreaking(s, dictionary):
    X = [False]*(len(s)+1)
    X[-1] = True
    for m in range(0,len(s)):
        # calculate X[m]
        for k in range(-1,m):
            #print "Break point is at k=", k
            #print "The word is ", s[k+1:m+1]
            if (not X[k] == False)  and (s[k+1:m+1] in dictionary):
                # record X[m] = k in order to backtrack
                X[m] = k
                #print "Setting X[m] to be true m =" , m
                break
        
    print X
    if not X[-2] == False: 
        #print "X[-2] =", X[-2]
        index = len(s)-1
        A = []
        while True:
            #print "index =", index
            A.append(index)
            index = X[index]
            if index ==  -1:
                break
            
        print A
        listWords = []
        for i in range(len(A)):
            if i == (len(A)-1):
                listWords.append(s[0:(A[i]+1)])
            else:
                listWords.append(s[A[i+1]+1: A[i]+1])
        return listWords
    else:
        return s + ": Not Breakable with Words in the dictionary"


def main():
    dictionary = {"bed":1, "bath":1, "and":1, "beyond":1,"ben":1}
    
    print wordBreaking("bedbathandbeyon", dictionary)
    print wordBreaking("bedbathandbeyond", dictionary)
    
if __name__ == "__main__":
    main()