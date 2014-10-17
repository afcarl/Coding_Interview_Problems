// Ben Athiwaratkun
#include<iostream>

using namespace std;

int binarySearch(int * array, int beginIndex, int endIndex, int number){


  // assume that it is sorted ascending
  int midIndex = (beginIndex+endIndex)/2;
  //cout << "midIndex" << midIndex << endl;

  if(beginIndex == endIndex and array[midIndex] != number ){
    cout << "Number not found" << endl;
    return -1;
  }

  if(array[midIndex] < number){
    return binarySearch(array, min(midIndex+1, endIndex), endIndex, number);
  } else if(array[midIndex] > number){
    return binarySearch(array, beginIndex, max(beginIndex,midIndex-1), number);
  } else if (array[midIndex] == number){
    return midIndex;
  } 
}

int main(){
  int array[6] = {1,2,5,76,885,3425};
  cout << binarySearch(array,0, 6, 347032);

}
