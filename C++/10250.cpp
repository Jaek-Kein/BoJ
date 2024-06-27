#include <iostream>
#include <string>
using namespace std;

int main()
{
  int testCase, height, width, customerNumber;
  string roomNumber;

  cin >> testCase;

  for (int i = 0; i < testCase; i++)
  {
    cin >> height >> width >> customerNumber;
    roomNumber.append(to_string(customerNumber % height + 1));
    roomNumber.append(to_string(customerNumber / height + 1));
    cout << roomNumber;
  }
  //TODO customerNumber / height + 1 = roomNumber, customerNumber % height = floorNumber
  //TODO Parse to string and append roomNumber to FloorNumber
  return 0;
}