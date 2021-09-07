/******************************
 * PROGRAM:  exercise-5-3-1.c
 * AUTHOR:   Haidar Al-Aubiydy
 * DATE:     April 11, 2017
 * TOPIC:    Handling Files
 ******************************/

/**************************************************************************
 * Declare include files
 **************************************************************************/
#include <stdio.h>
#include <stdlib.h>

/**************************************************************************
 * Macro Defines
 **************************************************************************/
//N/A

/**************************************************************************
 * Global variables
 **************************************************************************/
// N/A

/**************************************************************************
 * Function prototypes
 **************************************************************************/
int lineCount(FILE *);
int wordCount(FILE *);
int charCount(FILE *);
void printFile(FILE * fp);
void addStringToFile(FILE * fp);
void menu(void);

/**************************************************************************
 * Main
 **************************************************************************/
int main( int argc, char *argv[] )
{
    int i=0,
        linecount = 0,
        wordcount = 0,
        charcount = 0;
    char operation = NULL,
        *filename = NULL;
    FILE *fp;

    filename = (char *)malloc(sizeof(char));

    printf("Please enter a file name:  ");
    scanf("%s", filename);
    fflush(stdin);

    fp = fopen(filename,"a+");
    if(fp == NULL)
    {
        printf("\nError opening file %s, exiting...\n", filename);
        return (EXIT_FAILURE);
    }
    else
    {
        printf("\nFile %s was opened successfully\n\n", filename);
    }

    while(1)
    {
        menu();
        scanf("%c", &operation);
        fflush(stdin);

        switch(operation)
        {
            case 'c':
                charcount = charCount(fp);
                printf("\nThere are %i characters in file %s\n\n", charcount, filename);
                break;
            case 'w':
                wordcount = wordCount(fp);
                printf("\nThere are %i words in file %s\n\n", wordcount, filename);
                break;
            case 'l':
                linecount = lineCount(fp);
                printf("\nThere are %i lines in file %s\n\n", linecount, filename);
                break;
            case 'p':
                printFile(fp);
                break;
            case 'a':
                addStringToFile(fp);
                break;
            case 'e':
                printf("\nThank you, exiting...\n");
                fclose(fp);
                return EXIT_SUCCESS;
            default:
                printf("\nError, please select an option from the menu\n\n");
        }
    }
    return EXIT_SUCCESS;
}

/**************************************************************************
 * Function:   int newlineCount(argv);
 **************************************************************************/
int lineCount(FILE * fp)
{
    int count=0, line_empty=1;
    char ch;

    while(ch != EOF)
    {
        ch=getc(fp);
        if((ch == '\n' || ch == EOF || ch == ' ') && line_empty==1)
        {
            continue;
        }
        else if((ch != '\n' || ch != EOF) && line_empty==1)
        {
            line_empty=0;
        }
        else if((ch == '\n' || ch == EOF) && line_empty==0)
        {
            count++;
            line_empty=1;
        }
    }
    rewind(fp);
    return count;
}

/**************************************************************************
 * Function:   int wordCount(argv);
 **************************************************************************/
int wordCount(FILE * fp)
{
    int count = 0;
    char end_of_file = NULL;
    char ch[50];

    while(end_of_file != EOF)
    {
        end_of_file = fscanf(fp, "%s", ch);
        if(end_of_file == EOF)
        {
            break;
        }
        count++;
    }
    rewind(fp);
    return count;
}

/**************************************************************************
 * Function:   int charCount(argv);
 **************************************************************************/
int charCount(FILE * fp)
{
    int count = 0;
    char ch;

    while((ch=getc(fp)) != EOF)
    {
        if(ch == ' ' || ch == '\n')
        {
            continue;
        }
        count++;
    }
    rewind(fp);
    return count;
}

/**************************************************************************
 * Function:   void addStringToFile(FILE * fp);
 **************************************************************************/
void addStringToFile(FILE * fp)
{
    char * add_string = NULL;
    add_string = (char *)malloc(sizeof(char));

    printf("Please type a string to be added to the file: ");
    gets(add_string);

    fputc('\n', fp);
    fputs(add_string,fp);

    printf("The string \"%s\" was added to the file\n", add_string);
    rewind(fp);
}

/**************************************************************************
 * Function:   void printFile(FILE * fp);
 **************************************************************************/
void printFile(FILE * fp)
{
    char ch;
    while( (ch=getc(fp) ) != EOF )
    {
        printf("%c", ch);
    }
    printf("\n");
    rewind(fp);
}


/**************************************************************************
 * Function:   void menu(void);
 **************************************************************************/
void menu(void)
{
    printf("-c           Print the character count\n");
    printf("-w           Print the word count\n");
    printf("-l           Print the non-empty line count\n");
    printf("-p           Print contents of the file\n");
    printf("-a           Add a string to the end of the file\n");
    printf("-e           Exit\n");
    printf("   Please enter an operation: ");
}
