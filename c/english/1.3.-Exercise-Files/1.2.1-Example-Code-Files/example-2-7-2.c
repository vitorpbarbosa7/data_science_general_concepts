#include <stdio.h>

int main()
{
    char color[6];
    color[0] = 'b';
    color[1] = 'l';
    color[2] = 'a';
    color[3] = 'c';
    color[4] = 'k';

    printf("the last element of this array has index 4 and value %c\n", color[4]);

    return 0;
}
