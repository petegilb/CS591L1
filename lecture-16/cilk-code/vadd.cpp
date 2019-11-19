#include <cilk/cilk.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void vadd(int* A, int* B, int* C, int n) {
  if (n == 1) {
    C[0] = A[0] + B[0];
  }

  else {
    cilk_spawn vadd(A, B, C, n/2);
    cilk_spawn vadd(A+n/2, B+n/2, C+n/2, n-n/2);
    cilk_sync;
  }
}

// this wont really speed things up
// https://jayconrod.com/posts/29/parallelization--harder-than-it-looks
void vadd2(int* A, int* B, int* C, int n) {
  cilk_for (int i = 0; i < n; i++) {
    C[i] = A[i] + B[i];
  }
}

void fill_array(int *A, int n) {
  for (int i = 0; i < n; i++) {
    A[i] = i;
  }
}

int main(int argc, char* argv[]) {
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

  // Done
  printf("done in %d seconds\n", time2 - time1);
  return 0;
}
