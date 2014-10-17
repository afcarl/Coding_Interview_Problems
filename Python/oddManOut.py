'''
Created on Oct 9, 2014

@author: Ben Athiwaratkun (pa338)

'''
from __future__ import division
import numpy as np
from __builtin__ import True

# given an unsorted array of integers where every
# integer appears only once, write an algorithm 
# that finds the integer that appears only once
def oddManOut(seq):
    # O(n) performance
    _d = {}
    for el in seq:
        if el in _d:
            del _d[el]
        else:
            _d[el] = True
    return _d.keys()[0]
        
# do this without a hashtable    
def oddManOut2(seq):
    _b = binarySearchTree(len(seq))
    _b2 = binarySearchTree(len(seq))
    
    for el in seq:
        #_b.printTree()
        if _b.contains(el):
            _b2.add(el)
        else:
            _b.add(el)
    _b.printTree()
    _b2.printTree()
    
    
    for el in seq:
        b_contained = _b.contains(el)
        b2_contained = _b2.contains(el)
        if b_contained and not b2_contained:
            return el
        elif not b_contained and b2_contained:
            return el
    


class binarySearchTree:
    def __init__(self, maxSize):
        self.tree = [None]*(maxSize**2)
    
    def printTree(self):
        print self.tree
        
    def getRoot(self):
        return self.tree[0]

    def add(self, x, startNode=0):
        #print "Adding ", x
        #print startNode
        if self.tree[startNode] == None:
            self.tree[startNode] = x
            return
        elif x > self.tree[startNode]:
            self.add(x, self.getRight(startNode))
        else:
            self.add(x, self.getLeft(startNode))
                
    def getRight(self,node):
        return 2*node + 2
    
    def getLeft(self,node):
        return 2*node + 1
    
    def remove(self,x, startNode=0):
        print "Removing", x
        # assume that we know x is in the tree
        if self.tree[startNode] == x:
            # do we switch with right or left
            print "startNode", startNode
            if self.tree[self.getRight(startNode)] == None:
                self.tree[startNode] = self.getLargest(self.getLeft(startNode))
                print "updated to",self.tree[startNode]
            else:
                self.tree[startNode] = self.getSmallest(self.getLeft(startNode))
            #self.percolateDown(startNode)
            
            #self.tree[startNode] = val
            #self.percolateTo(startNode)
            # this will return
        elif x > self.tree[startNode]:
            self.remove(x, self.getRight(startNode))
        else:
            self.remove(x, self.getLeft(startNode))
    
    '''def percolateLargest(self, node):
        if self.tree[self.getLeft(node)] == None and self.tree[self.getRight(node)] == None:
            return self.tree[node]
        elif self.tree[self.getRight(node)] == None:
            self.swap(node, self.getLeft(node))
            return self.percolateLargest(self.getLeft(node))
        else:
            self.swap(node, self.getRight(node))
            return self.percolateLargest(self.getRight(node))'''
    
    #def percolateDown(self, node):
    #    if self.tree[node] < self.tree[self.getLeft(node)]:
            
    
    def getSmallest(self, node):
        # know that node is not None
        if self.tree[self.getLeft(node)] == None and self.tree[self.getRight(node)] == None:
            val = self.tree[node]
            self.tree[node] = None
            return val
        elif self.tree[self.getLeft(node)] == None:
            return self.getSmallest(self.getRight(node))
        else:
            return self.getSmallest(self.getLeft(node))  
    
    def getLargest(self, node):
        if self.tree[self.getLeft(node)] == None and self.tree[self.getRight(node)] == None:
            val = self.tree[node]
            self.tree[node] = None
            print "Largest returning", val
            return val
        elif self.tree[self.getRight(node)] == None:
            val = self.tree[node]
            # percolate
            return self.tree[node]
        else:
            return self.getLargest(self.getRight(node))  
       
    def swap(self,node1, node2):
        temp = self.tree[node1]
        self.tree[node1] = self.tree[node2]
        self.tree[node2] = temp
    
    '''def percolateSmallest(self, node):
        if self.tree[self.getLeft(node)] == None and self.tree[self.getRight(node)] == None:
            return self.tree[node]
        elif self.tree[self.getLeft(node)] == None:
            self.swap(node, self.getRight(node))
            return self.percolateSmallest(self.getRight(node))
        else:
            self.swap(node, self.getLeft(node))
            return self.percolateLargest(self.getLeft(node))'''
    
    def percolateTo(self, node):
        if self.tree[self.getLeft(node)] == None and self.tree[self.getRight(node)] == None:
            self.tree[node] = None
        elif self.tree[self.getLeft(node)] == None:
            self.tree[node] = self.tree[self.getRight(node)]
            self.percolateTo(self.getRight(node))
        #elif self.Tree[self.getRight(node)] == None:
        else:
            self.tree[node] = self.tree[self.getLeft(node)]
            self.percolateTo(self.getLeft(node))
        
            
    
    def contains(self,x,startNode=0):
        if self.tree[startNode] == x:
            return True
        elif self.tree[startNode] == None:
            return False
        elif x > self.tree[startNode]:
            return self.contains(x, self.getRight(startNode))
        else:
            return self.contains(x, self.getLeft(startNode))


def main():
    print oddManOut2([44,4,2,21,44,21,2,5,6,789,4,5,789])
    
if __name__ == "__main__":
    main()
