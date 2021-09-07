/* Section 2: Program1 */

#include <stdio.h>
//#define MESSAGE "and please come back again."
//#define SIZE 50

void add (int num1, int num2);

int main()
{
    int number1;
    int number2;
    char user_name[50];
    char c;

    printf("what is you name: ");
    scanf("%s", user_name);

    printf("enter a number: ");
    scanf("%d", &number1);

    printf("enter a second number: ");
    scanf("%d%c",&number2, &c);

    add(number1,number2);
    printf("Thank you %s, and have a good day\n", user_name);
    //printf("%s\n", MESSAGE);

    return 0;
}

void add (int num1, int num2)
{
    printf("The result is: %d\n", num1+num2);
}
