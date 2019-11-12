#include <cilk/cilk.h>
#include <stdio.h>
#include <stdlib.h>

int fib(int n) {
  if (n < 2) {
    return n;
  }

  int x, y;
  x = cilk_spawn fib(n - 1);
  y = fib(n - 2);
  cilk_sync;

  return x + y;
}

int main(int argc, char* argv[]) {
  int n = atoi(argv[1]);
  printf("%d = %d\n", n, fib(n));
  return 0;
}
