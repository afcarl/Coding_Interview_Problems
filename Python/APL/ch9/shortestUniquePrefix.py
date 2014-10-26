'''
Finding the shortest prefix of s which is not a prefix of any string in D
tested - works
Created on Oct 26, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
#import numpy as np


def buildTrie(dictionary):
    # 1. construct a trie based on the dictionary
    chPosition = 0
    trie = {}
    
    for el in dictionary:
        curDict = trie
        for chPosition in range(len(el)):
            key = el[chPosition]
            if not key in curDict:
                curDict[key] = {}
                curDict = curDict[key]
            else:
                curDict = curDict[key]
    # 2. find the shortest unique prefix
    return trie

def findShortestUniquePrefix(word, trie):
    prefixArray = []
    currentTrie = trie
    exist = False
    for chPosition in range(len(word)):
        if not word[chPosition] in currentTrie:
            prefixArray.append(word[chPosition])
            #print "set exist to true"
            #print currentTrie
            exist = True
            break
        else:
            prefixArray.append(word[chPosition])
            currentTrie = currentTrie[word[chPosition]]
    if exist:
        return prefixArray
    else:
        return []

def sup(word, dictionary):
    trie = buildTrie(dictionary)
    return findShortestUniquePrefix(word, trie)

def main():
    trie1 = buildTrie( {"dog","be", "cut", "car", "cat"})
    print trie1
    print sup("cat", {"dog","be", "cut"})
    print sup("cat", {"dog","be", "cut", "car"})
    print sup("cat", {"dog","be", "cut", "car", "cat"})
    
if __name__ == "__main__":
    main()