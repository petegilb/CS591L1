from aspectlib import Aspect, Proceed, Return, weave
import json

table = dict()

@Aspect(bind=True)
def memoize_aspect(func, *args, **kwargs):
  key = '{}:{}:{}'.format(func.__name__, json.dumps(args), json.dumps(kwargs))

  if key in table:
    yield Return(table[key])
  else:
    result = yield Proceed(*args, **kwargs)
    table[key] = result
    yield Return(result)

def memoize_weave(): 
  weave('__main__', memoize_aspect)
