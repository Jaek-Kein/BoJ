#include <iostream>
#include <string>
using namespace std;

int main(){
  string word;
  int number;

  cin >> word;      // cin = 입력받기 / cout = 출력하기
  cin >> number;

  cout << word.substr(number-1, 1);

  return 0;
}