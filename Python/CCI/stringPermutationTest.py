'''
Created on Dec 15, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
#import numpy as np

''' This function is based on hash table'''
def isPermutation(sa, sb):
    if not len(sa) == len(sb):
        return False
    else:
        _da = {}
        _db = {}
        for ch in sa:
            if ch in _da:
                _da[ch] += 1
            else:
                _da[ch] = 1
        for ch in sb:
            if ch in _db:
                _db[ch] += 1
            else:
                _db[ch] = 1
        ## check for same keys
        if len(_da.keys()) != len(_db.keys()):
            return False
        else:
            for key in _da:
                if not key in _db:
                    return False
                else:
                    if _da[key] != _db[key]:
                        return False
            ## check for same values
        print _da
        print _db
        return True

''' this function is based on sorting
    Performance: O(n log n)
'''
def isPermutationSort(sa, sb):
    if len(sa) != len(sb):
        return False
    else:
        # note : sort works for array of numbers I think
        # sorted works for more general case
        sa_sorted = sorted(list(sa))
        sb_sorted = sorted(list(sb))
        for i in range(len(sa)):
            if sa_sorted[i] != sb_sorted[i]:
                return False
        return True
    

def main():
    sa = 'dadbcd'
    sb = 'bcdade'
    print isPermutation(sa,sb)
    print isPermutationSort(sa, sb)
    
    
if __name__ == "__main__":
    main()