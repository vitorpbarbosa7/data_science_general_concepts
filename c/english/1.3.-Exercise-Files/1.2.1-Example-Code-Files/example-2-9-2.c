#include <stdio.h>

int main()
{
    int id_nums[5] = {1,2,3,4,5};
    int *pt = &id_nums[0];

    printf("the address of pt is %p\n", &pt);
    printf("the address stored in pt is %p\n", pt);
    printf("the address of id_nums is %p\n", &id_nums);
    printf("the address of the first element in id_nums is %p\n", &id_nums[0]);
    printf("the value pt is pointing to is %d\n", *pt);

    pt = pt + 3;
    printf("\nafter moving 3 indexes forward to the 4th element, the address stored in pt is %p\n", pt);
    printf("the value pt is pointing to is %d\n", *pt);

    pt--;   // same as pt = pt - 1;
    printf("\nafter moving 1 index backward to the 3rd element, the address stored in pt is %p\n", pt);
    printf("the value pt is pointing to is %d\n", *pt);

    *pt = 88;
    printf("\nthe value stored in the 3rd element of id_nums is now %d\n", id_nums[2]);

    //id_nums++;

    return 0;
}
