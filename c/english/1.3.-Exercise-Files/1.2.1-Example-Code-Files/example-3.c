#include <stdio.h>
#include <stdlib.h>

int main()
{
    int result, number1, number2;
    char option, c;

    printf("enter a number: ");
    scanf("%d", &number1);

    printf("enter a second number: ");
    scanf("%d",&number2);

    printf("What would you like to do:\n");
    printf("enter 'a' for addition\n");
    printf("enter 's' for subtraction\n");
    printf("enter 'm' for multiplication\n");
    printf("enter 'd' for division\n");

    c = getchar(); // this will capture the "\n" from the printf above
    //printf("c = %c", c);
    option = getchar();
    //printf("option = %c\n", option);

    switch (option)
    {
        case 'a':
            result = number1+number2;
            break;
        case 's':
            result = number1-number2;
            break;
        case 'm':
            result = number1*number2;
            break;
        case 'd':
            result = number1/number2;
            break;
        default:
            printf("Error: you have not choosen one of the option\n");
            return EXIT_FAILURE;
    }

    printf("The result is  %d\n", result);

    return 0;
}
