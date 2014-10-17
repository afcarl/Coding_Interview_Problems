'''
Created on Oct 16, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
import numpy as np

# sudoku checker

def checkOneToNine(A):
    # check that the array A contains numbers 1 to 9, each exactly once
    B = [0]*9
    for i in range(9):
        print A[i]-1
        print i
        print A
        if B[ A[i] -1 ] > 0:
            return False
        else:
            B[A[i] - 1] = 1
    return True

def sudokuChecker(Mat):
    for row in range(9):
        if not checkOneToNine(Mat[row,:]):
            return False
    for col in range(9):
        if not checkOneToNine(Mat[:,col]):
            return False
    for block_row in range(3):
        for block_col  in range(3):
            if not checkOneToNine( reduce(lambda x,y: list(x) + list(y),  Mat[3*block_row:3*block_row+3,3*block_col: 3*block_col+3] )   ):
                return False
    return True

def main():
    Mat = np.array([[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,4,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]])
    print sudokuChecker(Mat)

if __name__ == "__main__":
    main()


