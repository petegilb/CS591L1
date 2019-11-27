#include <cilk/cilk.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// function that takes an array and its length
// and fills it with values
void fill_array(int A[], int n) {
  for (int i = 0; i < n; i++) {
    A[i] = i;
  }
}

// function that takes an array and its length
// and prints its contents
void print_array(int A[], int n) {
  for (int i = 0; i < n; i++) {
    printf("%d\n", A[i]);
  }
}

// function that takes 3 arrays and their length, returns nothing
// instead it modifies C itself to become A + B
// this is a common pattern in C
void vadd(int* A, int* B, int* C, int n) {
  if (n == 1) {
    C[0] = A[0] + B[0];
  }

  // A + n/2 is the same as &(A[n/2])
  // in python, this is similar to A[n/2:]
  else {
    vadd(A, B, C, n/2);
    vadd(A+n/2, B+n/2, C+n/2, n-n/2);
  }
}

int main(int argc, char* argv[]) {
  // get desired length from the command line arguments
  // and make it an int
  int n = atoi(argv[1]);

  // Allocate A, B, and C
  int* A = (int*) malloc(sizeof(int) * n);
  int* B = (int*) malloc(sizeof(int) * n);
  int* C = (int*) malloc(sizeof(int) * n);

  // Fill arrays
  fill_array(A, n);
  fill_array(B, n);
  fill_array(C, n);

  // Call vadd and time it
  int time1 = time(NULL);
  vadd(A, B, C, n);
  int time2 = time(NULL);

  printf("elements at 0, 1, 2\n");
  print_array(C, 3);
  printf("elements at 10, 11, 12\n");
  print_array(C+10, 3);

  // Done
  printf("done in %d seconds\n", time2 - time1);
  return 0;
}
