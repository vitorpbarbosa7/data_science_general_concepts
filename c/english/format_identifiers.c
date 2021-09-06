#include <stdio.h>

int main()
{
  int num_students = 10;
  float account_balance = 20.1;
  int hex = 0x0a; //same as /n new line
  char last_initial =  'A';
  char name[] = "Haidar";
  //point to another value already declared
  int *pt = &num_students;

  printf("The value: %d is stored in adress: %p\n\n", num_students, &num_students);
  printf("Account balance is $%f \n\n", account_balance);
  printf("Variable hex = %x and num_students in hex = %x\n\n", hex, num_students);
  printf("My last initial is %c \n\n", last_initial);
  printf("My first name is %s \n\n", name);
  printf("Pointer pt is pointing to address: %p which has the value : %d \n\n", (void *)pt, *pt);
  printf("You have to use double %% to display the symbol %% \n\n");
}
