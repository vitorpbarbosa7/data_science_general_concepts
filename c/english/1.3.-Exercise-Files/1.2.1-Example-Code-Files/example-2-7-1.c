#include <stdio.h>

int main()
{
    int student_id = 0;
    int ids[3] = {200,100,400};

    student_id = ids[1];

    printf("student_id now holds the value: %d\n", student_id);

    return 0;
}
