'''
Created on Sep 19, 2014

@author: Ben Athiwaratkun (pa338)

'''
# incorrect
def binarySearch(list, value):
    mid = len(list)/2;
    if value < list[mid]:
        return binarySearch(list[:mid], value)
    elif value > list[mid]:
        return binarySearch(list[mid:], value)
    else:
        return mid;
        

def main():
    print binarySearch([1,5,6,7,89,6542,743453,7575473], 743453)
    
if __name__ == "__main__":
    main()