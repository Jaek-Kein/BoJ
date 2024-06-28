using System;

class Program
{
  static void Main()
  {
    while (true){
      string? input = Console.ReadLine(); if (input == null) return;
      bool Palindrome = true;

      if (input.Equals("0")) break;

      char[] array = new char[input.Length];

      for (int i = 0 ; i < input.Length ; i++)
      {
        array[i] = input[input.Length-1-i];
      }

      for (int i = 0 ; i < input.Length ; i++)
      {
        if (array[i] != input[i])
        {
          Palindrome = false;
          break;
        }
      }

      if (Palindrome) Console.WriteLine("yes");
      else Console.WriteLine("no"); 
      
    }
  }
}