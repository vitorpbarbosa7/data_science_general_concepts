#include <stdio.h>

int add_nums(int , int );

int main()
{
    int num1 = 3;
    int num2 = 3;
    int result;

    result = add_nums(num1, num2);

    printf("the result is %d\n", result);

    return 0;
}

int add_nums(int a, int b)
{
    //num1 = 5;
    //num2 = 5;

    return a + b;
}
