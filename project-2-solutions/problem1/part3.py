import sys, ast, astor
from aspectlib import Proceed, Return, Aspect, weave

# Aspect oriented programming portion
@Aspect(bind=True)
def null_aspect(f, *args, **kwargs):
  result = yield Proceed(*args, **kwargs)

  if f.__name__.startswith('_n_'):
    if result is None:
      raise ValueError('null-safe function returned None!')

  yield Return(result)

def null_weave():
  weave('__main__', null_aspect)


# Instrumentation portion
def instrument_function_parameters(node):
  instrumented = []
  for arg in node.args.args:
    name = arg.arg
    if name.startswith('_n_'): # instrument null check here
      code = 'if {} is None: raise ValueError(\'parameter {} in function {} is None\')'.format(name, node.name, name)
      instrumented += ast.parse(code).body

  node.body = instrumented + node.body

if __name__ == '__main__':
  filename = sys.argv[1]
  with open(filename, 'r') as code_file:
    code = code_file.read()
    tree = ast.parse(code)

  for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
      instrument_function_parameters(node)

  print(astor.to_source(tree))
