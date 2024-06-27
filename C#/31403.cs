using System;

class Program
{
  static void Main()
  {
    string A, B, C;
    A = Console.ReadLine();
    B = Console.ReadLine();
    C = Console.ReadLine();
    calculateAsNumber(Convert.ToInt32(A), Convert.ToInt32(B), Convert.ToInt32(C));
    calculateAsString(A, B, Convert.ToInt32(C));
    
  }

  static void calculateAsNumber(int A, int B, int C)
  {
//TODO : 숫자열로 생각할때 계산
  Console.WriteLine(A+B-C);
  }

  static void calculateAsString(string A, string B, int C)
  {
//TODO : 문자열로 생각할때 계산
  string temp;

  temp = A + B;
  Console.WriteLine(Convert.ToInt32(temp) - C);
  }
}