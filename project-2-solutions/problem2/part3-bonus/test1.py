import time

from optimizer import call, print_table

# Create some big list
l = list(range(2000000))

# Two test functions
def test1(l, v):
  s = sum(l)
  return v + s
  
def test2(l, v):
  mid = len(l) // 2
  return sum(l[:mid]) + v + sum(l[mid:])

# Call the first function on the list twice
t1 = time.time()
print(call(test1, l, 5))
t2 = time.time()
print(round(t2 - t1), 'seconds')

t1 = time.time()
print(call(test1, l, 1))
t2 = time.time()
print(round(t2 - t1), 'seconds')

# Print the table
print_table()


# Call the second function on the list twice
t1 = time.time()
print(call(test2, l, 15))
t2 = time.time()
print(round(t2 - t1), 'seconds')

t1 = time.time()
print(call(test2, l, 12))
t2 = time.time()
print(round(t2 - t1), 'seconds')

# Print the table
print_table()
