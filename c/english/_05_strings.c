// In c there is no data type which represents strings
// There is only a sequence of chars in a array which we call a string


# include <stdio.h>

int main()
{
  char my_name[20] = "Haidar";

  printf("my name is %s\n", my_name);

  my_name[7] = 'A';
  printf("my last initial is %c\n", my_name[7]);

  // What really happens is that printf thinks we got to the end of that string
  // because it found the end of line character \0
  printf("my name is %s\n", my_name);

  my_name[6] = ' ';

  my_name[7] = 'A';

  printf("my last initial is  %c\n", my_name[7]);
  printf("my name is %s\n", my_name);

  return 0;
}
