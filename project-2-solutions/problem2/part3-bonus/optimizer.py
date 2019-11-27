import json
from lazy import Lazy

def lazy_nd_list(l, label):
  res = []

  for v in l:
    if isinstance(v, list):
      res.append(lazy_nd_list(v, label))
    else:
      res.append(Lazy(v, label))

  return res


table = dict()


def call(func, arg1, arg2):
  key = func.__name__ + ':' + json.dumps(arg1)
  if key in table:
    return table[key].eval(arg2)

  lazy_arg1 = lazy_nd_list(arg1, 1)
  lazy_arg2 = Lazy(arg2, 2)

  lazy_result = func(lazy_arg1, lazy_arg2)
  table[key] = lazy_result
  return lazy_result.eval(arg2)

def print_table():
  print('\nTABLE:')
  for key in table:
    print(table[key])
  print('\n')
