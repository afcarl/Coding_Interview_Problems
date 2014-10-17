'''
Created on Oct 13, 2014

@author: Ben Athiwaratkun (pa338)

'''
import numpy as np



class Node:
    value = None
    next = None
    def __init__(self, initValue):
        self.value = initValue
        self.next = None
    
    #def value(self):
        #return self.value
    
class LinkedList:
    start = None
    def __init__(self, listOfValues):
        self.start = Node(listOfValues[0])
        currentNode = self.start
        for i in range(1,len(listOfValues)):
            currentNode.next = Node(listOfValues[i])
            currentNode = currentNode.next
    
    def listAll(self):
        currentNode = self.start
        print "Listing All Values in the Linked List"
        while not currentNode == None:
            print "Value is %r" % currentNode.value
            currentNode = currentNode.next
            
def mergeTwoLists(l1, l2):
    current1 = l1.start
    current2 = l2.start
    newList = []
    print "new list", newList
    print "type", type(newList)
    while True:
        print "Current 1 %r and Current 2 %r" % (current1, current2)
        if current1 == None and current2 == None:
            break
        elif current2 == None:
            newList.append(current1.value)
            current1 = current1.next
        elif current1 == None:
            newList.append(current2.value)
            current2 = current2.next
        elif current1.value <= current2.value:
            newList.append(current1.value)
            current1 = current1.next
        else:
            newList.append(current2.value)
            current2 = current2.next
    print newList
    return LinkedList(newList)
    #l1 = LinkedList(newList)
    #return l1
            

def main():
    ll1 = LinkedList([1,2,6,9 ,12])
    ll2 = LinkedList([0,3,5,7,8,100])
    #ll1.listAll()
    #ll2.listAll()
    merged_list = mergeTwoLists(ll1,ll2)
    print "Two List Merged:"
    merged_list.listAll()
    #print "The merged List is : %r" % merged_list
    
    
if __name__ == "__main__":
    main()