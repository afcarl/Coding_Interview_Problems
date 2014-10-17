'''
Created on Oct 14, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
import numpy as np
WALL = 9
VISITED = 8
DESTINATION = 7
START = 6
UNVISITED = 0
import Queue

def findPath(graph):
    q = Queue.Queue()
    q.put((9,0));
    
    while not q.empty():
        node = q.get()
        for v in getAdjacentVertices(graph,node):
            if graph[v[0],v[1]] == DESTINATION:
                return v
            graph[v[0],v[1]] = VISITED
            q.put(v)
    
def findPathDFS(graph):
    pass
    

def getAdjacentVertices(graph,node):
    # assume node is (a,b) where a is the first index and b is the second index
    y = node[0]
    x = node[1]
    edges = []
    size_y = np.shape(graph)[0]
    size_x = np.shape(graph)[1]
    if y > 0:
        # down
        _y = y-1
        _x = x
        if graph[_y,_x] == UNVISITED or graph[_y,_x] == DESTINATION:
            edges.append((y-1,x))
    if y < size_y-1:
        _y = y+1
        _x = x
        if graph[_y,_x] == UNVISITED or graph[_y,_x] == DESTINATION:
            edges.append((y+1,x))
    if x > 0:
        _y = y
        _x = x-1
        if graph[_y,_x] == UNVISITED or graph[_y,_x] == DESTINATION:
            edges.append((y,x-1))
    if x < size_x-1:
        _y = y
        _x = x+1
        if graph[_y,_x] == UNVISITED or graph[_y,_x] == DESTINATION:
            edges.append((y,x+1))
    #print node
    #print "Adjacent Vertices are %r" % edges
    return edges


def main():
    G = np.array([[9,0,0,0,0,0,9,9,0,7],
                  [0,0,9,0,0,0,0,0,0,0],
                  [9,0,9,0,0,9,9,0,9,9],
                  [0,0,0,9,9,9,0,0,9,0],
                  [0,9,9,0,0,0,0,0,0,0],
                  [0,9,9,0,0,9,0,0,0,0],
                  [0,0,0,0,9,0,0,0,0,0],
                  [9,0,9,0,9,0,0,0,0,0],
                  [9,0,9,9,0,0,0,9,9,0],
                  [1,0,0,0,0,0,0,9,0,0]])
    print "Destination is (%r,%r)" % findPath(G)
    


    
if __name__ == "__main__":
    main()