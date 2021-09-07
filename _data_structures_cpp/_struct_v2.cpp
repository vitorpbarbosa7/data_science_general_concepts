

# include <bits/stdc++.h>
using namespace std;

/// You're able to define a data type structure

struct Books
{
  char Title[20];
  char Author[20];
  int ID;
  float price;
}book1;

// book1 as global variable

// To access any member of a structure, we must use
// the member access operator dot.


// Create a function to print books:
void printingBooks(Books variableBook){
  cout<<variableBook.Author<<"\n";
  cout<<variableBook.Title<<"\n";
  cout<<variableBook.ID<<"\n";
  cout<<variableBook.price<<"\n";
}

int main ()
{
  book1.ID = 10;
  book1.price = 13.67;

  // Put strings
  strcpy(book1.Title, "Data structures");
  strcpy(book1.Author, "Mark");


  // Call the function
  printingBooks(book1);

  // Declare book2 as local var:
  // Datatype Books created with struct is here called
  Books book2;

  book2.ID = 100;
  cout<<book2.ID<<"\n";

  printingBooks(book2);
}
