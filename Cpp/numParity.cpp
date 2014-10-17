#include <iostream>
// many ways to calculate the parity 
using namespace std;

bool parityHelper(unsigned long long num, int start, int end){
  if (start == (end-1) ){
    return (num & (1<<start) ) >> start ;
  } else {
    int mid = (start + end)/2;
    return parityHelper(num, start, mid) ^ parityHelper(num,mid,end);
  }
}

bool parity(unsigned long long num){
  return parityHelper(num, 0, 64);
}

bool parity2(unsigned long long num){
  bool par = false;
  for(int i=0; i< 64; i++){
    par = par ^ ( (num & (1<<i) ) >> i );
  }
  return par;
}

bool parity3(unsigned long long num){
  bool par = false;
  while(num){
    par = par ^ (num & 1);
    num = num >> 1;
  }
  return par;
}

int main(){
  cout << "parity of 7 is" << parity(7LL) << endl;
  cout << "parity of 15 is" << parity(15LL) << endl;
  cout << "parity of 1 is" << parity(1LL) << endl;
  cout << "parity of 5 is" << parity(5LL) << endl;
  cout << "test" << endl;
  cout << "parity of 7 is" << parity2(7LL) << endl;
  cout << "parity of 15 is" << parity2(15LL) << endl;
  cout << "parity of 1 is" << parity2(1LL) << endl;
  cout << "parity of 5 is" << parity2(5LL) << endl;
  
  cout << "parity of 10 is" << parity3(10LL);
}
