from functools import reduce
import random
import time

def prototype(mat, v):
  # LU Factorization depends only on mat
  n = len(mat)

  lower = [[0 for x in range(n)] for y in range(n)];
  upper = [[0 for x in range(n)] for y in range(n)];

  for i in range(n):
    for k in range(i, n):
      s = 0;
      for j in range(i):
        s = (lower[i][j] * upper[j][k]) + s;
      upper[i][k] = mat[i][k] - s;

    for k in range(i, n):
      if (i == k):
          lower[i][i] = 1;
      else:
        s = 0;
        for j in range(i):
          s = (lower[k][j] * upper[j][i]) + s;
        lower[k][i] = (mat[k][i] - s) // upper[i][i];

  # useless example, that cannot be optimized because it depends on both parameters
  return v + sum(map(sum, lower))

# example usage of optimization code
from part2 import optimize

if __name__ == '__main__':
  n = 200 # generate random matrix of size n
  mat = [[random.randint(0, 1000000) for i in range(n)] for j in range(n)]

  # run the prototype code the first time: this will take a long time
  t1 = time.time()
  result = optimize(prototype, mat, 5)
  t2 = time.time()
  print(result, int(t2 - t1))

  # run the prototype code the second time: now it will be a lot faster
  t1 = time.time()
  result = optimize(prototype, mat, 10)
  t2 = time.time()
  print(result, int(t2 - t1))
