from part1 import memoize

def fib(n):
  print('fib is called', n)
  if n == 0:
    return 1
  elif n == 1:
    return 1

  return memoize(fib, n-1) + memoize(fib, n-2)

print('calling fib via memoize', 10)
print(memoize(fib, 10))
print('')

print('calling fib via memoize', 10)
print(memoize(fib, 10))
print('')

print('calling fib via memoize', 35)
print(memoize(fib, 35))
print('')
