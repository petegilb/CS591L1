#include <stdio.h> // for printf and scanf
#include <stdlib.h> // for malloc, atoi

int main(int argc, char* argv[]) {
  // <type>* -> a pointer to something of that type
  // pointers are just what their name implies
  // they point to the location of the value

  // the following is a regular variable
  int x = 1; 
  // this is a pointer
  int* ptr = &x; // & gets us the address of x(a pointer to x)

  x = 2; // change the value of x
  *(ptr) = 3; // also changes the value of x
  printf("x = %d \n", x); // %d means a decimal number (i.e. an integer)
  printf("&x = %p \n", &x); // %p means pointers
  printf("ptr = %p \n", ptr);
  printf("*ptr = %d \n", *ptr);
  printf("&ptr = %p \n\n\n\n", &ptr);

  // arrays
  // we can define *static arrays* easily
  // static means that the length is a constant known at compile time
  // so memory allocation can happen statically via the compiler/linker/loader
  int arr1[10];

  // arrays can be accessed regularly
  arr1[0] = 0;
  printf("arr1[0] = %d\n\n\n\n", arr1[0]);

  // turns out, arrays are really pointers to contigious memory locations!
  printf("arr1 = %p\n", arr1);
  printf("&(arr1[0]) = %p\n", &(arr1[0]));
  printf("&(arr1[1]) = %p\n", &(arr1[1]));
  printf("sizeof(int) = %lu\n\n\n\n", sizeof(int)); // %lu = unsigned long

  // we can use arrays as pointers and vice-versa, but we have to be careful not to
  // go out of bounds
  arr1[0] = 100;
  arr1[1] = 150;
  arr1[2] = 200;
  printf("*arr1 = %d\n", *arr1);
  printf("*(arr1+1) = %d\n", *(arr1+1));
  printf("*(arr1+2) = %d\n", *(arr1+2));

  // dynamic arrays (where length is dynamic, i.e. available only at runtime)
  // these can be defined via dynamic memory allocation
  // they are traditionally treated as pointers
  int n = 100;
  int* arr2 = (int*) malloc(sizeof(int) * n); // include <stdlib.h> for this
  arr2[0] = 10;
  arr2[1] = 20;
  arr2[n-1] = n;

  printf("arr2[0] = %d\n", arr2[0]);
  printf("arr2[1] = %d\n", arr2[1]);
  printf("arr2[n-1] = %d\n\n\n\n", arr2[n-1]);
  
  // argv is of type char* [] which is *equivalent* to char** or char[][]
  // you can think of this as a 2d character array
  // or more logically an array of strings (each string is an array of characters)
  printf("argv[0] = %s, argv[1] = %s\n", argv[0], argv[1]);
  int param = atoi(argv[1]);
  printf("argv[1] as a number = %d\n", param);

  return 0;
}
