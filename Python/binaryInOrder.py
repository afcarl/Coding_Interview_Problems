'''
Created on Oct 13, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
import numpy as np

def inOrder(tree,node):
    if hasLeft(tree,node):
        inOrder(tree,left(node))
    print tree[node]
    if hasRight(tree,node):
        inOrder(tree,right(node))

# find a successor of a node with value key
def findSuccessorInOrder(tree,node, key, acc):
    newAcc = acc
    if hasLeft(tree,node):
        newAcc = findSuccessorInOrder(tree, left(node), key, acc)
    print "current acc %r" % acc 
    print "going through node %r" % tree[node]
    newAcc = newAcc + str(tree[node])
    #if len(newAcc) >= 2 and  newAcc[-2] == key:
    #    return newAcc
    
    if hasRight(tree,node):
        newAcc = findSuccessorInOrder(tree, right(node), key, newAcc)
    return newAcc
    

def findSuccessorOfIndex(tree,index):
    if hasRight(tree, index):
        print "hasRight"
        startIndex = right(index)
        while True:
            print "index %d" % startIndex
            if hasLeft(tree,startIndex):
                startIndex = left(startIndex)
            #elif hasRight(tree, startIndex):
            #    startIndex = right(startIndex)
            else:
                break;
        return startIndex
            
    else:
        # go up to successor
        startIndex = index
        while True:
            if startIndex == left(parent(startIndex)) :
                startIndex = parent(startIndex)
                break
            else:
                startIndex = parent(startIndex)
        return startIndex
                
        
def parent(node):
    return (node-1)/2

def hasParent(node):
    return node >= 0

def hasLeft(tree, node):
    l_index = left(node)
    return (l_index < len(tree)) and (tree[l_index] != None)
    
def hasRight(tree, node):
    r_index = right(node)
    return (r_index < len(tree)) and (tree[r_index] != None)

def left(node):
    return 2*node+1

def right(node):
    return 2*node+2

def main():
    tree = [1,2,3,4,None,None,None, 5,6,None,None,None,None,None,None]
    #inOrder(tree,0)
    # expect this to return 2
    #print "Successor of 6 is %r " % findSuccessorInOrder(tree, 0, 6, "")
    tree2 = ["A","B","I","C","F","J","O","D","E","M","G",None,"K",None,"P"]
    #print "Successor of G is %r " % findSuccessorInOrder(tree2, 0, "E", "")
    #print "Successor of E is %r " % findSuccessorInOrder(tree2, 0, "E", "")
    print "Successor of Index %d with Value %r is %r " % (1, 
                                                          tree2[1], 
                                                          tree2[findSuccessorOfIndex(tree2, 1)])
    ind = 10
    print "Successor of Index %d with Value %r is %r " % (ind, 
                                                          tree2[ind], 
                                                          tree2[findSuccessorOfIndex(tree2, ind)])
    ind = 0
    print "Successor of Index %d with Value %r is %r " % (ind, 
                                                          tree2[ind], 
                                                          tree2[findSuccessorOfIndex(tree2, ind)])
    ind = 12
    print "Successor of Index %d with Value %r is %r " % (ind, 
                                                          tree2[ind], 
                                                          tree2[findSuccessorOfIndex(tree2, ind)])
    
if __name__ == "__main__":
    main()