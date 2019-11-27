import json

table = dict()

def memoize(func, *args, **kwargs):
  key = '{}:{}:{}'.format(func.__name__, json.dumps(args), json.dumps(kwargs))
  if key in table:
    return table[key]

  value = func(*args, **kwargs)
  table[key] = value
  return value
