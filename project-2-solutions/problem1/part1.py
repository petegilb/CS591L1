import ast
import sys

# keeps track of the position of null-safe parameters for every function
function_table = {}


def check_expression_is_null_safe(node, value):
  if isinstance(value, ast.NameConstant) and value.value is None:
    print('Error: None', '...   Line:', node.lineno)

  if isinstance(value, ast.Call) and not value.func.id.startswith('_n_') and value.func.id != 'null_cast':
    print('Error: nullable function call', value.func.id, '...   Line:', node.lineno)

  if isinstance(value, ast.Name) and not value.id.startswith('_n_'):
    print('Error: nullable variable', value.id, '...   Line:', node.lineno)


def handle_function_call(node):
  name = node.func.id

  if not name in function_table:
    return
  
  for i in function_table[name]:
    check_expression_is_null_safe(node, node.args[i])


def handle_assignment(node):
    target = node.targets[0]
    if not isinstance(target, ast.Name):
      return

    if not target.id.startswith('_n_'):
      return

    check_expression_is_null_safe(node, node.value)
    

def handle_function_definition(node):
  name = node.name
  function_table[name] = [] # will keep track of null-safe parameter positions
  
  args = node.args.args  # we assume we have positional arguments only
  for i, arg in enumerate(args):
    if arg.arg.startswith('_n_'):
      function_table[name].append(i)

  # now we must check that the function does return a null-safe value if it is a null-safe function
  if not name.startswith('_n_'):
    return

  # look for return statement
  for statement in node.body:
    if isinstance(statement, ast.Return):
      check_expression_is_null_safe(statement, statement.value)
      return

  # function does not have return but it should
  print('Error: null-safe function does not have return statement', node.name, '... Line:', node.lineno)


def check(tree):
  # first do function definitions to build a map of which functions have null-safe parameters
  for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
      handle_function_definition(node)
  
  # second, handle everything else
  for node in ast.walk(tree):
    if isinstance(node, ast.Assign):
      handle_assignment(node)
    if isinstance(node, ast.Call):
      handle_function_call(node)


if __name__ == '__main__':
  filename = sys.argv[1]
  with open(filename, 'r') as code_file:
    code = code_file.read()
    tree = ast.parse(code)
    check(tree)  # your solution's entry function
