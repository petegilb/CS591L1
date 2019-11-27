from functools import reduce
import random
import time

from optimizer import call

def solve(mat, v):
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

  return v + sum(map(sum, lower))


n = 300
mat = [[random.randint(0, 10000) for i in range(n)] for j in range(n)]

t1 = time.time()
print(call(solve, mat, 5))
t2 = time.time()
print(round(t2 - t1), 'seconds')

t1 = time.time()
print(call(solve, mat, 10))
t2 = time.time()
print(round(t2 - t1), 'seconds')
