'''
Created on Jan 25, 2015

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
import numpy as np

# yay!!
def printSpiral(A):
    B = np.zeros(np.shape(A))
    horizontal = True
    increment = 1
    row = 0
    col = 0
    maxRows, maxCols = np.shape(A)
    while True:
        if B[row,col] == 1:
            break
        print A[row,col]
        B[row,col] = 1
        # check if we need to change direction
        if horizontal:
            if row + increment >= maxRows or B[row + increment,col] == 1:
                horizontal = False
                
        else:
            if col + increment >= maxCols or B[row, col + increment] == 1:
                horizontal = True
                increment *= -1
        
            
        # update the next location
        if horizontal:
            row += increment
        else:
            col += increment
            


def main():
    A = np.array([[1,2,3],[4,5,6],[7,8,9]])
    printSpiral(A)
    
if __name__ == "__main__":
    main()