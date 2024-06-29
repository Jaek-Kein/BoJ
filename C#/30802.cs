using System;
using System.Linq;

class Program
{
  static void Main()
  {
    int visitor, tpile, ppile, tcounter = 0;

    visitor = Convert.ToInt32(Console.ReadLine());
    int[] tInputs = Console.ReadLine().Split(' ').Select(int.Parse).ToArray(); if (tInputs == null) return;
    string[] pInputs = Console.ReadLine().Split(' '); if(pInputs == null) return;
    tpile = Convert.ToInt32(pInputs[0]);
    ppile = Convert.ToInt32(pInputs[1]);

    //TODO 티셔츠 묶음 계산식
    for (int i = 0 ; i < 6 ; i++)
    {
      if (tInputs[i] == 0) continue;
      if (tInputs[i] <= tpile) tcounter++ ;
      else 
      {
        tcounter += (tInputs[i] / tpile) + 1;
      }
    }

    Console.WriteLine(tcounter);
    Console.WriteLine($"{visitor / ppile} {visitor % ppile}");
  }
}