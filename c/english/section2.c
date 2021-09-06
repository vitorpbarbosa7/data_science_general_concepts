/* # tells the c preprocessor to search for this library before compile */
/* Header file */
#include <stdio.h>

// Definitions of macros to tell the c preprocessor what to do with them
#define MESSAGE "and please come back again"
#define SIZE 50

void add (int num1, int num2);

// Declares a main function which returns 0 if everything was done sucessfully
int main()
{
  int number1;
  int number2;
  char user_name[SIZE];
  char c;

  printf("what is your name: ");
  scanf("%s", user_name);

  printf("enter a number: ");
  // number1 is passed as argument to the add function
  scanf("%d", &number1);

  printf("enter a second number: ");
  // number2 is passed as argument to the add function
  scanf("%d%c", &number2, &c);

  add(number1, number2);
  printf("Thank you %s, and have a good day \n", user_name);
  printf("%s\n" MESSAGE);

  return 0;
}

void add (int num1, int num2)
{
    printf("The result is: %d\n", num1+num2);
}
