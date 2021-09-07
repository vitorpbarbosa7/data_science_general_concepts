#include <stdio.h>

int main()
{
    int a = 30;
    int *pt = &a;

    //int *pt;
    //pt = &a;

    printf("the address of pt is %p\n", &pt);
    printf("the address stored in pt is %p\n", pt);
    printf("the address of a is %p\n", &a);
    printf("the value pt is pointing to is %d\n", *pt);

    *pt = 100;
    printf("the value of a is now %d\n", a);

    return 0;
}
