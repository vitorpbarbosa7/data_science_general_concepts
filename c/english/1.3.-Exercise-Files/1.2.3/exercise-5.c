#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

   int name[100];
   int name2[100];
   char *description;

   if (name == name2)
   {
       return 0;
   }

   strcpy(name, "Zara Ali");

   /* allocate memory dynamically */
   description = malloc( 1 * sizeof(char) );

   if( description == NULL ) {
      fprintf(stderr, "Error - unable to allocate required memory\n");
   }
   else {
      strcpy( description, "Zara ali a DPS student in class 10th");
      strcpy( name, description);
   }

   printf("Name = %s\n", name );
   printf("Description: %s\n", description );
}
