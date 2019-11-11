from part2 import memoize_weave, table
import time

def fib(n):
  if n == 0:
    return 1
  elif n == 1:
    return 1

  return fib(n-1) + fib(n-2)  # Note that we do not have to call memoize explicitly


# first, call the function directly and see how much time it takes
print('calling fib directly', 35)
t1 = time.time()
print(fib(35))
t2 = time.time()
print('took time', t2 - t1)
print('')

# weave
memoize_weave()

# call the function again, it should be faster because recursive calls are now linear
print('calling fib after weave', 35)
t1 = time.time()
print(fib(35))
t2 = time.time()
print('took time', t2 - t1)
print('')

# display what is saved in the table
print('keys in the table:')
print(sorted(table.keys(), key=lambda str: (len(str), str)))
print('')

# call the function again, it should be even faster since its result is saved in the table
print('calling fib after weave', 35)
t1 = time.time()
print(fib(35))
t2 = time.time()
print('took time', t2 - t1)
print('')
