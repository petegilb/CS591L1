from collections import namedtuple

BinOp = namedtuple('BinOp', ['op', 'left', 'right'])

def _ev(op, l, r):
  if op == '+':
    return l + r
  elif op == '-':
    return l - r
  elif op == '*':
    return l * r
  elif op == '//':
    return int(l / r)

class Lazy(object):
  def __init__(self, value, label):
    self.value = value
    self.label = label # 1 = first parameter, 2 = second parameter, 3 = a mix

  # override + and *
  def __add__(self, o):
    return operation('+', self, o)

  def __radd__(self, o):
    return operation('+', self, o)

  def __sub__(self, o):
    return operation('-', self, o)

  def __mul__(self, o):
    return operation('*', self, o)

  def __floordiv__(self, o):
    return operation('//', self, o)

  def eval(self, second_value):
    if self.label == 1:
      return self.value

    elif self.label == 2:
      return second_value

    else:
      l = self.value.left.eval(second_value)
      r = self.value.right.eval(second_value)
      return _ev(self.value.op, l, r)

  def __str__(self):
    if self.label == 1:
      return str(self.value)

    elif self.label == 2:
      return 'v2'

    else:
      l = str(self.value.left)
      r = str(self.value.right)
      return '({} {} {})'.format(l, self.value.op, r)

def operation(op, left, right):
  if left.label == 1:
    if isinstance(right, int): return Lazy(_ev(op, left.value, right), 1)
    if right.label == 1: return Lazy(_ev(op, left.value, right.value), 1)

  return Lazy(BinOp(op, left, right), 3)
