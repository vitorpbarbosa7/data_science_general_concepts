// An array is not a data type, but rather a data structure
// Hold multiple variables at once

// Initialize array:
#include <stdio.h>

int main()
{
  int student_id = 0;

  int ids[3] = {200,100,400};

  // update student_id variable
  // assigned variable
  student_id = ids[1];

  printf("The student id is %f", &student_id);

  return 0;
}
