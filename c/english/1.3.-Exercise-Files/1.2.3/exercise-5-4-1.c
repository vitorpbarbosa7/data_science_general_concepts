/******************************
 * PROGRAM:  exercise-5-4-1.c
 * AUTHOR:   Haidar Al-Aubiydy
 * DATE:     April 11, 2017
 * TOPIC:    Header Files
 ******************************/

/**************************************************************************
 * Declare include files
 **************************************************************************/
#include <stdio.h>
#include <stdlib.h>

/**************************************************************************
 * Macro Defines
 **************************************************************************/
// N/A

/**************************************************************************
 * Global Variables
 **************************************************************************/
struct node
{
    int data;
    struct node *next;
};

/**************************************************************************
 * Function Prototypes
 **************************************************************************/
int Add(struct node** headRef, int new);
int Delete(struct node** headRef);
void PrintList(struct node* head);
int Length(struct node* head);
void ZeroList(struct node** headRef);

/**************************************************************************
 * Main:
 * Create an empty linked list
 * Read user selection in relation to the linked list
 * Call appropriate function
 **************************************************************************/
int main( void )
{
    int x = 0;
    char selection = 0, c = 0;
    struct node *Head = NULL;

    while(1)
    {
        printf("(a)dd {x}  = add a new node with value x to the list, at the head of the list\n");
        printf("(d)el      = delete the fist node of list\n");
        printf("(l)ength   = print the number of nodes in the list\n");
        printf("(p)rint    = print the complete list\n");
        printf("(z)ero     = delete the entire list\n");
        printf("(e)xit     = quit the program\n");
        printf("\nwhat would you like to do:  ");

        fscanf(stdin, "%c", &selection);
        if(selection == 'a')
        {
            fscanf(stdin, "%d", &x);
            printf("%d added to the list\n\n", Add(&Head, x));
        }
        else if(selection == 'd')
        {
            printf("the delete head node is %d\n\n", Delete(&Head));
        }
        else if(selection == 'p')
        {
            printf("list elements:  ");
            PrintList(Head);
            printf("\n");
        }
        else if(selection == 'l')
        {
            printf("the are %d items in the list\n\n", Length(Head));
        }
        else if(selection == 'z')
        {
            ZeroList(&Head);
            printf("the list has been deleted\n\n");
        }
        else if(selection == 'e')
        {
            printf("exiting...\n");
            break;
        }
        else
        {
            printf("you have not entered a valid selection, try again");
        }
        fscanf(stdin, "%c", &c);
    }

    printf("see you next time\n");
    return (EXIT_SUCCESS);
}

/**************************************************************************
 * Function:
 * void Add(struct node** headRef, int new);
 **************************************************************************/
int Add(struct node** headRef, int new)
{
    struct node *newNode = malloc(sizeof(struct node));
    newNode->data = new;
    newNode->next = *headRef;
    *headRef = newNode;
    return new;
}

/**************************************************************************
 * Function:
 * int Delete(struct node** headRef);
 **************************************************************************/
int Delete(struct node** headRef)
{
    struct node *temp = *headRef;
    int n=0;
    n = temp->data;
    *headRef = temp->next;
    free(temp);
    return n;
}

/**************************************************************************
 * Function:
 * void PrintList(struct node* head);
 **************************************************************************/
void PrintList(struct node* head)
{
    struct node *nextNode = head;

    while(nextNode != NULL)
    {
        printf("--->%d", nextNode->data);
        nextNode = nextNode->next;
    }
    printf("\n");
}

/**************************************************************************
 * Function:
 * int Length(struct node* head);
 **************************************************************************/
int Length(struct node* head)
{
    int count = 0;
    struct node *nextNode = head;

    while(nextNode != NULL)
    {
        count++;
        nextNode = nextNode->next;
    }
    return count;
}

/**************************************************************************
 * Function:
 * void ZeroList(struct node** headRef);
 **************************************************************************/
void ZeroList(struct node** headRef)
{
    struct node *temp = *headRef;
    while(temp != NULL)
    {
        *headRef = temp->next;
        free(temp);
        temp = *headRef;
    }
    free(temp);
}

