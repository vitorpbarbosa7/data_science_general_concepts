# include <bits/stdc++.h>

using namespace std;

int main()
{
  // Declare five variables of data type integer
  int a = 5, b = 8, maximum;

  // Return the maximum number between a and b
  maximum = max(a,b);

  swap(a,b);

  //Print values statements
  printf("a value %d\n, b value %d\n and maximum value %d\n\n", a, b, maximum);

  // Cubic root:

  int number = 2;
  double cubicRoot;

  cubicRoot = pow((double) (number), 1.0/3);

  // It seems like a bitwise operator
  // shift binary file to left and right

  cout<<fixed<<setprecision(3)<<cubicRoot<<"\n\n";

  return 0;
}
