'''
Created on Oct 15, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
#import numpy as np
import itertools

# we can do it by adding a number to the array
def listPermutations(s):
    n = len(s)
    perms = itertools.permutations(range(n))
    dict_perm = {}
    for el in perms:
        newS = ""
        #for i in range(len(el)):
        for ch in el:
            print ch
            newS = newS + str(s[ch])
        print "newS %r " % newS
        if newS not in dict_perm:
            dict_perm[newS] = 1
    return dict_perm.keys()
    


def hashAlgorithm(n, A, res):
    if n == 1:
        # make a deep copy and append to result list
        res.append(list(A))
    else:
        for i in range(n):
            hashAlgorithm(n-1, A, res)
            if ((n-1) % 2) == 1:
                # if n is odd
                j=0
            else:
                j=i
            swap(A,j,n-1)

def swap(A,j,n):
    temp = A[j]
    A[j] = A[n]
    A[n] = temp


def permutationGeek(n, A,res,i):
    if i == n-1:
        res.append(list(A))
    else:
        for j in range(i,n):
            swap(A,i,j)
            permutationGeek(n, A, res, i+1)
            swap(A,i,j)

def main():
    
    result_list = []
    A = [0,1,2]
    hashAlgorithm(len(A),A,result_list)
    print "The result list is %r" % result_list
    print "using itertools"
    perm = itertools.permutations([0,1,2])
    for el in perm:
        print el
    print "\n\n"
    print "All permutations of 'bedbath' is %r" % listPermutations("bedbath")
    result_list2 = []
    permutationGeek(len(A), A, result_list2 , 0) 
    print "Perm Geek %r" % result_list2
    
if __name__ == "__main__":
    main()