/******************************
 * PROGRAM:  exercise-5-1-1.c
 * AUTHOR:   Haidar Al-Aubiydy
 * DATE:     April 11, 2017
 * TOPIC:    Dynamic Arrays
 ******************************/

/**************************************************************************
/* Declare include files
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
struct students{
    int student_id;
    char student_fist_initial;
};

/**************************************************************************
/* Function prototypes
**************************************************************************/
void fillDynamicArray(struct students *);

/**************************************************************************
 * Function: int main( void );
 **************************************************************************/
int main(void)
{
    struct students *student;
    student = (struct students *) malloc(sizeof(struct students)*10);
    if (student == NULL)
    {
        free (student);
        return EXIT_FAILURE;
    }

    fillDynamicArray(student);

    return EXIT_SUCCESS;
}

/**************************************************************************
 * Function: void fillDynamicArray(struct students * stud);
 **************************************************************************/
void fillDynamicArray(struct students * stud)
{
    int i;
    for(i=0 ; i<10 ; i++)
    {
        stud->student_id = i + 1000;
        stud->student_fist_initial = 65 + i;
        if(i<9)
        {
            stud++;
        }
    }
    stud -= 9;

    for(i=0 ; i<10 ; i++)
    {
        printf("stud is pointing to address: %p\n  Student_id has the value: %d\n   Student first initial is: %c\n\n", stud, stud->student_id, stud->student_fist_initial);
        if(i<9)
        {
            stud++;
        }
    }

    free(stud);

}

