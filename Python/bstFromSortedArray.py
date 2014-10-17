'''
Created on Oct 14, 2014

@author: Ben Athiwaratkun (pa338)

'''


def buildSortedArrayToBst(A,bst):
    # A is the sorted array
    if (len(A)) == 0:
        return
    
    mid = len(A)/2
    addElementToBst(bst, A[mid])
    
    buildSortedArrayToBst(A[0:mid], bst)
    if mid+1 < len(A):
        buildSortedArrayToBst(A[mid+1:], bst)

def addElementToBst(bst, el, node=0):
    print "Node %r El %r" % (node, el)
    if bst[node] == None:
        print "Setting Element"
        bst[node] = el
    elif el <= bst[node]:
        print "Left"
        addElementToBst(bst, el, node=left(node))
    else:
        print "Right"
        addElementToBst(bst, el, node=right(node))


def left(node):
    return 2*node+1

def right(node):
    return 2*node+2


def main():
    bst = [None]*20
    '''addElementToBst(bst,5)
    print bst
    addElementToBst(bst,1)
    print bst
    addElementToBst(bst,10)
    print bst
    addElementToBst(bst,11)
    print bst'''
    A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    buildSortedArrayToBst(A, bst)
    print bst
    
if __name__ == "__main__":
    main()